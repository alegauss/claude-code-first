# Orientation and pages

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A skill that outgrows one turn's budget becomes a capped orientation that points to pages,
each with a ceiling of its own.

## Context

roadkeep's shipped skill, which received the content that had left the every-turn file.
Shio's area files show the same growth where no ceiling was found. The remedy has one
origin, roadkeep; the growth it answers is recorded in both projects.

## Problem

Content moved out of the every-turn file leaves the only check that was counting it, and the
destination receives the additions the every-turn file used to receive. A skill's body is
paid in full on each turn that loads it, so a skill that grows becomes a large cost on
exactly the turns that need it.

## Forces

- Every page is a place where a finished task can write its reasoning down.
- A ceiling on the part that shrank says nothing about the parts that did not.
- Refusing content loses it; splitting keeps it but adds files to route between.

## Solution

roadkeep split its skill, which had reached 65,885 code units a turn, into an orientation
held under a ceiling and two pages. When the two uncapped pages grew, each was given a
figure of its own, and a page past its figure is split rather than refused.

## Consequences

What one turn loads is bounded: the orientation landed at 11,148 units. The total the project
carries is not, and roadkeep calls its ceilings a cadence rather than a size. The ceiling
works only where it is set: the first split left two pages uncapped, and one later task added
1,361 units to one of them. No source records a skill ceiling failing a build. Without any
ceiling, Shio's area files grew from 184,521 bytes at the split to 1,730,001.

## Known uses

- roadkeep: "the split landed at 11,148 against 65,885 before it," [roadkeep@91754240:tests/test_skill.py#L133]
  under "ORIENTATION_MAX = 13_000" [roadkeep@91754240:tests/test_skill.py#L136].
- roadkeep: "RK1437 gave the ceiling to the half that shrank and left these two unbounded" [roadkeep@91754240:tests/test_skill.py#L144],
  answered by RK1643 [roadkeep@d849f061], under which "a page past it is a page to split" [roadkeep@91754240:docs/CHANGELOG.md#L824].

## Related

- Resolves: [Moved bloat](../anti-patterns/moved-bloat.md).
- Rules: [IS-4](../../IS.md) and [IS-2](../../IS.md).
- Findings: [F3](../../../evidence/findings/F3.md) and [F2](../../../evidence/findings/F2.md).
- Patterns: [Trigger-loaded skill](trigger-loaded-skill.md) and
  [Budget as a gate](budget-as-a-gate.md).
