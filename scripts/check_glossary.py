"""Fail when a rule uses a term the glossary does not define.

In a rule's normative sentence (the bold line under a rule heading such as `### IS-3 ...`),
a defined term is written in italics. Every italic term there must match, ignoring case,
a `## ` heading in spec/glossary.md. Run from the repository root; exit 1 on any term
without an entry.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SPEC = Path("spec")
GLOSSARY = SPEC / "glossary.md"
RULE = re.compile(r"^### [A-Z]{2}-\d+ ")
SENTENCE = re.compile(r"^\*\*(.+)\*\*\s*$")
ITALIC = re.compile(r"(?<![*\w])\*([^*]+)\*(?![*\w])|(?<!\w)_([^_]+)_(?!\w)")


def terms(root: Path) -> set[str]:
    text = (root / GLOSSARY).read_text(encoding="utf-8")
    return {line[3:].strip().lower() for line in text.splitlines() if line.startswith("## ")}


def used(root: Path) -> list[tuple[str, int, str]]:
    """(file, line, term) for every italic term in a rule's normative sentence."""
    found = []
    for chapter in sorted((root / SPEC).glob("*.md")):
        lines = chapter.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines):
            if not RULE.match(line):
                continue
            for offset, candidate in enumerate(lines[number + 1 : number + 4], number + 2):
                sentence = SENTENCE.match(candidate)
                if sentence:
                    for m in ITALIC.finditer(sentence.group(1)):
                        found.append((chapter.as_posix(), offset, (m.group(1) or m.group(2)).strip()))
                    break
    return found


def main(argv: list[str] | None = None) -> int:
    root = Path(argv[0]) if argv else Path(".")
    defined = terms(root)
    missing = [(f, n, t) for f, n, t in used(root) if t.lower() not in defined]
    for file, line, term in missing:
        print(f"{file}:{line}: '{term}' is used in a rule and has no entry in {GLOSSARY.as_posix()}")
    print(f"{len(defined)} term(s) defined, {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
