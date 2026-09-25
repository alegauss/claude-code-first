# example: Development Guide

<!-- IS-1, IS-2: this file is loaded on every turn, so it is an index, and its budget is
declared in roadkeep.toml and enforced by roadkeep lint. Keep only what a turn that
touches no specific area needs; everything else goes in a skill. -->

**What this is.** One sentence on what the project does, and one on who uses it.

## Laws

| # | Law |
|---|---|
| L1 | The rule a change must never break, even if asked. |
| L2 | The planning files are written by the planning tool only. |

## Layout

```
agents.md, roadkeep.toml   this file, and the planning tool's configuration
.claude/                   the Claude Code pointer, settings, hooks and skills
docs/                      the governed roadmap, ledger, rationale and decisions
src/, tests/               the code and its tests
```

## Where the rest is

- **Committing, and the gates before it**: the `example-dev` skill.
- **Writing anything a person reads**: the `example-writing` skill.
