# Adopting Claude Code First in an existing codebase

This guide brings a repository that already has history, instructions and perhaps a
backlog under the specification. Every step names the rules it satisfies and the level it
reaches; the rules are in the [chapters](../spec/README.md), and the levels in
[conformance.md](../spec/conformance.md). The steps reach level 2, with one ceiling from
level 3 that an existing project needs earlier than a new one.

**The evidence is one case.** Shio is the only brownfield project in the corpus: its
history starts on 2019-07-30, and 1,778 commits precede the first commit that touches an
agent file, on 2026-03-24 ([case study](../evidence/cases/shio.md), section 1). Shio did
not follow the order below. It added its instructions first, split them after they grew,
adopted a planning tool four months later and put its gates on every push later still.
The order here is the one its incidents argue for, and each step says which incident.
A project with no history starts from [greenfield.md](greenfield.md) instead.

## Before changing anything

Inventory what the repository already tells an agent and what it already records, and
write nothing until the inventory is read. An adoption that starts by writing a fresh
`agents.md` over an existing one, or a fresh roadmap beside a kept one, creates two
authorities on one subject, which is the drift the corpus records most
([../evidence/drift.md](../evidence/drift.md); DR9 is Shio's own two descriptions of how
its planning engine arrives).

List, with the size of each in bytes and lines:

- **Instruction files**: `CLAUDE.md` in any folder, `.claude/CLAUDE.md`, `agents.md`,
  `AGENTS.md`, and everything they import. These are what every turn pays for.
- **Skills and commands** under `.claude/`, and any plugin the repository publishes
  (`.claude-plugin/`), kept apart in the list.
- **Settings and hooks**: `.claude/settings.json`, `.mcp.json`, and what each allow, deny
  and ask rule and each hook covers.
- **Planning and history files**: roadmaps, changelogs, issue exports, design documents,
  with the date each was last changed (`git log -1 --format=%cs -- <path>`).
- **Gates**: test commands, lint, and each CI workflow with its triggers. Shio's
  workflows were dispatch-only until SH579 ([case study](../evidence/cases/shio.md),
  section 4); a list of workflows that does not record the triggers misses that.
- **The commit tool and the ignore file**, and whether the tool stages everything.

