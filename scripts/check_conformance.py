"""Check a repository against the rules a script can decide from its files.

Run in, or pointed at, a target repository. Each detector returns one of three verdicts
(spec/glossary.md, verdict): passed, failed, or could not decide, never a pass for a
check that could not run (VG-3). Rules no detector covers are left to the audit's
judgement pass and are not reported here.

    python scripts/check_conformance.py <repo> [--level 1|2|3] [--json] [--report <path>]

The claimed level and the project's waivers come from the target's ccf.toml
(spec/deviations.md): a current waiver reports its rule as waived, an expired one as
failed. Exit 1 when a rule at or below the claimed level fails, or ccf.toml is malformed. Standard library only, so it
runs in any repository with Python and git.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import subprocess
import sys
import tomllib
from pathlib import Path

PASSED, FAILED, UNDECIDED = "passed", "failed", "could not decide"
EVERY_TURN = ("CLAUDE.md", ".claude/CLAUDE.md", "AGENTS.md")
IMPORT = re.compile(r"^@(\S+)\s*$", re.MULTILINE)
GATE_COMMAND = re.compile(
    r"(pytest|npm (run )?test|dotnet test|mvnw?\b|gradlew?\b|cargo test|go test|roadkeep lint|ruff|vitest|jest)"
    r"[^\n|]*\|(?!\|)"
)
PUSH = re.compile(r"^on:\s*(\[[^\]]*\bpush\b|push\b)|^\s{2}push:", re.MULTILINE)


def read(repo: Path, path: str) -> str | None:
    target = repo / path
    return target.read_text(encoding="utf-8-sig", errors="replace") if target.is_file() else None


def roadkeep_config(repo: Path) -> dict | None:
    raw = read(repo, "roadkeep.toml")
    try:
        return tomllib.loads(raw) if raw else None
    except tomllib.TOMLDecodeError:
        return None


def exists(repo: Path, path: str) -> bool:
    """Whether the file exists with exactly this name: Windows matches names in any case."""
    target = repo / path
    return target.is_file() and target.name in {p.name for p in target.parent.iterdir()}


def every_turn_files(repo: Path) -> list[str]:
    """The every-turn files present, and the files they import, relative to the repo."""
    found, queue = [], [p for p in EVERY_TURN if exists(repo, p)]
    while queue:
        path = queue.pop(0)
        if path in found or not exists(repo, path):
            continue
        found.append(path)
        for target in IMPORT.findall(read(repo, path) or ""):
            joined = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
            if not joined.startswith(".."):
                queue.append(joined)
    return found


def is_1(repo: Path) -> tuple[str, str]:
    """IS-1: where there is an every-turn file, a budget a gate enforces covers it."""
    files = every_turn_files(repo)
    if not files:
        return PASSED, "no every-turn file (allowed by decision D2)"
    budgets = (roadkeep_config(repo) or {}).get("budgets", {})
    if not budgets:
        return UNDECIDED, "every-turn files present; no budget declared in a format this checker reads"
    missing = [f for f in files if f not in budgets]
    over = []
    for name, limit in budgets.items():
        text = read(repo, name)
        if text is None:
            continue
        if "lines" in limit and len(text.splitlines()) > limit["lines"]:
            over.append(f"{name} over {limit['lines']} lines")
        if "bytes" in limit and len(text.encode("utf-8")) > limit["bytes"]:
            over.append(f"{name} over {limit['bytes']} bytes")
    if missing or over:
        return FAILED, "; ".join([f"no budget for {m}" for m in missing] + over)
    return PASSED, f"{len(files)} every-turn file(s) under declared budgets"


def pg_1(repo: Path) -> tuple[str, str]:
    """PG-1: planning files are governed files (declared to a tool, with a guard wired)."""
    config = roadkeep_config(repo)
    if config is None:
        return UNDECIDED, "no planning-tool configuration this checker reads"
    wiring = (read(repo, ".claude/settings.json") or "") + (read(repo, "hooks/hooks.json") or "")
    if "PreToolUse" in wiring:
        return PASSED, "planning files declared in roadkeep.toml, and a PreToolUse guard is wired"
    if (repo / ".claude-plugin").is_dir():
        return UNDECIDED, "no PreToolUse guard in the committed settings; this repository is a plugin, whose payload may carry it"
    return FAILED, "planning files declared, but no PreToolUse guard in .claude/settings.json or hooks/hooks.json"


def vg_2(repo: Path) -> tuple[str, str]:
    """VG-2: no file that tells the agent how to run a gate pipes the gate's output."""
    paths = every_turn_files(repo) + sorted(
        p.relative_to(repo).as_posix() for p in (repo / ".claude" / "skills").glob("*/*.md")
    )
    hits = []
    for path in paths:
        for number, line in enumerate((read(repo, path) or "").splitlines(), 1):
            if GATE_COMMAND.search(line):
                hits.append(f"{path}:{number}")
    if hits:
        return FAILED, "gate piped in " + ", ".join(hits[:5])
    return PASSED, f"{len(paths)} instruction file(s) scanned, no piped gate"


def vg_5(repo: Path) -> tuple[str, str]:
    """VG-5: a CI workflow runs on every push."""
    workflows = sorted((repo / ".github" / "workflows").glob("*.y*ml"))
    if not workflows:
        return FAILED, "no workflow in .github/workflows"
    on_push = [w.name for w in workflows if PUSH.search(w.read_text(encoding="utf-8", errors="replace"))]
    if not on_push:
        return FAILED, "no workflow triggers on push"
    return PASSED, "on push: " + ", ".join(on_push)


