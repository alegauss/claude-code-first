# claude-code-first — Development Guide

**What this is.** An evidence-based specification of how to run a software project with
Claude Code as the primary author, distilled from five projects: roadkeep, polyweave,
freewilly, winwright and Shio. New projects adopt it; existing ones, those five included,
use it to realign when they have drifted.

## The three laws

A change that breaks one is wrong even if requested.

| # | Law |
|---|---|
| L1 | **Every normative statement traces to evidence**: a graded finding, or documented harness behaviour, cited by path and commit in the source project. A practice with no evidence is an open question, not a rule. |
| L2 | **Every artefact is in English**: specification, evidence, backlog, commits, code and comments. |
| L3 | **The governed docs are written by `roadkeep` only**: `docs/ROADMAP.md`, `CHANGELOG.md`, `IMPROVEMENTS.md` and `DECISIONS.md` are never hand-edited. |

## Layout

```
agents.md, roadkeep.toml   this file, and the backlog's configuration (prefix CCF)
.claude/CLAUDE.md          imports this file and nothing else
.claude/skills/            the detail, loaded when a task needs it
docs/                      the governed backlog, ledger, rationale and decisions
evidence/field-notes/      preliminary extraction per corpus project: leads, not evidence
```

## Where the rest is

- **Filing, picking or closing a task**: the `roadkeep` skill. Start with
  `roadkeep brief --claim`, file with `roadkeep add`, close with `roadkeep ship`, and run
  `roadkeep lint` before every commit. The rationale for an open task is its section in
  `docs/IMPROVEMENTS.md`, which `brief` prints.
- **Committing, and the gates before it**: the `ccf-dev` skill. One task, one commit,
  staged by path.
- **The corpus**: `evidence/field-notes/README.md` names each project's root. Nothing in
  the field notes may be cited until it is verified against a pinned commit.