Then measure the backlog before choosing its limits. roadkeep's `adopt` command does this
and writes nothing: `roadkeep adopt docs/ROADMAP.md` for the roadmap, `--ledger` for a
changelog and `--sections` for a rationale file. Shio's configuration keeps what such a
measurement found at adoption: "0 of 78 lines exceed" [shio@821f18d74:roadkeep.toml#L328]
the symptom limit, while "70 of 78 lines exceed it" [shio@821f18d74:roadkeep.toml#L333]
for the reason field, and its header states the aim, "Every value here is what docs/ROADMAP.md already spells" [shio@821f18d74:roadkeep.toml#L13].

Report the inventory to the person, with a proposed level and the waivers the history
will need, before the first write. The level and every waiver are the person's decision.

## 1. Start with an index and a budget

Write the every-turn file as a short index with a budget a gate enforces, and move each
area's detail into a skill or a file read on demand from the start. Put a ceiling on
those files too.

Shio shows the cost of the other order. `agents.md` was 9,843 bytes at adoption, 40,375 on
2026-07-26 and 185,734 at the end of 2026-07-28, under a token budget stated in the same
file and checked by nothing ([F1](../evidence/findings/F1.md)). The split of the next day
took it to 14,433 bytes and moved the detail into `docs/agents/` and eight skills
([F2](../evidence/findings/F2.md)). The moved content then kept growing with no ceiling:
the area files went from 184,521 bytes at the split to 1,730,001 at the pin
([F3](../evidence/findings/F3.md)). The index at the pin states the principle it was
split on: "it is deliberately thin: it is loaded into every session on every turn, so P3 applies to it" [shio@821f18d74:agents.md#L61-L62].

Where the inventory found an instruction file already, keep its content and move it; do
not discard what the project already learnt. With roadkeep, the budget is a `[budgets]`
entry in `roadkeep.toml`, held by `roadkeep lint`. Set it just above the size the index
lands at, in lines and in bytes.

| Rule | What this step gives it | Level |
|---|---|---|
| [IS-1](../spec/IS.md) | the every-turn file and what it imports carry a budget a gate enforces | 1 |
| [IS-2](../spec/IS.md) | the file is an index that points at skills and area files | 1 |
| [IS-3](../spec/IS.md) | each skill's description names the occasions it loads on | 1 |
| [IS-4](../spec/IS.md) | each skill body and area file has a ceiling of its own under a gate | 3 |

IS-4 is a level 3 rule, but an existing project has the content already, so the ceiling
costs least on the day the content is moved.

## 2. Import the backlog and accept its legacy limits explicitly

Bring the existing roadmap, changelog and rationale under the planning tool, as they are,
and state in its configuration where the history cannot meet a limit.

With roadkeep, `roadkeep init --existing` declares the files that are already there,
reads the prefix from the ids the roadmap carries and the blocks from its headings, and
scaffolds only what is missing. Run `roadkeep lint`, then set each limit from the
measurement taken before changing anything. Where old entries exceed a limit, raise the
limit for that file only and write the reason beside it. Shio did this for its ledger:
"233 entries predate the tool and read 1038" [shio@821f18d74:roadkeep.toml#L345]
characters at the median, so its changelog limit is "why = 4200" [shio@821f18d74:roadkeep.toml#L350],
and two prose rules are switched off for the same file as "The two prose rules this file's history cannot obey" [shio@821f18d74:roadkeep.toml#L354].
The roadmap keeps the strict limits, and the write path still refuses long new entries,
because what the tool writes "is short by construction" [shio@821f18d74:roadkeep.toml#L349].

A legacy limit of this kind is not a waiver. [AW-2](../spec/AW.md) governs the prose an
agent writes, and the write path still refuses it; the raised limit covers entries no
agent will write again.

Shio rewrote its roadmap before the tool took it over ("make the roadmap a queue again" [shio@490a698a0]),
after its lines had reached an average of 142 words under a one-sentence rule stated in
prose; at the pin its open lines average 52 words with none above 61
([F101](../evidence/findings/F101.md)). The sources cannot separate the rewrite's effect
from the limit's, so a rewrite first is an option, not a step.

| Rule | What this step gives it | Level |
|---|---|---|
| [PG-1](../spec/PG.md) | the roadmap, ledger and rationale are governed files | 1 |
| [AW-2](../spec/AW.md) | new planning prose is refused at the write over its limit | 1 |
| [PG-5](../spec/PG.md) | each open block gets criteria written with it, kept where shipping does not delete them | 1 |
| [PG-6](../spec/PG.md), [HR-1](../spec/HR.md) | a deferred store (`roadkeep declare deferred`) holds work waiting on a person or on hardware | 1 |

## 3. Keep legacy artefacts, and say which copy is live

Leave files that predate the adoption where they are, and write, in the file or in the
index, that they are history and which file replaced them. Shio keeps its old
`CHANGELOG.md` at the root, whose newest entry is "0.3.8 (Oct 10, 2021)" [shio@821f18d74:CHANGELOG.md#L1]
and whose last change is dated 2021-10-10 [shio@9cf45529a], beside the governed ledger in
`docs/CHANGELOG.md`. Nothing at the pin marks the root file as superseded.

This step satisfies no rule. No finding records harm from an unmarked legacy file, and
the practice of one live copy per fact is itself an open question in
[IS.md](../spec/IS.md). The reason to do it anyway is the drift inventory, in which every
item is two artefacts that state one fact differently
([../evidence/drift.md](../evidence/drift.md)); a mark costs one sentence.

## 4. Wire the guards and write the commit rules

Wire the planning tool's guard, name what stands in for any prompt the settings remove,
and write the commit rules where the agent reads them. With roadkeep,
`roadkeep install --committed` writes the launcher and `.mcp.json`. Where the repository
already has a `.claude/settings.json`, merge the hook entries into it by hand; do not
replace it.

Shio's commit tool stages the whole tree, and its ignore file records why each pattern
was added: the tool "stages everything, so a" [shio@821f18d74:.gitignore#L60-L61]
stray log is committed with the fix. A brownfield tree carries more such files than a new
one, so read `git status --short` before the first governed commit and add ignore rules
for what it shows.

| Rule | What this step gives it | Level |
|---|---|---|
| [PG-1](../spec/PG.md) | a `PreToolUse` guard is wired for the governed files | 1 |
| [PS-1](../spec/PS.md) | the guards and gates that replace removed prompts are named in committed files | 1 |
| [PS-3](../spec/PS.md) | credentials leave the working tree, whatever the ignore file says | 1 |
| [CD-1](../spec/CD.md) to [CD-6](../spec/CD.md) | one task per commit, staged by path, a title the agent writes, filings that name something wrong, attribution stated | 1 |
| [PS-2](../spec/PS.md), [GH-3](../spec/GH.md) | forbidden actions are refused by ask or deny rules; the guard matches the shell | 2 |

## 5. Add gates that measure before the agent's first feature

Before the agent ships its first feature, put the project's existing test and lint
commands on every push, written without pipes, and take the first measurements the gates
will be compared against. Where a suite is already red, record each red as an expiring
exception tied to the task that removes it rather than turning the suite off.

Shio adopted its instructions on 2026-03-24 and put its suites on every push with SH579 on
2026-08-07. Before that the workflows were dispatch-only, and two suites stayed red while
"Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4]
mentioned either ([case study](../evidence/cases/shio.md), section 4). Its remedy is the
ledger this step asks for: each red is "dated, time-boxed, and pointing at the open task that removes it" [shio@821f18d74:red-suites.json#L2].

A brownfield gate also has a history to be measured against: the size of the every-turn
file, the length of the roadmap's lines, the number of tests the suite reports. Record
them in the adoption commit's body or the rationale of the first task, so the first
change that claims an improvement has a figure to beat.

| Rule | What this step gives it | Level |
|---|---|---|
| [VG-5](../spec/VG.md) | the gates run in CI on every push to the branches work lands on | 2 |
| [VG-1](../spec/VG.md), [VG-8](../spec/VG.md) | work is called done, and shipped, only on a passing gate | 2 |
| [VG-2](../spec/VG.md) | no file that documents a gate pipes it; skills included, which Shio's lint missed | 2 |
| [VG-3](../spec/VG.md), [VG-6](../spec/VG.md) | a check that did not run is not a pass; a red about something else is a defect | 2 |
| [VG-7](../spec/VG.md) | a known red is an exception that expires | 2 |
| [GH-2](../spec/GH.md), [GH-5](../spec/GH.md) | the planning lint runs in CI behind the guard; the committed settings are under a test | 2 |
| [EP-2](../spec/EP.md) | line terminators are declared and held; an old tree is where mixed endings are found | 2 |
| [VG-9](../spec/VG.md) | a change made to improve a figure is measured before and after | 3 |

## 6. Keep project skills apart from published ones

Where the repository publishes skills or a plugin for other agents, keep the skills that
serve a session changing this source tree apart from the ones it publishes, and load the
published ones in the repository's own settings. Shio's four published skills "were published by, and never loaded in, the repository that wrote them" [shio@d1853cbea];
its rule since SH949 is that "a plugin skill serves a session driving an instance; a project skill serves a session changing this source tree" [shio@821f18d74:agents.md#L90-L91],
and a test fails if a name appears in both sets
([case study](../evidence/cases/shio.md), section 6).

Loading the published artefact is a rule of the agent-facing profile. Keeping the two
name sets apart is not: [AP.md](../spec/AP.md) records it as an open question, because
no collision of names is recorded and the test is not seen failing.

| Rule | What this step gives it | Level |
|---|---|---|
| [AP-3](../spec/AP.md) | the published surface is exercised as installed, not only from the checkout | profile |
| [AP-1](../spec/AP.md), [AP-2](../spec/AP.md) | the published surface has ceilings and checked names | profile |

## 7. Declare the level and run the checker

Write `ccf.toml` at the root with the level the person chose, the specification version
and the waivers below, then run the checker:

```sh
python <this-repository>/scripts/check_conformance.py <repository>
```

It decides IS-1, PG-1, CD-1, VG-2, VG-5 and EP-2 from the files and the history, and
reads the level and waivers from `ccf.toml`. CD-1 is decided over the whole history of the
ledger, so a commit from before the adoption that added several entries fails it; that
is a waiver, not a rewrite of history. The rules the checker cannot decide are for the
audit skill, run once the first governed tasks have shipped.

## Waivers for what the history cannot meet

A waiver in `ccf.toml` records a rule the project departs from on purpose, with a reason,
an owner, a date and either an expiry or the task that ends it
([deviations.md](../spec/deviations.md)). A departure without one is drift, and the
checker reports it as a failure. The shape follows Shio's red-suite ledger.

```toml
level = 2
spec_version = "0.1.0"
profile = false

[[waiver]]
rule = "EP-2"
reason = "line endings are being renormalised across the tree"
owner = "the person accountable for the decision"
date = "2026-09-25"
task = "EX12"

[[waiver]]
rule = "CD-1"
reason = "commits before the adoption added several ledger entries each"
owner = "the person accountable for the decision"
date = "2026-09-25"
expires = "2026-12-31"
```

Three kinds of departure are common in an existing repository:

- **History that cannot be rewritten**, such as batched ledger commits before the
  adoption. The waiver names the reason; an expiry forces the person to look again.
- **Work in progress**, such as renormalising line endings or moving a suite onto CI. The
  waiver names the task that ends it.
- **A rule the project judges wrong for its case.** The waiver says why. A rule most
  adopters waive is a rule the specification re-examines.

A legacy limit in the planning tool's configuration, as in step 2, is not a waiver: the
rule it bears on is still met where new prose is written.

## What one case cannot tell you

- **Whether this order works better than Shio's.** Shio followed another order, and its
  incidents argue for this one; no project has followed this one from an existing
  history.
- **Whether the split lowered what a task reads.** The moved content outgrew what it
  replaced, and what a session read is only in transcripts
  ([F2](../evidence/findings/F2.md), [F3](../evidence/findings/F3.md)).
- **How much depends on Shio's rate.** Shio ran at 4.1 commits per active day before the
  adoption and 20.1 after it, with 936 commits in August 2026
  ([case study](../evidence/cases/shio.md), section 7). Rules that answer incidents at that
  rate may matter less at a slower one.
- **Whether the rewrite or the limit held the roadmap.** The rewrite came two days before
  the limit ([F101](../evidence/findings/F101.md)).
- **What an unmarked legacy file costs.** Shio's root changelog is unmarked and no harm
  from it is recorded.
- **How a second copy of the tooling behaves.** Shio's two descriptions of how its engine
  arrives disagree at the pin ([F403](../evidence/findings/F403.md)), which says a
  declaration alone does not settle which copy answers.
- **Teams, other harnesses and other platforms.** The evidence is one person, one harness,
  one model family, and Windows ([../evidence/validity.md](../evidence/validity.md)).
