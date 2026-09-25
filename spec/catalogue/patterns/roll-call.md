# Roll call

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A test gate compares the tests its runner discovered with the tests that reported a result,
and reports any difference as could not run.

## Context

winwright's .NET suite, where a dying test host still printed a pass. The remedy has one
origin, winwright; the failure it answers, a pass over work that did not run, is recorded
in three projects.

## Problem

A runner reports on the tests that reported. A test that never started reports nothing, so
the green covers it.

## Forces

- The runner's own summary is what everyone reads.
- Discovery and results live in different outputs, and joining them is extra machinery.
- A bare invocation of the runner skips any wrapper the project built around it.

## Solution

winwright added a roll call of what discovery listed against what the results file recorded
(WW117), and made a bare test run take it (WW138), so the check does not depend on the agent
choosing the wrapper.

## Consequences

It closes a gap measured at twenty-two unrun tests inside a green. It is one project's
remedy and no source records it catching a real run. It covers only test suites: a capture
of the wrong window or a vacuous assertion passes a roll call, since both report a result.
It is the concrete form of the third verdict for a test suite.

## Known uses

- winwright: "measured here at 352 of 374, a green covering twenty-two tests that" [winwright@861b82e:.github/workflows/ci.yml#L42]
  never ran, answered by a roll call of "what discovery listed against what the results file recorded" [winwright@861b82e:docs/CHANGELOG.md#L14]
  in [winwright@6351b80], which a bare run takes since [winwright@2eeb059].

## Related

- Resolves: [Silent green](../anti-patterns/silent-green.md).
- Rules: [VG-4](../../VG.md) and [VG-3](../../VG.md).
- Findings: [F302](../../../evidence/findings/F302.md).
- Patterns: [Third verdict](third-verdict.md).
