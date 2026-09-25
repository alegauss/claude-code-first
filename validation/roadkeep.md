# Conformance audit: roadkeep

- Commit: `77a3eaeb60540dc464a14e631fdc7ae4b3b82d7f`, audited 2026-09-25
- Specification version: 0.1.0
- Claimed level: 3; achieved level: 0; agent-facing profile audited
- Checker: 0.1.0; audit skill: 0.1.0

## Summary by chapter

| Chapter | pass | fail | waived | not applicable | could not run |
|---|---|---|---|---|---|
| AP | 2 | 2 | 0 | 0 | 0 |
| AW | 2 | 1 | 0 | 0 | 0 |
| CD | 1 | 5 | 0 | 0 | 0 |
| CS | 3 | 1 | 0 | 0 | 1 |
| EP | 4 | 1 | 0 | 0 | 1 |
| GH | 3 | 3 | 0 | 0 | 0 |
| HR | 1 | 1 | 0 | 0 | 0 |
| IS | 4 | 2 | 0 | 0 | 0 |
| PG | 6 | 0 | 0 | 0 | 0 |
| PS | 1 | 2 | 0 | 0 | 0 |
| VG | 5 | 4 | 0 | 0 | 0 |

## Rules

| Rule | Level | Verdict | By | Locus | Evidence |
|---|---|---|---|---|---|
| AP-1 | profile | fail | verifier | tests/test_commands.py:116 | Only the /help description of the four commands/*.md bodies is capped at 60 characters; no test or budget caps the bodies an agent receives, and [reads] caps only the brief, list and show responses. |
| AP-2 | profile | fail | verifier | tests/test_skill.py:256-259 | The names test checks only the hand-typed _MUST_NAME tuple, so a wrong write-tool name in skills/roadkeep/writing.md:17-24 would pass every gate. |
| AP-3 | profile | pass | verifier | .github/workflows/gate.yml payload job | The job installs the pinned CLAUDE_VERSION 2.1.220 and runs tests/test_plugin.py against the tree as the plugin loader reads it. |
| AP-4 | profile | pass | verifier | README.md:203 | Shio is named as the reference adoption with counted facts, and tests/corpora.py pins its revision. |
| AW-1 | 3 | fail | verifier | README.md:169 | The README says the twelve MCP tools while serving.TOOLS holds 71 at this commit, and no test reads that sentence. |
| AW-2 | 1 | pass | verifier | roadkeep.toml:47-73 | [limits], [non_goals] and [criteria] declare widths that the write path refuses. |
| AW-3 | 3 | pass | verifier | tests/test_skill.py:289 | The declared prose-shape rules are held by tests that read the governed prose. |
| CD-1 | 1 | fail | checker |  | 11 commit(s) add several ledger entries, e.g. 59230344, 2d6ca3ab, 5657be7b |
| CD-2 | 1 | fail | verifier | commit bc738ea6 | Filing Block J (9ecfa187) turned the suite red and bb40b38c fixed it later, so RK1690 was committed on a red tree. |
| CD-3 | 1 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md:65,69,83 | The default commit route stages everything, while the same skill says parallel sessions share this checkout. |
| CD-4 | 1 | fail | verifier | commit 06e56a8c | A docs commit writing ledger, decision, rationale and roadmap entries has a diff-generated title with no task id; 4473b6eb and 9a90f81a have the same shape. |
| CD-5 | 1 | pass | verifier | docs/ROADMAP.md:47-51 | Each open line names a fault or a missing capability. |
| CD-6 | 1 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md:59 | No commit rule says whether commits carry attribution, and d71c1625 and cdf09ac9 carry a Co-Authored-By trailer. |
| CS-1 | 2 | pass | verifier | .claude/skills/roadkeep-dev/SKILL.md:69-73 | The skill requires claim with --path, and claim reads the scope back against the tree. |
| CS-2 | 2 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md:69 | The prescribed stager adds every path in a checkout parallel sessions share, so it stages outside the claim. |
| CS-3 | 2 | pass | verifier | .githooks/pre-commit:15-26,37-44 | The hook derives the bump from the committed version and stages only the version files. |
| CS-4 | 2 | pass | verifier | tests/conftest.py:9-60 | Tests whose tree moved under the run skip with a warning instead of passing or failing. |
| CS-5 | 3 | could not run | verifier |  | Whether a cited count was taken while another session had uncommitted work cannot be read from the repository. |
| EP-1 | 2 | pass | verifier | .mcp.json | The committed .mcp.json declares the checkout's own scripts/roadkeep.py as the server that answers. |
| EP-2 | 2 | pass | checker |  | line terminators declared in .gitattributes |
| EP-3 | 2 | fail | verifier | src/roadkeep/installing.py:2844-2848 | subprocess.run with text=True and no encoding decodes a child's output with the locale codec; scripts/like_ci.py does the same. |
| EP-4 | 2 | pass | verifier | src/roadkeep/verbs/reading.py:45-62 | One leading U+FEFF is stripped from piped stdin. |
| EP-5 | 2 | could not run | verifier |  | The order in which past encoding defects were diagnosed is not recorded in a checkable form. |
| EP-6 | 2 | pass | verifier | .claude/skills/roadkeep-dev/SKILL.md:30 | Heredoc edits are forbidden and the only incident predates the rule. |
| GH-1 | 2 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md:30 | The heredoc rule was seen broken (RK1091) and stays prose only: no deny rule, and the guard does not refuse it. |
| GH-2 | 2 | pass | verifier | .github/workflows/gate.yml lint job | The guarded rule is also checked by roadkeep lint in CI. |
| GH-3 | 2 | fail | verifier | hooks/hooks.json:16 | The PreToolUse matcher leaves out the PowerShell tool, which can write a governed file on the Windows machine this project runs on. |
| GH-4 | 2 | fail | verifier | hooks/roadkeep-launch.py:427 | When no engine runs, the guard returns 0 and writes nothing, so the session is not told it is unguarded. |
| GH-5 | 2 | pass | verifier | tests/test_plugin.py:140-346 | The hook wiring and manifest are held by tests that run in CI. |
| GH-6 | 3 | pass | verifier | src/roadkeep/linting.py:1580-1662 | Lint reports install.stale and install.absent for a copy behind its source. |
| HR-1 | 1 | pass | verifier | docs/ROADMAP.md:47,51 | Lines waiting on a person carry (requires: decision) and stay open. |
| HR-2 | 2 | fail | verifier | commit a4c2ccec | When the weighing test went red, the agent lowered its own margin from 1.5 to 1.2 with no bar set by a person. |
| IS-1 | 1 | pass | checker |  | 2 every-turn file(s) under declared budgets |
| IS-2 | 1 | pass | verifier | agents.md | The every-turn file holds the laws and a layout index, and points to trigger-loaded skills. |
| IS-3 | 1 | pass | verifier | .claude/skills/roadkeep-dev/SKILL.md:3 | Skill descriptions name occasions and trigger words, held by a test. |
| IS-4 | 3 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md | This 5,990-byte trigger-loaded body has no ceiling in [budgets] or in the skill tests. |
| IS-5 | 3 | fail | verifier | skills/roadkeep/writing.md:17-24 | The list given as the whole write path leaves out served write tools, and no test checks it against serving.TOOLS. |
| IS-6 | 3 | pass | verifier | roadkeep.toml:75-232 | Per-tool and session ceilings on served schemas are enforced by lint. |
| PG-1 | 1 | pass | checker |  | planning files declared in roadkeep.toml, and a PreToolUse guard is wired |
| PG-2 | 1 | pass | verifier | docs/ROADMAP.md:47-51 | Open lines lead with the observed symptom. |
| PG-3 | 1 | pass | verifier | roadkeep.toml:306-308 | Falsified premises are recorded in place with the reason. |
| PG-4 | 1 | pass | verifier | docs/CHANGELOG.md | Ship entries carry design-recorded-in pointers, and decisions go to DECISIONS.md. |
| PG-5 | 1 | pass | verifier | roadkeep.toml:289-294 | Blocks carry done-when criteria, and permanent headings keep an emptied block from reading as closed. |
| PG-6 | 1 | pass | verifier | docs/ROADMAP.md:47,51 | Waiting lines carry the requirement with its declared reason. |
| PS-1 | 1 | fail | verifier | gui/.claude/settings.json:4-8 | This committed settings file carries allow rules, and nothing in gui/ names the guard or gate that stands in for the removed prompts. |
| PS-2 | 2 | fail | verifier | .claude/skills/roadkeep-dev/SKILL.md:30 | Heredoc edits are forbidden only in prose; no deny or ask rule and no guard refuses them. |
| PS-3 | 1 | pass | verifier | git ls-files | No tracked file has a credential-like name. |
| VG-1 | 2 | fail | verifier | commit bc738ea6 | RK1690 was recorded as shipped while the suite was red from filing Block J, with no red-suite exception. |
| VG-2 | 2 | pass | checker |  | 3 instruction file(s) scanned, no piped gate |
| VG-3 | 2 | fail | verifier | .github/workflows/gate.yml:62-64 | The corpus round-trip cases skip in CI and the job reports success, so checks that did not execute count toward a green run. |
| VG-4 | 3 | fail | verifier | .github/workflows/gate.yml:64 | The test gate is a bare pytest run, and nothing compares the tests collected with the tests that reported a result. |
| VG-5 | 2 | pass | checker |  | on push: gate.yml, gui-site.yml, gui.yml, site.yml |
| VG-6 | 2 | pass | verifier | tests/conftest.py | The recorded red from an outside cause was answered by narrowing the tests, not by rerunning. |
| VG-7 | 2 | pass | verifier | git log | No gate is recorded as kept red while other work continued. |
| VG-8 | 2 | fail | verifier | commit c66d7b30 | A behaviour change was recorded as shipped though the commit changes only settings and docs and no gate covers it. |
| VG-9 | 3 | pass | verifier | roadkeep.toml:75-232 | Each ceiling raise cites a reading taken before the change. |
