# Adopting Claude Code First on a new project

This guide starts a project governed from its first commit. It installs the pieces in an
order where each one protects the next: the guards exist before the first planning file,
the gates exist before the first feature, and the every-turn file carries a budget from
the moment it exists. Every step names the rules it satisfies and the level it reaches;
the rules themselves are in the [chapters](../spec/README.md), and the levels in
[conformance.md](../spec/conformance.md). The steps reach level 2. Level 3 and the
agent-facing profile are named under "What this does not cover".

The files come from the [templates](../templates/README.md), assembled by
`scripts/assemble_templates.py`, not written from scratch. roadkeep is the planning tool
the templates are written for; another tool that meets the same rules would do.

**The reference case.** polyweave was governed from its first commit: the root commit adds
`roadkeep.toml`, the governed roadmap, ledger and rationale, the instruction file and two
specs, and no code, with 36 tasks already on the roadmap
([case study](../evidence/cases/polyweave.md), section 1). At its pin it measures 132
commits over 3 active days, 44.0 commits per active day
([metrics.csv](../evidence/metrics/metrics.csv)). That figure says little about starting
from nothing. polyweave inherited a mature toolchain: roadkeep, the guard launcher, the
no-clobber hook and an audit pair arrived complete and were imported, not grown there
(case study, section 2). roadkeep, the project that built that toolchain, measures 43.2
commits per active day over 45 active days, winwright 30.8, freewilly 21.1 and Shio 6.7,
from the same file. Three active days against 45 or 515 is not a fair comparison, and a
commit is a ship event, not a measure of effort. What polyweave shows is the order, not
the speed.

## Before the first commit

Six choices are the person's, and the steps below record each where the agent reads it.
None of them is a default the agent can take for itself.

| Decision | What is chosen | Where it lands | Rule or divergence |
|---|---|---|---|
| Level | 1, 2 or 3; this guide reaches 2 | `ccf.toml` | [conformance.md](../spec/conformance.md) |
| Attribution | whether commits carry a trailer naming the agent | the commit skill | [CD-6](../spec/CD.md), D1 |
| Commit message | the agent writes the title, and either the body too or a tool generates it | the commit skill | [CD-4](../spec/CD.md), D5 |
| Permission posture | how broad the committed allow list is, and whether sessions run with a local bypass | `.claude/settings.json`, the commit skill | [PS-1](../spec/PS.md), [PS-2](../spec/PS.md), D3 |
| Every-turn file | whether the project has one; the templates assume it does | `agents.md`, `roadkeep.toml` | [IS-1](../spec/IS.md), [IS-2](../spec/IS.md), D2 |
| Language | the language of every artefact | the writing skill | [AW-3](../spec/AW.md) once declared |

The divergences are in [../evidence/divergences.md](../evidence/divergences.md). Four of
them leave the choice open on purpose:

- **Attribution (D1).** Either answer conforms. The rule asks only that the choice be
  stated where the agent reads its commit rules, because the corpus shows the trailer
  applied by habit, on a few percent of commits and unevenly.
- **Commit message (D5).** A generated body conforms. The title is the agent's, because a
  model that sees only the diff titled documentation commits as implementations.
- **Permission posture (D3).** The evidence cannot say how broad an allow list may safely
  be. What it fixes is that a project which removes prompts names, in committed files,
  the guard or gate standing in for them. The templates commit no allow rules and keep
  ask rules for `git push`, `git reset --hard` and `rm -rf`.
- **Every-turn file (D2).** Having none conforms. Where there is one, its budget is gated.

The language has no rule behind it: the specification records it as an open question
([AW.md](../spec/AW.md)). Declaring it in the writing skill makes it a house style rule,
which [AW-3](../spec/AW.md) asks to be checked by a gate at level 3.

## 1. Assemble the templates

In the new, empty repository, run from a checkout of this specification:

```sh
python <this-repository>/scripts/assemble_templates.py <new-repository>
```

It writes `agents.md`, `.claude/CLAUDE.md`, `.claude/settings.json`, the two example
skills, `.gitignore`, `.gitattributes`, `roadkeep.toml`, `.github/workflows/check.yml` and
`ccf.toml`, and refuses to overwrite a file that exists. The ignore rules are in place
before anything is written that could leak, and the line terminators are declared before
the first text file is committed.

| Rule | What this step gives it | Level |
|---|---|---|
| [PS-3](../spec/PS.md) | `.gitignore` keeps credentials, local settings, logs and caches out of the tree's commits | 1 |
| [EP-2](../spec/EP.md) | `.gitattributes` declares the terminators; the gate that holds them is step 7 | 2 |

## 2. Wire the guards

The assembled `.claude/settings.json` already wires the roadkeep guard on `SessionStart`,
`PreToolUse` and `Stop`, and the no-clobber hook on `Write`. Make the files they call
exist:

```sh
roadkeep install --committed
```

