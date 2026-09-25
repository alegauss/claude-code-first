# Index, not encyclopedia

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

The every-turn file holds what a turn touching no specific area needs, and points to the
rest.

## Context

Shio and roadkeep, each with an every-turn instruction file that grew with the work. The
pattern applies only where a project has such a file: freewilly and winwright have none
and keep their rules in skills.

## Problem

Everything in the every-turn file, and everything it imports, is paid on every turn. The
file is where a finished task's reasoning is cheapest to write down, so it grows into a
resident encyclopedia of rules that most turns never use.

## Forces

- A rule written where every session reads it feels like the rule most likely to be kept.
- Most rules are needed only on some turns: building, committing, writing a governed file.
- Moving content needs a destination and a pointer that sends the agent there.

## Solution

The file keeps orientation and pointers. Detail moves to trigger-loaded skills or to files
read on demand, and a written rule keeps it out afterwards. Shio split its 185,734-byte file
into an index of 14,433 bytes, area files and eight skills. roadkeep moved 26 lines needed
only on build or commit turns into a project skill, taking its file from 125 to 104 of 125
lines.

## Consequences

The every-turn file shrank by counted amounts. The total did not: at Shio's split the area
files and skills held more than the bytes they replaced, and they kept growing where they
landed. Whether a task then read less in total is not known, since what a session read is
only in transcripts. The index needs a budget of its own, or it grows back, and each pointer
is one more place a name can go stale.

## Known uses

- Shio: "it is deliberately thin: it is loaded into every session on every turn, so P3 applies to it" [shio@821f18d74:agents.md#L61-L62],
  after the split [shio@f4ffdb0d9].
- roadkeep: "26 lines of the every-turn file are needed only on a turn that builds or commits" [roadkeep@91754240:docs/CHANGELOG.md#L667],
  kept out by "What loads every turn is only what a turn touching no governed file needs." [roadkeep@91754240:agents.md#L111]

## Related

- Resolves: [Resident encyclopedia](../anti-patterns/resident-encyclopedia.md).
- Rules: [IS-2](../../IS.md), [IS-1](../../IS.md) and [IS-4](../../IS.md).
- Findings: [F2](../../../evidence/findings/F2.md), [F1](../../../evidence/findings/F1.md)
  and [F3](../../../evidence/findings/F3.md).
- Patterns: [Trigger-loaded skill](trigger-loaded-skill.md),
  [Budget as a gate](budget-as-a-gate.md) and [Orientation and pages](orientation-and-pages.md).