def ep_2(repo: Path) -> tuple[str, str]:
    """EP-2 (declared half): line terminators are declared in .gitattributes."""
    text = read(repo, ".gitattributes") or ""
    if re.search(r"\b(eol=|text=auto|-?text\b)", text):
        return PASSED, "line terminators declared in .gitattributes"
    return FAILED, "no text or eol rule in .gitattributes"


def cd_1(repo: Path) -> tuple[str, str]:
    """CD-1: no commit ships more than one ledger entry."""
    config = roadkeep_config(repo)
    if config is None:
        return UNDECIDED, "no ledger declared in a format this checker reads"
    changelog = config.get("files", {}).get("changelog", "docs/CHANGELOG.md")
    log = subprocess.run(
        ["git", "-C", str(repo), "log", "-p", "--format=@@commit %h", "--", changelog],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if log.returncode != 0:
        return UNDECIDED, "git history could not be read"
    batched, commit, added = [], None, 0
    for line in log.stdout.splitlines() + ["@@commit end"]:
        if line.startswith("@@commit "):
            if commit and added > 1:
                batched.append(commit)
            commit, added = line.split()[1], 0
        elif re.match(r"^\+- \S+ \*\*\w+\d+\*\*", line):
            added += 1
    if batched:
        return FAILED, f"{len(batched)} commit(s) add several ledger entries, e.g. {', '.join(batched[:3])}"
    return PASSED, "every commit adds at most one ledger entry"


WAIVED = "waived"
REPORT_VERDICT = {PASSED: "pass", FAILED: "fail", UNDECIDED: "could not run", WAIVED: "waived"}
WAIVER_FIELDS = ("rule", "reason", "owner", "date")


def declarations(repo: Path) -> tuple[dict, list[str]]:
    """The adopter's ccf.toml (spec/deviations.md), and the problems found in it."""
    raw = read(repo, "ccf.toml")
    if raw is None:
        return {}, []
    try:
        config = tomllib.loads(raw)
    except tomllib.TOMLDecodeError as error:
        return {}, [f"ccf.toml does not parse: {error}"]
    problems = []
    for i, waiver in enumerate(config.get("waiver", [])):
        missing = [f for f in WAIVER_FIELDS if not waiver.get(f)]
        if not (waiver.get("expires") or waiver.get("task")):
            missing.append("expires or task")
        if missing:
            problems.append(f"ccf.toml waiver {waiver.get('rule', i)}: missing {', '.join(missing)}")
    return config, problems


def apply_waivers(results: list[dict], waivers: list[dict], today: str) -> None:
    """A waived rule reports waived; an expired waiver turns its rule into a failure."""
    by_rule = {w.get("rule"): w for w in waivers}
    for result in results:
        waiver = by_rule.get(result["rule"])
        if not waiver:
            continue
        expires = str(waiver.get("expires", ""))
        if expires and expires < today:
            result["verdict"] = FAILED
            result["detail"] = f"waiver expired on {expires}: {waiver.get('reason', '')}"
        else:
            result["verdict"] = WAIVED
            end = f"until {expires}" if expires else f"tracked by {waiver.get('task')}"
            result["detail"] = f"{end}: {waiver.get('reason', '')} ({waiver.get('owner', '')})"


def write_report(repo: Path, level: int, results: list[dict], target: Path) -> None:
    """A report skeleton holding the checker's verdicts; the audit adds the judged rules."""
    import datetime

    here = Path(__file__).resolve().parent.parent
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True)
    manifest = json.loads((here / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    rules = []
    for r in results:
        entry = {"rule": r["rule"], "level": str(r["level"]), "verdict": REPORT_VERDICT[r["verdict"]], "by": "checker"}
        entry["waiver" if r["verdict"] == WAIVED else "evidence"] = r["detail"]
        rules.append(entry)
    report = {
        "spec_version": manifest.get("version", "unversioned"),
        "repository": repo.resolve().name,
        "commit": head.stdout.strip() or "0000000",
        "date": datetime.date.today().isoformat(),
        "claimed_level": level if level in (1, 2, 3) else 1,
        "achieved_level": 0,
        "profile": False,
        "tools": {"checker": manifest.get("version", "unversioned"), "skill": manifest.get("version", "unversioned")},
        "rules": rules,
    }
    sys.path.insert(0, str(Path(__file__).parent))
    from report import achieved  # noqa: E402

    report["achieved_level"] = achieved(rules, report["claimed_level"])
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


DETECTORS = {"IS-1": (1, is_1), "PG-1": (1, pg_1), "CD-1": (1, cd_1),
             "VG-2": (2, vg_2), "VG-5": (2, vg_5), "EP-2": (2, ep_2)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--level", type=int,
                        help="the level claimed (default: the level in ccf.toml, else 1)")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--report", metavar="PATH",
                        help="also write a report skeleton (spec/report.schema.json) for the audit to complete")
    parser.add_argument("--today", help=argparse.SUPPRESS)  # fixes the date in tests
    args = parser.parse_args(argv)
    repo = Path(args.repo)
    config, problems = declarations(repo)
    claimed = args.level or config.get("level") or 1
    results = []
    for address, (level, detector) in DETECTORS.items():
        verdict, detail = detector(repo)
        results.append({"rule": address, "level": level, "verdict": verdict, "detail": detail})
    import datetime

    apply_waivers(results, config.get("waiver", []), args.today or datetime.date.today().isoformat())
    if args.report:
        write_report(repo, claimed, results, Path(args.report))
    for problem in problems:
        print(problem)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['rule']:5} L{r['level']}  {r['verdict']:16} {r['detail']}")
    failing = [r for r in results if r["verdict"] == FAILED and r["level"] <= claimed]
    return 1 if failing or problems else 0


if __name__ == "__main__":
    sys.exit(main())
