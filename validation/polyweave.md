# Conformance audit: polyweave

- Commit: `15874cc0a331f70d6964aa41604cd0befe9491cc`, audited 2026-09-25
- Specification version: 0.1.0
- Claimed level: 3; achieved level: 0; agent-facing profile audited
- Checker: 0.1.0; audit skill: 0.1.0

## Summary by chapter

| Chapter | pass | fail | waived | not applicable | could not run |
|---|---|---|---|---|---|
| AP | 3 | 1 | 0 | 0 | 0 |
| AW | 2 | 1 | 0 | 0 | 0 |
| CD | 3 | 3 | 0 | 0 | 0 |
| CS | 2 | 2 | 0 | 0 | 1 |
| EP | 3 | 2 | 0 | 0 | 1 |
| GH | 1 | 4 | 0 | 0 | 1 |
| HR | 2 | 0 | 0 | 0 | 0 |
| IS | 3 | 2 | 0 | 0 | 1 |
| PG | 5 | 1 | 0 | 0 | 0 |
| PS | 1 | 2 | 0 | 0 | 0 |
| VG | 6 | 1 | 0 | 0 | 2 |

## Rules

| Rule | Level | Verdict | By | Locus | Evidence |
|---|---|---|---|---|---|
| AP-1 | profile | pass | verifier | src/polyweave/server.py:41-49 | Tool, list, skill and response budgets have reasons beside them and are enforced by tests. |
| AP-2 | profile | pass | verifier | tests/test_plugin.py:53-58 | Every name in the shipped skill and specs is checked against the registry and the code. |
| AP-3 | profile | fail | verifier | .github/workflows/gates.yml:27 | CI installs editable and tests the checkout; no test loads the MCP server or skill from a built or installed artefact. |
| AP-4 | profile | pass | verifier | commits 5eb1a8e, ddad82d | Adoption claims name Cottony and a counted change there. |
| AW-1 | 3 | fail | verifier | CLAUDE.md:58 | CLAUDE.md says five constraints bind the project while docs/ROADMAP.md lists six non-goals, and nothing checks the count. |
| AW-2 | 1 | pass | verifier | roadkeep.toml:16-26 | [limits] are enforced by the roadkeep write path. |
| AW-3 | 3 | pass | verifier | roadkeep.toml:24-26 | No house style is declared beyond the fill width roadkeep applies. |
| CD-1 | 1 | pass | checker |  | every commit adds at most one ledger entry |
| CD-2 | 1 | pass | verifier | git log | No commit bundles several finished tasks; parts are marked. |
| CD-3 | 1 | fail | verifier | CLAUDE.md:64 | The prescribed commit tool stages the whole tree while the audit skill expects other sessions to share the checkout. |
| CD-4 | 1 | fail | verifier | commit 8d762a2 (also 3771c41) | Titles carry no task id and bodies are generated bullets walking the diff. |
| CD-5 | 1 | pass | verifier | docs/DEFERRED.md | Open lines and deferral entries each name a symptom. |
| CD-6 | 1 | fail | verifier | CLAUDE.md:61-64 | The commit rules do not say whether commits carry attribution. |
| CS-1 | 2 | pass | verifier | roadkeep.toml:33-35 | Claims are configured and tasks start through roadkeep brief. |
| CS-2 | 2 | fail | verifier | .gitignore:7-9 | The commit tool stages the whole tree, so in a shared checkout it stages outside any claim. |
| CS-3 | 2 | pass | verifier | repository root | No commit-time hook is tracked. |
| CS-4 | 2 | fail | verifier | tools/gate.py:136-141 | The lock detects only another run of the gate itself, so a run disturbed by another session's edits still reports green or red. |
| CS-5 | 3 | could not run | verifier |  | The clone keeps no record of other sessions' uncommitted work when counts were taken. |
| EP-1 | 2 | pass | verifier | .claude/hooks/roadkeep-launch.py:26-36 | The launcher declares the resolution order and roadkeep.toml pins the version. |
| EP-2 | 2 | pass | checker |  | line terminators declared in .gitattributes |
| EP-3 | 2 | fail | verifier | src/polyweave/capabilities.py:57-63 | Child output is decoded with the locale default; also loop.py:81-88 and tools/gate.py. |
| EP-4 | 2 | fail | verifier | hooks/guard.py:167 | The shipped guard does not strip a byte-order mark, and its bare except then allows the call silently. |
| EP-5 | 2 | pass | verifier | tests/test_readable.py | The PW73 encoding defect is checked on bytes. |
| EP-6 | 2 | could not run | verifier |  | The clone does not record which tool wrote source files. |
| GH-1 | 2 | pass | verifier | docs/CHANGELOG.md PW137, PW135 | Recorded breaches were moved into gates. |
| GH-2 | 2 | fail | verifier | .claude/settings.json:24-34 | The no-clobber guard's rule has no gate in CI and no test. |
| GH-3 | 2 | fail | verifier | .claude/settings.json:26 | no-clobber is matched only on Write, so a shell redirect can replace a file unguarded. |
| GH-4 | 2 | fail | verifier | .claude/hooks/roadkeep-launch.py:421-427 | When no engine runs, the guard returns 0 silently, so the session is not told it is unguarded. |
| GH-5 | 2 | fail | verifier | .claude/settings.json:1-69 | No test reads settings.json or .mcp.json; losing a PreToolUse or Stop entry fails nothing. |
| GH-6 | 3 | could not run | verifier | .claude/skills/roadkeep/ | No gate in the tree compares the vendored copy with its source; the external lint action cannot be judged from the clone. |
| HR-1 | 1 | pass | verifier | docs/DEFERRED.md | Work needing a person's judgement is set aside rather than shipped. |
| HR-2 | 2 | pass | verifier | skills/polyweave/references/specs.md | Bounds record a person as their origin, and the agent is told not to move them. |
| IS-1 | 1 | could not run | checker |  | every-turn files present; no budget declared in a format this checker reads |
| IS-2 | 1 | pass | verifier | CLAUDE.md:1-64 | The every-turn file holds purpose, gates and commit rule, and points to specs and skills for the rest. |
| IS-3 | 1 | pass | verifier | .claude/skills/*/SKILL.md | Skill descriptions name the occasions they load on. |
| IS-4 | 3 | fail | verifier | CLAUDE.md:42-47 | Only skills/polyweave has a ceiling; nothing bounds docs/specs (196 KB the agent is sent to), the audit skill or the roadkeep pages. |
| IS-5 | 3 | fail | verifier | .claude/skills/audit/SKILL.md:36-37 | Config keys and paths named in the audit skill and CLAUDE.md are not checked against their source. |
| IS-6 | 3 | pass | verifier | src/polyweave/server.py:41-49 | The served MCP schemas are held under budgets by tests that CI runs. |
| PG-1 | 1 | pass | checker |  | planning files declared in roadkeep.toml, and a PreToolUse guard is wired |
| PG-2 | 1 | pass | verifier | docs/ROADMAP.md | Open lines state symptoms. |
| PG-3 | 1 | pass | verifier | commit 5eb1a8e | The false premise under PW56 was recorded in the open. |
| PG-4 | 1 | pass | verifier | docs/CHANGELOG.md | Shipped entries point to where the design lives. |
| PG-5 | 1 | fail | verifier | site/src/lib/roadmap.ts:42-44 | The site counts a block as built when nothing under it is open, regardless of its declared criteria. |
| PG-6 | 1 | pass | verifier | docs/DEFERRED.md | Waiting work is recorded as deferrals with reasons. |
| PS-1 | 1 | fail | verifier | .claude/settings.json:5 | Bash(*) is allowed with empty deny and ask lists, and nothing committed names what stands in. |
| PS-2 | 2 | fail | verifier | CLAUDE.md:64 | Never pushing is prose only; no deny or ask rule and no guard refuses git push. |
| PS-3 | 1 | pass | verifier | git ls-files | No credential-like file is tracked. |
| VG-1 | 2 | could not run | verifier |  | CI run results per commit are not in the clone. |
| VG-2 | 2 | pass | checker |  | 5 instruction file(s) scanned, no piped gate |
| VG-3 | 2 | pass | verifier | tools/gate.py:83-102,136-141 | Skipped tests are reported apart from passed, and a held lock exits without a verdict. |
| VG-4 | 3 | fail | verifier | tools/gate.py:83-102 | The gate tallies the JUnit report and never compares it with the tests collected. |
| VG-5 | 2 | pass | checker |  | on push: gates.yml, roadkeep.yml, site.yml |
| VG-6 | 2 | could not run | verifier |  | CI history is not in the clone. |
| VG-7 | 2 | pass | verifier | .github/workflows/gates.yml | No gate is recorded as kept red while work continued. |
| VG-8 | 2 | pass | verifier | git log | Sampled behaviour-changing commits each add or change a test. |
| VG-9 | 3 | pass | verifier | tests/test_budgets.py | Size budgets are set from measured values written beside them. |
