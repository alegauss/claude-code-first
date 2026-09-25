# Audit notes: roadkeep

The verdicts are in [roadkeep.json](roadkeep.json), rendered as [roadkeep.md](roadkeep.md).
These notes hold what the report format has no field for.

## How this audit was run

- **Target**: roadkeep's current head, `77a3eaeb60540dc464a14e631fdc7ae4b3b82d7f`
  (2026-09-24), read from a fresh clone so the project's own checkout was not touched. It
  is not the study's pin: an audit judges the project as it stands.
- **Level**: 3 with the agent-facing profile, to measure every rule. roadkeep declares no
  level of its own.
- **Deviation from the audit skill**: one scanner read every judged rule, instead of one
  scanner per chapter, to keep the run within the session's usage limits. The verifier ran
  as the skill describes.
- **Verifier outcome**: all 20 findings the scanner reported were confirmed, none was a
  false positive, and one rule the scanner passed (PS-1) was found broken.

## Circularity

roadkeep supplied many of the rules. Two rules rest on findings whose only case is
roadkeep, PG-4 and PG-5, and both pass: that is roadkeep conforming to its own design, not
evidence that the rules hold. Of the 56 rules, 42 have roadkeep among the cases of their
findings. That roadkeep fails 22 of them anyway (20 judged, plus CD-1 from the checker and
one more from the verifier) is the test the audit was meant to be: the specification can
find fault with its main source.

## Classification of the failures (proposed; the owner decides)

Each failure is proposed as drift (the project means to conform), divergence (a
deliberate choice, to be waived with a reason) or obsolescence (the rule may not fit, to
be reported upstream). The owner decides; none is final until then.

| Rule | Proposed | Why |
|---|---|---|
| CD-1, CD-2, VG-1, VG-8 | drift | ships recorded on red trees or without a covering check, against the project's own one-task discipline |
| CD-3, CS-2 | divergence | the commit tool that stages everything is a deliberate, documented choice; a waiver would name the claim scope as what stands in |
| CD-4 | drift | diff-generated titles with no task id on filing commits |
| CD-6 | drift | no stated attribution policy, with trailers still appearing |
| AW-1, IS-5, AP-2 | drift | typed counts and lists with no check against their source |
| AP-1, IS-4 | drift | served command bodies and the dev skill body carry no ceiling |
| EP-3 | drift | child-process output decoded with the locale codec |
| GH-1, PS-2 | drift | the heredoc rule, broken once, is still prose |
| GH-3 | drift | the guard's matcher omits the PowerShell tool |
| GH-4 | obsolescence candidate | the silent fail-open is deliberate ("unenforced beats broken"); GH-4 asks for a message, not a block, so the rule may need wording that makes that plain |
| HR-2 | drift | an acceptance margin lowered by the agent with no person's bar |
| PS-1 | drift | allow rules in `gui/.claude/settings.json` with nothing named as their stand-in |
| VG-3 | divergence | corpus cases skip in CI by design; a waiver would name where they run |
| VG-4 | drift | no roll call of collected against reported tests |

## Tasks offered

One realignment task per drifted rule is offered to roadkeep's owner, following
[../adoption/realignment.md](../adoption/realignment.md).

**Decision (2026-09-25).** The owner accepted the tasks for the 18 rules proposed as
drift above. The divergence and obsolescence proposals (CD-3, CS-2, VG-3, GH-4) are not
yet decided. The tasks are filed in roadkeep's own backlog by a session in that
repository, not from here, since this repository does not edit an adopter's.

## Before and after

roadkeep is the project measured for the effect of realignment. The window before is
[roadkeep-before.json](roadkeep-before.json), the 14 days ending at the audited commit,
written by `scripts/window_metrics.py`, whose docstring states how each figure is
counted:

| Measure | Before |
|---|---|
| commits, first parent | 36 |
| tasks shipped | 24 |
| commits per task | 1.5 |
| bytes loaded every turn | 8,622 |
| stray files | 3 |
| days with a red gate, of days the gate ran | 5 of 5 |
| drift findings | 22 |

The window after is measured the same way, over 14 days ending a comparable period after
the last realignment task ships, into `roadkeep-after.json`. The comparison is
observational, not an experiment: roadkeep changes for other reasons, the models change,
and the person learns, and the report of the difference will say which of those it can
rule out. The gate ran only on the days work was pushed, so red days are counted against
those days, and the run list comes from the GitHub API rather than from git.

## Cost

| Step | Tokens | Wall time |
|---|---|---|
| checker | none (a script) | a few seconds |
| scanner | 181,312 | 637 s |
| verifier | 136,906 | 318 s |
