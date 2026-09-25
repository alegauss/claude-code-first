# Deferred for judgement

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S2 |

## Intent

Work that needs a person's look, or hardware the machine lacks, is set aside with its reason
and closed only when the person or the hardware answers.

## Context

polyweave, whose product depends on renders a person judges and on engines the machine may
lack, and winwright, whose cases need a controller. Both are projects with physical or
aesthetic inputs, and the person is always the one owner.

## Problem

An agent that must finish substitutes a proxy, a margin of its own or a run on the hardware
it has, and reports the proxy's result as the verdict. The ledger then records the shipping
session's claim, which reads exactly like one the person accepted.

## Forces

- A loop that drains a backlog wants every task closed.
- Some acceptance conditions cannot be computed.
- A task left open is retried by the next pick.

## Solution

polyweave declared a deferred store, set such tasks aside with the reason, and brought each
back when the missing input arrived. A bar the person sets becomes a value the check reads,
so the next task against it needs no new margin from the agent.

## Consequences

Work waits on the person, and a deferral that nobody revisits is a quiet second backlog. The
store is one project's practice: winwright closed such work instead, and had to correct the
entry. The alternative cost more: the agent's own margin blocked a port for a day. Whether a
stored bar is reused without asking again is not yet observed.

## Known uses

- polyweave: "Godot is not installed on this machine" [polyweave@5a3a26c], then "now that there is a Godot" [polyweave@0a82ee0].
- polyweave: "a person looked at the rig's 0.3977 beside the shipped sprite at display size and accepted it, so the bar moved to 0.41" [polyweave@d2ae97c],
  after "The dim star's 0.37 was a margin nobody asked for and it blocked a port for a day" [polyweave@6d1c136:docs/ROADMAP.md#L35].
- winwright, the failure avoided: "The cases were written on a desk with no controller, so the two that need one had never run." [winwright@d2a9081]

## Related

- Resolves: [Self-certified look](../anti-patterns/self-certified-look.md).
- Rules: [PG-6](../../PG.md), [HR-1](../../HR.md) and [HR-2](../../HR.md).
- Findings: [F105](../../../evidence/findings/F105.md) and
  [F104](../../../evidence/findings/F104.md).
