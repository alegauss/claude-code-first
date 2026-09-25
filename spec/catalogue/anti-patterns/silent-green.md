# Silent green

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A gate reports a pass over work that did not run or a check that looked at the wrong thing.

## Context

winwright, Shio and freewilly, each on its own stack: a .NET test runner, Maven and pnpm, and
a desktop capture in a guest.

## Problem

A green is the absence of a reported failure. A test host that dies, a stale build
directory, a check that matches nothing, or a picture taken before the window arrived all
produce no failure, and so read as success. The agent then closes the task on that green.

## Forces

- A pass is what the agent expects, so it is not questioned.
- The failure to run is quiet; only its absence of output would show it.
- Counting what should have run needs a second source, such as the discovery list.

## Refactored solution

"Did not run" became a verdict distinct from a pass, and checks waited for the positive
signal they needed. winwright added a roll call of what discovery listed against what the
results file recorded; freewilly's capture case waits for the menu to report an entry, and its
budget asserts every figure exactly. See [Third verdict](../patterns/third-verdict.md) and
[Roll call](../patterns/roll-call.md).

## Consequences

A third verdict turns some greens into work, since each unrun check has to be explained. The
roll call is only as good as the discovery it counts against.

## Known uses

- winwright: "measured here at 352 of 374, a green covering twenty-two tests that" [winwright@861b82e:.github/workflows/ci.yml#L42]
  never ran, answered by WW117 [winwright@6351b80].
- Shio: "mvn compile can report success on code that does not compile" [shio@052550e68];
  and the assertion-debt test's first run, where "on the first run its own declaration made all forty entries read as" [shio@821f18d74:agents.md#L234]
  asserted.
- freewilly, whose desktop capture case "photographed the guest's WALLPAPER, and passed" [freewilly@c1c2eaf].

## Related

- Rules: [VG-3](../../VG.md) and [VG-4](../../VG.md).
- Findings: [F302](../../../evidence/findings/F302.md).
- Anti-pattern: [Piped gate](piped-gate.md).
