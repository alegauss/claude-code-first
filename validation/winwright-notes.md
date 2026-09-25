# Audit notes: winwright

The verdicts are in [winwright.json](winwright.json), rendered as
[winwright.md](winwright.md). These notes hold what the report format has no field for.

## How this audit was run

- **Target**: winwright's current head, `861b82e2cb7d0864cf2dc41799f04f4de3ec0e6e`
  (2026-09-21), read from a fresh clone. It is also the study's pin. The owner's local
  checkout has uncommitted work and unpushed commits, which a clone of the committed head
  does not see.
- **Level**: 3 with the agent-facing profile, since winwright ships a plugin and an MCP
  server. winwright declares no level of its own.
- **Deviation from the audit skill**: one scanner read every judged rule, not one per
  chapter.
- **Verifier outcome**: 19 scanner findings confirmed and two rejected as false positives:
  CS-2 (the commit staged only its task's files and the shared governed files, a case the
  CS chapter leaves open) and PS-3 (no credential file is in the clone, and the runner's
  default location is outside the tree; its existence elsewhere was checked, its contents
  were not read). The verifier also decided GH-6, which the scanner had not examined:
  it fails.

## What stops level 1

CD-1, CD-3, CD-4, CD-6, HR-1 and PG-2 fail. winwright has no every-turn file, which
decision D2 allows.

## Circularity

No rule rests on winwright alone; 46 of the 56 rules have winwright among the cases of
their findings.

## Classification of the failures (proposed; the owner decides)

| Rule | Proposed | Why |
|---|---|---|
| CD-1 | drift | commits that add several ledger entries, against the project's own rule |
| CD-3 | divergence | the commit tool that stages everything is a deliberate choice; a waiver names what stands in |
| CD-4, CD-6 | drift | a generated title with no task id; no stated attribution policy |
| HR-1 | drift | a task needing a controller recorded as shipped before the cases ran |
| PG-2 | drift | a task line that carries its design |
| AW-1, AW-3, GH-1 | drift | a stale criteria count in a skill; the ASCII-title rule broken twice and still prose |
| AP-1, AP-2, AP-3 | drift | served schemas uncapped, `llms.txt` names unchecked, the plugin never loaded as a consumer loads it |
| EP-1, GH-6 | drift | two skills disagree on which roadkeep copy answers, and a stale copy fails no gate |
| EP-3 | drift | UTF-8 child output and MCP stdin decoded with the default code page |
| GH-3 | drift | the product's harness guard sees only file-edit tools |
| GH-5 | drift | the committed agent configuration is read by no test |
| IS-4, IS-5 | drift | skill pages unbounded; the block table stale against the roadmap |
| PS-2 | drift | the ban on raw commits is prose only |
| VG-7 | divergence, or drift | CI red for twenty-odd pushes; D4 allows a hardware gate to be deviated, but the red itself had no exception |

## Tasks offered

One realignment task per drifted rule is offered to winwright's owner
([../adoption/realignment.md](../adoption/realignment.md)). None has been filed.

## Cost

| Step | Tokens | Wall time |
|---|---|---|
| checker | none (a script) | a few seconds |
| scanner | 219,700 | 1,059 s |
| verifier | 105,671 | 314 s |