This writes `.claude/hooks/roadkeep-launch.py`, `.mcp.json` and the roadkeep skill, and
records in `roadkeep.toml` the engine version that wrote them. A committed launcher is
meant to reach a session that installs no plugin, such as one on the web; whether that is
still needed is an open question in [GH.md](../spec/GH.md). Then copy
`.claude/hooks/no-clobber.py` from this repository; it is vendored from polyweave with its
source commit in its header, and refuses a `Write` over an existing non-empty file.

From here, a hand edit of a governed file is refused. This is why the guard comes before
the planning files: there is no window in which they exist and are unguarded.

| Rule | What this step gives it | Level |
|---|---|---|
| [PG-1](../spec/PG.md) | a `PreToolUse` guard is wired for the files step 3 creates | 1 |
| [PS-1](../spec/PS.md) | the ask and deny rules are committed; any allow rule added now names these guards and the gates of step 7 as its stand-ins | 1 |
| [PS-2](../spec/PS.md) | push, hard reset and recursive delete are asked for, not only forbidden in prose | 2 |
| [GH-3](../spec/GH.md) | the guard's matcher includes `Bash`, not only the edit tools | 2 |

If the person chose a broader allow list, add it to `.claude/settings.json` now, and write
in the commit skill which guards and gates stand in for the prompts it removes.

## 3. Create the planning files under the guard

`roadkeep init` writes the governed files and a configuration, and refuses where a
configuration exists. Set the template's configuration aside, let `init` write the files,
then put the template's configuration back, since it carries the budgets and limits:

```sh
mv roadkeep.toml roadkeep.template.toml
roadkeep init --prefix <PREFIX> --block A
mv -f roadkeep.template.toml roadkeep.toml
roadkeep declare decisions
roadkeep declare deferred
roadkeep lint
```

Replace `EX` in `roadkeep.toml` with the same prefix. `declare deferred` adds
the store that `roadkeep defer` moves a waiting task to. polyweave did not declare one at
the start and needed it on its first day, when a task could not be finished from the
machine (case study, section 3). The template's `.gitattributes` already routes
`docs/DEFERRED.md` to the merge driver beside the other four.

| Rule | What this step gives it | Level |
|---|---|---|
| [PG-1](../spec/PG.md) | the roadmap, ledger, rationale and decisions are governed files | 1 |
| [AW-2](../spec/AW.md) | the limits in `roadkeep.toml` are refused at the write | 1 |
| [PG-6](../spec/PG.md) | work waiting on a person or on hardware has somewhere to wait, with its reason | 1 |
| [HR-1](../spec/HR.md) | such work can be set aside instead of shipped by the agent | 1 |
| [PG-5](../spec/PG.md) | the `[criteria]` table is declared; write each block's criteria with `roadkeep criterion` when the block is | 1 |

## 4. Write the every-turn file and set its budget

Replace `example` and the placeholder sentences in `agents.md` and `.claude/CLAUDE.md`.
Keep `agents.md` an index: what the project is, its laws, its layout, and where the rest
is. `.claude/CLAUDE.md` imports it and holds nothing else. Then lower the budgets in
`roadkeep.toml` to just above the size each file landed at, in lines and in bytes, and run
`roadkeep lint`. A budget with room to spare is room the next addition takes.

The budget arrived in step 1 with the file it governs, so there was never a version of the
every-turn file without one.

| Rule | What this step gives it | Level |
|---|---|---|
| [IS-1](../spec/IS.md) | each every-turn file, and each file it imports, has a budget `roadkeep lint` enforces | 1 |
| [IS-2](../spec/IS.md) | the file is an index that points to skills | 1 |

## 5. Write the commit rules and the writing rules

Rename the two skills from `example-dev` and `example-writing` to the project's name, in
the folder, the `name:` line and the pointers in `agents.md`. Then record the day-one
decisions in them:

- **The commit skill** states the attribution choice, that the agent writes the title with
  the task id, how the body is written, and which guards and gates stand in for any
  prompt removed. It keeps the template's rules on one task per commit, staging by path
  and filing only what is wrong or missing.
- **The writing skill** states the language and any house style, each with the check that
  holds it, or marked as advice where no check does.

| Rule | What this step gives it | Level |
|---|---|---|
| [CD-1](../spec/CD.md), [CD-2](../spec/CD.md) | one task per commit, a batch worked one task at a time | 1 |
| [CD-3](../spec/CD.md) | `git add --` with this task's paths, never everything | 1 |
| [CD-4](../spec/CD.md) | the agent writes the title (D5) | 1 |
| [CD-5](../spec/CD.md) | a filing names something wrong or missing | 1 |
| [CD-6](../spec/CD.md) | the attribution choice is written where the agent reads it (D1) | 1 |
| [PS-1](../spec/PS.md) | the stand-ins for removed prompts are named (D3) | 1 |
| [IS-3](../spec/IS.md) | each skill's description names the occasions it loads on | 1 |

## 6. Declare the level

