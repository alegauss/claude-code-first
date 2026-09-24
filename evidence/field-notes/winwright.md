# winwright: field notes (preliminary, unverified)

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
