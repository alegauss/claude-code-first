# Third verdict

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A check that did not run reports *could not run*, a verdict distinct from passed and failed.

## Context

winwright, Shio and freewilly, where gates went green over tests that never ran, a stale
build and a capture of the wrong window; Shio and roadkeep, where a disturbed run reported
reds that were not about the change.

## Problem

A green is the absence of a reported failure. A dying test host, a stale build directory, a
vacuous check or a failed setup produces no failure, or a failure about something else, so
a gate with two answers reports it as a pass or as a real red.

## Forces

- A third state is one more thing to act on, and it holds a close open.
- The sign that a check actually ran is often missing from the tool's own output.
- A red that is not about the change costs a diagnosis every time.

## Solution

The gate distinguishes three verdicts and never counts the third as a pass. winwright's
shipped skill states it for the product's own checks. Shio records a failed clean as
inconclusive rather than red, and its runner refuses a second concurrent run of one gate.
freewilly's capture case now waits for the positive signal before it judges.

## Consequences

A check that could not run still has to run somewhere before the work closes, so the verdict
moves work rather than removing it. The verdict is shared across the projects but the means
of detecting it are not: a lock, a snapshot, a wait for a signal. No source records the
inconclusive state or the lock firing on a real run.

## Known uses

- winwright: "A check that could not run is a third verdict and never a pass" [winwright@861b82e:skills/winwright/SKILL.md#L71].
- Shio: "recorded as INCONCLUSIVE rather than red (SH828)" [shio@821f18d74:scripts/run-gate.mjs#L94].
- freewilly: a capture "photographed the guest's WALLPAPER, and passed" [freewilly@c1c2eaf],
  and the case now waits for the menu to report an entry.

## Related

- Resolves: [Silent green](../anti-patterns/silent-green.md) and
  [Permanent red](../anti-patterns/permanent-red.md).
- Rules: [VG-3](../../VG.md), [CS-4](../../CS.md) and [VG-6](../../VG.md).
- Findings: [F302](../../../evidence/findings/F302.md),
  [F304](../../../evidence/findings/F304.md) and [F202](../../../evidence/findings/F202.md).
- Patterns: [Roll call](roll-call.md).
