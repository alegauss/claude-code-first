# Drift inventory

Drift here is two artefacts of one project stating contradictory facts at that project's
pinned commit: a guide and the workflow it describes, a configuration comment and the
index it advises on, a ledger entry and the gate it says exists. Each item below was
checked at the pin in [corpus.md](corpus.md), both loci and the commit that made them
disagree. **Since** names the commit that introduced the later of the two sides, from
which the contradiction has stood; days standing are the pin's date minus that commit's
date. The list is what was met while checking a set of candidates, not the result of an
exhaustive search, so it bounds nothing. It supports the rule that a fact lives in one
place, and one item (DR2) is a claim about another project rather than internal drift.

## DR1 roadkeep's configuration calls the index the cheap cut, and its every-turn file says the prose is what to compress

**Locus 1.** `roadkeep.toml` says `budget --file` "reads the index at 36%" [roadkeep@91754240:roadkeep.toml#L244],
and concludes "the cheap cut, and it is the safe one" [roadkeep@91754240:roadkeep.toml#L246].

**Locus 2.** `agents.md` says the index is a "fifth of it, held by a test, so the prose is what to compress" [roadkeep@91754240:agents.md#L113].

**Since.** 2026-08-11, RK1094: "The index is now identified as 36% of the bytes" [roadkeep@c6464dd6].
The same commit edited `agents.md` and left the older advice in it (`git show
c6464dd6:agents.md` still says "a fifth"). RK1135 later rewrote that sentence and kept the
advice, "reclaim budget in agents.md without dropping a rule" [roadkeep@e3d27ce4].

**Could a check have caught it.** No. Both sides are prose advice drawn from a measurement;
the configuration itself says the figure should be re-read with `budget --file` and never
restated, and the remedy is one place for the advice, not a test.

**Status at the pin.** Open.

## DR2 roadkeep's configuration says Shio's agents.md declared 150 lines about itself, which Shio's file does not

This is a claim one project makes about another, not drift inside one project.

**Locus 1.** roadkeep's budget comment says the prose arrangement is the one "that let Shio's reach 186 KB while declaring 150 lines about itself." [roadkeep@91754240:roadkeep.toml#L235-L237]

**Locus 2.** Shio's `agents.md` at the commit where it reached 186 KB [shio@e73516a9f:agents.md]
has no line limit: `git show e73516a9f:agents.md | grep -n 150` matches only task ids
(SH150) and figures such as `--max-ops, default 1500`. `git log -S"150 lines" 821f18d74 --
agents.md CLAUDE.md` finds no Shio commit that ever added the phrase.

**Since.** 2026-07-29, RK30, the commit that wrote the comment: "hold the every-turn file to a declared budget" [roadkeep@13272828].

**Could a check have caught it.** No. The claim is about another repository's history, which
no check in roadkeep reads; a citation to the Shio commit would have exposed it.

**Status at the pin.** Open.

## DR3 polyweave's audit skill lists roadmap blocks A to H, and the roadmap has blocks through J

**Locus 1.** The audit skill tabulates the blocks `roadkeep block list` gives "today it answers:" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L52],
ending at H, "Proof on a real game" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L63].

**Locus 2.** The roadmap has two more blocks: "Voxel models from a declaration" [polyweave@6d1c136:docs/ROADMAP.md#L31]
and "A bar a person sets once" [polyweave@6d1c136:docs/ROADMAP.md#L33].

**Since.** 2026-09-24, block I: "plan voxel models from a declaration" [polyweave@91937d4].
The skill has one commit, its creation on 2026-09-22 [polyweave@c45f7b3].

**Could a check have caught it.** Yes: a test that compares the table with the output of
`roadkeep block list`, or a table generated from it. winwright moved a skill's count of
block criteria under such a test after the same kind of drift [winwright@a686d44].

**Status at the pin.** Open.

## DR4 polyweave's audit skill counts three governed files, and the configuration declares four

**Locus 1.** The audit skill runs lint over "the three governed docs" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L29],
says "The three governed files are written by the tool" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L115],
and that the configuration governs the roadmap, the changelog "and the improvements, and nothing else" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L128].

