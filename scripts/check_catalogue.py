"""Hold every catalogue entry to the form in spec/catalogue/README.md.

Each file under spec/catalogue/patterns/ and spec/catalogue/anti-patterns/ must have a
`# <Name>` title, a field table with a Kind matching its folder and a grade R1-R4/S1-S4,
every section of its kind in order, no RFC 2119 keyword outside code (entries describe;
rules prescribe), and a Related section that links at least one rule address in a
chapter. Run from the repository root; exit 1 on any problem.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CATALOGUE = Path("spec/catalogue")
KINDS = {"patterns": "pattern", "anti-patterns": "anti-pattern"}
COMMON = ["Intent", "Context", "Problem", "Forces"]
TAIL = ["Consequences", "Known uses", "Related"]
SECTIONS = {
    "pattern": COMMON + ["Solution"] + TAIL,
    "anti-pattern": COMMON + ["Refactored solution"] + TAIL,
}
KEYWORDS = re.compile(r"\b(MUST|SHALL|SHOULD|REQUIRED|RECOMMENDED|MAY|OPTIONAL)\b")
CODE = re.compile(r"`[^`\n]*`")
RULE_LINK = re.compile(r"\]\((?:\.\./)+[A-Z]{2}\.md(?:#[^)]*)?\)")
FIELD = re.compile(r"^\|\s*(Kind|Grade)\s*\|\s*(.*?)\s*\|\s*$")
GRADE = re.compile(r"^R[1-4]/S[1-4]$")


def check(path: Path, kind: str) -> list[str]:
    where = path.as_posix()
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    problems = []
    if not lines or not lines[0].startswith("# "):
        problems.append(f"{where}: first line is not a '# <Name>' title")
    fields = dict(m.groups() for m in map(FIELD.match, lines) if m)
    if fields.get("Kind") != kind:
        problems.append(f"{where}: Kind must be {kind!r} in this folder")
    if not GRADE.match(fields.get("Grade", "")):
        problems.append(f"{where}: Grade must be R1-R4/S1-S4")
    headings = [line[3:].strip() for line in lines if line.startswith("## ")]
    if headings != SECTIONS[kind]:
        problems.append(f"{where}: sections must be {', '.join(SECTIONS[kind])}, in that order")
    prose, fenced = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            prose.append(CODE.sub("", line))
    for keyword in sorted(set(KEYWORDS.findall("\n".join(prose)))):
        problems.append(f"{where}: uses the keyword {keyword}; entries describe, rules prescribe")
    related = text.split("\n## Related", 1)[1] if "\n## Related" in text else ""
    if not RULE_LINK.search(related):
        problems.append(f"{where}: Related links no rule in a chapter")
    return problems


def main(argv: list[str] | None = None) -> int:
    root = Path(argv[0]) if argv else Path(".")
    problems, entries = [], 0
    for folder, kind in KINDS.items():
        for path in sorted((root / CATALOGUE / folder).glob("*.md")):
            entries += 1
            problems += check(path, kind)
    for problem in problems:
        print(problem)
    print(f"{entries} entr{'y' if entries == 1 else 'ies'} checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
