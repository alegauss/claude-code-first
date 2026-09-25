# Conformance audit: shio

- Commit: `fb966f8dae563c5b188933f894cc84b6da3f4c48`, audited 2026-09-25
- Specification version: 0.1.0
- Claimed level: 3; achieved level: 0; agent-facing profile audited
- Checker: 0.1.0; audit skill: 0.1.0

## Summary by chapter

| Chapter | pass | fail | waived | not applicable | could not run |
|---|---|---|---|---|---|
| AP | 2 | 2 | 0 | 0 | 0 |
| AW | 2 | 1 | 0 | 0 | 0 |
| CD | 3 | 3 | 0 | 0 | 0 |
| CS | 3 | 2 | 0 | 0 | 0 |
| EP | 2 | 4 | 0 | 0 | 0 |
| GH | 0 | 6 | 0 | 0 | 0 |
| HR | 2 | 0 | 0 | 0 | 0 |
| IS | 2 | 3 | 0 | 0 | 1 |
| PG | 5 | 1 | 0 | 0 | 0 |
| PS | 0 | 3 | 0 | 0 | 0 |
| VG | 4 | 5 | 0 | 0 | 0 |

## Rules

| Rule | Level | Verdict | By | Locus | Evidence |
|---|---|---|---|---|---|
| AP-1 | profile | fail | verifier | claude-plugin/test/plugin.test.mjs:94-97 | MCP schemas, responses and CLI help are capped, but the published plugin's skill descriptions and bodies have no ceiling, only a minimum length. |
| AP-2 | profile | fail | verifier | claude-plugin/skills/shio-verify/SKILL.md:31 | The plugin skill names MCP tools, and no test checks plugin skill text against the tool catalogue. |
| AP-3 | profile | pass | verifier | claude-plugin/test/plugin.test.mjs:266 | Sessions load the published plugin from its marketplace, the SH949 test holds that, and clean-room.test.mjs checks the packed CLI. |
| AP-4 | profile | pass | verifier | README.md | No claim that a consumer adopted Shio. |
| AW-1 | 3 | fail | verifier | agents.md:181 | The every-turn file says ten IT classes while 13 are tracked, and the figures test does not cover the sentence. |
| AW-2 | 1 | pass | verifier | roadkeep.toml:327-351 | [limits] declared for roadkeep to refuse at the write. |
| AW-3 | 3 | pass | verifier | shio-site/scripts/ai-writing.test.mjs | The declared writing pass is backed by a tracked lint. |
| CD-1 | 1 | fail | checker |  | 1 commit(s) add several ledger entries, e.g. 543c6c2e7 |
| CD-2 | 1 | pass | verifier | f88c4616a | The commit files SH577-SH579 as new open lines and ships no task, so no batch is shown. |
| CD-3 | 1 | fail | verifier | agents.md:239-245 | The mandated run-commit.cmd runs git add * in a checkout other sessions share, with no step checking the tree first. |
| CD-4 | 1 | pass | verifier | agents.md:251-253 | The agent writes the title with -m, and recent subjects carry task ids. |
| CD-5 | 1 | pass | verifier | ebe36e63c | Filings and retirements each name a defect or a wrong premise. |
| CD-6 | 1 | fail | verifier | agents.md:237-253 | Nothing the agent reads states a commit attribution policy, while some agent commits carry the trailer. |
| CS-1 | 2 | pass | verifier | .claude/skills/roadkeep/SKILL.md:24-26,122-160 | The committed roadkeep skill tells a session to claim its line and declare its paths. |
| CS-2 | 2 | fail | verifier | agents.md:241 | In a shared checkout the prescribed tool stages with git add *, sweeping paths outside any session's claim. |
| CS-3 | 2 | pass | verifier | package.json | No commit-time hook. |
| CS-4 | 2 | fail | verifier | 632cbdac4 | Another session's uncommitted edits turned pnpm test red and it was reported failed; the gate has no detection that would yield could not run. |
| CS-5 | 3 | pass | verifier | 1dcd16a1e | The census was deliberately taken after another session's edits left the tree. |
| EP-1 | 2 | fail | verifier | roadkeep.toml:7-11 | roadkeep.toml and agents.md disagree on which roadkeep copy answers, and no committed file fixes the copy and version. |
| EP-2 | 2 | pass | checker |  | line terminators declared in .gitattributes |
| EP-3 | 2 | fail | verifier | scripts/install_roadkeep.py:76-78 | A child's stdout is decoded with the locale default. |
| EP-4 | 2 | pass | verifier | cli/src/commands/apply.mjs:139-143 | A leading BOM on piped stdin is refused by JSON.parse, not kept as content. |
| EP-5 | 2 | fail | verifier | 08eeb9290 | SH519 was filed after byte checks along the product path only, and retired four hours later when the fault was the agent's own reads. |
| EP-6 | 2 | fail | verifier | docs/ROADMAP.md:29 | SH1119 records a heredoc that corrupted two committed regexes. |
| GH-1 | 2 | fail | verifier | agents.md:247 | One task one commit, called the most violated rule, is read by no hook, test or workflow. |
| GH-2 | 2 | fail | verifier | .github/workflows/roadkeep.yml:12-13 | roadkeep lint, the gate behind the guard, runs only on workflow_dispatch. |
| GH-3 | 2 | fail | verifier | .claude/settings.json:74 | The guard's matcher omits PowerShell, which settings.json allows and which can write the governed files. |
| GH-4 | 2 | fail | verifier | .claude/hooks/roadkeep-launch.py:420-427 | With no engine, the guard returns 0 without telling the session. |
| GH-5 | 2 | fail | verifier | claude-plugin/test/plugin.test.mjs:266-289 | Only two keys of .claude/settings.json are asserted; the hook wiring, permissions and .mcp.json are read by no test. |
| GH-6 | 3 | fail | verifier | install-roadkeep.cmd:38 | Several roadkeep copies are reachable, and the staleness check is run by no workflow or test. |
| HR-1 | 1 | pass | verifier | docs/CHANGELOG.md | No ship closed work that needed a person or hardware. |
| HR-2 | 2 | pass | verifier | cli/src/acceptance.properties | The acceptance bar is stored where a test reads it. |
| IS-1 | 1 | could not run | checker |  | every-turn files present; no budget declared in a format this checker reads |
| IS-2 | 1 | fail | verifier | agents.md:109-124 | The every-turn index carries area-specific rules also held in area files and skills. |
| IS-3 | 1 | pass | verifier | .claude/skills/*/SKILL.md | All skill descriptions state their occasions. |
| IS-4 | 3 | fail | verifier | docs/agents/cli.md | No gate caps skill bodies or the area files the index points to (cli.md 376,898 bytes, agent-surface.md 305,908). |
| IS-5 | 3 | fail | verifier | agents.md:65-84 | The area table's paths and skill names are read by no test. |
| IS-6 | 3 | pass | verifier | ShMcpToolBudgetTest.java | Served MCP schema sizes are capped by a test that runs on push. |
| PG-1 | 1 | pass | checker |  | planning files declared in roadkeep.toml, and a PreToolUse guard is wired |
| PG-2 | 1 | pass | verifier | docs/ROADMAP.md:29 | Open lines state a symptom and point to their rationale. |
| PG-3 | 1 | pass | verifier | c17ed995a | The false SH519 premise was recorded as a retirement with its reason. |
| PG-4 | 1 | pass | verifier | agents.md:285-288 | Shipped decisions go to area files. |
| PG-5 | 1 | fail | verifier | ca57c16b4 | Block S was declared closed because its only task was retired, and a test enforces dropping any block with no open task while [criteria] stays empty. |
| PG-6 | 1 | pass | verifier | docs/ROADMAP.md | No open line waits on a person or hardware. |
| PS-1 | 1 | fail | verifier | .claude/settings.json:7-54 | Bash, PowerShell, Edit and Write are allowed under acceptEdits, and nothing committed names what stands in. |
| PS-2 | 2 | fail | verifier | agents.md:244-245 | Hand-authored commits are forbidden in prose only, and 871410748 was hand-authored anyway. |
| PS-3 | 1 | fail | verifier | scripts/sonar/sonar-scan.sh:34,70 | An analysis token is written into the working tree, excluded only by an ignore line. |
| VG-1 | 2 | fail | verifier | 632cbdac4 | The commit landed with pnpm test red on the tree the gate ran on, with no red-suite exception. |
| VG-2 | 2 | fail | checker |  | gate piped in .claude/skills/shio-build-test/SKILL.md:17 |
| VG-3 | 2 | fail | verifier | agents.md:188-193 | Schema ITs skip without Docker and count as Skipped under a green run, not as could not run. |
| VG-4 | 3 | fail | verifier | scripts/gate-stamp.mjs:356 | The gate checks only that a suite printed a summary, never tests discovered against tests reported. |
| VG-5 | 2 | pass | checker |  | on push: suites.yml |
| VG-6 | 2 | pass | verifier | scripts/gate-stamp.mjs:330-365 | Outside-cause reds were filed and fixed by narrowing, not rerun. |
| VG-7 | 2 | pass | verifier | red-suites.json | Exceptions carry a task, a date and an expiry, and a test kills an expired entry. |
| VG-8 | 2 | fail | verifier | cli/test/assertion-debt.test.mjs:197-233 | The DEBT list names shipped behaviour-changing tasks with no covering assertion. |
| VG-9 | 3 | pass | verifier | agents.md:195-202 | Measurement comes before a fix, as SH957 shows. |
