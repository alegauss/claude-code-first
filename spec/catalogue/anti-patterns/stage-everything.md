# Stage everything

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R2/S2 |

## Intent

A commit step that stages the whole tree commits whatever else the tree holds.

## Context

The owner's commit tool, used in all five projects, stages everything before it writes a
message. The recorded leaks are in Shio and freewilly, in sessions that left run logs,
bytecode or a rewritten settings file beside their work.

## Problem

An agent session leaves artefacts beside its change. A stage-all commit owns all of them, so
each rides into the next commit under a message written for another task. An ignore rule
added afterwards closes only the pattern it names, and a file under a new name leaks in turn.

## Forces

- Staging everything is one command and never forgets a file the task did touch.
- Scratch files are produced by the session's own diagnostics, not by the change.
- A shared tool is costly to change, since every repository depends on it.

## Refactored solution

Each commit stages only the paths its task changed, and the ignore rules remain a second
line for known scratch patterns. freewilly retired the tool fix and protected the tree with
ignore rules; the rules of this specification stage by path.

## Consequences

Staging by path needs the task to know its own paths. A stray that is never staged stays in
the tree until someone removes it.

## Known uses

- Shio, where a teed log was committed with a feature, "which is how sh545.log landed in b04ee918" [shio@821f18d74:.gitignore#L62],
  and a later scratch file passed the new rule: "so it landed in the SH778 commit" [shio@44e6ef232].
- freewilly, where "the second time the deletion rode into a commit about" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L278]
  something else, "because run-commit.cmd stages everything by design." [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L279]

## Related

- Rules: [CD-3](../../CD.md) and [CS-2](../../CS.md).
- Findings: [F200](../../../evidence/findings/F200.md), [F201](../../../evidence/findings/F201.md).
