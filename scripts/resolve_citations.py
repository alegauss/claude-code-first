"""Check every evidence pointer in the repository against the pinned corpus.

A pointer names a corpus project, a commit, and optionally a path and a line range:

    [shio@821f18d74]                       a commit
    [shio@821f18d74:agents.md]             a file at that commit
    [shio@821f18d74:agents.md#L247]        one line
    [shio@821f18d74:agents.md#L247-L251]   a range

A quoted string directly before a pointer is a quote the pointer vouches for:
"the single most violated rule" [shio@821f18d74:agents.md#L247] must find that text,
whitespace aside, within those lines (within the file with no range, and in the commit
message for a bare commit). A quote may wrap onto the line before its pointer, may keep
backticks, and may run across the lines of a source comment; see `quoted`.

The grammar and the reasons for it are in evidence/method.md. Pointers inside fenced
code blocks or inline code are examples and are not checked.

Each pointer is checked for: a project named in evidence/corpus.md; a commit that exists
and lies in the history of that project's pin; a path that exists at that commit; a line
range inside the file; and the quote. Exit 1 if any check fails, or if a project could
not be reached and is not named with --allow-unreachable.

Sources are found, in order: `--source name=path`; the environment variable
`CCF_SOURCE_<NAME>`; a partial clone of the remote in evidence/corpus.md, kept under
.cache/corpus/. Run from the repository root.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

CORPUS = Path("evidence/corpus.md")
SCANNED = ("evidence", "spec", "adoption")
CACHE = Path(".cache/corpus")

# A quote may wrap across lines, and may sit on the line before its pointer, but never
# across a blank line: a quote that crosses a paragraph is no longer one sentence.
POINTER = re.compile(
    r"(?:[\"“](?P<quote>(?:(?!\n[ \t]*\n)[^\"“”]){1,400})[\"”]\s*)?"
    r"\[(?P<project>[a-z][a-z0-9-]*)@(?P<commit>[0-9a-f]{7,40})"
    r"(?::(?P<path>[^\]\s#]+)(?:#L(?P<start>\d+)(?:-L(?P<end>\d+))?)?)?\]"
)
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
COMMENT_MARKER = re.compile(r"^\s*(?:///|//|#|\*|--|;)\s?")
FORMATTING = re.compile(r"[`*]")
PIN_ROW = re.compile(
    r"^\|\s*(?P<name>[^|]+?)\s*\|\s*`(?P<remote>[^`]+)`\s*\|[^|]*\|\s*`(?P<pin>[0-9a-f]{40})`"
)


@dataclass
class Pointer:
    file: Path
    line: int
    text: str
    project: str
    commit: str
    path: str | None
    start: int | None
    end: int | None
    quote: str | None


def read_pins(corpus: Path) -> dict[str, tuple[str, str]]:
    """Map each project name, lower-cased, to (remote, pinned commit) from corpus.md."""
    pins = {}
    for row in corpus.read_text(encoding="utf-8").splitlines():
        match = PIN_ROW.match(row)
        if match:
            pins[match["name"].lower()] = (match["remote"], match["pin"])
    return pins


def prose(text: str) -> str:
    """The text with fenced code blocks blanked out, line count kept."""
    lines, fenced = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            fenced = not fenced
            lines.append("")
        else:
            lines.append("" if fenced else line)
    return "\n".join(lines)


def scan(root: Path) -> list[Pointer]:
    """Every pointer in the scanned Markdown files, outside code.

    A whole file is matched at once, so a quote that wraps onto the line before its
    pointer is still read as its quote (CCF63). A pointer that starts inside an inline
    code span is an example and is skipped; code inside a quote is kept as written.
    """
    found = []
    for top in SCANNED:
        for md in sorted((root / top).rglob("*.md")):
            text = prose(md.read_text(encoding="utf-8").replace("\r\n", "\n"))
            spans = [m.span() for m in INLINE_CODE.finditer(text)]
            for m in POINTER.finditer(text):
                opening = m.start("project") - 1
                if any(start <= opening < end for start, end in spans):
                    continue
                found.append(
                    Pointer(
                        file=md.relative_to(root),
                        line=text.count("\n", 0, opening) + 1,
                        text=" ".join(m.group(0).split()),
                        project=m["project"],
                        commit=m["commit"],
                        path=m["path"],
                        start=int(m["start"]) if m["start"] else None,
                        end=int(m["end"]) if m["end"] else (int(m["start"]) if m["start"] else None),
                        quote=" ".join(m["quote"].split()) if m["quote"] else None,
                    )
                )
    return found


def quoted(quote: str, haystack: str) -> bool:
    """Whether the quote occurs in the source text, whitespace aside.

    Two looser readings are tried after the literal one: with a comment marker (`///`,
    `//`, `#`, `*`) dropped from each source line, so a quote can run across the lines of
    a doc comment; and with Markdown emphasis and backticks dropped from both sides, so a
    quote need not reproduce the source's bold or code formatting.
    """
    wanted = normalise(quote)
    if wanted in normalise(haystack):
        return True
    uncommented = "\n".join(COMMENT_MARKER.sub("", line) for line in haystack.splitlines())
    if wanted in normalise(uncommented):
        return True
    plain = normalise(FORMATTING.sub("", quote))
    return plain in normalise(FORMATTING.sub("", uncommented))


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace"
    )


def locate(name: str, remote: str, pin: str, sources: dict[str, str], root: Path) -> Path | None:
    """A local repository holding the pin, or None where none can be reached."""
    given = sources.get(name) or os.environ.get(f"CCF_SOURCE_{name.upper().replace('-', '_')}")
    if given:
        repo = Path(given)
    else:
        repo = root / CACHE / name
        url = remote if "://" in remote else f"https://{remote}.git"
        if not (repo / "HEAD").exists() and not (repo / ".git").exists():
            repo.parent.mkdir(parents=True, exist_ok=True)
            cloned = subprocess.run(
                ["git", "clone", "--quiet", "--bare", "--filter=blob:none", url, str(repo)],
                capture_output=True,
                text=True,
                env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
            )
            if cloned.returncode != 0:
                return None
    if git(repo, "cat-file", "-e", f"{pin}^{{commit}}").returncode != 0:
        git(repo, "fetch", "--quiet", "--filter=blob:none", "origin", pin)
    if git(repo, "cat-file", "-e", f"{pin}^{{commit}}").returncode != 0:
        return None
    return repo


def normalise(text: str) -> str:
    return " ".join(text.split())


class Source:
    """One corpus repository, read through a single `git cat-file --batch` process.

    Spawning git once per pointer made a full run take minutes (CCF64). Here every object
    is read through one long-lived process, the pin's ancestry is listed once as a set,
    and each object is read at most once.
    """

    def __init__(self, repo: Path, pin: str):
        self.batch = subprocess.Popen(
            ["git", "-C", str(repo), "cat-file", "--batch"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )
        history = git(repo, "rev-list", pin)
        self.ancestry = set(history.stdout.split())
        self.objects: dict[str, tuple[str, bytes] | None] = {}

    def read(self, rev: str) -> tuple[str, bytes] | None:
        """(sha, content) of an object, or None where the revision names none."""
        if rev not in self.objects:
            self.batch.stdin.write(rev.encode("utf-8") + b"\n")
            self.batch.stdin.flush()
            header = self.batch.stdout.readline().decode("utf-8", "replace").split()
            if len(header) != 3:
                self.objects[rev] = None
            else:
                content = self.batch.stdout.read(int(header[2]))
                self.batch.stdout.read(1)
                self.objects[rev] = (header[0], content)
        return self.objects[rev]

    def close(self):
        self.batch.stdin.close()
        self.batch.wait()
        self.batch.stdout.close()


def check(pointer: Pointer, source: Source, pin: str) -> str | None:
    """The reason a pointer does not resolve, or None where it does."""
    found = source.read(f"{pointer.commit}^{{commit}}")
    if found is None:
        return f"no commit {pointer.commit} in {pointer.project}"
    commit, body = found
    if commit not in source.ancestry:
        return f"{pointer.commit} is not in the history of the {pointer.project} pin {pin[:12]}"
    if pointer.path is None:
        text = body.decode("utf-8", "replace")
        haystack = text.split("\n\n", 1)[1] if "\n\n" in text else ""
    else:
        shown = source.read(f"{commit}:{pointer.path}")
        if shown is None:
            return f"no file {pointer.path} at {pointer.commit}"
        haystack = shown[1].decode("utf-8", "replace")
        lines = haystack.splitlines()
        if pointer.start is not None:
            if pointer.start < 1 or pointer.end < pointer.start:
                return f"line range L{pointer.start}-L{pointer.end} is empty"
            if pointer.end > len(lines):
                return f"{pointer.path} has {len(lines)} lines at {pointer.commit}, not {pointer.end}"
            haystack = "\n".join(lines[pointer.start - 1 : pointer.end])
    if pointer.quote and not quoted(pointer.quote, haystack):
        return f'quote "{pointer.quote}" not found there'
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", action="append", default=[], metavar="NAME=PATH",
                        help="a local repository for one project")
    parser.add_argument("--allow-unreachable", action="append", default=[], metavar="NAME",
                        help="a project whose pointers may go unchecked when it cannot be reached")
    parser.add_argument("--root", default=".", help="the repository to scan")
    args = parser.parse_args(argv)

    root = Path(args.root)
    sources = dict(item.split("=", 1) for item in args.source)
    pins = read_pins(root / CORPUS)
    pointers = scan(root)

    failures, unreachable, resolved = [], {}, 0
    repos: dict[str, Source | None] = {}
    for pointer in pointers:
        where = f"{pointer.file.as_posix()}:{pointer.line}: {pointer.text}"
        if pointer.project not in pins:
            failures.append(f"{where}: {pointer.project} is not a project in {CORPUS.as_posix()}")
            continue
        remote, pin = pins[pointer.project]
        if pointer.project not in repos:
            repo = locate(pointer.project, remote, pin, sources, root)
            repos[pointer.project] = Source(repo, pin) if repo else None
        source = repos[pointer.project]
        if source is None:
            unreachable[pointer.project] = unreachable.get(pointer.project, 0) + 1
            continue
        reason = check(pointer, source, pin)
        if reason:
            failures.append(f"{where}: {reason}")
        else:
            resolved += 1
    for source in repos.values():
        if source:
            source.close()

    for failure in failures:
        print(failure)
    refused = {name: n for name, n in unreachable.items() if name not in args.allow_unreachable}
    for name, n in sorted(unreachable.items()):
        state = "allowed" if name not in refused else "a failure"
        print(f"{name}: unreachable, {n} pointer(s) unchecked ({state})")
    print(f"{len(pointers)} pointer(s): {resolved} resolved, {len(failures)} failed, "
          f"{sum(unreachable.values())} unchecked")
    return 1 if failures or refused else 0


if __name__ == "__main__":
    sys.exit(main())
