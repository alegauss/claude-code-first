# Realigning a project that has drifted

This guide is for a project that adopted Claude Code First, or grew up near it, and no
longer meets the level it claims. It turns an audit report into work the project can do
in order: classify each failure, file the drift as tasks when the owner asks for them,
work one level at a time, and measure each level with a second audit. The rules are in
the [chapters](../spec/README.md), the levels in
[conformance.md](../spec/conformance.md) and the report in [report.md](../spec/report.md).
A project starting from nothing reads [greenfield.md](greenfield.md) instead.

The `realign` skill in [../skills/realign/SKILL.md](../skills/realign/SKILL.md) walks an
agent through the same steps.

**Who decides.** The audit reports and offers tasks. Filing them in the project's
backlog, writing a waiver into its `ccf.toml`, and changing its code are the owner's
decisions, and nothing in this guide makes them on the owner's behalf. That is a
non-goal of this specification ("Editing an adopter's repository", in
[../docs/ROADMAP.md](../docs/ROADMAP.md)), and it is the boundary rule
[HR-1](../spec/HR.md) draws for the agent inside a project too.

## 1. Run the audit

Run the `audit` skill ([../skills/audit/SKILL.md](../skills/audit/SKILL.md)) against the
project at the level it claims in `ccf.toml`, or at the level it means to reach. The
report names every rule examined, with a verdict, a locus and evidence. Keep the JSON
file: it is the baseline every later audit is compared with.

Two verdicts need care before anything is classified:

- **could not run** is neither a pass nor a failure. It keeps the level from being
  achieved until it is resolved, so settle why the check could not decide (a missing
  tool, a configuration the checker cannot read) before treating the rest as the whole
  picture.
- **fail on an expired waiver** is a decision that ran out, not new drift. Its owner
  either renews it with a new date or files the work it was waiting for.

A scanner reads a sample of the repository, so a clean chapter does not prove the
chapter clean. Some drift no check can see: [DR1 and DR9](../evidence/drift.md) are two
prose statements of one fact that disagree, where the remedy is one place for the fact,
not a test.

## 2. Classify each failure

Every `fail` in the report is one of three things, and the person decides which. An agent
can propose a class from the evidence; it cannot choose divergence or obsolescence, since
both are claims about what the project or the specification ought to be.

| Class | What it means | What follows |
|---|---|---|
| Drift | the project meant to conform and slipped | a task in the project's own backlog, one per rule |
| Divergence | the project departs from the rule on purpose | a waiver in `ccf.toml`, with a reason, an owner, a date and an end |
| Obsolescence | the rule no longer fits the case it was written for | a report upstream to this specification, and a waiver while it is examined |

### Drift

The test for drift is that the project's own files already state the rule it broke.
Each item in [../evidence/drift.md](../evidence/drift.md) was checked at the corpus pins,
and four of them show what a drift failure looks like in an audit:

- **DR8, Shio.** `agents.md` forbids piping a gate into `grep`, and the `shio-build-test`
  skill gives the suite piped into `grep`. The audit fails [VG-2](../spec/VG.md), whose
  scope is every file that tells an agent how to run a gate. The project had already
  chosen the rule, so this is drift. Shio's lint over the files that document the suite
  does not read the skill ([F300](../evidence/findings/F300.md)); adding the skill to that
  lint is the check [GH-1](../spec/GH.md) asks for.
- **DR3 and DR4, polyweave.** The audit skill tabulates roadmap blocks A to H while the
  roadmap has blocks through J, and counts three governed files where `roadkeep.toml`
  declares four. Both are lists in a skill that no gate checks against their source, a
  failure of [IS-5](../spec/IS.md) ([F7](../evidence/findings/F7.md)). The skill meant to
  be accurate, so this is drift. The better remedy names no count and points at the
  configuration.
- **DR7, Shio.** `agents.md` says the suites workflow runs two of the three gates, and it
  runs all three. A count about the present state typed into prose fails
  [AW-1](../spec/AW.md). Shio already has a test that reads its CI workflows, so the
  check exists in kind.

These are level 2 and level 3 rules, which matters for the order in section 4.

### Divergence

A divergence is a choice the owner would make again. The specification leaves some
choices open on purpose ([../evidence/divergences.md](../evidence/divergences.md)), and a
rule the project departs from deliberately is recorded as a waiver in `ccf.toml`
([deviations.md](../spec/deviations.md)):

