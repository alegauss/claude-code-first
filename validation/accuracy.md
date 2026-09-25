# How far the audit can be trusted

An audit that judges other projects is only as useful as its error rate is known. This
page reports what has been measured so far and holds the sample on which the rest will be
measured. The rest needs a person: an agent checking an agent's audit measures agreement,
not accuracy.

## What has been measured: scanner against verifier

In each of the five audits a scanner reported findings and a verifier, run separately,
re-read each cited locus and classified it. Both were the same model.

| Project | Scanner findings | Confirmed | Rejected | Passes the verifier turned into failures | Rules only the verifier judged |
|---|---|---|---|---|---|
| roadkeep | 20 | 20 | 0 | 1 | 0 |
| polyweave | 17 | 17 | 0 | 0 | 5 |
| freewilly | 24 | 23 | 1 | 1 | 0 |
| winwright | 21 | 19 | 2 | 0 | 1 |
| Shio | 30 | 28 | 2 | 0 | 0 |
| **All** | **112** | **107** | **5** | **2** | **6** |

The verifier confirmed 107 of 112 findings (95.5%). It rejected five, each for a reason a
reader can check in the project's notes: a rule whose condition did not hold (VG-7 in
freewilly), a commit that filed tasks rather than shipping them (CD-2 in Shio), an
instruction the scanner missed (CS-1 in Shio), and two findings about files outside the
committed tree (CS-2 and PS-3 in winwright). It found two failures the scanner had passed.

**What this does not show.** Scanner and verifier share a model, so an error they share
passes both. A high agreement rate is compatible with a systematic misreading of a rule.
That is why the measure below is taken against a person.

## What remains: the person's verdicts

For the 35 rules below, drawn at random with a fixed seed so the draw can be repeated
(three judged failures, three judged passes and one checker verdict per project), the
person records a verdict without reading the audit's first. Agreement is then computed per
rule and overall, with Cohen's kappa where the sample allows, and every disagreement is
listed with its cause: an ambiguous rule, a checker defect, a missing fixture, or the
person's own error. Ambiguous rules are rewritten; defects become tasks.

| Project | Rule | Audit verdict | By | Locus | Person's verdict |
|---|---|---|---|---|---|
| roadkeep | VG-4 | fail | verifier | .github/workflows/gate.yml:64 | |
| roadkeep | AP-1 | fail | verifier | tests/test_commands.py:116 | |
| roadkeep | VG-1 | fail | verifier | commit bc738ea6 | |
| roadkeep | PS-3 | pass | verifier | git ls-files | |
| roadkeep | PG-3 | pass | verifier | roadkeep.toml:306-308 | |
| roadkeep | EP-4 | pass | verifier | src/roadkeep/verbs/reading.py:45-62 | |
| roadkeep | VG-5 | pass | checker | | |
| polyweave | PG-5 | fail | verifier | site/src/lib/roadmap.ts:42-44 | |
| polyweave | EP-3 | fail | verifier | src/polyweave/capabilities.py:57-63 | |
| polyweave | CD-4 | fail | verifier | commit 8d762a2 | |
| polyweave | GH-1 | pass | verifier | docs/CHANGELOG.md | |
| polyweave | VG-3 | pass | verifier | tools/gate.py:83-102 | |
| polyweave | AP-4 | pass | verifier | commits 5eb1a8e, ddad82d | |
| polyweave | CD-1 | pass | checker | | |
| freewilly | VG-1 | fail | verifier | commit d1f00b9 | |
| freewilly | CD-6 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md | |
| freewilly | PS-2 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:22 | |
| freewilly | CS-4 | pass | verifier | docs/CHANGELOG.md | |
| freewilly | AP-4 | pass | verifier | README.md, docs/, llms.txt | |
| freewilly | VG-7 | pass | verifier | commit d1f00b9 | |
| freewilly | VG-5 | pass | checker | | |
| winwright | CD-4 | fail | verifier | commit d44d623 | |
| winwright | AP-2 | fail | verifier | site/public/llms.txt:133-136 | |
| winwright | PG-2 | fail | verifier | docs/ROADMAP.md:28 | |
| winwright | CS-2 | pass | verifier | commit d44caee | |
| winwright | HR-2 | pass | verifier | repository-wide | |
| winwright | PS-3 | pass | verifier | tools/run-tests-vm.ps1:55-59 | |
| winwright | IS-1 | pass | checker | | |
| Shio | CD-6 | fail | verifier | agents.md:237-253 | |
| Shio | GH-2 | fail | verifier | .github/workflows/roadkeep.yml:12-13 | |
| Shio | EP-1 | fail | verifier | roadkeep.toml:7-11 | |
| Shio | CD-4 | pass | verifier | agents.md:251-253 | |
| Shio | AW-3 | pass | verifier | shio-site/scripts/ai-writing.test.mjs | |
| Shio | VG-6 | pass | verifier | scripts/gate-stamp.mjs:330-365 | |
| Shio | PG-1 | pass | checker | | |

**Repeatability.** The verifier is a model, so the same audit run twice on the same commit
may differ. Running one audit a second time at its commit, and comparing the reports with
`scripts/report.py diff`, measures that. It has not been run yet.

## Limits

The sample is 35 of the 280 verdicts, seven per project, drawn to include both verdicts
and both kinds of check; it is small, and the rate it yields will carry a wide interval.
One person gives the reference verdicts, and that person owns all five projects, which is
the internal threat of [../evidence/validity.md](../evidence/validity.md) applied to the
audit itself.
