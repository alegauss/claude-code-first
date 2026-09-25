# Batch commit

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

Several finished tasks ship in one commit.

## Context

winwright, roadkeep and freewilly, each with a written one-task-one-commit rule, and a
request to work through a block of tasks. polyweave is the contrary case: none of its 110
ship commits records two ships.

## Problem

The rule lives in a skill or an every-turn file, and nothing refuses a commit that ships two
tasks. A request to work through a block invites the agent to finish several tasks and
commit once, which ties unrelated changes to one message and one revert.

## Forces

- The request names several tasks at once and reads as one unit of work.
- One commit at the end is less overhead than one per task.
- The rule is prose, and prose does not refuse a commit (see [Rule in prose](rule-in-prose.md)).

## Refactored solution

A batch request is worked as a loop that validates, ships and commits one task per
iteration. Each project's rule singles out the multi-task request as not being permission to
batch.

## Consequences

Counted from the ledgers, batching commits are a small share: under 1 percent of ship
commits in roadkeep, about 4 percent in winwright, clustered in one week. The loop costs one
commit step per task.

## Known uses

- winwright, whose skill says a batch request "is not permission to batch" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L39-L40],
  and which shipped "fix(WW216,WW217,WW219,WW220): keep a limit where its value is read and a claim to what was observed" [winwright@03e119b].
- roadkeep, whose rule is "One task → one commit, the instant it is validated." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L61-L62]
  and which shipped "feat: RK1398-RK1400 - a documentation area, built by a workflow and never committed" [roadkeep@4c1caa58].
- freewilly, which calls it "the single most violated rule" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L10-L11]
  and shipped "fix(engine): DD267 and DD269 keep a start from racing the engine unpack" [freewilly@7bef7a5].

## Related

- Rules: [CD-1](../../CD.md) and [CD-2](../../CD.md).
- Findings: [F203](../../../evidence/findings/F203.md).
