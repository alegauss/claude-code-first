# winwright: field notes (verified)

Extracted 2026-09-24; last commit `861b82e` (2026-09-21). .NET; drives Windows desktop UI
for agents; shipped as a Claude Code plugin with an MCP server.

## 1. Instruction surface

No CLAUDE.md or AGENTS.md. Reason stated in a test, `tests/Winwright.Tests/SkillTests.cs:10-14`
(WW69): "The whole content of an instruction file is loaded on every turn against a budget,
which is why the catalogue belongs in a skill and only the rules belong in the file the
harness reads." README "Adopting it in Claude Code" (L65-130): "committing that file wires
every clone. There is no per-machine install"; the MCP server means "the format arrives as
a schema rather than as prose somebody loaded and then typed a key out of"; "a hook that
denies what it did not understand is one that gets removed, after which nothing is guarded
at all". Shipped skill `skills/winwright/SKILL.md` (80 lines): "Do not write a harness";
"Do not type a field name from memory"; "A check that could not run is a third verdict and
never a pass". In-repo `roadmap-docs` skill: "⛔ One task, one commit (non-negotiable)";
"A multi-task request… is not permission to batch"; "A rule stated in two files is a rule
two files can disagree about, so nothing here repeats it".

## 2. Surfaces

Internal: `settings.json` (roadkeep MCP; guard on SessionStart, PreToolUse
`Edit|MultiEdit|NotebookEdit|Write|Bash`, Stop 30 s); `.mcp.json` roadkeep from a sibling
checkout; vendored roadkeep skill (72.6 KB); `roadmap-docs` (17.4 KB).
External: `.claude-plugin/marketplace.json` + `plugin.json` v1.0.0; `hooks/hooks.json`
PreToolUse `Write|Edit|MultiEdit` → .NET guard; `skills/winwright/SKILL.md`; 4 MCP tools
(`tools/Winwright.Mcp/Served.cs:62-96`). No slash commands by decision (`df203a9`, WW224).
Install: `claude plugin marketplace add … --scope project` + `claude plugin install …`.

## 3. Docs

prefix WW; ROADMAP 181 lines, CHANGELOG 146 KB (498 ✅ / 7 🗑), IMPROVEMENTS 75 lines.
Blocks by capability, reused: "A block empties; it does not close". Done-when criteria
exist because blocks closed on a zero count were "reopened six times"
(`roadmap-docs/SKILL.md:122-124`); `Criteria.cs` pairs each criterion with its
demonstrating case (WW176, `b26f7d7`). Retirements "Open with the decision… Give the
evidence… in numbers".

## 4. Gates

