---
name: example-dev
description: How finished work in this repository becomes a commit, and the gates it passes first. Use before any commit, stage, ship or filing of a task, and whenever several tasks are to be worked.
---

# Committing work in example

<!-- CD-1 to CD-6 and VG-1. Loaded when a turn commits, not on every turn (IS-2). -->

## One task, one commit

- A task is finished when its commit lands, carrying its code, its tests and its ledger
  entry together.
- Several tasks are worked one at a time: each committed, after its gates pass on the
  tree that commit holds, before the next begins.
- A task is filed only when it names something observed to be wrong or missing.

## The gates

Run every gate before committing, and let a red gate stop the work. Never pipe a gate's
output through a filter that can hide its exit status.

| Command | What it holds |
|---|---|
| `roadkeep lint` | the governed planning files and the every-turn budgets |
| the project's test command | the behaviour |

## Staging and the message

1. `git status --short` first; a file this task did not write belongs to someone else.
2. `git add -- <this task's paths>`, never everything.
3. Write the title yourself, conventional-commits style with the task id, and the body
   as what changed and why. State whether commits carry attribution: this project's
   choice is recorded here.
