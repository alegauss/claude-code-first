---
name: ccf-dev
description: How a finished task in this repository becomes a commit, and the gates it passes first. Use before any commit, stage, `roadkeep ship`, `roadkeep add` or filing of a task here, and whenever a batch of CCF ids is to be worked.
---

# Committing work in claude-code-first

Loaded when a turn commits, stages, ships or files, and not on every turn: 26 lines of
roadkeep's every-turn file were needed only on a turn that builds or commits (roadkeep
RK1136, `b12d28b5`). Citations below are to the field notes in `evidence/field-notes/`,
which are leads still to be verified (CCF11).

## One task, one commit

- **A task is finished when its commit lands**, and what `roadkeep ship` wrote goes in
  that same commit, so the governed docs never describe work that did not ship. Shio and
  freewilly each call this the most violated rule in the project (Shio agents.md L247;
  freewilly's `freewilly-roadmap-docs` skill).
- **Never do a second task before committing the first.** A request naming a block or
  several ids is a request to run them one at a time. A batch of two or more runs under
  `/loop`, one task per iteration (Shio agents.md L250-251).
- **Before growing `agents.md`**, `roadkeep budget --file agents.md` says what room is
  left; the budget is lowered when content moves out, never raised to fit.
- **Before starting the next task**, `git status --short` holds none of the last one's
  files.

## Stage by path

1. `git status --short` first. Anything listed that this task did not write belongs to
   someone else, often another session in the same checkout (roadkeep RK280, RK1117).
2. `git add -- <this task's paths>`: the code, and the governed docs `ship` printed in its
   `stage` line. Never `git add -A`, `.` or `*`.
3. `git diff --cached --stat` lists this task's files and nothing else.

`run-commit.cmd` stages everything, which is how Shio committed `sh545.log` (`b04ee918`).
Use it only when step 1 shows nothing but this task's files, and then always with
`-m "<title>"`: without it a docs commit describing shipped work is misread as a feature.

## The message

Write it to a scratchpad file and run `git commit -F <file>` from the repository root.
A message composed on the command line can lose an em dash or an accent on the way
(roadkeep RK1474).

- Title: conventional commits, ASCII, the task id last: `docs(spec): <outcome> (CCF24)`.
  Add `, with CCF<n> filed` when the task filed new lines.
- Body: a few plain lines on what changed and why, and anything left unverified.
- No `Co-Authored-By` trailer, no "Generated with" line, no `--author`, no `--no-verify`.
- Never push. Commits stay local until the owner pushes them.

## The gates

Run all of them before every commit. A red gate is fixed, never skipped.

| Command | What it holds |
|---|---|
| `python .claude/hooks/roadkeep-launch.py lint` | the governed docs, and the `[budgets]` on the every-turn files |
| `python scripts/check_skills.py` | the size caps on every skill this repository writes |
| `npx markdownlint-cli2 "**/*.md"` | the rule set in `.markdownlint-cli2.jsonc` |
| `lychee --config lychee.toml "./**/*.md"` | every internal link and anchor; with no local lychee, run the `lycheeverse/lychee` image with the repository mounted at `/input` |

CI runs the same four on every push (`.github/workflows/`), so a local green that CI
turns red means the two have drifted.

## Filing what a task revealed

A task that revealed nothing wrong files nothing. roadkeep once shipped 5 tasks and filed
10, of which 3 were real, and a loop told to stop when nothing remained could never stop
(roadkeep `35fc90c2`). Before `add`, check `delivered <block> --near "<symptom>" --open`
and `non-goal list`; a line already covering the finding gets a `section amend` instead.
