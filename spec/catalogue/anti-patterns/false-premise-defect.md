# False-premise defect

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A defect is blamed on the wrong component, and the fix built on that reading is wrong too.

## Context

polyweave and Shio, with encoding defects on Windows, and roadkeep, polyweave and winwright,
with designs written before implementation that implementation overturned.

## Problem

The first reading of a symptom names a component, and a fix or a filing follows at once. The
agent's own tools sit in the path and are the last place it looks. When the reading is wrong,
the fix enforces the wrong thing and the filing sends the next session after a defect that
does not exist.

## Forces

- The symptom is real, so the diagnosis feels confirmed.
- Measurements along the product's path can be correct and still miss the agent's own tool.
- A fix shipped quickly looks like progress.

## Refactored solution

The symptom was kept apart from the design, encoding was judged on bytes, and a premise found
false was recorded by retiring the task or amending its reason in the open, not rewritten in
place. See [Measure first](../patterns/measure-first.md).

## Consequences

Both recorded encoding cases were caught within hours, so the cost was one reverted sentence
and one retired filing. Designs also survive measurement, so measuring first sometimes
confirms what was already believed.

## Known uses

- polyweave: "The first reading was that cp1252 cannot hold an em dash" [polyweave@f203b0a],
  but "What reads the pipe decodes UTF-8" [polyweave@f203b0a], and "The ASCII semicolon PW71 put in that sentence an hour ago is reverted" [polyweave@f203b0a].
- Shio: "the CLI corrupts non-ASCII content on the way in (SH519)" [shio@08eeb9290], retired
  because "the mojibake was mine, not the CLI's" [shio@c17ed995a].
- roadkeep: "A design section can carry a stale premise and ship drops it in silence" [roadkeep@91754240:docs/CHANGELOG.md#L130].
- winwright: "take the per-code-unit send back out, the rate did not move" [winwright@5012473].

## Related

- Rules: [PG-2](../../PG.md), [PG-3](../../PG.md), [EP-5](../../EP.md) and [VG-9](../../VG.md).
- Findings: [F405](../../../evidence/findings/F405.md), [F103](../../../evidence/findings/F103.md).
