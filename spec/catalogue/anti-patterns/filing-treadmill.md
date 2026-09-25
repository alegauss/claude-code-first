# Filing treadmill

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

An agent files tasks faster than it ships them, including tasks that describe nothing wrong.

## Context

roadkeep, Shio, winwright and freewilly, where an agent working through a backlog is told to
file the improvements its work revealed.

## Problem

Each observation made while working becomes a task. Some describe nothing wrong: a defect
that was the agent's own, a duplicate filed without reading the open lines, a premise nobody
measured. A loop told to stop when nothing remains never stops, and whoever picks up a wrong
filing pays more than the bug would have cost.

## Forces

- Filing is cheap and feels diligent.
- An observation has no other obvious home than a new task.
- The agent's reading of the tree, such as a truncated listing, can be wrong in ways it does
  not see.

## Refactored solution

Filing needed a bar: a task names something wrong, and an observation that revealed nothing
wrong goes in the commit body instead. A premise was measured before the task was built on it.
See [Measure first](../patterns/measure-first.md).

## Consequences

Some real observations are left in commit bodies, where a backlog query does not find them.
The retired shares at the pins are small, so the bar trims a minority of filings.

## Known uses

- roadkeep, over one session of 5 shipped and 10 filed, where "Three of those ten qualified" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L47],
  answered by "A task that revealed nothing wrong files nothing." [roadkeep@35fc90c2:.claude/skills/roadkeep-dev/SKILL.md#L41]
- Shio: "A filed defect that does not exist costs whoever picks it up more than the bug would have" [shio@c17ed995a].
- winwright: "Filed without reading Block E's open lines" [winwright@861b82e:docs/CHANGELOG.md#L198].
- freewilly: "Filed against the wrong writer" [freewilly@c1c2eaf:docs/CHANGELOG.md#L98].

## Related

- Rules: [CD-5](../../CD.md) and [PG-3](../../PG.md).
- Findings: [F102](../../../evidence/findings/F102.md).
