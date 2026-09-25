# Absent guard

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A guard hook that is not reached looks exactly like a guard that approved.

## Context

roadkeep, Shio, winwright and freewilly, each relying on a `PreToolUse` hook to refuse
hand edits of governed or generated files, with hooks built to fail open so that their own
errors never block a turn.

## Problem

A hook answers only for the tool calls it is matched on, in sessions where it is installed
and able to run. A tool it was not matched on, a web session where the plugin did not load,
or a fresh clone with no build lets the write through, and nothing states that the guard is
not guarding. The gap is found after the fact.

## Forces

- A hook that denies on its own bug blocks every call and gets removed, so failing open is
  the stated design.
- The session cannot tell a silent guard from an approving one.
- The routes to a file (edit tools, the shell, other checkouts) are more than any one
  matcher lists.

## Refactored solution

Each gap was closed at its route, and a gate that runs elsewhere became the backstop. roadkeep
matched the shell and recorded shell writes at the `Stop` hook; Shio committed a launcher
wired from the committed settings so that the guard reached web sessions; winwright made its
hook name the missing build. The catalogue keeps no pattern for either remedy: the
launcher's premise is contradicted by current documentation (H10), and no source records
what an agent did after a refusal, so both are open questions in [GH](../../GH.md).

## Consequences

A backstop gate catches the drift only when it runs, so it depends on CI running on every
push. The launcher brought defects of its own, in choosing which engine answers.

## Known uses

- roadkeep: "The guard denies Edit and Write and answers silence to a shell command writing the same file" [roadkeep@91754240:docs/CHANGELOG.md#L989].
- Shio: "the guard that denies a hand-edit of the roadkeep-owned docs is absent" [shio@c215718bb].
- winwright: "one that went quiet. The launcher exits 1 and never 2" [winwright@861b82e:README.md#L114].
- freewilly, after its lint workflow was deleted: "drift arriving by any other route, which for a while reached" [freewilly@c1c2eaf:.github/workflows/check.yml#L15]
  main.

## Related

- Rules: [GH-2](../../GH.md), [GH-3](../../GH.md) and [GH-4](../../GH.md).
- Findings: [F301](../../../evidence/findings/F301.md), [F400](../../../evidence/findings/F400.md).