Set `level` in `ccf.toml` to the level the person chose, and `profile = true` only if the
project ships tools, skills or a plugin for other agents. A departure taken on purpose
is recorded as a waiver with a reason, an owner, a date and an end
([deviations.md](../spec/deviations.md)); a departure with no waiver is drift.

This step satisfies no rule by itself. It fixes which rules the checker and the audit hold
the project to: those of the declared level and every level below it.

## 7. Put the gates in CI before the first feature

The `gates` job in `.github/workflows/check.yml` ends in a step that fails on purpose.
Replace it with the project's build and test commands, written without pipes. The
`roadkeep lint` job lives in the `roadkeep.yml` workflow that `roadkeep install` wrote in
step 2. The `conformance` job runs the checker on every push, reading the level from
`ccf.toml`.

Do this before the first feature, so that the first task that changes behaviour already
has a gate to pass. polyweave's CI ran its roadmap lint and its site build but never its
Python tests or linter, which ran only on the author's machine (case study, section 4).

| Rule | What this step gives it | Level |
|---|---|---|
| [VG-5](../spec/VG.md) | the gates run on every push | 2 |
| [VG-2](../spec/VG.md) | no gate is run through a pipe | 2 |
| [VG-1](../spec/VG.md), [VG-8](../spec/VG.md) | a gate exists for work to pass before it is called done or shipped | 2 |
| [GH-2](../spec/GH.md) | `roadkeep lint` in CI stands behind the guard of step 2 | 2 |

The templates stop short of three level 2 rules, which are the project's to add here: a
test that fails when an entry of `.claude/settings.json` is lost ([GH-5](../spec/GH.md)),
a gate that fails on a file whose line terminators depart from `.gitattributes`
([EP-2](../spec/EP.md)), and, where the project's own code reads another process's
output, a named encoding ([EP-3](../spec/EP.md)).

## 8. Check, then commit

Run the checker on the new repository:

```sh
python <this-repository>/scripts/check_conformance.py <new-repository>
```

It decides IS-1, PG-1, CD-1, VG-2, VG-5 and EP-2, and exits non-zero when one at or below
the claimed level fails. Fix what it reports. Then make the first commit, staged by path:
governance and no code, as polyweave's root commit was. From here each task is filed
with `roadkeep add`, picked with `roadkeep brief --claim` and closed with `roadkeep ship`,
one commit each.

| Rule | What this step gives it | Level |
|---|---|---|
| [IS-1](../spec/IS.md), [PG-1](../spec/PG.md), [CD-1](../spec/CD.md) | decided by the checker, and passed | 1 |
| [VG-2](../spec/VG.md), [VG-5](../spec/VG.md), [EP-2](../spec/EP.md) | decided by the checker, and passed (EP-2 in its declared half) | 2 |
| [CD-3](../spec/CD.md) | the first commit is staged by path | 1 |

A clean run reaches level 2 for the rules a script can decide. The rest of level 2 is
judged, which is what the first audit is for.

## The first audit

The checker decides six rules; the rest need judgement. Run the audit skill of this
specification's plugin once the first block has shipped, so that there are commits,
ledger entries and skills for the scanners to read. It runs the checker, one scanner per
chapter for the rules at or below the claimed level, and a verifier, and writes a report
in the form of [report.md](../spec/report.md). A claimed level holds only while such a
report, made against a stated commit, backs it ([conformance.md](../spec/conformance.md)).

Run it again when the agent surface changes, not only on a calendar. polyweave's own audit
skill had drifted from the roadmap by the pin, listing blocks A to H while the roadmap had
I and J, and no commit at the pin records it being run (case study, section 2).
An audit that is written once and never run reports nothing.

The audit reports and proposes. Filing what it finds into the backlog is a separate step
the person asks for.

## What this does not cover

- **Level 3.** Ceilings on every skill body and file read on demand
  ([IS-4](../spec/IS.md)), lists and figures generated or checked against their source
  ([IS-5](../spec/IS.md), [AW-1](../spec/AW.md)), a gate over the declared house style
  ([AW-3](../spec/AW.md)), a roll call of the tests ([VG-4](../spec/VG.md)), measurement
  before a change ([VG-9](../spec/VG.md)), a gate on stale copies
  ([GH-6](../spec/GH.md)) and measurements on a quiet tree ([CS-5](../spec/CS.md)). The
  templates do not provide these, and each needs a gate of the project's own.
- **The agent-facing profile.** A project that ships a surface to other agents adds the
  rules of [AP.md](../spec/AP.md).
- **Concurrent sessions.** The rules of [CS.md](../spec/CS.md) apply once several sessions
  share the checkout. roadkeep's claims (`roadkeep brief --claim`) are where they start.
- **An existing repository.** A project with history, or one that has drifted, starts from
  the brownfield or realignment guide in this folder instead.
- **Teams.** The evidence comes from one person, one harness and one model family
  ([../evidence/validity.md](../evidence/validity.md)).
- **Other platforms.** The environment rules rest on Windows observations
  ([EP.md](../spec/EP.md)).
