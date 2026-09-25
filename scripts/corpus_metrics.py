"""Compute the corpus metrics at each project's pin, the same way for all five.

Every figure is counted from git at the pin in evidence/corpus.md, never from a working
tree, so a rerun at the same pins gives the same numbers. The output is data, written to
evidence/metrics/metrics.json and metrics.csv, and a figure the specification quotes is
taken from there rather than typed (CCF23).

Sources are found as scripts/resolve_citations.py finds them: `--source name=path`,
`CCF_SOURCE_<NAME>`, or a partial clone of the remote under .cache/corpus/.

Methods, stated so they can be challenged:

  commits              git rev-list --count <pin>
  active_days          distinct committer dates in git log <pin>
  conventional_share   subjects matching `type(scope)!: text`, with the Conventional
                       Commits types build, chore, ci, docs, feat, fix, perf, refactor,
                       revert, style and test
  task_id_share        subjects naming <prefix><digits>, the prefix read from the
                       project's roadkeep.toml at the pin
  coauthored_share     commit messages carrying a Co-Authored-By trailer naming Claude
  every_turn_bytes     CLAUDE.md, .claude/CLAUDE.md, AGENTS.md at the root, and every file
                       those import with an @path line, plus the name and description
                       of each SKILL.md under .claude/skills; MCP tool schemas are not
                       in the tree and are not counted
  every_turn_tokens    every_turn_bytes / 4, the estimate freewilly used; it is an
                       estimate, not a tokenizer count
  ledger_*             lines of the changelog and roadmap named in roadkeep.toml:
                       shipped and retired by their markers, open by the roadmap's open
                       markers; deferred counts task lines in a DEFERRED.md beside them
  test_declarations    declared tests: `def test_` in Python, [Fact], [Theory], [Test]
                       and [TestMethod] in C#, @Test in Java, and it( or test( in
                       JavaScript and TypeScript test files; a count of declarations,
                       not of cases a runner collects

    python scripts/corpus_metrics.py --source shio=<path> ...

Run from the repository root.
"""

from __future__ import annotations

import argparse
import csv
import json
import posixpath
import re
import subprocess
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from resolve_citations import CORPUS, locate, read_pins  # noqa: E402

OUT = Path("evidence/metrics")
CONVENTIONAL = re.compile(r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([^)]*\))?!?: ")
COAUTHOR = re.compile(r"^Co-Authored-By:.*Claude", re.IGNORECASE | re.MULTILINE)
IMPORT = re.compile(r"^@(\S+)\s*$", re.MULTILINE)
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
TESTS = {
    "*.py": r"^\s*(async\s+)?def test_",
    "*.cs": r"\[(Fact|Theory|Test|TestMethod)(\(|\])",
    "*.java": r"^\s*@Test\b",
    "*.test.*": r"^\s*(it|test)\(",
    "*.spec.*": r"^\s*(it|test)\(",
}


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace"
    ).stdout


