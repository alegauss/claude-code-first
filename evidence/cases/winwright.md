# Case study: winwright

## 1. Context

winwright is a .NET library and Claude Code plugin for "Driving a Windows desktop application from a test" [winwright@861b82e:README.md#L3].
It targets "net10.0-windows" [winwright@861b82e:hooks/winwright-guard.cmd#L19]. It is a
greenfield case: the first commit, `1602be7`, is dated 2026-08-21 [winwright@1602be7], and
the adoption commit `fd4162f`, thirty minutes later on the same day, adopts roadkeep and
adds the shipping-discipline skill [winwright@fd4162f]. The pin is `861b82e`, dated
2026-09-21 [winwright@861b82e]. At the pin, `git rev-list --count 861b82e` gives 708
commits, `git log 861b82e --format=%cs | sort -u | wc -l` gives 23 active days, and
`git ls-tree -r --name-only 861b82e | wc -l` gives 638 tracked files.

`git log --format=%an 861b82e | sort | uniq -c` gives four author names: two spellings of
the owner's name (689 and 1 commits), github-actions[bot] (17) and dependabot[bot] (1).

## 2. Agent surface

**No every-turn instruction file.** `git ls-tree -r --name-only 861b82e | grep -ciE '(^|/)(CLAUDE|AGENTS)\.md$'`
gives 0, and `git log 861b82e -- CLAUDE.md AGENTS.md '*/CLAUDE.md'` lists no commit, so no
such file existed at any point in the pinned history. The design of this case study says
the absence is justified by a test, WW69. The source supports a narrower statement. The
test's doc comment argues about where content goes, not about having no file: "The whole content of an instruction file is loaded on every turn against a budget, which is" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L10]
"why the catalogue belongs in a skill and only the rules belong in the file the harness reads." [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L11]
That sentence presumes a file that holds the rules. WW69 itself concerns the shipped skill:
its ledger title is "the skill is loaded on every turn against a budget it does not need" [winwright@861b82e:docs/CHANGELOG.md#L349].
In this repository the working rules live in a skill instead, `roadmap-docs`, which states "One task, one commit (non-negotiable)" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L32].
No source at the pin states why the repository has no instruction file of its own.

**Skills.** Two skills serve work in the repository: a vendored roadkeep skill of 72,597
bytes across three files (`git ls-tree -r -l 861b82e -- .claude/skills/roadkeep`)
[winwright@861b82e:.claude/skills/roadkeep/SKILL.md] and `roadmap-docs`, 17,193 bytes
[winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md]. `roadmap-docs` defers the write
path to roadkeep on the ground that "A rule stated in two files is a rule two files can disagree about, so nothing here repeats it" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L15-L16].
A third skill ships to adopters, `skills/winwright/SKILL.md`, 79 lines
[winwright@861b82e:skills/winwright/SKILL.md], with the headed rule "Do not write a harness" [winwright@861b82e:skills/winwright/SKILL.md#L21].

**Skill budgets and name checks.** `SkillTests.cs` measures the shipped skill's two costs
separately, because "the description sits in context on every" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L12]
"turn whether or not the skill is ever used, and the body is paid once" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L13].
The caps are "private const int Description = 700;" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L27]
and "private const int Body = 6000;" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L33],
in characters as measured by `Length` [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L40-L41].
A second test holds that "the description has to name the occasion" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L47-L48]
and asserts six trigger words [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L51-L53].
A third reads every backticked name in the body against the engine assembly's exported
types [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L62-L70], because a stale
name "sends an agent confidently at something that is not there" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L16-L18].
It guards against its own vacuity: "A walk that matched nothing would pass this test while checking none of it." [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L103]

