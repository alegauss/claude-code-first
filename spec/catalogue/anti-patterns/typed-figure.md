# Typed figure

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R4/S4 |

## Intent

A count or list typed into prose goes stale in silence when what it describes changes.

## Context

All five projects, in instruction files, skills, READMEs, contributor guides and site copy
that state how many of something there are.

## Problem

A figure typed into prose is true on the day it is written. When the thing it counts changes,
nothing ties the prose to it, so the figure drifts and no check fails. A check built from a
typed list reproduces the fault: it compares the prose with a second typed copy, not with the
source.

## Forces

- A concrete number makes prose read as precise.
- The figure lives in a different file from the thing it counts.
- Records of a moment, such as a ledger entry's count, are legitimately typed, which blurs the
  line.

## Refactored solution

Figures were generated from their source or checked against it. freewilly and Shio generated
their site figures; Shio, roadkeep and winwright added checks, and winwright's reads the
build's own catalogue of keys instead of a typed list. See
[Generated figure](../patterns/generated-figure.md).

## Consequences

Generation needs a build step for the prose. A check is a remedy only when it reads the
source of the figure.

## Known uses

- roadkeep: two figures a non-goal argued from were "stated in five places and both have drifted" [roadkeep@91754240:docs/CHANGELOG.md#L354].
- Shio: "25 mutating paths" [shio@be9fa3727] when "The scan finds twenty-eight roots" [shio@be9fa3727].
- freewilly: llms.txt "counted four window destinations against the five" [freewilly@0794e60] declared.
- polyweave: the audit skill lists blocks "for the current set; today it answers:" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L52]
  and misses two the roadmap holds.
- winwright: the old gate checked "nine names somebody typed" [winwright@861b82e:docs/CHANGELOG.md#L453],
  and the new check, with the key taken "back out turned the case red naming it" [winwright@ae44ecc].

## Related

- Rules: [AW-1](../../AW.md) and [IS-5](../../IS.md).
- Findings: [F7](../../../evidence/findings/F7.md).
