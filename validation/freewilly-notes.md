# Audit notes: freewilly

The verdicts are in [freewilly.json](freewilly.json), rendered as
[freewilly.md](freewilly.md). These notes hold what the report format has no field for.

## How this audit was run

- **Target**: freewilly's current head, `c1c2eaf4694a03df85f8a8eeb83a7de03886b056`
  (2026-09-17), read from a fresh clone. It is also the study's pin: freewilly has not
  moved since.
- **Level**: 3 with the agent-facing profile, since freewilly ships an agent skill,
  `llms.txt` and an agent budget. freewilly declares no level of its own.
- **Deviation from the audit skill**: one scanner read every judged rule, not one per
  chapter.
- **Verifier outcome**: 23 scanner findings confirmed, one rejected as a false positive
  (VG-7: nobody chose to keep the red suite, it went unnoticed, which is VG-1's defect),
  and one rule the scanner passed found broken (EP-1: an unpinned roadkeep plugin can
  answer in place of the declared vendored copy).

## What stops level 1

CD-1, CD-2, CD-3, CD-4, CD-6, PS-1 and PS-3 fail. freewilly has no every-turn file, which
decision D2 allows, so the IS rules that depend on one pass by their condition.

## Circularity

No rule rests on freewilly alone; 45 of the 56 rules have freewilly among the cases of
their findings, the most of any project, which makes its failures the least surprising
and its passes the least independent.

## Classification of the failures (proposed; the owner decides)

| Rule | Proposed | Why |
|---|---|---|
| CD-1, CD-2, GH-1 | drift | tasks batched in one commit against the project's own most-stated rule |
| CD-3 | divergence | the commit tool that stages everything is a deliberate choice; a waiver names what stands in |
| CD-4, CD-6 | drift | a diff-generated title; no stated attribution policy though trailers appear |
| AW-1, AW-3 | drift | a stale contributor guide; the em-dash rule broken with no gate |
| AP-1, AP-2, AP-3 | drift | the agent surface's skill uncapped, `llms.txt` names unchecked, verbs never run from the published binary |
| EP-1, GH-6 | drift | the answering roadkeep copy is not the declared one, and its only check skips on every runner |
| EP-2, EP-3 | drift | no line-ending rule; child output decoded in the console code page |
| GH-3 | drift | the guard omits the PowerShell tool, which is allowed |
| GH-4 | obsolescence candidate | the deliberate silent fail-open, as in roadkeep and polyweave |
| IS-4, IS-5 | drift | skill pages unbounded; roadkeep verbs listed unchecked |
| PS-1, PS-2 | drift | broad allows with nothing named in their place; the one-task rule is prose |
| PS-3 | divergence, or drift | a VM credential kept in the working tree by design, behind an ignore line; the owner decides whether it moves out |
| VG-1, VG-3, VG-4, VG-8 | drift | a ship on a test red for five days, a skip counted as a pass, no roll call, a behaviour change with no test |

## Tasks offered

One realignment task per drifted rule is offered to freewilly's owner
([../adoption/realignment.md](../adoption/realignment.md)). None has been filed.

## Cost

| Step | Tokens | Wall time |
|---|---|---|
| checker | none (a script) | a few seconds |
| scanner | 165,841 | 482 s |
| verifier | 101,401 | 396 s |
