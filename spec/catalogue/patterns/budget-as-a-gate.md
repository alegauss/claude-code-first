# Budget as a gate

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S4 |

## Intent

A size budget is a number that a check reads and fails on, so each addition past it becomes
a decision.

## Context

roadkeep's every-turn file; the tool schemas Shio and roadkeep serve to their own agent; and
the surfaces Shio, roadkeep, freewilly and winwright ship to other agents.

## Problem

A budget written in the file it governs is read by the agent adding to that file and checked
by nothing. Shio's index carried "Tokens are a measured budget" [shio@821f18d74:agents.md#L22]
while it grew about nineteenfold.

## Forces

- Every addition is small and reasonable on its own.
- A budget that never moves blocks real work; one that moves freely bounds nothing.
- A line budget alone is met by writing longer lines.

## Solution

The figure lives in a file that a test or lint reads, the build fails when it is crossed,
and a raise is written beside the number with its reason. roadkeep moved its every-turn
budget out of prose and into its gate, counting bytes as well as lines. Shio held its
serialized tool list under a ceiling that a test enforces.

## Consequences

Shio's test fired on a real change three tokens over, and a description was trimmed instead
of the ceiling raised. The budget does not stop growth: roadkeep raised its session ceiling
twelve times, each with the task that paid for it, so what it buys is a written decision per
raise. The gate can go red for the wrong reason, and freewilly's needed deterministic inputs
before it could be trusted. With tool search on, what a session pays for a schema is
disputed by the harness documentation, although the measured sizes are not.

## Known uses

- Shio: "3 tokens over its 2200 ceiling" [shio@821f18d74:docs/CHANGELOG.md#L22], and the
  description "trimmed instead of the ceiling raised" [shio@821f18d74:docs/CHANGELOG.md#L22].
- roadkeep: "This budget lived in prose at" [roadkeep@91754240:roadkeep.toml#L235] the bottom
  of the file, and is now "lines = 125, bytes = 8400" [roadkeep@91754240:roadkeep.toml#L249],
  since "a line budget alone is met by writing longer lines" [roadkeep@91754240:roadkeep.toml#L239].
- freewilly: "the budget gate that can go red for the wrong reason" [freewilly@f514e11],
  and the same gate over a whole canonical task "caught it on the commit" [freewilly@c1c2eaf:agent-budget.json#L113-L114]
  that widened one response by 43 tokens.

## Related

- Resolves: [Rule in prose](../anti-patterns/rule-in-prose.md) and
  [Resident encyclopedia](../anti-patterns/resident-encyclopedia.md).
- Rules: [IS-1](../../IS.md), [IS-6](../../IS.md), [IS-4](../../IS.md), [AP-1](../../AP.md)
  and [AP-6](../../AP.md).
- Findings: [F4](../../../evidence/findings/F4.md), [F406](../../../evidence/findings/F406.md),
  [F409](../../../evidence/findings/F409.md) and [F1](../../../evidence/findings/F1.md).
- Patterns: [Index, not encyclopedia](index-not-encyclopedia.md) and
  [Write-time schema](write-time-schema.md).
