"""Check every evidence pointer in the repository against the pinned corpus.

A pointer names a corpus project, a commit, and optionally a path and a line range:

    [shio@821f18d74]                       a commit
    [shio@821f18d74:agents.md]             a file at that commit
    [shio@821f18d74:agents.md#L247]        one line
    [shio@821f18d74:agents.md#L247-L251]   a range

A quoted string directly before a pointer is a quote the pointer vouches for:
"the single most violated rule" [shio@821f18d74:agents.md#L247] must find that text,
whitespace aside, within those lines (within the file with no range, and in the commit
message for a bare commit).

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
SCANNED = ("evidence", "spec")
CACHE = Path(".cache/corpus")

POINTER = re.compile(
    r"(?:[\"“](?P<quote>[^\"“”\n]+)[\"”]\s*)?"
    r"\[(?P<project>[a-z][a-z0-9-]*)@(?P<commit>[0-9a-f]{7,40})"
    r"(?::(?P<path>[^\]\s#]+)(?:#L(?P<start>\d+)(?:-L(?P<end>\d+))?)?)?\]"
)
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
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


def scan(root: Path) -> list[Pointer]:
    """Every pointer in the scanned Markdown files, outside code."""
    found = []
    for top in SCANNED:
        for md in sorted((root / top).rglob("*.md")):
            fenced = False
            for number, raw in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
                if FENCE.match(raw):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                line = INLINE_CODE.sub("", raw)
                for m in POINTER.finditer(line):
                    found.append(
                        Pointer(
                            file=md.relative_to(root),
                            line=number,
                            text=m.group(0),
                            project=m["project"],
                            commit=m["commit"],
                            path=m["path"],
                            start=int(m["start"]) if m["start"] else None,
                            end=int(m["end"]) if m["end"] else (int(m["start"]) if m["start"] else None),
                            quote=m["quote"],
                        )
                    )
    return found


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


def check(pointer: Pointer, repo: Path, pin: str) -> str | None:
    """The reason a pointer does not resolve, or None where it does."""
    full = git(repo, "rev-parse", "--verify", "--quiet", f"{pointer.commit}^{{commit}}")
    if full.returncode != 0:
        return f"no commit {pointer.commit} in {pointer.project}"
    commit = full.stdout.strip()
    if git(repo, "merge-base", "--is-ancestor", commit, pin).returncode != 0:
        return f"{pointer.commit} is not in the history of the {pointer.project} pin {pin[:12]}"
    if pointer.path is None:
        haystack = git(repo, "log", "-1", "--format=%B", commit).stdout
    else:
        shown = git(repo, "show", f"{commit}:{pointer.path}")
        if shown.returncode != 0:
            return f"no file {pointer.path} at {pointer.commit}"
        lines = shown.stdout.splitlines()
        haystack = shown.stdout
        if pointer.start is not None:
            if pointer.start < 1 or pointer.end < pointer.start:
                return f"line range L{pointer.start}-L{pointer.end} is empty"
            if pointer.end > len(lines):
                return f"{pointer.path} has {len(lines)} lines at {pointer.commit}, not {pointer.end}"
            haystack = "\n".join(lines[pointer.start - 1 : pointer.end])
    if pointer.quote and normalise(pointer.quote) not in normalise(haystack):
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
    repos: dict[str, Path | None] = {}
    for pointer in pointers:
        where = f"{pointer.file.as_posix()}:{pointer.line}: {pointer.text}"
        if pointer.project not in pins:
            failures.append(f"{where}: {pointer.project} is not a project in {CORPUS.as_posix()}")
            continue
        remote, pin = pins[pointer.project]
        if pointer.project not in repos:
            repos[pointer.project] = locate(pointer.project, remote, pin, sources, root)
        repo = repos[pointer.project]
        if repo is None:
            unreachable[pointer.project] = unreachable.get(pointer.project, 0) + 1
            continue
        reason = check(pointer, repo, pin)
        if reason:
            failures.append(f"{where}: {reason}")
        else:
            resolved += 1

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
