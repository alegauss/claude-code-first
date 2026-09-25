# Resident encyclopedia

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

The file loaded on every turn becomes the place where everything is written down.

## Context

Shio and roadkeep, each with an instruction file that the harness loads on every turn of
every session, worked by agents that finish tasks at a steady rate.

## Problem

A finished task's rationale is cheapest to record in the every-turn file, so each task adds
to it and none removes from it. The whole file, with what it imports, is paid on every turn,
including the turns that need none of it. A budget written into the same file is read by the
agent that is adding to it and checked by nothing.

## Forces

- The every-turn file is the one place every future session is sure to read.
- Removing a paragraph needs a decision about where it goes; adding one needs none.
- The cost is spread thinly over every turn, so no single addition looks expensive.

## Refactored solution

The every-turn file became an index held to a budget by a gate. roadkeep moved its budget
out of prose and into the gate, counting bytes as well as lines; when the file reached the
ceiling, content was compressed or moved into a skill. Shio split its file into an index and
area files. See [Index, not encyclopedia](../patterns/index-not-encyclopedia.md) and
[Budget as a gate](../patterns/budget-as-a-gate.md).

## Consequences

A gated file forces a choice at each addition about what to move or cut. The moved content
does not stop growing where it lands (see [Moved bloat](moved-bloat.md)).

## Known uses

- Shio, whose file carried the law "Tokens are a measured budget" [shio@821f18d74:agents.md#L22]
  while it grew from 9,843 bytes [shio@6bf11b754] to 185,734 [shio@e73516a9f], and which
  records "P3 violated by the file that declares P3" [shio@821f18d74:agents.md#L283-L285].
- roadkeep, where "budget --file agents.md answers 125 of 125, 0 left" [roadkeep@a3ecd54c],
  and after a move into a skill "the every-turn file dropped to 104 of 125 lines" [roadkeep@91754240:docs/CHANGELOG.md#L667].

## Related

- Rules: [IS-1](../../IS.md) and [IS-2](../../IS.md).
- Findings: [F1](../../../evidence/findings/F1.md), [F2](../../../evidence/findings/F2.md).
