# Case study: polyweave

## 1. Context

polyweave is a Claude Code plugin, written in Python, for making 3D assets on Blender,
Godot and a generative mesh service ([corpus.md](../corpus.md)). It is greenfield. The
pin is `6d1c136` (`6d1c1363270a0fe40c5a08e009ee9b5bac5c68e9`), dated 2026-09-24 17:47
-03:00 [polyweave@6d1c136]. The first commit is also the adoption commit, 2026-09-22
10:29 [polyweave@26bd699]. `git rev-list --count 6d1c136` returns 132, and
`git log 6d1c136 --format=%ad --date=short | sort | uniq -c` returns 59 commits on
2026-09-22, 54 on 2026-09-23 and 19 on 2026-09-24. The whole history is three days long.

The project started governed. The root commit adds `roadkeep.toml`, `docs/ROADMAP.md`,
`docs/CHANGELOG.md`, `docs/IMPROVEMENTS.md`, `CLAUDE.md`, the vendored roadkeep skill and
two specs, and no code [polyweave@26bd699]. At that commit the roadmap already names 36
tasks: `git show 26bd699:docs/ROADMAP.md | grep -o -E 'PW[0-9]+' | sort -u | wc -l`
returns 36 (PW1 to PW36). The first code arrives with PW1, 79 minutes after the root
commit [polyweave@8d1c9ab]; `git ls-tree -r --name-only c45f7b3` lists no file under
`src/` or `tests/`. The audit skill describes the same order: "polyweave started as a roadmap and a set of drafted specs, and the code arrives block by block" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L10-L11].

## 2. Agent surface

