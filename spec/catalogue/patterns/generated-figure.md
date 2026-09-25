# Generated figure

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R4/S4 |

## Intent

A count, version or list stated in prose is produced from its source, or checked against
that source by a gate, rather than typed.

## Context

All five projects, where a figure or enumeration in a skill, a README, a configuration
comment or a contributing guide went stale when what it described changed.

## Problem

A typed number is true when written and has no link to what it counts. The change that makes
it false is made elsewhere, often by another session, and the next agent trusts the prose.

## Forces

- Typing a number is the cheapest way to make a sentence concrete.
- Generation needs machinery where the prose is built.
- A check that compares the prose with a typed list reproduces the fault it guards.

## Solution

The figure is generated from its source, as freewilly's and Shio's site figures are, or the
sentence is checked against a measurement that reads the source: winwright's check over the
build's own catalogue of keys, Shio's figures test, roadkeep's sweep of caller-facing prose.

## Consequences

winwright's check was seen to fail on a control, when the key was taken out again. The remedy
covers only the prose it reaches: freewilly generates its site counts, and its contributing
guide still names two workflows where four are in the tree. A check built from typed names
missed the key it existed to hold. Records of a moment, such as a ledger count on the day a
task shipped, are left typed.

## Known uses

- winwright: the old gate checked "nine names somebody typed" [winwright@861b82e:docs/CHANGELOG.md#L453],
  and taking the key "back out turned the case red naming it" [winwright@ae44ecc].
- freewilly: "Counts and versions are generated, not written" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L97],
  while "Two workflows, and each runs exactly one of them" [freewilly@c1c2eaf:CONTRIBUTING.md#L21] stays typed.
- Shio: "25 mutating paths" [shio@be9fa3727] against "The scan finds twenty-eight roots" [shio@be9fa3727],
  now held by a test.

## Related

- Resolves: [Typed figure](../anti-patterns/typed-figure.md).
- Rules: [AW-1](../../AW.md), [IS-5](../../IS.md) and [AP-2](../../AP.md).
- Findings: [F7](../../../evidence/findings/F7.md).
- Patterns: [Grep, then lint](grep-then-lint.md).
