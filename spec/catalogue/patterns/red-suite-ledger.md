# Red-suite ledger

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A red that is known and allowed to stay is recorded as a dated exception, which turns the
gate red again once it expires.

## Context

Shio, after two suites stayed red at the head of the branch across nineteen commits that no
message mentioned. winwright records the failure the ledger avoids, a red nobody could act
on.

## Problem

A red that nobody recorded looks the same as a red nobody knows about, and a red that nobody
can act on stops being read. The next true red then arrives unread beside it.

## Forces

- Some reds cannot be fixed before other work continues.
- Rerunning or disabling the suite hides the true red along with the known one.
- An exception with no end becomes the new normal.

## Solution

Shio's SH579 added a ledger of dated exceptions, each tied to the task that will fix it, and
a test that reads the ledger so a forgotten exception goes red. The same task ran the suites
on every push, so the colour is seen without anyone choosing to look.

## Consequences

The red gains an owner and an end. The ledger is one more file to keep, it is one project's
remedy, and no source records it firing. It fits a red the project understands; a red for a
cause outside the change is a defect of the gate, not an exception to record.

## Known uses

- Shio: "Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4]
  mentioned either; the ledger now works "so a forgotten exception goes red instead of quiet" [shio@821f18d74:red-suites.json#L2].
- winwright, the failure avoided: "Twenty-odd pushes each produced a red nobody could act on" [winwright@7a37e95].

## Related

- Resolves: [Permanent red](../anti-patterns/permanent-red.md).
- Rules: [VG-7](../../VG.md), [VG-5](../../VG.md) and [VG-6](../../VG.md).
- Findings: [F303](../../../evidence/findings/F303.md) and
  [F304](../../../evidence/findings/F304.md).
- Patterns: [Third verdict](third-verdict.md).
