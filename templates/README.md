# Reference templates

A minimal conforming file for each artefact a project needs, to copy into a new or
realigning repository and then edit. Each file names, in a comment, the rules it
implements. `scripts/test_templates.py` assembles a repository from this folder and runs
the conformance checker on it at level 2, so a template that stops conforming fails the
build here before it spreads.

Dotfiles are stored with a `dot-` prefix (`dot-claude/`, `dot-gitignore`), so that a
session working in this repository never reads the example project's `.claude/` as its
own. `python scripts/assemble_templates.py <target>` writes them under their real names.

| File | Implements |
|---|---|
| `agents.md` | IS-1, IS-2: a short index loaded every turn |
| `.claude/CLAUDE.md` | IS-2: a pointer that imports `agents.md` and holds nothing else |
| `.claude/settings.json` | PG-1, GH-1, PS-1, PS-2: guards wired, prompts kept for irreversible actions |
| `.gitignore` | PS-3, CD-3: logs, caches and credentials kept out of any commit |
| `.gitattributes` | EP-2: line terminators declared; planning files merged by entry |
| `roadkeep.toml` | PG-1, IS-1, AW-2: governed planning files, budgets, length limits |
| `.github/workflows/check.yml` | VG-5, VG-1: the gates and the conformance checker on every push |
| `.claude/skills/example-dev/SKILL.md` | CD-1 to CD-6, VG-1: how finished work becomes a commit |
| `.claude/skills/example-writing/SKILL.md` | AW-1, AW-3: the project's writing rules, and what checks them |
| `ccf.toml` | the claimed level and specification version, and any waivers |

## What is not copied here

Two files are generated or canonical elsewhere, and a copy here would drift from its
source, which is the failure rule GH-6 exists to catch:

- **The hook launcher**, `.claude/hooks/roadkeep-launch.py`, is written by
  `roadkeep install --committed`, which also records the engine version that wrote it.
- **The no-clobber hook**, `.claude/hooks/no-clobber.py`, is vendored from polyweave with
  its source commit in its header; take it from this repository's `.claude/hooks/`.

## Using them

1. Run `python scripts/assemble_templates.py <repository>`, then replace `example`, `EX`
   and the placeholder text with the project's own names.
2. Run `roadkeep install --committed` to write the launcher, and copy the no-clobber hook.
3. Lower the budgets in `roadkeep.toml` to just above the size the files land at.
4. Run `python <path-to-this-repository>/scripts/check_conformance.py .` and fix what it
   reports before the first commit.
