# Measure first

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A change meant to improve a measurable quantity is preceded by a measurement of it, and kept
only if a second measurement shows the gain.

## Context

roadkeep, polyweave and winwright, where a design or diagnosis written before implementation
was overturned once it was built or measured; winwright and Shio, where a filed premise did
not survive a measurement.

## Problem

A design is a prediction written when the task is filed, from what the author knew then.
Built on without a measurement, it ships, or it is reverted after its cost is paid.

## Forces

- A written design looks settled because it is written down.
- Measuring first costs time before any visible progress.
- Designs also survive measurement, so the step sometimes confirms what was believed.

## Solution

The quantity is measured before building and again after. A premise that fails the first
measurement retires its task with the reason; a change that fails the second is reverted.

## Consequences

winwright retired two filed tasks before building them and reverted one after. polyweave's
measurement of parallel sampling confirmed its design, so the step settles the question and
does not show that designs usually fail. Measuring one path can still miss another: Shio's
first encoding diagnosis rested on four measurements of bytes along the product's path,
missed the agent's own tool, and was withdrawn the same day.

## Known uses

- winwright: "Measured before building it, and the premise did not survive" [winwright@861b82e:docs/CHANGELOG.md#L485];
  "take the per-code-unit send back out, the rate did not move" [winwright@5012473].
- polyweave: "The design proposed a declared range, and measuring it is what settled the line the other way." [polyweave@7024e7e]
  Against it: "Which is what the design predicted" [polyweave@871a15b].
- Shio: "Four measurements" [shio@08eeb9290], then "the mojibake was mine, not the CLI's" [shio@c17ed995a].

## Related

- Resolves: [False-premise defect](../anti-patterns/false-premise-defect.md).
- Rules: [VG-9](../../VG.md), [PG-3](../../PG.md) and [EP-5](../../EP.md).
- Findings: [F103](../../../evidence/findings/F103.md),
  [F102](../../../evidence/findings/F102.md) and [F405](../../../evidence/findings/F405.md).
