# Conformance audit: freewilly

- Commit: `c1c2eaf4694a03df85f8a8eeb83a7de03886b056`, audited 2026-09-25
- Specification version: 0.1.0
- Claimed level: 3; achieved level: 0; agent-facing profile audited
- Checker: 0.1.0; audit skill: 0.1.0

## Summary by chapter

| Chapter | pass | fail | waived | not applicable | could not run |
|---|---|---|---|---|---|
| AP | 1 | 3 | 0 | 0 | 0 |
| AW | 1 | 2 | 0 | 0 | 0 |
| CD | 1 | 5 | 0 | 0 | 0 |
| CS | 5 | 0 | 0 | 0 | 0 |
| EP | 3 | 3 | 0 | 0 | 0 |
| GH | 2 | 4 | 0 | 0 | 0 |
| HR | 2 | 0 | 0 | 0 | 0 |
| IS | 4 | 2 | 0 | 0 | 0 |
| PG | 6 | 0 | 0 | 0 | 0 |
| PS | 0 | 3 | 0 | 0 | 0 |
| VG | 5 | 4 | 0 | 0 | 0 |

## Rules

| Rule | Level | Verdict | By | Locus | Evidence |
|---|---|---|---|---|---|
| AP-1 | profile | fail | verifier | build/agent/SKILL.md:3 | agent-budget.json caps responses, refusals and a hypothetical MCP head, but nothing caps the shipped skill's description or body. |
| AP-2 | profile | fail | verifier | site/public/llms.txt:125 | llms.txt names CLI flags and verbs, and the only gate reading it checks tray captions and the Quit wording, not names against the command catalogue. |
| AP-3 | profile | fail | verifier | .github/workflows/check.yml:131-171 | The published .exe runs in CI only with --version, --plan and --preflight, and the skill is read from the source tree. |
| AP-4 | profile | pass | verifier | README.md, docs/, llms.txt | No claim that a consumer adopted the product is made. |
| AW-1 | 3 | fail | verifier | CONTRIBUTING.md:21 | The guide says two workflows while four exist, says the lint gate was removed while roadkeep.yml runs it, and nothing checks the guide. |
| AW-2 | 1 | pass | verifier | roadkeep.toml [limits] | Widths are set and the governed files are written through the roadkeep CLI, which refuses writes over them. |
| AW-3 | 3 | fail | verifier | README.md:375 | The writing skill bans the em dash in the README, which still has two, and nothing reads prose for the character. |
| CD-1 | 1 | fail | checker |  | 3 commit(s) add several ledger entries, e.g. 7bef7a5, 19bb532, d465734 |
| CD-2 | 1 | fail | verifier | commit 7bef7a5 | One commit ships DD267 and DD269 with two ledger entries. |
| CD-3 | 1 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:33 | run-commit.cmd stages everything, the self-check looks only for the previous task's leftovers, and unrelated files have landed in commits. |
| CD-4 | 1 | fail | verifier | commit 9aeea71 | The title names no task id and describes the diff, typed fix for a wording change. |
| CD-5 | 1 | pass | verifier | docs/ROADMAP.md | No open lines, and each retired entry names a defect. |
| CD-6 | 1 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:1-36 | The commit rules say nothing on attribution, while 17 commit bodies carry a Co-Authored-By trailer. |
| CS-1 | 2 | pass | verifier | roadkeep.toml [claims] | No shared checkout is shown, and claims are configured. |
| CS-2 | 2 | pass | verifier | repository history | No sessions shown sharing the checkout, so the condition does not hold. |
| CS-3 | 2 | pass | verifier | git ls-files | No git commit-time hook. |
| CS-4 | 2 | pass | verifier | docs/CHANGELOG.md | No gate run recorded as disturbed by other work. |
| CS-5 | 3 | pass | verifier | docs/CHANGELOG.md | No measurement recorded as taken on a busy tree. |
| EP-1 | 2 | fail | verifier | .claude/settings.json:62-63 | The vendored copy is declared at 0.2.473, but the unpinned roadkeep@alegauss plugin is also enabled and the launcher lets it answer whenever it is wired. |
| EP-2 | 2 | fail | checker |  | no text or eol rule in .gitattributes |
| EP-3 | 2 | fail | verifier | src/FreeWilly.Core/Agent/BundledComposeCli.cs:87-94 | docker compose output is read with no StandardOutputEncoding set; BuildHistory.cs does the same. |
| EP-4 | 2 | pass | verifier | .claude/hooks/roadkeep-launch.py:577 | The launcher passes the hook payload as bytes, and no product tool reads piped text. |
| EP-5 | 2 | pass | verifier | docs/CHANGELOG.md:40 | Encoding entries record byte-level diagnosis. |
| EP-6 | 2 | pass | verifier | docs/, .claude/ | No heredoc source edit is recorded. |
| GH-1 | 2 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:10-11 | One-task-one-commit, broken in 7bef7a5, is prose only; the em-dash rule was broken with no gate. |
| GH-2 | 2 | pass | verifier | .github/workflows/roadkeep.yml | The guarded rule is also checked by roadkeep lint on push. |
| GH-3 | 2 | fail | verifier | .claude/settings.json:87 | The guard is not matched on PowerShell, which is allowed and can write the governed files. |
| GH-4 | 2 | fail | verifier | .claude/hooks/roadkeep-launch.py:427 | When no engine runs, the guard returns 0 silently, so the session is not told it is unguarded. |
| GH-5 | 2 | pass | verifier | tests/FreeWilly.Preflight.Tests/PackagingTests.cs:272-337 | Tests fail if the allow floor or the guard wiring is lost, and they run in CI. |
| GH-6 | 3 | fail | verifier | tests/FreeWilly.Preflight.Tests/PackagingTests.cs:366-369 | The check of which roadkeep copy answers returns early on every CI runner, and no workflow runs install-roadkeep.cmd --check. |
| HR-1 | 1 | pass | verifier | docs/CHANGELOG.md | Entries needing a clean Windows were closed with a guest run, none on a person's judgement alone. |
| HR-2 | 2 | pass | verifier | agent-budget.json | The tolerance margin is stored in the committed budget file the test reads. |
| IS-1 | 1 | pass | checker |  | no every-turn file (allowed by decision D2) |
| IS-2 | 1 | pass | verifier | repository root | No every-turn file, so the condition does not hold. |
| IS-3 | 1 | pass | verifier | .claude/skills/*/SKILL.md:3 | Skill descriptions name when to use them. |
| IS-4 | 3 | fail | verifier | .claude/skills/roadkeep/writing.md | No skill body or page has a gated ceiling (49,464, 21,817 and 8,620 bytes). |
| IS-5 | 3 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:48-52 | The skill lists roadkeep verbs, and nothing checks them against roadkeep's catalogue. |
| IS-6 | 3 | pass | verifier | agent-budget.json mcp | The project serves no MCP tools of its own, which a test enforces. |
| PG-1 | 1 | pass | checker |  | planning files declared in roadkeep.toml, and a PreToolUse guard is wired |
| PG-2 | 1 | pass | verifier | docs/ROADMAP.md | No open lines; ledger lines lead with the symptom. |
| PG-3 | 1 | pass | verifier | docs/CHANGELOG.md | False premises are recorded as retirements with reasons. |
| PG-4 | 1 | pass | verifier | docs/specs/DD33-mcp-is-a-second-head.md | The lasting rationale lives in a spec a test reads. |
| PG-5 | 1 | pass | verifier | docs/ROADMAP.md | No block is declared closed. |
| PG-6 | 1 | pass | verifier | docs/ROADMAP.md | No open task waits on a person or hardware. |
| PS-1 | 1 | fail | verifier | .claude/settings.json:4-49 | Bash, PowerShell, Write and WebFetch are allowed under acceptEdits with empty deny and ask lists, and only the governed-file guard is named in their place. |
| PS-2 | 2 | fail | verifier | .claude/skills/freewilly-roadmap-docs/SKILL.md:22 | Starting a second task before committing the first is forbidden only in prose. |
| PS-3 | 1 | fail | verifier | .gitignore:19-25 | The repository keeps a VM credential file in its working tree by design, out of commits only through an ignore line. |
| VG-1 | 2 | fail | verifier | commit d1f00b9 | DD116 shipped with a test that stayed red on every push until 2026-08-19. |
| VG-2 | 2 | pass | checker |  | 6 instruction file(s) scanned, no piped gate |
| VG-3 | 2 | fail | verifier | tests/FreeWilly.Preflight.Tests/PackagingTests.cs:366-369 | When its precondition is missing the test returns and counts as passed. |
| VG-4 | 3 | fail | verifier | .github/workflows/check.yml:47 | A bare dotnet test, with no comparison of tests discovered against tests reported. |
| VG-5 | 2 | pass | checker |  | on push: check.yml, roadkeep.yml, site.yml |
| VG-6 | 2 | pass | verifier | docs/CHANGELOG.md:234 | Outside-cause reds were fixed by narrowing the test, not rerun until green. |
| VG-7 | 2 | pass | verifier | commit d1f00b9 | Nobody chose to keep the red; it went unnoticed, which is VG-1's defect, not this rule's. |
| VG-8 | 2 | fail | verifier | commit 5d1463a | DD75 changed behaviour and was recorded as shipped with no test, verified by hand. |
| VG-9 | 3 | pass | verifier | agent-budget.json baseline | The agent surface was measured against a baseline before it was built. |