**Hooks.** `.claude/settings.json` enables the roadkeep MCP server and runs roadkeep's
guard on SessionStart, on PreToolUse for Edit, MultiEdit, NotebookEdit, Write and Bash,
and on Stop with a 30 s timeout [winwright@861b82e:.claude/settings.json#L1-L38]. The
plugin registers one PreToolUse hook on Write, Edit and MultiEdit
[winwright@861b82e:hooks/hooks.json#L3-L14]. WW67 introduced it, to "deny a hand-written harness at the write, and name the case file that replaces it" [winwright@f197cb4].
The guard denies content naming three engine namespaces
[winwright@861b82e:tools/Winwright.Guard/Guard.cs#L57-L62], and its rationale is timing: "So the refusal arrives before the work rather than after it" [winwright@861b82e:tools/Winwright.Guard/Guard.cs#L39].
The README states the limit that keeps it installed: "a hook that denies what it did not understand is one that gets removed, after which nothing is guarded at all" [winwright@861b82e:README.md#L129-L130].

**MCP server.** The plugin serves four tools, `winwright_format`, `winwright_vocabulary`,
`winwright_check` and `winwright_run` [winwright@861b82e:tools/Winwright.Mcp/Served.cs#L62-L96].
WW66 answered a problem it named as "the schema of a case arrives as flag names typed from memory" [winwright@861b82e:docs/CHANGELOG.md#L347]
and set out to "give the tools the loader's own schema" [winwright@d678d09]. At the pin
the check tool's input schema is built as "var schema = ScenarioSchema.AsJsonSchema();" [winwright@861b82e:tools/Winwright.Mcp/Served.cs#L171],
so, in the README's words, "a misspelled key is not a thing the caller can send" [winwright@861b82e:README.md#L93].
The shipped skill repeats the rule as "Do not type a field name from memory" [winwright@861b82e:skills/winwright/SKILL.md#L43].
There are no slash commands, by decision, which is "why there are no slash commands" [winwright@df203a9].

## 3. Planning governance

roadkeep writes `docs/ROADMAP.md`, `docs/CHANGELOG.md` and `docs/IMPROVEMENTS.md`, and a
hand-edit is denied by the hook [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L8-L12].
Task ids use the prefix WW, the highest being WW507 [winwright@3f5009b]. Work is grouped
in eleven lettered blocks named by capability, and "A block empties; it does not close" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L94].

**Done-when criteria.** `git show 861b82e:docs/ROADMAP.md | grep -c '^## Done when'` gives
11, one heading per block. The design says these criteria were born from six reopened
blocks. The source does not support that as a winwright incident. The skill attributes
the six reopenings to roadkeep: "They are the answer to a failure roadkeep measured" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L122],
where a block closed on a zero line count "was reopened six times" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L122-L124].
The same passage is already in the adoption commit, "closed that way was reopened six times" [winwright@fd4162f:.claude/skills/roadmap-docs/SKILL.md#L122],
which also declares 32 criteria [winwright@fd4162f:.claude/skills/roadmap-docs/SKILL.md#L119].
The criteria therefore arrived with adoption on the first day, carrying a reason measured
in another project; no winwright block is recorded as reopened. The rule for their use is
that a finished block "is that reading, never a line count reaching zero" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L147].
What winwright added is a test: WW176 set out to "pair every criterion with the case that demonstrates it" [winwright@b26f7d7],
filed as "file the criteria nothing demonstrates, which is how WW169 got written" [winwright@87be7cc].

**Retirement.** `git show 861b82e:docs/CHANGELOG.md | grep -o '🗑' | wc -l` gives 7 retired entries. WW186 was retired as a
duplicate of WW40, "Filed without reading Block E's open lines" [winwright@861b82e:docs/CHANGELOG.md#L198].

## 4. Gates

**The split suite.** The test suite drives real windows, so it runs in a "VMware guest so the host stays usable" [winwright@861b82e:run-tests-vm.cmd#L6],
because "for the two and a half minutes a full run lasts the machine belongs to it" [winwright@861b82e:tools/run-tests-vm.ps1#L7-L8].
The guest receives the working tree, uncommitted files included, because "testing a tree nobody has in front of them is the failure this whole project is about" [winwright@861b82e:tools/run-tests-vm.ps1#L41-L42].
WW417 split the suite, to "answer the desk-free half of the suite on the host before starting the VM" [winwright@fb7377d].
The last guest total recorded before the pin is "2222 of 2222 in the guest" [winwright@d81f637].

**CI.** The workflow runs on `windows-latest` [winwright@861b82e:.github/workflows/ci.yml#L22]
and, since `7a37e95`, runs only the host half, with a filter derived by
`tools/host-gate.ps1` [winwright@861b82e:.github/workflows/ci.yml#L66-L71]. The desk half
runs only in the guest, which CI does not check.

**The roll call and the third verdict.** Two separate mechanisms answer a green that hides
unrun work. For the engine's own verdict, WW1 made a run read as "one of three outcomes whose enum values are the exit codes themselves" [winwright@861b82e:docs/CHANGELOG.md#L5],
and WW2 defined the hole: "A hole is now constructed from an absent named precondition and from nothing else" [winwright@861b82e:docs/CHANGELOG.md#L6].
The shipped skill states it as "A check that could not run is a third verdict and never a pass" [winwright@861b82e:skills/winwright/SKILL.md#L71].
For the project's own test suite, WW117 added a roll call comparing "what discovery listed against what the results file recorded" [winwright@861b82e:docs/CHANGELOG.md#L14].
The CI comment records the measured failure it answers, a dying host "measured here at 352 of 374, a green covering twenty-two tests that" [winwright@861b82e:.github/workflows/ci.yml#L42]
never ran.

**What is not gated.** The criteria are checked for presence and pairing, not truth:
"Nothing goes red when a criterion is untrue" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L151-L152].

## 5. Commit practice

The unit is one task per commit, and "is not permission to batch" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L39-L40]
applies to multi-task requests. Commits go through `run-commit.cmd -m`
[winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L47]. By subject prefix
(`git log 861b82e --format=%s | grep -cE '^<type>(\(|:|!)'`) there are 285 feat, 204 docs,
114 fix, 43 test, 30 chore and 24 refactor commits. The task id first sat in the scope, as
in `feat(WW66)` [winwright@d678d09], and later moved to a suffix, as in `(WW474)`
[winwright@7a37e95]. 14 subjects end in a filing note
(`git log 861b82e --format=%s | grep -cE ', with WW[0-9]+ filed'`), such as ", with WW507 filed" [winwright@3f5009b].
23 messages state adopter impact (`git log 861b82e --format=%B | grep -c 'No adopter'`),
for instance "No adopter surface: this is how this repository runs its own tests." [winwright@7a37e95]

**Attribution.** `git log 861b82e -i --grep='Co-Authored-By: Claude' --format=%h | wc -l`
gives 33 of 708 commits with a Claude co-author trailer; adding `--format=%cs | sort | uniq -c`
shows 24 of them dated 2026-08-24. An example is
"Co-Authored-By: Claude Opus 5" [winwright@15dc5db].

## 6. Timeline

- **2026-08-21, adoption with imported criteria.** roadkeep and the discipline skill
  arrive together [winwright@fd4162f], carrying the six-reopenings rationale measured in
  roadkeep [winwright@fd4162f:.claude/skills/roadmap-docs/SKILL.md#L120-L122]. Mechanism:
  Done-when criteria from day one.
- **2026-08-21, the third verdict.** WW1 introduced three outcomes and exit codes
  [winwright@0fbd8f2], and WW2 the hole [winwright@d2df0e5].
- **2026-08-22, a dead test host printed a pass.** WW117 added the roll call
  [winwright@6351b80]; WW138 made a bare `dotnet test` take it [winwright@2eeb059].
- **2026-08-23, a run occupied the host.** The suite moved to a VMware guest [winwright@2acc0ee].
- **2026-08-24, criteria nothing demonstrated.** WW176 paired each criterion with a case
  [winwright@b26f7d7].
- **2026-08-26, the agent-facing surface.** WW66 gave the tools the loader's schema
  [winwright@d678d09]; WW67 added the harness guard [winwright@f197cb4]; WW69 moved the
  shipped skill to load on a window and measured both costs [winwright@7c456e0]; WW221 made
  the launcher report a missing build [winwright@3bb1a26].
- **2026-09-06, the name check went red for a true reason.** Control-type words in the
  skill failed the exported-types check, since "a skill saying them went red for a true and irrelevant" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L85]
  reason; WW414 checked them against the tree's vocabulary instead [winwright@5fe977c].
  The same day WW417 split the suite into host and guest halves [winwright@fb7377d].
- **2026-09-15, ship before run left reds for the next person.** "WW438: that happened twice in one session" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L157];
  `a686d44` wrote the order of ship, pairing and run where it is read [winwright@a686d44].
- **2026-09-20, CI red on the desk.** The commit records "Red since 2026-09-17 and never about the tree." [winwright@7a37e95]
  and "Twenty-odd pushes each produced a red nobody could act on" [winwright@7a37e95].
  CI moved to the host half; "The desk half is gated on the guest before any commit" [winwright@7a37e95].
  The same run reports "1130 of 1130 on the host." [winwright@7a37e95] and "2194 of 2194 in the guest" [winwright@7a37e95].
- **2026-09-21, adoption proved by deletion in claude-tray.** WW86 closed with claude-tray's
  harness removed [winwright@2b452ec]. Its ledger entry states "claude-tray still carries a 3,004-line interaction harness" [winwright@861b82e:docs/CHANGELOG.md#L449]
  and that the script "checked 31 in 46 s and crashed" [winwright@861b82e:docs/CHANGELOG.md#L449].
- **2026-09-21, adoption proved by deletion in pportal.** WW88's commit reports pportal's
  file "is deleted, 285 lines in which every case decided for itself how long to wait" [winwright@6917d3f],
  and a correction the same day admits "The cases were written on a desk with no controller, so the two that need one had never run." [winwright@d2a9081]
- **2026-09-21, release.** v1.0.0 [winwright@7f64cf1]; `git tag --merged 861b82e | wc -l`
  gives 18 tags, 17 alphas and v1.0.0. alpha.1 was declared and never tagged
  [winwright@d17805a].

## 7. Metrics

From [../corpus.md](../corpus.md): 708 commits, 23 active days, first commit and adoption
on 2026-08-21, greenfield. `git log 861b82e --format=%cs | sort | uniq -c | sort -rn | head -1`
gives a peak of 91 commits on 2026-08-24.

Figures the project recorded itself: the skill caps of 700 and 6,000 characters (section
2); a roll-call gap of 352 of 374 (section 4); host and guest totals of 1130 and 2194 on
2026-09-20 [winwright@7a37e95], and 2222 in the guest on 2026-09-21 [winwright@d81f637];
for claude-tray, "23 cases check 95 claims in 128-159 s" [winwright@861b82e:docs/CHANGELOG.md#L449].
Block J's criterion asks for exactly this kind of figure: "the number of lines removed is reported rather than described" [winwright@861b82e:docs/ROADMAP.md#L137].
`git rev-list --count --since=2026-09-17T00:00:00-03:00 7a37e95^` gives 25 commits between
the start of the red and the CI change (a date with no time of day makes `--since` depend
on when the command runs, which is how a first draft of this count read 22). Git records commits, not pushes, so the count is consistent
with "twenty-odd" but does not measure it.

## 8. What is particular to this case

- The product is itself a Claude Code plugin. The skill budgets, the loader schema and the
  harness guard govern what adopters' agents see, not only this repository's agent.
- Its test suite needs an interactive Windows desk, which is why it is split and why CI
  runs only half of it. That constraint is specific to a UI-automation tool.
- Its proof of adoption lies in other repositories. The deletions in claude-tray and pportal
  are cited here only through winwright's own ledger and messages; pportal commit
  `cca77634` is named in [winwright@6917d3f] but is outside this corpus.
- roadkeep is wired from a sibling checkout rather than the plugin
  [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L18-L21], so the governance
  rules arrived from roadkeep already formed, criteria included.
- It has no every-turn instruction file at all.

## 9. Open questions

- Why the repository has no instruction file of its own. WW69 argues for a skill over an
  instruction file for the catalogue, but no source at the pin addresses this repository.
- How long CI was red. The commit says since 2026-09-17 [winwright@7a37e95], while the
  workflow comment says "it answered wrongly for three weeks" [winwright@861b82e:.github/workflows/ci.yml#L49];
  the pin's history cannot settle the discrepancy, nor the push count.
- The size of claude-tray's harness. The ledger says 3,004 lines
  [winwright@861b82e:docs/CHANGELOG.md#L449], while an engine comment says "claude-tray's harness is 2,732 lines for" [winwright@861b82e:src/Winwright/Scenarios/StepDeclaration.cs#L71]
  eight cases. The two may describe different dates; the pin does not say.
- Whether the harness guard ever fired on a real write. The pin records its tests and
  rationale, not a denial observed in use.
- Why 24 of the 33 co-author trailers fall on one day, 2026-08-24.
