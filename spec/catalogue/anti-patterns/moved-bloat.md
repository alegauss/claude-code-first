# Moved bloat

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A split of the every-turn file relocates its growth instead of ending it.

## Context

Shio and roadkeep, after each moved content out of the every-turn file into skills or area
files that load only on the turns that need them.

## Problem

Moving content into a trigger-loaded file takes it out of the every-turn budget, and with it
out of the only check that was counting it. The destination then receives the additions the
every-turn file used to receive. A skill's body is paid in full on each turn that loads it,
so a skill that grows becomes a large cost on exactly the turns that trigger it.

## Forces

- The split is recorded as a success, measured at the moment it lands.
- The new file has no budget of its own unless someone adds one.
- A ceiling given to one half of a split says nothing about the other half.

## Refactored solution

Each file that took content out of the every-turn file was given a ceiling of its own.
roadkeep split its skill into an orientation and two pages, capped the orientation, then
capped each page after the two it had left unbounded grew, with the rule that a page past its
figure is a page to split. See [Orientation and pages](../patterns/orientation-and-pages.md).

## Consequences

A ceiling per file bounds what one turn loads, not the total the project carries. Each new
file is one more figure to maintain.

## Known uses

- Shio, where docs/agents/build.md went from 5,238 bytes [shio@f4ffdb0d9] to 149,685
  [shio@821f18d74:docs/agents/build.md] with no size limit found at the pin.
- roadkeep, where "the split landed at 11,148 against 65,885 before it," [roadkeep@91754240:tests/test_skill.py#L133]
  but "RK1437 gave the ceiling to the half that shrank and left these two unbounded" [roadkeep@91754240:tests/test_skill.py#L144],
  answered by RK1643 [roadkeep@d849f061].

## Related

- Rules: [IS-4](../../IS.md) and [IS-2](../../IS.md).
- Findings: [F3](../../../evidence/findings/F3.md), [F2](../../../evidence/findings/F2.md).
- Anti-pattern: [Resident encyclopedia](resident-encyclopedia.md).
