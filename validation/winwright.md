# Conformance audit: winwright

- Commit: `861b82e2cb7d0864cf2dc41799f04f4de3ec0e6e`, audited 2026-09-25
- Specification version: 0.1.0
- Claimed level: 3; achieved level: 0; agent-facing profile audited
- Checker: 0.1.0; audit skill: 0.1.0

## Summary by chapter

| Chapter | pass | fail | waived | not applicable | could not run |
|---|---|---|---|---|---|
| AP | 1 | 3 | 0 | 0 | 0 |
| AW | 1 | 2 | 0 | 0 | 0 |
| CD | 2 | 4 | 0 | 0 | 0 |
| CS | 3 | 0 | 0 | 0 | 2 |
| EP | 4 | 2 | 0 | 0 | 0 |
| GH | 2 | 4 | 0 | 0 | 0 |
| HR | 1 | 1 | 0 | 0 | 0 |
| IS | 4 | 2 | 0 | 0 | 0 |
| PG | 5 | 1 | 0 | 0 | 0 |
| PS | 2 | 1 | 0 | 0 | 0 |
| VG | 8 | 1 | 0 | 0 | 0 |

## Rules

| Rule | Level | Verdict | By | Locus | Evidence |
|---|---|---|---|---|---|
| AP-1 | profile | fail | verifier | tests/Winwright.Tests/McpTests.cs:82-93 | The tools/list test checks shape only, and no test caps the serialized schemas or tool responses; only the shipped skill is capped. |
| AP-2 | profile | fail | verifier | site/public/llms.txt:133-136 | llms.txt names the four MCP tools, and nothing checks it against Served.Tools. |
| AP-3 | profile | fail | verifier | tests/Winwright.Tests/PluginTests.cs:42-43 | Plugin surfaces are read from the checkout, and no CI step installs or loads the plugin as a consumer does. |
| AP-4 | profile | pass | verifier | docs/CHANGELOG.md:400,401,449 | Each adoption entry gives a counted deletion in a named consumer. |
| AW-1 | 3 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md:148 | The skill says 33 criteria while the roadmap holds 32, and the criteria test does not match the wording. |
| AW-2 | 1 | pass | verifier | roadkeep.toml:15-24 | Limits declared and refused at the write. |
| AW-3 | 3 | fail | verifier | commit 5493b65 | Titles carry an em dash against the declared ASCII-title rule, and nothing checks titles. |
| CD-1 | 1 | fail | checker |  | 20 commit(s) add several ledger entries, e.g. 0ebd67e, eaeb4cc, 3cc3d29 |
| CD-2 | 1 | pass | verifier | git log since 2026-09-17 | Recent commits ship one task each. |
| CD-3 | 1 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md:47-48 | The only commit route stages everything, while another session writes in the same checkout. |
| CD-4 | 1 | fail | verifier | commit d44d623 | A commit opening Block L has a generic generated title with no task id. |
| CD-5 | 1 | pass | verifier | docs/ROADMAP.md:27-29 | Open lines each name a defect. |
| CD-6 | 1 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md:32-54 | The commit rules never say whether commits credit the agent. |
| CS-1 | 2 | could not run | verifier |  | Claims are uncommitted state; the clone holds no trace of them. |
| CS-2 | 2 | pass | verifier | commit d44caee | The commit staged only its task's files and the shared governed files, a case the CS chapter leaves open. |
| CS-3 | 2 | pass | verifier | repository-wide | No commit-time hook. |
| CS-4 | 2 | pass | verifier | tools/host-gate.ps1:137-160 | A run that did not happen is reported apart from a pass, and no disturbed run is recorded. |
| CS-5 | 3 | could not run | verifier |  | Cannot be read from committed files. |
| EP-1 | 2 | fail | verifier | .claude/skills/roadkeep/SKILL.md:10 | Two skills contradict each other on which roadkeep copy answers, CI uses @main, and no version is declared. |
| EP-2 | 2 | pass | checker |  | line terminators declared in .gitattributes |
| EP-3 | 2 | fail | verifier | tests/Winwright.Tests/Fixture.cs:99-103 | UTF-8 child output and MCP stdin are decoded with the default code page. |
| EP-4 | 2 | pass | verifier | tools/run-tests-vm.ps1:882-892 | A leading BOM is stripped or refused. |
| EP-5 | 2 | pass | verifier | docs/CHANGELOG.md | Encoding entries describe byte-level checks. |
| EP-6 | 2 | pass | verifier | .claude/skills | No heredoc instruction. |
| GH-1 | 2 | fail | verifier | commit 5493b65 | The ASCII-title rule, seen broken twice, is still prose only. |
| GH-2 | 2 | pass | verifier | .github/workflows/roadkeep.yml | The guarded rule is re-checked by roadkeep lint in CI. |
| GH-3 | 2 | fail | verifier | hooks/hooks.json:5 | The plugin guard matches only file-edit tools, so a harness written through Bash is not seen. |
| GH-4 | 2 | pass | verifier | hooks/winwright-guard.cmd:26-29 | An unbuilt guard says on stderr that nothing is refusing, and a test holds it. |
| GH-5 | 2 | fail | verifier | .claude/settings.json:17-27 | No test or workflow reads the committed settings or .mcp.json. |
| GH-6 | 3 | fail | verifier | commit a18dd8d | A stale-copy notice ran all session while commits landed, and the lint reports it as a note, not a failure. |
| HR-1 | 1 | fail | verifier | commit 6917d3f | WW88 was recorded as shipped while the cases needing a controller had never run. |
| HR-2 | 2 | pass | verifier | repository-wide | No agent-chosen acceptance bar found. |
| IS-1 | 1 | pass | checker |  | no every-turn file (allowed by decision D2) |
| IS-2 | 1 | pass | verifier | repository root | No every-turn file, so the condition does not hold. |
| IS-3 | 1 | pass | verifier | .claude/skills/*/SKILL.md:3 | Skill descriptions say when to load. |
| IS-4 | 3 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md | Skill bodies and their pages have no gated ceiling; only skills/winwright is capped. |
| IS-5 | 3 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md:79-93 | The block table says eleven blocks while the roadmap declares Block L, unchecked. |
| IS-6 | 3 | pass | verifier | .mcp.json | winwright's own MCP server is not served to its own agent. |
| PG-1 | 1 | pass | checker |  | planning files declared in roadkeep.toml, and a PreToolUse guard is wired |
| PG-2 | 1 | fail | verifier | docs/ROADMAP.md:28 | WW506's line goes past the symptom into the design. |
| PG-3 | 1 | pass | verifier | docs/CHANGELOG.md | False premises recorded in the ledger. |
| PG-4 | 1 | pass | verifier | docs/CHANGELOG.md | Ledger entries say where the design went. |
| PG-5 | 1 | pass | verifier | roadkeep.toml:42 | Criteria declared, and blocks close on them. |
| PG-6 | 1 | pass | verifier | docs/ROADMAP.md:27-29 | No open line waits on a person or hardware. |
| PS-1 | 1 | pass | verifier | .claude/settings.json | No allow rules or permission mode committed. |
| PS-2 | 2 | fail | verifier | .claude/skills/roadmap-docs/SKILL.md:49-51 | Falling back to a raw git commit is forbidden in prose only. |
| PS-3 | 1 | pass | verifier | tools/run-tests-vm.ps1:55-59 | The clone holds no credential file and the runner defaults to a location outside the tree. |
| VG-1 | 2 | pass | verifier | .claude/skills/roadmap-docs/SKILL.md:154-160 | The gate runs on the tree to be committed. |
| VG-2 | 2 | pass | checker |  | 4 instruction file(s) scanned, no piped gate |
| VG-3 | 2 | pass | verifier | tools/host-gate.ps1:150-156 | A run that did not execute is never counted as a pass. |
| VG-4 | 3 | pass | verifier | tools/Winwright.RollCall | The roll call compares discovered with reported tests in CI. |
| VG-5 | 2 | pass | checker |  | on push: ci.yml, roadkeep.yml, site.yml |
| VG-6 | 2 | pass | verifier | commit 7a37e95 | The outside-cause red was filed and fixed by narrowing, not rerunning. |
| VG-7 | 2 | fail | verifier | commit 7a37e95 | CI stayed red for twenty-odd pushes while work continued, with no red-suite exception. |
| VG-8 | 2 | pass | verifier | docs/CHANGELOG.md | Recent behavioural ships carry covering cases. |
| VG-9 | 3 | pass | verifier | commit 5012473 | WW249 measured and reverted. |