```toml
[[waiver]]
rule = "VG-5"
reason = "the guest half of the suite needs a VMware host; it runs on the owner's machine before each release"
owner = "the person accountable for the decision"
date = "2026-09-25"
expires = "2027-03-25"
```

The example is winwright's, from decision D4: its guest suite cannot run on a hosted
runner, and D4 allows a gate that cannot run in CI as a documented deviation that names
the gate, the reason and where it does run. A waiver with no `expires` and no `task`, or
without a reason, owner or date, is refused by the checker.

Not every departure needs a waiver. A project with no every-turn file, as freewilly and
winwright have, is conforming under decision D2, and [IS-1](../spec/IS.md) and
[IS-2](../spec/IS.md) do not apply to it.

### Obsolescence

A rule is obsolete for a project when the case it was written for has changed, not when
it is costly. [IS-6](../spec/IS.md) shows how that can happen: it rests on served tool
schemas measured as a fixed cost of every session ([F4](../evidence/findings/F4.md)), and
the harness documentation now says a session with tool search on is not sent every
definition up front (H9 in [../evidence/harness.md](../evidence/harness.md)). A project that measures what its sessions pay and finds the rule's
premise gone has evidence the specification needs.

Report it upstream to this specification with the rule's address, the project and
commit, and the measurement. Waivers are evidence for revising a rule
([deviations.md](../spec/deviations.md)), and an obsolescence report is the strongest
kind. Until the rule changes, the project records a waiver that cites the report, so the
audit shows the departure as a decision and not as drift.

## 3. File the drift, when the owner asks

The audit offers the tasks; the owner decides whether they are filed. When the owner
asks, file them through the project's own roadkeep (or another planning tool that meets
[PG-1](../spec/PG.md)), never by editing its planning files:

- **One task per rule.** Several loci failing one rule are one task, because one change
  to the project's gates usually holds all of them. A task that spans rules is a batch,
  which [CD-2](../spec/CD.md) works one task at a time anyway.
- **The symptom on the line, the design in the rationale** ([PG-2](../spec/PG.md)). The
  line says what the audit saw, such as "the build skill pipes the test gate into grep".
  A task that names nothing wrong is not filed ([CD-5](../spec/CD.md)).
- **The rule's address in the rationale**, as a link to its chapter, with the report's
  locus and evidence, so the task can be closed against the rule and not against memory:
  `roadkeep add "<the symptom>" --section "<title>" --section-body-file <path>`.
- **The check with the fix.** A rule the project has now seen broken is held by a guard
  or a gate that reads what it governs ([GH-1](../spec/GH.md)). Most drift tasks
  therefore carry a test as well as the correction.

## 4. Work one level at a time

The levels are cumulative ([conformance.md](../spec/conformance.md)), so a level 2 fix
does not count while a level 1 rule fails. File and work the drift of the lowest failing
level first, and leave the tasks of the levels above unfiled until it is reached. The
first level's fixes often change what the second level finds: a split every-turn file
(section 6) moves content that later rules then judge in its new place.

In the examples above, DR8 (VG-2) is level 2 and DR3, DR4 and DR7 (IS-5, AW-1) are level
3. A project claiming level 2 fixes DR8 and the rest of level 2 before it opens the
level 3 tasks.

## 5. Re-audit after each level

When the last task of a level ships, run the audit again at that level and compare the
two reports:

```sh
python scripts/report.py diff docs/audits/<older>.json docs/audits/<newer>.json
```

The first line gives both commits and the achieved level before and after; each line
under it is one rule whose verdict changed. A level is reached when the report's
`achieved_level` says so, which `report.py validate` holds to the verdicts. A rule that
moved from `pass` to `fail` during the work is new drift, filed like the rest.

Commit each report and its Markdown rendering under the path the project declares, such
as `docs/audits/<date>-<commit>.json`, so the project's history shows the trend. Then
update `level` in `ccf.toml` if the claim has changed, and start the next level.

## 6. Recipes for known migrations

Three migrations recur in the corpus and have a recipe. Each is one task and one commit
([CD-1](../spec/CD.md)).

### Splitting an every-turn file

