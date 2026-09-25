# Drifted copy

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A vendored or duplicate copy of a shared tool falls behind its source, and sessions run it
without noticing.

## Context

winwright, freewilly, roadkeep's adopting projects and Shio, where a shared engine or skill
could be answered by a vendored copy, a sibling checkout, an installed plugin or a stale
registry entry.

## Problem

Which copy answers is not decidable by looking. A stale copy is read with the trust of the
original, so the session works from documentation that lacks a command, or runs an engine
other than the one the repository declares. A notice at session start reports the drift and
is read past.

## Forces

- Vendoring pins a known version, which is the reason it was done.
- Refreshing the copy is a separate step that nothing in the adopting project runs.
- A notice costs nothing to ignore when the session is mid-task.

## Refactored solution

One declared copy answers, and a gate fails when the copy that answers is stale against its
source or is not the intended one. The notice alone is shown not to be enough.

## Consequences

No source at the pins shows such a gate holding: freewilly's check that printed both
versions was deleted with its workflow. A gate over the copy adds a refresh step to every
upstream change.

## Known uses

- winwright, whose surfaces "were stale all session" [winwright@a18dd8d], "I read past it every time" [winwright@a18dd8d],
  at a cost of "five refusal round-trips over the 250-word limit, each re-sending the whole paragraph" [winwright@a18dd8d].
- freewilly: "ROADKEEP_HOME arrives unexpanded, so every hook runs a sibling checkout rather than the engine this repo vendors" [freewilly@c1c2eaf:docs/CHANGELOG.md#L200].
- roadkeep, recording an adopter's skill "78 lines behind" [roadkeep@91754240:src/roadkeep/guarding.py#L57-L59]
  its source.
- Shio, which vendored the engine because "which copy answers is not decidable by looking" [shio@821f18d74:agents.md#L277].

## Related

- Rules: [EP-1](../../EP.md) and [GH-6](../../GH.md).
- Findings: [F403](../../../evidence/findings/F403.md).