`CLAUDE.md` is 63 lines [polyweave@6d1c136:CLAUDE.md]. It names the gates, "and the gates are" [polyweave@6d1c136:CLAUDE.md#L7-L9]
`python -m pytest` and `python -m ruff check .`; requires a site rebuild after each ship,
with "the regenerated module goes in the same commit" [polyweave@6d1c136:CLAUDE.md#L11-L14];
and states its central design rule: "The caller is an agent in a terminal, not a person at a screen." [polyweave@6d1c136:CLAUDE.md#L18]
It sends the reader to Cottony for evidence [polyweave@6d1c136:CLAUDE.md#L25-L37], to
`docs/specs/` for formats [polyweave@6d1c136:CLAUDE.md#L39-L48], and to the CLI for the
governed docs: "A hand edit is refused" [polyweave@6d1c136:CLAUDE.md#L52-L53].

`.claude/settings.json` allows every Bash command, "Bash(*)" [polyweave@6d1c136:.claude/settings.json#L5],
enables the roadkeep MCP server [polyweave@6d1c136:.claude/settings.json#L11] and the
plugin "roadkeep@alegauss" [polyweave@6d1c136:.claude/settings.json#L59], and registers
four hooks [polyweave@6d1c136:.claude/settings.json#L13-L52]. Three run the roadkeep
guard through a committed launcher, which exists because "Claude Code on the web has no" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L9]
plugin command. The fourth, `no-clobber.py`, refuses a `Write` over an existing non-empty
file [polyweave@6d1c136:.claude/hooks/no-clobber.py#L1-L12]. Its rationale is an incident
in another repository, "where this hook was written" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L4],
in which `Write` "destroyed roughly 700 lines across four occasions" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L5].
It also states that "A hook that denies on its own bug is worse than no hook" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L17-L18].

Two agents and an audit skill were added together, 38 minutes after the root commit
[polyweave@c45f7b3]. The scanner has only Read, Grep and Glob and runs on sonnet
[polyweave@6d1c136:.claude/agents/scanner.md#L4-L6]; it holds that "An invented finding costs more than a missed one" [polyweave@6d1c136:.claude/agents/scanner.md#L10-L11]
and emits one fixed line per finding [polyweave@6d1c136:.claude/agents/scanner.md#L14-L18].
The verifier adds Bash and runs on opus [polyweave@6d1c136:.claude/agents/verifier.md#L4-L6].
It classifies findings as CONFIRMED, FALSE POSITIVE or UNVERIFIABLE and open tasks as
"STILL VALID, ALREADY DONE, OUTDATED or NEEDS REWORDING" [polyweave@6d1c136:.claude/agents/verifier.md#L3].
It may run gates but "Modify no file." [polyweave@6d1c136:.claude/agents/verifier.md#L14],
and "And never a call that spends." [polyweave@6d1c136:.claude/agents/verifier.md#L25]
That the cheaper model scans and the stronger one verifies is the author's reading of the
two `model` fields; no file states it as a principle.

The audit skill's product is "a reconciled backlog, not a patch" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L7-L8].
It runs the gates as a baseline, one scanner per roadmap block in parallel plus a specs row
and a wiring row, a deduplication, one verifier in each mode, and then "Reconcile, through roadkeep only" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L113].
Each verdict maps to one verb: ALREADY DONE to `ship`, OUTDATED to `retire`, NEEDS
REWORDING to `restate` or `amend` [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L120-L125];
a confirmed finding is filed with `add` after a duplicate check with `delivered`
[polyweave@6d1c136:.claude/skills/audit/SKILL.md#L133-L148]. "FALSE POSITIVE and UNVERIFIABLE findings are not filed." [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L155]
The audit does not commit: "Do not commit. An audit is not a task" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L159].

The skill had drifted from the project by the pin. Its block table lists A to H
[polyweave@6d1c136:.claude/skills/audit/SKILL.md#L54-L63], while the roadmap has Blocks I
and J [polyweave@6d1c136:docs/ROADMAP.md#L31-L33]. It says "This project declares no decisions file" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L127]
and counts three governed files, while `roadkeep.toml` also declares a deferred store
[polyweave@6d1c136:roadkeep.toml#L10-L14]. No commit title or body at the pin records an
audit run: `git log 6d1c136 -i --grep=reconcil` returns nothing. The agent surface was
last changed on the first day: `git log -1 --format=%h 6d1c136 -- .claude .mcp.json CLAUDE.md`
returns `3771c41` [polyweave@3771c41], and `git rev-list --count 3771c41..6d1c136` returns 100.

## 3. Planning governance

roadkeep governs the backlog under the prefix PW, with four files: roadmap, changelog,
improvements and deferred [polyweave@6d1c136:roadkeep.toml#L1-L14]. A shipped task
leaves the roadmap, gains a ✅ line in the ledger and loses its rationale section, as the
diffs of [polyweave@f203b0a] and [polyweave@7024e7e] show for `docs/IMPROVEMENTS.md`. At
the pin the 26 rationale sections (`git grep -c '^### §PW' 6d1c136 -- docs/IMPROVEMENTS.md`
returns 26) are exactly the 18 open roadmap lines and the 8 deferred lines, by id.

**The deferred store.** It was not declared at the start. It was added when PW36 could not
be finished: "That needed a deferred store, which this project had never declared." [polyweave@e26bd7c]
The reasons given there are a repository the project does not own and a rule that "a baseline recorded once the answer is known is a justification" [polyweave@e26bd7c].
At the pin `docs/DEFERRED.md` holds 8 ⏸ lines; seven read "set aside (a person's judgement)" [polyweave@6d1c136:docs/DEFERRED.md#L20-L26]
and PW36 reads "set aside (Nobody has recorded that baseline yet.)" [polyweave@6d1c136:docs/DEFERRED.md#L19].
The history also shows the store used for absent hardware and then emptied of it: PW56 was
set aside because "Godot is not installed on this machine" [polyweave@5a3a26c] and brought
back 143 minutes later, "now that there is a Godot" [polyweave@0a82ee0]. PW76 was set
aside because the result was "a call for somebody looking at" [polyweave@113f220] a
comparison image, and shipped the next day once "a person looked at the rig's 0.3977 beside the shipped sprite at display size and accepted it, so the bar moved to 0.41" [polyweave@d2ae97c].
That episode produced a new block, "Block J, a new block" [polyweave@f07740e], titled
"A bar a person sets once" [polyweave@6d1c136:docs/ROADMAP.md#L33]; its first line records
that "The dim star's 0.37 was a margin nobody asked for and it blocked a port for a day" [polyweave@6d1c136:docs/ROADMAP.md#L35].

**Specs and rationale.** `docs/specs/` holds 13 files that are not governed: "Nothing governs them" [polyweave@6d1c136:docs/specs/README.md#L8].
The split is by length and purpose: a rationale section "is capped at 250 words and says" [polyweave@6d1c136:CLAUDE.md#L43-L45]
why, and the spec says what. The index maps each spec to the task ids it binds
[polyweave@6d1c136:docs/specs/README.md#L20-L33] and treats a disagreement as information:
"the first implementation that disagrees with one is evidence about the spec, not only about the code" [polyweave@6d1c136:docs/specs/README.md#L16-L17].
Ledger lines name the spec that records the design [polyweave@6d1c136:docs/CHANGELOG.md#L5],
and a ship can edit a spec in the same commit: "docs/specs/adoption.md gains the rule" [polyweave@f203b0a].

## 4. Gates

Locally, the gates are pytest and ruff [polyweave@6d1c136:CLAUDE.md#L7-L9], plus the
site's `npm run build && npm test` after a ship [polyweave@6d1c136:CLAUDE.md#L11-L14] and
`roadkeep lint` [polyweave@6d1c136:CLAUDE.md#L54-L55]. `git grep -h -E 'def test_' 6d1c136 -- tests | wc -l`
returns 1266. As hooks, the roadkeep guard refuses hand edits to the governed files and
`no-clobber.py` refuses overwrites (section 2).

In CI there are two workflows. One runs `roadkeep lint`, whose "exit code is the whole contract" [polyweave@6d1c136:.github/workflows/roadkeep.yml#L4];
it was added on the first day [polyweave@3771c41]. The other builds and tests the site
[polyweave@6d1c136:.github/workflows/site.yml#L40-L71] and opens with a comment written
before the plugin had code, "so this is the whole CI" [polyweave@6d1c136:.github/workflows/site.yml#L1].
`git grep -n -e pytest -e ruff 6d1c136 -- .github` returns no match: the Python suite and
the linter run only on the author's machine. The record that they ran is the commit body.
`git log 6d1c136 --grep=Gates: --format=%h | wc -l` returns 18, for example "Gates: ruff clean, 1161 tests (6 new), site 30/30." [polyweave@fae7981].
These trailers are self-reported, and 18 of 132 commits carry one.

Real artefacts entered the suite on the first evening. Binary routing through LFS landed
before the files it was for [polyweave@a7b72ba]; then three copies from Cottony were added
because a real mesh and its drawing agree at a "silhouette IoU of 0.4343" [polyweave@0cacaad],
while "The synthetic tests clear 0.8" [polyweave@0cacaad].

## 5. Commit practice

The rule is one local commit per task, "staged by path, never pushed" [polyweave@6d1c136:CLAUDE.md#L62-L63],
through `run-commit.cmd`, which the repository names [polyweave@6d1c136:CLAUDE.md#L63]
but does not contain. Every title opens with a conventional type; 108 carry a scope
(`git log 6d1c136 --format=%s | grep -c -E '^[a-z]+\([^)]+\)'`) and 125 name a PW id
(`git log 6d1c136 --format=%s | grep -c -E 'PW[0-9]+'`). Tasks found during work are
named in the title: 23 titles contain `, with PW`, as in "(PW1), with PW37 filed" [polyweave@8d1c9ab];
13 mark a partial ship, as in "(PW56 part)" [polyweave@5eb1a8e]. The six deferrals are
committed as `docs:`, for example "docs: set the port aside until somebody records what it replaces (PW36)" [polyweave@e26bd7c].
`git log 6d1c136 --format=%an` gives one author for all 132 commits, and
`git log 6d1c136 -i --grep=co-authored-by` returns nothing. The four commits before PW1
have generic bullet bodies [polyweave@26bd699] [polyweave@c45f7b3]; from PW1 the bodies
are narrative prose with measurements, with three later exceptions [polyweave@8d762a2]
[polyweave@3771c41] [polyweave@91937d4].

## 6. Timeline

- **2026-09-22, governed from the first commit.** Roadmap, ledger, rationale, config and
  36 tasks precede any code [polyweave@26bd699].
- **2026-09-22, audit pair and hooks.** Scanner, verifier, audit skill, `no-clobber.py`
  and the launcher arrive in one commit, imported rather than grown here
  [polyweave@c45f7b3].
- **2026-09-22, a design confirmed by measurement.** PW45 measured parallel sampling
  against serial and found the cheap rungs lose and the final rung gains "3.7x" [polyweave@871a15b];
  the commit states "Which is what the design predicted" [polyweave@871a15b]. This
  confirmed the design; it did not falsify it.
- **2026-09-22, inherited folklore.** A solver claim carried over from Cottony: "That does not reproduce on Blender 5.2.1" [polyweave@963b652].
- **2026-09-22, the deferred store.** PW36 cannot proceed without a person-made baseline;
  the store is declared [polyweave@e26bd7c].
- **2026-09-22, real fixtures.** A threshold picked from synthetic inputs would have
  failed a correct real match [polyweave@0cacaad].
- **2026-09-23, work that needs a person.** PW53 "cannot be finished without a person, three times over" [polyweave@ab4835e].
- **2026-09-23, absent hardware.** PW56 deferred [polyweave@5a3a26c] and resumed once
  Godot was installed [polyweave@0a82ee0].
- **2026-09-23, a design falsified during implementation.** PW63's design proposed a
  declared range for rig parameters: "The design proposed a declared range, and measuring it is what settled the line the other way." [polyweave@7024e7e]
  Because the rig is legitimately driven with lights at zero, "A range would have refused real work or caught nothing." [polyweave@7024e7e]
  The shipped mechanism is a unit on each value, and the commit is explicit about its
  limit: "This does not refuse the mistake and does not claim to." [polyweave@7024e7e]
- **2026-09-23, a false first diagnosis.** PW71 shipped at 12:41 [polyweave@898d788]. At
  13:08 PW73 reported that "The first reading was that cp1252 cannot hold an em dash" [polyweave@f203b0a]
  and that it was wrong: "What reads the pipe decodes UTF-8" [polyweave@f203b0a]. The lint
  rule the design had leant towards "would have enforced the wrong thing" [polyweave@f203b0a],
  and "The ASCII semicolon PW71 put in that sentence an hour ago is reverted" [polyweave@f203b0a].
  The roadmap line kept its symptom because "the premise was false, not the observation" [polyweave@f203b0a].
- **2026-09-23 to 2026-09-24, a person's bar.** PW76 deferred for a look
  [polyweave@113f220], shipped after a person accepted it [polyweave@d2ae97c], and the
  experience filed as Block J [polyweave@f07740e].

## 7. Metrics

From [corpus.md](../corpus.md): 132 commits over 3 active days, first commit and adoption
both `26bd699` on 2026-09-22.

Throughput is measured here from the ledger's history rather than estimated.
`git log 6d1c136 --format=%ad --date=short -G'✅' -- docs/CHANGELOG.md | sort | uniq -c`
returns 51 commits on 2026-09-22, 42 on 2026-09-23 and 17 on 2026-09-24: 110 of 132
commits change a ✅ line. Counting added ✅ lines per commit in
`git log 6d1c136 --format='C %h' -p -- docs/CHANGELOG.md` gives exactly one for each of
those 110 commits, so each ship commit adds one ledger line. Seven of the 110 lines were
partial ships later replaced (`grep -c '^-- ✅'` over the same log returns 7), which leaves
103: `git grep -c ✅ 6d1c136 -- docs/CHANGELOG.md` returns 103. The median gap between
consecutive ship commits, from `git log 6d1c136 --reverse --format=%at -G'✅' -- docs/CHANGELOG.md`,
is 7.2 minutes over 109 gaps (minimum 1.2, maximum 1,133, the overnight gap). These are
commit timestamps, not effort: a ship's work may begin before the previous commit.

The backlog grew while it was drained. The highest id at the pin is PW122
(`git grep -h -o -E 'PW[0-9]+' 6d1c136 -- docs`), against 36 at the root commit. At the
pin 18 lines are open (`git show 6d1c136:docs/ROADMAP.md | grep -c -E '^- (📋|💭|⏳)'`) and
8 are deferred. The agent surface under `.claude/` totals 2,248 lines in eight files, for
example the 590-line launcher [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L590].
The project records one measurement of its own purpose: each constant of Cottony's render
rig was "found by hand at two minutes a sample" [polyweave@6d1c136:CLAUDE.md#L29-L30].

## 8. What is particular to this case

- **Governed from the first minute, with a pre-written backlog.** Thirty-six tasks, their
  rationale and two specs existed before any code (section 1). The throughput in section 7
  is therefore the throughput of draining and extending a designed backlog, not of
  discovering one.
- **An imported agent surface.** The hooks, agents and audit skill arrived complete within
  38 minutes of the root commit and were not changed after the first day (section 2).
  `no-clobber.py` cites an incident in another repository, and the launcher carries
  roadkeep's task ids, for example "(RK1189)" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L55].
  Rules here were not learned from this project's failures.
- **An external evidence source.** Cottony is the consumer where "Nearly every symptom in the backlog was measured in" [polyweave@6d1c136:CLAUDE.md#L25],
  and a non-goal holds that "Cottony is the first consumer and not the specification" [polyweave@6d1c136:docs/ROADMAP.md#L117-L118].
  Porting work edits a repository polyweave does not own: "It edits D:/Git/viglet/cottony, which this repository does not own." [polyweave@e26bd7c]
  The project itself filed the limit: "every symptom in the backlog was measured on one game" [polyweave@6d1c136:docs/ROADMAP.md#L28].
- **A domain with physical and aesthetic dependencies.** Renderers, an engine, a paid
  service and a person's eye are all inputs, which is why a deferred store was needed, and
  why "nothing here spends money on an agent's own judgement" [polyweave@6d1c136:CLAUDE.md#L57-L58].
- **Local-only code gates.** CI checks the backlog and the site, not the Python code
  (section 4).
- **Short and single-author.** Three days, one author, one machine.

## 9. Open questions

- Whether the audit skill was ever run. No commit at the pin records a reconciliation, and
  its drift (section 2) is consistent with it not having been run since the first day,
  which is an inference.
- Whether the local gates were run on the 114 commits without a `Gates:` trailer. The pin
  holds no record either way.
- How much of the measured throughput comes from the pre-written backlog rather than from
  the agent surface. There is no ungoverned comparison inside this project.
- Whether the design rules hold for a second adopter. PW117 names this as open
  [polyweave@6d1c136:docs/ROADMAP.md#L28].
- What the working tree held at extraction. Uncommitted work for PW106, PW135 and PW141 is
  outside the pin ([corpus.md](../corpus.md)).