def show(repo: Path, pin: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{pin}:{path}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return result.stdout if result.returncode == 0 else None


def every_turn(repo: Path, pin: str) -> int:
    """Bytes of the every-turn files, their imports, and each skill's name and description."""
    seen, queue, total = set(), ["CLAUDE.md", ".claude/CLAUDE.md", "AGENTS.md"], 0
    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        text = show(repo, pin, path)
        if text is None:
            continue
        total += len(text.encode("utf-8"))
        base = posixpath.dirname(path)
        for target in IMPORT.findall(text):
            queue.append(posixpath.normpath(posixpath.join(base, target)))
    for path in git(repo, "ls-tree", "-r", "--name-only", pin, "--", ".claude/skills").split():
        if path.endswith("/SKILL.md"):
            head = FRONTMATTER.match(show(repo, pin, path) or "")
            if head:
                fields = [line for line in head.group(1).splitlines() if line.startswith(("name:", "description:"))]
                total += len("\n".join(fields).encode("utf-8"))
    return total


def ledger(repo: Path, pin: str) -> dict:
    """Shipped, retired, open and deferred counts from the governed files at the pin."""
    raw = show(repo, pin, "roadkeep.toml")
    if raw is None:
        return {"prefix": None}
    config = tomllib.loads(raw)
    files = config.get("files", {})
    markers = config.get("markers", {})
    changelog = show(repo, pin, files.get("changelog", "docs/CHANGELOG.md")) or ""
    roadmap = show(repo, pin, files.get("roadmap", "docs/ROADMAP.md")) or ""
    folder = Path(files.get("roadmap", "docs/ROADMAP.md")).parent.as_posix()
    deferred = show(repo, pin, files.get("deferred", f"{folder}/DEFERRED.md")) or ""
    shipped, retired = markers.get("shipped", "✅"), markers.get("retired", "\U0001f5d1")
    opened = markers.get("open", [])

    def count(text: str, marks: list[str]) -> int:
        return sum(1 for line in text.splitlines() if any(line.startswith(f"- {m} ") for m in marks))

    # A ledger may omit the shipped marker (Shio's does): every task line that is not
    # marked retired is a shipped entry.
    prefix = config.get("prefix", "")
    entry = re.compile(rf"^- (?:\S+ )?\*\*{re.escape(prefix)}\d+\*\*")
    entries = sum(1 for line in changelog.splitlines() if entry.match(line))
    gone = count(changelog, [retired])
    return {
        "prefix": prefix or None,
        "ledger_shipped": max(entries - gone, count(changelog, [shipped])),
        "ledger_retired": gone,
        "ledger_open": count(roadmap, opened),
        "ledger_deferred": sum(1 for line in deferred.splitlines() if re.match(r"^- \S+ \*\*", line)),
    }


def tests(repo: Path, pin: str) -> int:
    total = 0
    for glob, pattern in TESTS.items():
        out = git(repo, "grep", "-c", "-E", pattern, pin, "--", glob)
        total += sum(int(line.rsplit(":", 1)[1]) for line in out.splitlines() if line.rsplit(":", 1)[-1].isdigit())
    return total


def measure(name: str, repo: Path, pin: str) -> dict:
    subjects = git(repo, "log", "--format=%s", pin).splitlines()
    messages = git(repo, "log", "--format=%B%x00", pin).split("\x00")[:-1]
    days = set(git(repo, "log", "--format=%cs", pin).split())
    commits = int(git(repo, "rev-list", "--count", pin).strip())
    record = {"project": name, "pin": pin, "commits": commits, "active_days": len(days)}
    record["commits_per_active_day"] = round(commits / len(days), 1)
    record["conventional_share"] = round(sum(bool(CONVENTIONAL.match(s)) for s in subjects) / commits, 3)
    record.update(ledger(repo, pin))
    prefix = record.pop("prefix")
    tagged = re.compile(rf"\b{re.escape(prefix)}\d+\b") if prefix else None
    record["task_id_share"] = round(sum(bool(tagged.search(s)) for s in subjects) / commits, 3) if tagged else None
    record["coauthored_share"] = round(sum(bool(COAUTHOR.search(m)) for m in messages) / commits, 3)
    record["every_turn_bytes"] = every_turn(repo, pin)
    record["every_turn_tokens"] = record["every_turn_bytes"] // 4
    record["test_declarations"] = tests(repo, pin)
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    root = Path(args.root)
    sources = dict(item.split("=", 1) for item in args.source)

    rows, missing = [], []
    for name, (remote, pin) in read_pins(root / CORPUS).items():
        repo = locate(name, remote, pin, sources, root)
        if repo is None:
            missing.append(name)
            continue
        rows.append(measure(name, repo, pin))
    if missing:
        print(f"unreachable, not measured: {', '.join(missing)}")
        return 1

    out = root / OUT
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8", newline="\n")
    with open(out / "metrics.csv", "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
