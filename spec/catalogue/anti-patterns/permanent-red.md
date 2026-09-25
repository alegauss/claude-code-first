# Permanent red

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A gate stays red for a reason nobody can act on, and so is no longer read.

## Context

Shio, winwright and freewilly, with gates that went red for causes outside the change, and
Shio and freewilly with gates that did not run on every push.

## Problem

A red that means nothing costs a diagnosis every time, and then it is ignored. A true red
arriving beside it is ignored too. A gate that runs only when someone chooses to run it
leaves its red visible to nobody, and commits land over it unremarked.

## Forces

- Rerunning until green is cheaper than diagnosing the gate.
- A hosted runner cannot answer every check, such as one that needs a desktop.
- A known red has no owner and no end date, so it becomes the normal state.

## Refactored solution

A red about something else was filed as a defect of the gate and fixed by narrowing what it
concludes or where it runs; gates ran on every push; and a red that has to stay was covered by
a dated exception that turns red once it expires. See
[Red-suite ledger](../patterns/red-suite-ledger.md) and [Third verdict](../patterns/third-verdict.md).

## Consequences

Narrowing where a gate runs moves part of the suite to a local gate, which CI no longer
audits. Each exception is a record to keep.

## Known uses

- Shio: "Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4]
  mentions either, answered by a ledger of exceptions that works "so a forgotten exception goes red instead of quiet" [shio@821f18d74:red-suites.json#L2].
- winwright: "Twenty-odd pushes each produced a red nobody could act on" [winwright@7a37e95],
  and "A permanently red badge is one nobody reads, so the run that catches a real break" [winwright@861b82e:.github/workflows/ci.yml#L51].
- freewilly: "the budget gate that can go red for the wrong reason" [freewilly@f514e11].

## Related

- Rules: [VG-5](../../VG.md), [VG-6](../../VG.md) and [VG-7](../../VG.md).
- Findings: [F304](../../../evidence/findings/F304.md), [F303](../../../evidence/findings/F303.md).
