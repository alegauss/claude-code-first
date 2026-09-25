# Proof by deletion

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A tool built for agents proves adoption by a counted change in a named consumer, at best by
deleting the consumer's own replacement.

## Context

winwright, polyweave and roadkeep, each built for other agents and each proved in a named
consumer repository. The consumers are the same person's projects.

## Problem

A producer's suite exercises the inputs its author imagined, so it passes over what a
consumer's real artefacts break. A claim of adoption made from the producer's side reads the
same whether or not the consumer's cases run on the tool.

## Forces

- The producer controls its own tests and not the consumer's.
- A consumer's replacement keeps working, so nothing forces the switch.
- The evidence comes one consumer at a time.

## Solution

Adoption is closed by removing the consumer's hand-built replacement and reporting the lines
removed, so the consumer's cases either run on the tool or fail. polyweave takes its
thresholds from a consumer's real artefacts rather than from synthetic ones.

## Consequences

It is a test the producer cannot pass by construction, and the consumer found what the
producer's suite had passed: a real mesh agrees with its drawing far below the threshold
the synthetic tests clear. It can still overstate. winwright corrected its pportal entry the
same day because two cases had never run, and gives the deleted claude-tray harness as
3,004 lines in one record and 2,732 in another. A counted change is necessary, and the
cases it counts have to have run.

## Known uses

- winwright: "the number of lines removed is reported rather than described" [winwright@861b82e:docs/ROADMAP.md#L137];
  in pportal the file "is deleted, 285 lines in which every case decided for itself how long to wait" [winwright@6917d3f].
- polyweave: "silhouette IoU of 0.4343" [polyweave@0cacaad] while "The synthetic tests clear 0.8" [polyweave@0cacaad].

## Related

- Resolves: [Silent green](../anti-patterns/silent-green.md), where the green is the
  producer's own suite over inputs that are not the consumer's.
- Rules: [AP-4](../../AP.md) and [AP-3](../../AP.md).
- Findings: [F408](../../../evidence/findings/F408.md) and
  [F407](../../../evidence/findings/F407.md).
