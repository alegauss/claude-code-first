# Piped gate

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A gate run through a pipe reports the filter's exit status instead of its own.

## Context

Shio, where test suites were run through a pipe into a filter or a tee to keep the output
short. The pipe is one form of the silent green recorded in three projects; the pipe itself
is recorded in Shio only.

## Problem

A shell pipeline's status is its last command's. A failing suite piped into a filter exits 0,
and a failure line that went into the pipe is lost with it. The agent reads a pass and an
empty log.

## Forces

- A filtered output is shorter and cheaper to read in context.
- The pipeline reads better, and nothing fails when it is written.
- The rule against it is easy to state and easy to miss in a file the lint does not read.

## Refactored solution

The suite runs unpiped, through one runner that keeps the output in a file and returns the
suite's own exit code, and a lint reads the documents that say how to run the suite and fails
on a pipe. See [Grep, then lint](../patterns/grep-then-lint.md).

## Consequences

The full output has to be read from the kept file rather than from a filter. The lint covers
only the files it names: Shio's build skill still pipes the suite at the pin.

## Known uses

- Shio, where a failing test run printed an exit status of 0 [shio@821f18d74:agents.md#L155-L156],
  fixed in [shio@c1b9e8947]; an earlier failure "went into a pipe nobody kept" [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L33];
  and the runner states that "the exit code is not swallowed" [shio@821f18d74:scripts/run-gate.mjs#L9].
- Shio's rule, "Never pipe a gate into" [shio@821f18d74:agents.md#L150], with the skill
  that still reads "-Dskip.npm=true 2>&1" [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L17].

## Related

- Rules: [VG-2](../../VG.md) and [GH-1](../../GH.md).
- Findings: [F302](../../../evidence/findings/F302.md), [F300](../../../evidence/findings/F300.md).
- Anti-pattern: [Silent green](silent-green.md).
