# Audit notes: polyweave

The verdicts are in [polyweave.json](polyweave.json), rendered as
[polyweave.md](polyweave.md). These notes hold what the report format has no field for.

## How this audit was run

- **Target**: polyweave's current head, `15874cc0a331f70d6964aa41604cd0befe9491cc`
  (2026-09-25), read from a fresh clone; not the study's pin.
- **Level**: 3 with the agent-facing profile, since polyweave ships a plugin and an MCP
  server. polyweave declares no level of its own.
- **Deviation from the audit skill**: one scanner read every judged rule, not one per
  chapter. The scanner skipped the five IS rules it was given; the verifier judged them
  from the clone, so every rule has a verdict, but for those five no second reading
  exists. The scanner's run was also stopped once by mistake and resumed.
- **Verifier outcome**: all 17 scanner findings confirmed, no false positive, no passing
  rule turned into a failure; the five skipped rules judged (two fail: IS-4, IS-5).

## What stops level 1

IS-1 could not be decided: polyweave's every-turn file has no budget in a form the checker
reads, which is a verdict about the checker's reach as much as about the project. CD-3,
CD-4, CD-6, PG-5 and PS-1 fail.

## Circularity

No rule rests on polyweave alone; 20 of the 56 rules have polyweave among the cases of
their findings.

## Classification of the failures (proposed; the owner decides)

| Rule | Proposed | Why |
|---|---|---|
| IS-1 | drift, or a checker gap | a budget may exist in a form the checker cannot read; the owner can declare it or waive |
| CD-3, CS-2 | divergence | the commit tool that stages everything is a deliberate choice; a waiver names what stands in |
| CD-4 | drift | early setup commits with diff-generated titles and no task id |
| CD-6 | drift | no stated attribution policy |
| PG-5 | drift | the public site counts a block as built when nothing is open, not by its criteria |
| AW-1 | drift | a typed count of non-goals, already stale |
| IS-4, IS-5 | drift | specs and skill pages unbounded; names in the audit skill unchecked |
| AP-3 | drift | the surface is tested only from the source checkout |
| CS-4 | drift | the gate's lock sees only its own runs |
| EP-3, EP-4 | drift | locale-default decoding; the shipped guard does not strip a byte-order mark and then allows silently |
| GH-2, GH-3, GH-5 | drift | the no-clobber guard has no gate behind it and no shell matcher; the settings are under no test |
| GH-4 | obsolescence candidate | the silent fail-open is deliberate, as in roadkeep; see its notes |
| PS-1, PS-2 | drift | the whole shell is allowed with nothing named in its place; the push ban is prose |
| VG-4 | drift | no roll call of collected against reported tests |

## Tasks offered

One realignment task per drifted rule is offered to polyweave's owner
([../adoption/realignment.md](../adoption/realignment.md)). None has been filed.

## Cost

| Step | Tokens | Wall time |
|---|---|---|
| checker | none (a script) | a few seconds |
| scanner | 193,942 | 510 s |
| verifier | 88,659 | 219 s |