For a failure of [IS-1](../spec/IS.md) or [IS-2](../spec/IS.md): the file every turn
loads has grown past its budget, or holds what only some turns need. Shio's grew about
nineteenfold under a budget stated in prose, and roadkeep's grew to its gated ceiling
([F1](../evidence/findings/F1.md)).

1. Measure the file in bytes and lines, and mark each section with the turns that need
   it. What a turn touching no specific area needs stays; the rest moves.
2. Move each area into a trigger-loaded skill whose description names the occasions and
   words it loads on ([IS-3](../spec/IS.md)), or into a file the index points to.
   Shio's split took its file from 185,734 to 14,433 bytes
   ([F2](../evidence/findings/F2.md)).
3. Leave one line in the index for each thing moved, saying where it went.
4. Give every skill body and every file read on demand a ceiling that a gate enforces
   ([IS-4](../spec/IS.md)). Without one the moved content keeps growing where it lands:
   Shio's area files went from 184,521 bytes at the split to 1,730,001 at the pin
   ([F3](../evidence/findings/F3.md)).
5. Lower the every-turn budget to just above the file's new size. roadkeep did this after
   each move rather than leave the room free ([F2](../evidence/findings/F2.md)).

The split cuts what every turn pays. No finding shows it cuts what a task reads in total:
in Shio the moved content exceeded what it replaced (F2).

### Moving a procedure into a skill

For a procedure in the every-turn file that only some turns follow, such as building,
committing or releasing. roadkeep measured 26 lines of its file as needed only on a turn
that builds or commits, moved them into a project skill, and the file dropped to 104 of
125 lines ([F2](../evidence/findings/F2.md)).

1. Move the procedure into `.claude/skills/<name>/SKILL.md`, with a description naming
   when it loads ([IS-3](../spec/IS.md)), and replace it in the index with a pointer.
2. Give the body a ceiling that a gate enforces ([IS-4](../spec/IS.md)). winwright caps
   its skills at 700 characters of description and 6,000 of body
   ([F406](../evidence/findings/F406.md)).
3. Move the procedure's checks with it. Any lint that read the old location reads the
   new one. DR8 is this step missed: Shio's rule against piping a gate is held by a lint
   over the files that document the suite, and the build skill is not one of them
   ([F300](../evidence/findings/F300.md)).
4. Check the commands, paths and names the procedure lists against their source
   ([IS-5](../spec/IS.md)).
5. Lower the every-turn budget, as in the split above.

### Pinning line endings

For a failure of [EP-2](../spec/EP.md): no committed `.gitattributes` declares the line
terminators, or no gate holds them. roadkeep counted 45 modules ending CRLF and 11 ending
LF, and a CRLF file hid seven pages from an extractor in Shio
([F404](../evidence/findings/F404.md)).

1. Add `.gitattributes` from the [template](../templates/dot-gitattributes).
2. Run `git add --renormalize .` once, and read `git status` before committing: every
   file it lists changes only in its terminators.
3. Commit the renormalisation by itself, with no other change in it, so a later reader
   can skip it as one commit.
4. Add a gate that fails on a file whose terminators depart from the declaration. The
   checker decides only the declared half of EP-2; the gate is judged by the verifier.

Renormalisation touches files across the tree, so run it when no other session holds a
claim on them ([CS-2](../spec/CS.md)). If it has to wait, the waiver in
[deviations.md](../spec/deviations.md) is the model: a reason, an owner, and an end date.

### Not a recipe: committing a launcher

The backlog's design names committing a guard launcher as a migration. It is not a recipe
here, because the evidence for it is in doubt. The corpus committed a launcher under
`.claude/hooks/` because a guard shipped in a plugin did not load in a web session in
August 2026 ([F400](../evidence/findings/F400.md), R1/S2, harness observation O3). The
harness documentation read on 2026-09-24 says a plugin enabled for the claude.ai account
loads in cloud sessions as a synced plugin (H10 in
[../evidence/harness.md](../evidence/harness.md)). F400 has one origin, and its grade
requires the premise to be re-checked before a rule is drawn from it. Chapters
[EP](../spec/EP.md) and [GH](../spec/GH.md) carry it as an open question; until a cloud
session on a current release settles it, the audit fails no rule for a missing launcher,
and there is nothing to realign.
