"""Cap the size of every skill this repository writes.

A skill's description is loaded on every turn, so it is priced like an every-turn file;
its body loads only when the skill triggers, and a body that keeps growing is a rule that
belongs on a page of its own. The two caps are winwright's (`SkillTests.cs`): 700
characters of description and 6,000 of body.

`.claude/skills/roadkeep/` is left out: `roadkeep install` writes it, and
`roadkeep install --check` is what holds it.

Exit 1 when any skill is over a cap or has no description. Run from the repository root.
"""

import sys
from pathlib import Path

DESCRIPTION_MAX = 700
BODY_MAX = 6000
SKILLS = Path(".claude/skills")
PLUGIN_SKILLS = Path("skills")  # the skills the audit plugin ships to other repositories
TEMPLATE_SKILLS = Path("templates/dot-claude/skills")  # the skills adopters copy
NOT_OURS = {"roadkeep"}


def split(text):
    """Return (description, body) of a SKILL.md, or (None, text) with no frontmatter."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    description = None
    for line in text[4:end].splitlines():
        if line.startswith("description:"):
            description = line[len("description:"):].strip().strip('"')
    return description, text[end + 5:]


def main():
    failures = []
    checked = 0
    for skill in sorted([*SKILLS.glob("*/SKILL.md"), *PLUGIN_SKILLS.glob("*/SKILL.md"),
                         *TEMPLATE_SKILLS.glob("*/SKILL.md")]):
        if skill.parent.name in NOT_OURS:
            continue
        checked += 1
        description, body = split(skill.read_text(encoding="utf-8-sig"))
        if not description:
            failures.append(f"{skill}: no description in the frontmatter")
            continue
        if len(description) > DESCRIPTION_MAX:
            failures.append(
                f"{skill}: description is {len(description)} characters, cap is {DESCRIPTION_MAX}"
            )
        if len(body) > BODY_MAX:
            failures.append(f"{skill}: body is {len(body)} characters, cap is {BODY_MAX}")
    for failure in failures:
        print(failure)
    print(f"{checked} skill(s) checked, {len(failures)} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
