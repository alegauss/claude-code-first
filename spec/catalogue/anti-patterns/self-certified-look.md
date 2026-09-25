# Self-certified look

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

The agent closes work that needs a person's judgement, or hardware the machine lacks, on its
own claim.

## Context

polyweave and winwright, whose products depend on physical or aesthetic inputs such as a
renderer, an engine, a controller or a person's eye, and Shio and freewilly, whose ledgers
recorded shipped entries later found untrue.

## Problem

A ledger entry records the shipping session's own claim. Nothing in the planning files
records whether a person tried the work, so an entry closed without the person reads exactly
like one the person accepted. Where the agent sets its own bar in place of the person's, the
bar can block work as easily as pass it.

## Forces

- The agent can always produce a plausible pass, and the task looks finished.
- The person or the hardware is not present in the session.
- A margin the agent chose feels safer than the person's figure, and costs nobody at once.

## Refactored solution

Work that needs a person was deferred with its reason and closed only when the person or the
hardware answered, against a bar the person set and the check reads. See
[Deferred for judgement](../patterns/deferred-for-judgement.md).

## Consequences

Deferred work waits on the person, and a backlog can fill with it: at the pin seven of
polyweave's eight deferred lines await a person's judgement.

## Known uses

- winwright: "The cases were written on a desk with no controller, so the two that need one had never run." [winwright@d2a9081]
- polyweave: "The dim star's 0.37 was a margin nobody asked for and it blocked a port for a day" [polyweave@6d1c136:docs/ROADMAP.md#L35];
  PW76 shipped when "a person looked at the rig's 0.3977 beside the shipped sprite at display size and accepted it, so the bar moved to 0.41" [polyweave@d2ae97c].
- Shio: "Six corrections shipped half of themselves" [shio@14acb91ce], "with verification being a person asking an agent to look afterwards" [shio@14acb91ce].

## Related

- Rules: [HR-1](../../HR.md), [HR-2](../../HR.md) and [PG-6](../../PG.md).
- Findings: [F104](../../../evidence/findings/F104.md), [F105](../../../evidence/findings/F105.md).