~2,190 tests. Split suite: desk-free half on host/CI; desk half in a VMware guest
(`run-tests-vm.cmd`, WW157: "for the two and a half minutes a full run lasts the machine
belongs to it"; guest gets the uncommitted tree: "testing a tree nobody has in front of
them is the failure this whole project is about"). `7a37e95` (WW474): "1130 of 1130 on the
host", "2194 of 2194 in the guest". Roll call of discovered vs executed tests (WW117/WW138:
a dying host "still prints a pass — measured here at 352 of 374"). `run-typing.cmd`
refuses to conclude below a minimum round count ("Nothing seen over n rounds rules out a
rate under about 3/n"). Docs regenerated from real runs (WW493); README tables tested
against parser and build (`5ad1e08`, `ae44ecc`, `d3520f5`). "Prove it by running": "A
capture task is not done without the picture; an act task is not done without the
read-back".

## 5. Commits

708 commits: feat 285, docs 204, fix 114, test 43, chore 30, refactor 24; id moved from
scope to suffix; ", with WWn filed". One task per commit via `run-commit.cmd -m`.
Commits state whether adopters are affected ("No adopter surface: …", `7a37e95`). Bodies
moved from generic bullets (August) to argued prose with measurements (September)
(inference). No Claude co-author trailer.

## 6. Learnings

1. Skill text is paid every turn → `SkillTests.cs:23-33` caps description ≤700 chars,
   body ≤6,000; description must name its trigger words (L45-54).
2. A skill naming a renamed type "sends an agent confidently at something that is not
   there" (`SkillTests.cs:16-18`) → backticked names checked against exported types.
3. Agents type schema keys from memory (WW66, `d678d09`) → MCP schema is the loader's;
   errors addressed to a field.
4. Agents write their own harness ("a 2,732-line one", README L119-124; WW67 `f197cb4`) →
   PreToolUse deny naming the tool; "being asked to write the other thing" beats "being
   asked to delete what you just wrote".
5. A guard failing on a fresh clone (WW221, `3bb1a26`) → shim names the missing build.
6. The agent read past `install.stale` all session (`a18dd8d`: "I read past it every
   time"; five refusal round-trips re-sending a paragraph; `ca680df`).
7. Ship-then-run left red tests for the next person, twice (WW438) → fixed order.
8. A permanently red CI badge is ignored: "Twenty-odd pushes each produced a red nobody
   could act on" (`7a37e95`) → CI runs only the host half; full suite in guest pre-commit.
9. A green can hide tests that never ran (WW117; WW6) → third verdict "hole", roll call.
10. Measure before building: revert `5012473` (WW249); retirements WW120, WW169, WW186.
11. A version spent by mistake (`8ea4829` → `89caa29` → `d698580`, WW467).
12. Blocks closed by count and reopened → Done-when criteria.
13. Rendered pages cost an agent three renders (WW495, `6962bce`) → Markdown twins,
    `llms.txt`.
14. Adoption proved by deletion: claude-tray's 3,004-line script (WW86 `2b452ec`);
    pportal's 285-line harness (WW88 `6917d3f`).

## 7. Metrics

708 commits, 2026-08-21 (`1602be7`) → 2026-09-21 (`861b82e`), 23 active days, peak 91.
2 in-repo skills, 1 shipped; 3 internal hooks + 1 shipped; 4 MCP tools; README 1,099
lines; v1.0.0 after 18 alphas; highest id WW507.

## Verification

Checked against `861b82e` on 2026-09-24. 93 claims: 77 verified, 14 corrected, 1 refuted, 0 outside the pin, 1 inference. Error rate 16.3%.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | Header | The last commit is `861b82e`, dated 2026-09-21 | verified | `git log -1 --format=%cs 861b82e` = 2026-09-21 [winwright@861b82e] | |
| 2 | Header | A .NET project | verified | "net10.0-windows" [winwright@861b82e:hooks/winwright-guard.cmd#L19] | |
| 3 | Header | It drives Windows desktop UI for agents | corrected | "Driving a Windows desktop application from a test" [winwright@861b82e:README.md#L3] | It drives a Windows desktop application from a test; agents reach it through the plugin, whose "MCP server" answers the format as a schema [winwright@861b82e:README.md#L85] |
| 4 | Header | Shipped as a Claude Code plugin with an MCP server | verified | "The plugin wires an MCP server" [winwright@861b82e:README.md#L85]; [winwright@861b82e:.claude-plugin/plugin.json#L20] | |
| 5 | 1 | There is no CLAUDE.md or AGENTS.md | verified | `git ls-tree -r --name-only 861b82e` lists no file named CLAUDE.md or AGENTS.md at any depth [winwright@861b82e] | |
| 6 | 1 | `SkillTests.cs:10-14` (WW69) gives the reason, in the quoted sentence | verified | "The whole content of an instruction file is loaded on every turn against a budget, which is" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L10]; "why the catalogue belongs in a skill and only the rules belong in the file the harness reads." [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L11] (doc comment inside L10-L14) | |
| 7 | 1 | The README section "Adopting it in Claude Code" spans L65-130 | verified | "## Adopting it in Claude Code" [winwright@861b82e:README.md#L65]; the next heading is at L132 [winwright@861b82e:README.md#L132] | |
| 8 | 1 | README: committing that file wires every clone; there is no per-machine install | verified | "committing that file wires every" [winwright@861b82e:README.md#L74]; "There is no per-machine install" [winwright@861b82e:README.md#L75] (the source bolds the first phrase) | |
| 9 | 1 | README: the MCP server means the format arrives as a schema | verified | "the format arrives as a schema rather than as prose somebody loaded and then typed a key out of" [winwright@861b82e:README.md#L85-L86] | |
| 10 | 1 | README: a hook that denies what it did not understand gets removed | verified | "a hook that denies what it did not understand is one that gets removed, after which nothing is guarded at all" [winwright@861b82e:README.md#L129-L130] | |
| 11 | 1 | `skills/winwright/SKILL.md` is 80 lines | corrected | `git show 861b82e:skills/winwright/SKILL.md` = 79 lines, final line terminated [winwright@861b82e:skills/winwright/SKILL.md] | 79 lines [winwright@861b82e:skills/winwright/SKILL.md] |
| 12 | 1 | Shipped skill: Do not write a harness | verified | "Do not write a harness" [winwright@861b82e:skills/winwright/SKILL.md#L21] | |
| 13 | 1 | Shipped skill: Do not type a field name from memory | verified | "Do not type a field name from memory" [winwright@861b82e:skills/winwright/SKILL.md#L43] | |
| 14 | 1 | Shipped skill: a check that could not run is a third verdict | verified | "A check that could not run is a third verdict and never a pass" [winwright@861b82e:skills/winwright/SKILL.md#L71] | |
| 15 | 1 | `roadmap-docs`: one task, one commit, non-negotiable | verified | "One task, one commit (non-negotiable)" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L32] | |
| 16 | 1 | `roadmap-docs`: a multi-task request is not permission to batch | verified | "is not permission to batch" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L39-L40] | |
| 17 | 1 | `roadmap-docs`: a rule stated in two files, so nothing repeats it | verified | "A rule stated in two files is a rule two files can disagree about, so nothing here repeats it" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L15-L16] | |
| 18 | 2 | `.claude/settings.json` enables the roadkeep MCP server | verified | "enabledMcpjsonServers" [winwright@861b82e:.claude/settings.json#L2-L4] | |
| 19 | 2 | Guard on SessionStart, PreToolUse on Edit, MultiEdit, NotebookEdit, Write and Bash, and Stop with a 30 s timeout | verified | [winwright@861b82e:.claude/settings.json#L6-L38] (matcher at L19, Stop timeout 30 at L35) | |
| 20 | 2 | `.mcp.json` runs roadkeep from a sibling checkout | verified | "/../roadkeep/scripts/roadkeep.py" [winwright@861b82e:.mcp.json#L6] | |
| 21 | 2 | The vendored roadkeep skill is 72.6 KB | verified | `git ls-tree -r -l 861b82e -- .claude/skills/roadkeep` = 11,650 + 18,007 + 42,940 = 72,597 bytes [winwright@861b82e:.claude/skills/roadkeep/SKILL.md] | |
| 22 | 2 | `roadmap-docs` is 17.4 KB | corrected | `git ls-tree -l 861b82e -- .claude/skills/roadmap-docs/SKILL.md` = 17,193 bytes | 17,193 bytes, 17.2 KB [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md] |
| 23 | 2 | `.claude-plugin/marketplace.json` and `plugin.json` at v1.0.0 | verified | [winwright@861b82e:.claude-plugin/marketplace.json]; version 1.0.0 [winwright@861b82e:.claude-plugin/plugin.json#L4] | |
| 24 | 2 | `hooks/hooks.json` wires PreToolUse on Write, Edit and MultiEdit to a .NET guard | verified | [winwright@861b82e:hooks/hooks.json#L3-L9]; the launcher ends in "dotnet exec" [winwright@861b82e:hooks/winwright-guard.cmd#L32] | |
| 25 | 2 | The plugin ships `skills/winwright/SKILL.md` | verified | [winwright@861b82e:skills/winwright/SKILL.md] | |
| 26 | 2 | Four MCP tools, at `tools/Winwright.Mcp/Served.cs:62-96` | verified | winwright_format, winwright_vocabulary, winwright_check, winwright_run [winwright@861b82e:tools/Winwright.Mcp/Served.cs#L62-L96] | |
| 27 | 2 | No slash commands, by decision (`df203a9`, WW224) | verified | "why there are no slash commands" [winwright@df203a9] | |
| 28 | 2 | Install is `claude plugin marketplace add … --scope project` plus `claude plugin install …` | verified | "claude plugin marketplace add alegauss/winwright --scope project" [winwright@861b82e:README.md#L70-L71] | |
| 29 | 3 | Task ids use the prefix WW | verified | "WW507" [winwright@861b82e:docs/ROADMAP.md#L29] | |
| 30 | 3 | ROADMAP is 181 lines | corrected | `git show 861b82e:docs/ROADMAP.md` = 182 lines | 182 lines [winwright@861b82e:docs/ROADMAP.md] |
| 31 | 3 | CHANGELOG is 146 KB | verified | `git ls-tree -l 861b82e -- docs/CHANGELOG.md` = 146,398 bytes [winwright@861b82e:docs/CHANGELOG.md] | |
| 32 | 3 | CHANGELOG holds 498 ✅ entries | corrected | occurrences of ✅ in `git show 861b82e:docs/CHANGELOG.md` = 497 | 497 ✅ [winwright@861b82e:docs/CHANGELOG.md] |
| 33 | 3 | CHANGELOG holds 7 🗑 entries | verified | occurrences of 🗑 in `git show 861b82e:docs/CHANGELOG.md` = 7 [winwright@861b82e:docs/CHANGELOG.md] | |
| 34 | 3 | IMPROVEMENTS is 75 lines | corrected | `git show 861b82e:docs/IMPROVEMENTS.md` = 97 lines | 97 lines [winwright@861b82e:docs/IMPROVEMENTS.md] |
| 35 | 3 | Blocks are named by capability and reused | verified | "reused rather than opened" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L3]; named for the capability [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L97-L98] | |
| 36 | 3 | A block empties; it does not close | verified | "A block empties; it does not close" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L94] | |
| 37 | 3 | Done-when criteria exist because blocks closed on a zero count were reopened six times (`roadmap-docs/SKILL.md:122-124`) | verified | "reopened six times" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L122-L124] | |
| 38 | 3 | `Criteria.cs` pairs each criterion with its demonstrating case (WW176, `b26f7d7`) | verified | "pair every criterion with the case that demonstrates it" [winwright@b26f7d7]; [winwright@861b82e:tests/Winwright.Tests/Criteria.cs] | |
| 39 | 3 | Retirements open with the decision and give the evidence in numbers | verified | "Open with the decision, not with work." [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L194]; "in numbers where there are numbers" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L196] | |
| 40 | 4 | About 2,190 tests | corrected | "2194 of 2194 in the guest" [winwright@7a37e95] is from 2026-09-20; a later guest run records a higher total | The last guest total recorded before the pin is 2,222: "2222 of 2222 in the guest" [winwright@d81f637] (2026-09-21) |
| 41 | 4 | Split suite: desk-free half on host and CI, desk half in a VMware guest via `run-tests-vm.cmd` | verified | "VMware guest so the host stays usable" [winwright@861b82e:run-tests-vm.cmd#L6]; "The desk half is gated on the guest before any commit" [winwright@7a37e95] | |
| 42 | 4 | WW157: for the two and a half minutes a full run lasts the machine belongs to it | verified | "for the two and a half minutes a full run lasts the machine belongs to it" [winwright@861b82e:tools/run-tests-vm.ps1#L7-L8], the script `run-tests-vm.cmd` launches [winwright@861b82e:run-tests-vm.cmd#L25] | |
| 43 | 4 | The guest gets the uncommitted tree, with the quoted reason | verified | "testing a tree nobody has in front of them is the failure this whole project is about" [winwright@861b82e:tools/run-tests-vm.ps1#L41-L42] | |
| 44 | 4 | `7a37e95` (WW474) records 1130 of 1130 on the host and 2194 of 2194 in the guest | verified | "1130 of 1130 on the host" [winwright@7a37e95]; "2194 of 2194 in the guest" [winwright@7a37e95] | |
| 45 | 4 | Roll call of discovered against executed tests (WW117, WW138) | verified | "what discovery listed against what the results file recorded" [winwright@861b82e:docs/CHANGELOG.md#L14] | |
| 46 | 4 | A dying host still prints a pass, measured at 352 of 374 | verified | "still prints a pass — measured here at 352 of 374" [winwright@861b82e:.github/workflows/ci.yml#L42] | |
| 47 | 4 | `run-typing.cmd` refuses to conclude below a minimum round count, with the quoted rate bound | verified | "Nothing seen over n rounds rules out a rate under about 3/n" [winwright@861b82e:run-typing.cmd#L14]; "a short run's refusal names that number" [winwright@861b82e:run-typing.cmd#L16] | |
| 48 | 4 | Docs regenerated from real runs (WW493) | verified | "capture the build an adoption fails first, from a real run" [winwright@d44caee]; "run one adoption on a desk and capture what it answered" [winwright@01796dc] | |
| 49 | 4 | README tables tested against parser and build (`5ad1e08`, `ae44ecc`, `d3520f5`) | corrected | "hold the README's grammar table to the parser" [winwright@5ad1e08]; "hold the README's project example to every key the build reads" [winwright@ae44ecc]; "fail the build where the area links a README heading that is gone" [winwright@d3520f5] | Only `5ad1e08` tests a README table (the locator grammar, against the parser); `ae44ecc` tests the README's `winwright.json` example against the keys the build reads [winwright@ae44ecc]; `d3520f5` tests the site's links to README headings [winwright@d3520f5] |
| 50 | 4 | Prove it by running: capture and act tasks need the picture and the read-back | verified | "## Prove it by running" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L218]; "A capture task is not done without the picture; an act task is not done without the read-back" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L223-L224] | |
| 51 | 5 | 708 commits | verified | `git rev-list --count 861b82e` = 708 [winwright@861b82e] | |
| 52 | 5 | feat 285, docs 204, fix 114, test 43, chore 30, refactor 24 | verified | subject prefixes of `git log 861b82e --format=%s`: feat 285, docs 204, fix 114, test 43, chore 30, refactor 24 (plus build 3, revert or Revert 2, perf 1, ci 1, Merge 1) | |
| 53 | 5 | The id moved from the scope to a suffix | verified | subjects before 2026-09-15: 548 with the id as scope, 1 as suffix; from 2026-09-15: 80 as suffix, 6 as scope (`git log 861b82e --format=%s` with `--until`/`--since`); first suffix run at [winwright@4ba54dc] | |
| 54 | 5 | Subjects carry ", with WWn filed" | verified | 14 subjects in `git log 861b82e --format=%s` match `, with WW[0-9]+ filed`; ", with WW507 filed" [winwright@3f5009b] | |
| 55 | 5 | One task per commit via `run-commit.cmd -m` | verified | "One task → one" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L36]; `run-commit.cmd -m`, with `-m` always [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L47] | |
| 56 | 5 | Commits state whether adopters are affected (No adopter surface, `7a37e95`) | verified | "No adopter surface: this is how this repository runs its own tests." [winwright@7a37e95]; 23 messages in `git log 861b82e --format=%B` contain "No adopter" | |
| 57 | 5 | Bodies moved from generic bullets (August) to argued prose with measurements (September) | inference | Marked (inference) in the note; consistent with the bullet body of [winwright@b26f7d7] and the prose body of [winwright@7a37e95], not counted | |
| 58 | 5 | No Claude co-author trailer | refuted | 33 commits in `git log 861b82e -i --grep='Co-Authored-By: Claude'`, from 2026-08-21 to 2026-09-21; "Co-Authored-By: Claude Opus 5" [winwright@15dc5db] | 33 of 708 commits carry a Claude co-author trailer, e.g. [winwright@15dc5db] |
| 59 | 6 | Learning 1: skill text is paid every turn | corrected | "the description sits in context on every" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L12]; "turn whether or not the skill is ever used, and the body is paid once" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L13] | Only the description is paid every turn; the body is paid once, when a window is in play [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L12-L14] |
| 60 | 6 | `SkillTests.cs:23-33` caps the description at 700 characters and the body at 6,000 | verified | "private const int Description = 700;" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L27]; "private const int Body = 6000;" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L33] | |
| 61 | 6 | The description must name its trigger words (L45-54) | verified | "the description has to name the occasion" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L47-L48]; asserted at L51-L53 [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L45-L54] | |
| 62 | 6 | Learning 2: a renamed type sends an agent at something not there (`SkillTests.cs:16-18`) | verified | "sends an agent confidently at something that is not there" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L16-L18] | |
| 63 | 6 | Backticked names are checked against exported types | verified | "GetExportedTypes()" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L63]; "Backticked(body)" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L70] | |
| 64 | 6 | Learning 3: agents typed schema keys from memory (WW66, `d678d09`); the MCP schema is the loader's | verified | "the schema of a case arrives as flag names typed from memory" [winwright@861b82e:docs/CHANGELOG.md#L347]; "give the tools the loader's own schema" [winwright@d678d09] | |
| 65 | 6 | Errors are addressed to a field | verified | "the loader's own refusal, addressed as" [winwright@861b82e:README.md#L94] | |
| 66 | 6 | Learning 4: a 2,732-line harness (README L119-124) | verified | "a 2,732-line one" [winwright@861b82e:README.md#L119-L124] | |
| 67 | 6 | WW67 (`f197cb4`): PreToolUse deny naming what replaces the harness | verified | "deny a hand-written harness at the write, and name the case file that replaces it" [winwright@f197cb4]; "refusal names the case file and" [winwright@861b82e:README.md#L122] | |
| 68 | 6 | Asked to write the other thing beats asked to delete what you just wrote | verified | "being asked to write the other thing and being asked to delete what you just wrote" [winwright@861b82e:README.md#L123-L124] | |
| 69 | 6 | Learning 5: guard failing on a fresh clone (WW221, `3bb1a26`); the shim names the missing build | verified | "launch the plugin's surfaces through a shim that says when nothing is built" [winwright@3bb1a26]; "the guard is not built" [winwright@861b82e:hooks/winwright-guard.cmd#L27] | |
| 70 | 6 | Learning 6: the agent read past `install.stale` all session (`a18dd8d`) | verified | "I read past it every time" [winwright@a18dd8d]; "which were stale all session" [winwright@a18dd8d] | |
| 71 | 6 | Five refusal round-trips re-sending a paragraph | verified | "five refusal round-trips over the 250-word limit, each re-sending the whole paragraph" [winwright@a18dd8d] | |
| 72 | 6 | `ca680df` belongs to the same episode | corrected | "refresh the vendored roadkeep skill, which had drifted behind the engine answering here" [winwright@ca680df]; its message does not mention install.stale or round-trips | `ca680df` (2026-08-28) is an earlier, separate refresh of the drifted vendored skill; the episode is recorded in `a18dd8d` (2026-09-01) alone [winwright@a18dd8d] |
| 73 | 6 | Learning 7: ship-then-run left red tests for the next person, twice (WW438); fixed order | verified | "WW438: that happened twice in one session" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L157]; "say the order a ship imposes on the criteria catalogue" [winwright@a686d44] | |
| 74 | 6 | Learning 8: Twenty-odd pushes each produced a red nobody could act on (`7a37e95`) | verified | "Twenty-odd pushes each produced a red nobody could act on" [winwright@7a37e95] | |
| 75 | 6 | CI runs only the host half; the full suite runs in the guest before commit | verified | "So the Test step asks" [winwright@7a37e95] tools/host-gate.ps1 for the filter; "The desk half is gated on the guest before any commit" [winwright@7a37e95] | |
| 76 | 6 | Learning 9: a green can hide tests that never ran (WW117; WW6), answered by the third verdict hole and the roll call | corrected | WW117 is the roll call [winwright@861b82e:docs/CHANGELOG.md#L14]; WW6 makes the summary refuse the word every [winwright@861b82e:docs/CHANGELOG.md#L10] | The roll call answers WW117 and WW6 answers with a summary that refuses every while anything is unchecked; the third verdict and the hole come from WW1 and WW2 [winwright@861b82e:docs/CHANGELOG.md#L5-L6] |
| 77 | 6 | Learning 10: measure before building, revert `5012473` (WW249) | verified | "take the per-code-unit send back out, the rate did not move" [winwright@5012473] | |
| 78 | 6 | Retirements WW120 and WW169 were measured before building | verified | "Measured before deciding and the premise did not survive" [winwright@861b82e:docs/CHANGELOG.md#L358]; "Measured before building it, and the premise did not survive" [winwright@861b82e:docs/CHANGELOG.md#L485] | |
| 79 | 6 | Retirement WW186 was measured before building | corrected | "Filed without reading Block E's open lines" [winwright@861b82e:docs/CHANGELOG.md#L198] | WW186 was retired as a duplicate of WW40, filed without reading the open lines, not after a measurement [winwright@861b82e:docs/CHANGELOG.md#L198] |
| 80 | 6 | Learning 11: a version was spent by mistake (`8ea4829`, `89caa29`, `d698580`, WW467) | corrected | "would have spent the number after it" [winwright@d698580]; "the repair was reverting the bump" [winwright@d698580] | No version was spent: the alpha.11 bump (`8ea4829`) would have made the workflow publish alpha.12, and it was reverted (`89caa29`) before that; `d698580` fixed the workflow [winwright@d698580] |
| 81 | 6 | Learning 12: blocks closed by count and reopened led to Done-when criteria | verified | "reopened six times" [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md#L122-L124] | |
| 82 | 6 | Learning 13: rendered pages cost an agent three renders (WW495, `6962bce`); Markdown twins and `llms.txt` | verified | "an agent renders three pages to learn what the tool is" [winwright@861b82e:docs/CHANGELOG.md#L535]; "write a Markdown twin beside every page of the area" [winwright@6962bce] | |
| 83 | 6 | Learning 14: claude-tray's 3,004-line script deleted (WW86, `2b452ec`) | verified | "3,004-line interaction harness" [winwright@861b82e:docs/CHANGELOG.md#L449]; "ship claude-tray's harness deletion" [winwright@2b452ec] | |
| 84 | 6 | pportal's 285-line harness replaced (WW88, `6917d3f`) | verified | "285-line interaction harness is two cases" [winwright@861b82e:docs/CHANGELOG.md#L400]; "pportal's interaction harness is cases" [winwright@6917d3f] | |
| 85 | 7 | First commit 2026-08-21 (`1602be7`); last 2026-09-21 (`861b82e`) | verified | `git log 861b82e --max-parents=0 --format=%as` = 2026-08-21 [winwright@1602be7]; [winwright@861b82e] | |
| 86 | 7 | 23 active days | verified | distinct dates in `git log 861b82e --format=%as` = 23 | |
| 87 | 7 | Peak of 91 commits in a day | verified | 91 commits dated 2026-08-24 in `git log 861b82e --format=%as` | |
| 88 | 7 | Two in-repo skills, one shipped | verified | [winwright@861b82e:.claude/skills/roadkeep/SKILL.md]; [winwright@861b82e:.claude/skills/roadmap-docs/SKILL.md]; [winwright@861b82e:skills/winwright/SKILL.md] | |
| 89 | 7 | Three internal hooks plus one shipped | verified | SessionStart, PreToolUse, Stop [winwright@861b82e:.claude/settings.json#L6-L38]; PreToolUse [winwright@861b82e:hooks/hooks.json#L3-L14] | |
| 90 | 7 | Four MCP tools | verified | [winwright@861b82e:tools/Winwright.Mcp/Served.cs#L62-L96] | |
| 91 | 7 | README is 1,099 lines | verified | `git show 861b82e:README.md` = 1,099 lines [winwright@861b82e:README.md] | |
| 92 | 7 | v1.0.0 after 18 alphas | corrected | `git tag --merged 861b82e` lists v0.1.0-alpha.2 to alpha.18 and v1.0.0; alpha.1 is declared in [winwright@d17805a] and has no tag | v1.0.0 [winwright@7f64cf1] follows 17 tagged alphas (alpha.2 to alpha.18); alpha.1 was declared but never tagged [winwright@d17805a] |
| 93 | 7 | Highest id WW507 | verified | no WW number above 507 in `docs/` at the pin or in any message; "with WW507 filed" [winwright@3f5009b] | |
