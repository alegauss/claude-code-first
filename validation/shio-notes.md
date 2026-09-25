# Audit notes: Shio

The verdicts are in [shio.json](shio.json), rendered as [shio.md](shio.md). These notes
hold what the report format has no field for.

## How this audit was run

- **Target**: Shio's current head on the 2026.3 branch,
  `fb966f8dae563c5b188933f894cc84b6da3f4c48` (2026-09-25), read from a fresh clone;
  not the study's pin.
- **Level**: 3 with the agent-facing profile, since Shio publishes a plugin and serves an
  MCP surface. Shio declares no level of its own.
- **Deviation from the audit skill**: one scanner read every judged rule, not one per
  chapter. Cloning needed a one-off `safe.directory` setting because of the worktree's
  ownership; no git configuration was changed.
- **Verifier outcome**: 28 scanner findings confirmed and two rejected as false
  positives: CD-2 (the commit filed three new tasks and shipped none) and CS-1 (the
  committed roadkeep skill does tell a session to claim its line and its paths).

## What stops level 1

IS-1 could not be decided (no budget in a form the checker reads). CD-1, CD-3, CD-6, IS-2,
PG-5, PS-1 and PS-3 fail.

## Circularity

No rule rests on Shio alone; 50 of the 56 rules have Shio among the cases of their
findings, the most of any project. Many rules were written from Shio's incidents, so its
audit tests whether the project has since repaired what the specification learned from
it.

## A disagreement the verifier noted

Shio's rules say to commit only through the commit tool, while sessions hand-author and
stage by path whenever another session is in the tree (871410748). The prose rule and the
practice disagree; the practice is the one CD-3 asks for.

## Classification of the failures (proposed; the owner decides)

| Rule | Proposed | Why |
|---|---|---|
| IS-1, IS-2, IS-4, IS-5 | drift | the index carries area detail again, and the area files it points to are unbounded and unchecked |
| CD-1, GH-1 | drift | batched ships against the project's most-stated rule, which no gate reads |
| CD-3, CS-2, PS-2 | divergence | the stage-everything tool is a deliberate rule the sessions already break when they must; the owner decides which way |
| CD-6 | drift | no stated attribution policy |
| CS-4, VG-1 | drift | a gate red from another session's edits reported as failed, and a commit landed on it |
| EP-1, GH-6 | drift | two files disagree on which roadkeep copy answers; staleness is checked only by hand |
| EP-3, EP-5, EP-6 | drift | locale-default decoding; an encoding defect filed before the agent's own tool was checked; a heredoc corruption |
| GH-2 | drift | roadkeep lint runs only when someone dispatches it |
| GH-3, GH-4, GH-5 | drift; GH-4 an obsolescence candidate | the guard omits PowerShell, fails open in silence, and its wiring is under no test |
| AW-1 | drift | a stale count of IT classes in the every-turn file |
| AP-1, AP-2 | drift | plugin skills uncapped, and the tool names they cite unchecked |
| PG-5 | divergence, or drift | a block closed because its last task was retired, by a rule Shio enforces with a test; the owner decides whether criteria replace it |
| PS-1, PS-3 | drift | broad allows with nothing named in their place; an analysis token cached in the tree |
| VG-3, VG-4, VG-8 | drift | skipped suites counted as green, no roll call, a known list of shipped tasks with no assertion |

## Tasks offered

One realignment task per drifted rule is offered to Shio's owner
([../adoption/realignment.md](../adoption/realignment.md)). None has been filed.

## Cost

| Step | Tokens | Wall time |
|---|---|---|
| checker | none (a script) | a few seconds |
| scanner | 230,669 | 851 s |
| verifier | 131,712 | 439 s |