**Locus 2.** `roadkeep.toml` also declares a "deferred" [polyweave@6d1c136:roadkeep.toml#L14]
file in its `[files]` table [polyweave@6d1c136:roadkeep.toml#L10-L14].

**Since.** 2026-09-22, the commit that added the deferred store: "set the port aside until somebody records what it replaces" [polyweave@e26bd7c].

**Could a check have caught it.** Yes: a test that reads the `[files]` table and the
skill's statement of it; better, the skill names no count and points at the configuration.

**Status at the pin.** Open.

## DR5 freewilly's CONTRIBUTING says CI no longer runs roadkeep lint, and a workflow runs it on every push

**Locus 1.** CONTRIBUTING tells the reader to run lint by hand because "CI no longer does." [freewilly@c1c2eaf:CONTRIBUTING.md#L13-L14],
and says the lint gate on "every push was removed" [freewilly@c1c2eaf:CONTRIBUTING.md#L31-L32].

**Locus 2.** `.github/workflows/roadkeep.yml` runs "on: [push, pull_request]" [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L11]
a job named "name: roadkeep lint" [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L15],
through "uses: alegauss/roadkeep@main" [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L19].

**Since.** 2026-08-29: "put lint back in CI" [freewilly@714360e]. CONTRIBUTING was rewritten
when the gate was removed [freewilly@cd630d6] and `git log 714360e..c1c2eaf --
CONTRIBUTING.md` is empty. The CI header in `check.yml` was updated in the same commit and
agrees with the workflow [freewilly@c1c2eaf:.github/workflows/check.yml#L12-L15].

**Could a check have caught it.** Yes: a test that reads CONTRIBUTING's table of workflows
and the files under `.github/workflows/`. freewilly's `PackagingTests` already read
workflow files, so the kind of test exists in the project.

**Status at the pin.** Open.

## DR6 freewilly's ledger records DD118's gate as shipped, and the gate at the pin does not run it

**Locus 1.** The changelog entry for DD118 says "The gate runs the vendored engine beside the action it floats on and prints both versions" [freewilly@c1c2eaf:docs/CHANGELOG.md#L202].

**Locus 2.** The lint workflow at the pin has one step after the checkout, "uses: alegauss/roadkeep@main" [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L19];
no line of it names `.roadkeep` or prints a version. DD118 had added a step that ran the
vendored engine and printed both versions, and a test holding it: "ensuring that the gate runs the vendored engine alongside the main action" [freewilly@956e91e].

**Since.** 2026-08-19, the commit that deleted the workflow, "workflow as it is no longer needed" [freewilly@cd630d6],
and with it the test, "removing a redundant test related to the" [freewilly@cd630d6] workflow
(its diff removes `The_gate_runs_the_vendored_engine_beside_the_one_it_floats_on`). The
workflow restored on 2026-08-29 [freewilly@714360e] has the action and not the DD118 step.

**Could a check have caught it.** Yes, and one did until it was deleted: DD118's own test
read the workflow for the vendored engine's command. A check that every shipped entry
naming a gate still has its test would have failed on the deletion.

**Status at the pin.** Open.

## DR7 Shio's agents.md says the suites workflow runs two of the three gates, and it runs all three

**Locus 1.** The index names the gates, "Three commands are gates" [shio@821f18d74:agents.md#L168],
and says the suites workflow "runs two of the three on" [shio@821f18d74:agents.md#L175] every push.

**Locus 2.** `suites.yml` has a job for each of the three: "name: pnpm test" [shio@821f18d74:.github/workflows/suites.yml#L33],
"name: mvnw clean test" [shio@821f18d74:.github/workflows/suites.yml#L134]
and "name: pnpm conformance" [shio@821f18d74:.github/workflows/suites.yml#L195].

**Since.** 2026-08-10, SH241: "the java suite and the console walk run without being asked" [shio@65f8068a0].
The sentence in `agents.md` dates from the workflow's creation on 2026-08-07, when it had
two jobs [shio@9b7183ddf].

**Could a check have caught it.** Yes: a test that reads the sentence and the workflow's
jobs. Shio already has a test that reads its CI workflows, `ci-gates.test.mjs` [shio@821f18d74:agents.md#L161-L162].

**Status at the pin.** Open.

## DR8 Shio's build skill pipes the test gate into grep, which agents.md forbids

**Locus 1.** The index says "Never pipe a gate into" [shio@821f18d74:agents.md#L150] `grep`,
for the log and for the verdict.

**Locus 2.** The `shio-build-test` skill gives the command for counting tests as the suite
piped into `grep`: "-Dskip.npm=true 2>&1" [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L17].

**Since.** 2026-08-02, when the rule first entered `agents.md`: "keep the run when reading the suite total" [shio@ddec6a424].
The skill has one commit, its creation on 2026-07-29 [shio@f4ffdb0d9]; the rule's present
wording is from SH788 [shio@c1b9e8947].

**Could a check have caught it.** Yes: Shio holds this rule with a lint, which reads "The two files that document how to run this suite." [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L53]
The skill is not one of them; adding it to that list is the check.

**Status at the pin.** Open.

## DR9 Shio's roadkeep.toml says the engine is not vendored, and agents.md says it is

**Locus 1.** The configuration's header says "roadkeep is not vendored here and there is no path to a checkout" [shio@821f18d74:roadkeep.toml#L8]
and "This file is the only roadkeep artefact the repository carries." [shio@821f18d74:roadkeep.toml#L11]

**Locus 2.** The index says "The engine is vendored" [shio@821f18d74:agents.md#L272],
"git-ignored, reproduced by" [shio@821f18d74:agents.md#L273] the installer, which the
repository carries [shio@821f18d74:install-roadkeep.cmd].

**Since.** 2026-08-14: "vendor the engine into .roadkeep and always run that copy" [shio@1a541993e].
The header dates from 2026-08-02 [shio@6a4814549].

**Could a check have caught it.** No, not in practice: the header is a comment, and only a
test matching its wording could hold it. The remedy is to state how the engine arrives in
one file and point at it from the other.

**Status at the pin.** Open.

## Summary

| Id | Project | The two artefacts | Days standing | Checkable |
|---|---|---|---|---|
| DR1 | roadkeep | `roadkeep.toml` budget comment, `agents.md` | 44 | no |
| DR2 | roadkeep (about Shio) | `roadkeep.toml` budget comment, Shio `agents.md` | 57 | no |
| DR3 | polyweave | audit skill, `docs/ROADMAP.md` | 0 | yes |
| DR4 | polyweave | audit skill, `roadkeep.toml` | 2 | yes |
| DR5 | freewilly | `CONTRIBUTING.md`, `.github/workflows/roadkeep.yml` | 19 | yes |
| DR6 | freewilly | `docs/CHANGELOG.md` (DD118), `.github/workflows/roadkeep.yml` | 29 | yes |
| DR7 | Shio | `agents.md`, `.github/workflows/suites.yml` | 45 | yes |
| DR8 | Shio | `agents.md`, `shio-build-test` skill | 53 | yes |
| DR9 | Shio | `roadkeep.toml` header, `agents.md` | 41 | no |
