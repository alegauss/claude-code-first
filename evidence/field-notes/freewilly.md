# freewilly: field notes (verified)

Extracted 2026-09-24; last commit `c1c2eaf` (2026-09-17). .NET / WPF.

## 1. Instruction surface

No CLAUDE.md or AGENTS.md is tracked; `.roadkeep/agents.md` is the engine's, ignored.
`CONTRIBUTING.md` (41 lines): "The files under docs/ are written by a tool, not by hand"
("a hand edit is refused rather than reviewed", l.11-12) and "The gates" with "Three things
CI cannot do, stated here rather than implied by a green tick" (l.29). Drift: l.13-14 and
31-33 say CI no longer lints, but `714360e` restored `roadkeep.yml` after `cd630d6`
removed it. Rationale lives as comments where rules are enforced (`.gitignore:1-50`,
`winwright.json`, `install-roadkeep.cmd`, `run-cases.cmd`) (inference: house practice).

## 2. `.claude/`

- `settings.json` (committed): `defaultMode: acceptEdits`; ~40 tools allowed incl. bare
  Bash, PowerShell, Agent; plugin roadkeep; `env ROADKEEP_HOME`; guard on SessionStart,
  PreToolUse, Stop.
- `settings.local.json` (ignored): `bypassPermissions`,
  `skipDangerousModePermissionPrompt: true`.
- `.bak` files untracked, timestamped 17:07 on 2026-08-14, four minutes before `ac7e7ec`:
  "restore the permission entries a session trimmed … the second time in this session that
  file has been trimmed under me". (inference) manual snapshots.
- `hooks/roadkeep-launch.py` (31 KB) with the three rules (defer to plugin, never block a
  turn, never reach the network).
- Skills (4, 1,323 lines): `ai-writing-freewilly` ("Every word in this repository was
  written by a model"; em-dash ban; "Counts and versions are generated, not written");
  `freewilly-roadmap-docs` ("⛔ READ FIRST — one task, one commit … the single most
  violated rule"; `/loop` for batches; self-check; "A new block is the last resort");
  vendored `roadkeep`; `window-chrome` ("Found by capturing the window and comparing, not
  by reasoning. Do not undo them"; byte-identical PNG before/after).
- `agent-budget.json` (17.8 KB): token budget for the product's agent-facing CLI output,
  read by `AgentBudgetTests.cs` ("a build that made a response more expensive fails … the
  commit that raises one says what the tokens bought"); chars/4; baseline task 6 calls /
  11,711 tokens vs shaped surface 4 calls / 812; future MCP capped at `maxTools: 6`,
  `maxSchemaTokens: 1100`.
- `install-roadkeep.cmd`: fixed engine path because "Every distinct command path is a
  fresh authorization prompt" and an ImportError from a half-edited checkout (`89371b8`).

## 3. Docs

prefix DD; ledger 276 ✅ / 4 🗑; roadmap drained (8 empty blocks, 8 non-goals).
`docs/specs/` four "constitutions" (DD23 agent-first P1-P10, DD33 MCP, DD34 window, DD40
site). `docs/_preview/` output only.

## 4. Gates

~90 xUnit files with fakes; Winwright desktop cases outside the solution. Tests guarding
the agent setup: `PackagingTests.cs:272-330` (DD115) fails if `.claude/settings.json`
loses the minimum tools or the guard hooks; `AgentDiscoveryTests`; `PaletteTests`. CI
`check.yml` builds, tests, publishes and runs the exe (one Winwright case); `roadkeep.yml`
lint; VM-only engine install check (`scripts/vm.ps1`).

## 5. Commits

425/444 conventional (feat 136, fix 107, docs 99, chore 46, test 22, refactor 9, ci 4);
`type(scope): DD<n> <behaviour sentence>`; filing is its own commit. Bodies: generated
bullets from `ai_commit.py` or hand prose on important commits. 17 Co-Authored-By
trailers; 12 commits authored by Claude via PR #1 from a `claude/…` branch (`7968cc5`,
inference: web session).

## 6. Learnings

1. The harness rewrote `.claude/settings.json` mid-session, dropping fifteen entries,
   twice; the deletion rode into `46ec80f` (`ac7e7ec`) → DD115 build test (`646e121`).
2. Stage-everything commits sweep strays (DD117 retired: fix would touch a shared tool)
   → `.gitignore` for `__pycache__/`, `TestResults/`.
3. Lint removed from CI (`cd630d6`) and restored (`714360e`); drift "reached main
   unremarked" (`check.yml:12-15`); CONTRIBUTING never updated.
4. Hand edits pass where the plugin is not loaded → committed launcher.
5. Floating tool paths cost prompts and wrong versions → fixed engine path.
6. Agents batch tasks unless forced not to → `/loop`, `git status` check.
7. A commit without `-m` mislabels docs work.
8. Model-written prose is detectable: 207 em dashes, "two in every three sentences"
   (`0794e60`, DD184) → repo writing skill.
9. Typed counts go stale (`llms.txt` said 4 of 5) → generated counts.
10. Eye checks miss what capture comparison catches (`window-chrome` l.63-65).
11. A capture passed while photographing the guest's wallpaper (`c1c2eaf`) → wait for a
    semantic signal; an unmeasured case is not a gate.
12. Budget test failed for the wrong reason (`f514e11`, `ecaad33`, `bfa7d35`, `87cf631`)
    → deterministic fixtures, ±15% size band.
13. An edit silently did not apply (DD95) → missing test added, dead code deleted.
14. Hand-maintained lists drift (`0731091`, DD100) → reflection.
15. Wrong premises retired, not edited (DD195, DD268, DD77, DD117).
16. MCP vs CLI decided by Shio's measurement: "~2 400 tokens across eleven tools" per turn
    (`DD33-mcp-is-a-second-head.md`) → CLI first; MCP capped.
17. (inference) A "binding" spec law (DD23 P10) was overridden by `4575583` without
    amending the spec.

## 7. Metrics

444 commits, 2026-08-12 (`acc7fc1`) → 2026-09-17 (`c1c2eaf`); busiest 08-14 (92).
4 skills / 6 files; 1 hook script on 3 events; 1 MCP server; 4 specs; 373 tracked files.

## Verification

Checked against `c1c2eaf` on 2026-09-24. 106 claims: 85 verified, 13 corrected, 0 refuted, 3 outside the pin, 5 inference. Error rate 13.3%.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | Header | The last commit is `c1c2eaf`, dated 2026-09-17 | verified | [freewilly@c1c2eaf]; `git log -1 --format=%ci c1c2eaf` = 2026-09-17 18:09:50 -0300 | |
| 2 | Header | The project is .NET / WPF | verified | "UseWPF" [freewilly@c1c2eaf:src/FreeWilly.Tray/FreeWilly.Tray.csproj#L8] | |
| 3 | 1 | No CLAUDE.md or AGENTS.md is tracked | verified | `git ls-tree -r --name-only c1c2eaf` lists 373 paths and none is CLAUDE.md or AGENTS.md, in any case | |
| 4 | 1 | `.roadkeep/agents.md` is the engine's and is ignored | outside the pin | The file is not in any commit. The pin says only that the directory holds the vendored engine and is not committed: "reproduced by this script, never committed" [freewilly@c1c2eaf:install-roadkeep.cmd#L25], ignored at [freewilly@c1c2eaf:.gitignore#L17] | |
| 5 | 1 | `CONTRIBUTING.md` has 41 lines | corrected | `git show c1c2eaf:CONTRIBUTING.md` has 40 lines, the last ending in a newline [freewilly@c1c2eaf:CONTRIBUTING.md#L40] | `CONTRIBUTING.md` has 40 lines at the pin [freewilly@c1c2eaf:CONTRIBUTING.md#L1-L40] |
| 6 | 1 | A section heading says the files under docs/ are written by a tool, not by hand | verified | "are written by a tool, not by hand" [freewilly@c1c2eaf:CONTRIBUTING.md#L7] (the source sets docs/ in code formatting) | |
| 7 | 1 | "a hand edit is refused rather than reviewed", l.11-12 | verified | "a hand edit is refused rather than reviewed" [freewilly@c1c2eaf:CONTRIBUTING.md#L11-L12] | |
| 8 | 1 | A section "The gates" | verified | "The gates" [freewilly@c1c2eaf:CONTRIBUTING.md#L19] | |
| 9 | 1 | "Three things CI cannot do, stated here rather than implied by a green tick" at l.29 | verified | "Three things CI cannot do, stated here rather than implied by a green tick" [freewilly@c1c2eaf:CONTRIBUTING.md#L29] | |
| 10 | 1 | Lines 13-14 and 31-33 say CI no longer lints | verified | "CI no longer does" [freewilly@c1c2eaf:CONTRIBUTING.md#L13-L14]; "every push was removed" [freewilly@c1c2eaf:CONTRIBUTING.md#L31-L33] | |
| 11 | 1, 6 | `cd630d6` removed `roadkeep.yml` | verified | "workflow as it is no longer needed" [freewilly@cd630d6]; its diff deletes .github/workflows/roadkeep.yml (38 lines), dated 2026-08-19 | |
| 12 | 1, 6 | `714360e` restored `roadkeep.yml` after `cd630d6` removed it | verified | "put lint back in CI" [freewilly@714360e]; its diff creates .github/workflows/roadkeep.yml, dated 2026-08-29 | |
| 13 | 1 | Rationale comments at `.gitignore:1-50` | corrected | `.gitignore` has 49 lines at the pin [freewilly@c1c2eaf:.gitignore#L1-L49] | The rationale comments run through the whole of `.gitignore`, lines 1-49 [freewilly@c1c2eaf:.gitignore#L1-L49] |
| 14 | 1 | `winwright.json`, `install-roadkeep.cmd` and `run-cases.cmd` carry their rationale as comments | verified | [freewilly@c1c2eaf:winwright.json#L1-L7]; [freewilly@c1c2eaf:install-roadkeep.cmd#L4-L42]; [freewilly@c1c2eaf:run-cases.cmd#L1-L15] | |
| 15 | 1 | Rationale-as-comments is house practice | inference | | |
| 16 | 2 | `.claude/settings.json` is committed | verified | "settings.json IS committed" [freewilly@c1c2eaf:.gitignore#L9-L11] | |
| 17 | 2 | `defaultMode: acceptEdits` | verified | "acceptEdits" [freewilly@c1c2eaf:.claude/settings.json#L4] | |
| 18 | 2 | About 40 tools allowed, including bare Bash, PowerShell and Agent | verified | 42 entries in permissions.allow [freewilly@c1c2eaf:.claude/settings.json#L6-L47]; Bash at L6, PowerShell at L7, Agent at L18 | |
| 19 | 2 | The roadkeep plugin is enabled | verified | "roadkeep@alegauss" [freewilly@c1c2eaf:.claude/settings.json#L62-L64] | |
| 20 | 2 | `env ROADKEEP_HOME` is set | verified | "ROADKEEP_HOME" [freewilly@c1c2eaf:.claude/settings.json#L109-L111] | |
| 21 | 2 | The guard hook runs on SessionStart, PreToolUse and Stop | verified | [freewilly@c1c2eaf:.claude/settings.json#L73-L107], each stage running roadkeep-launch.py guard | |
| 22 | 2 | `settings.local.json` is ignored and holds `bypassPermissions` and `skipDangerousModePermissionPrompt: true` | outside the pin | Not tracked, so its content cannot be checked; `/.claude/*` is ignored [freewilly@c1c2eaf:.gitignore#L7] and only skills/, settings.json and hooks/ are negated [freewilly@c1c2eaf:.gitignore#L8-L15] | |
| 23 | 2 | `.bak` files are untracked, timestamped 17:07 on 2026-08-14, four minutes before `ac7e7ec` | outside the pin | The files are in no commit. `ac7e7ec` itself is dated 2026-08-14 17:11:04 -0300 [freewilly@ac7e7ec] | |
| 24 | 2 | `ac7e7ec` says "restore the permission entries a session trimmed … the second time in this session that file has been trimmed under me" | verified | "restore the permission entries a session trimmed" [freewilly@ac7e7ec]; "the second time in this session that file has been trimmed under me" [freewilly@ac7e7ec] | |
| 25 | 2 | The `.bak` files are manual snapshots | inference | | |
| 26 | 2 | `hooks/roadkeep-launch.py` is 31 KB | verified | `git cat-file -s c1c2eaf:.claude/hooks/roadkeep-launch.py` = 31057 bytes [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py] | |
| 27 | 2 | The hook states three rules: defer to the plugin, never block a turn, never reach the network | verified | "Three rules keep it from ever making things worse" [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L38]; "Defer to the plugin." [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L40]; "Never block a turn." [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L48]; "Never reach the network." [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L50] | |
| 28 | 2 | 4 skills, 1,323 lines | verified | `git ls-tree -r --name-only c1c2eaf .claude/skills` lists 6 files in 4 skill directories; their line counts at the pin are 140 + 84 + 164 + 266 + 598 + 71 = 1,323 | |
| 29 | 2 | `ai-writing-freewilly`: "Every word in this repository was written by a model" | verified | "Every word in this repository was written by a model" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L8] | |
| 30 | 2 | `ai-writing-freewilly` bans the em dash | verified | "No em dashes in published prose" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L30] | |
| 31 | 2 | `ai-writing-freewilly`: "Counts and versions are generated, not written" | verified | "Counts and versions are generated, not written" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L97] | |
| 32 | 2 | `freewilly-roadmap-docs`: "⛔ READ FIRST — one task, one commit … the single most violated rule" | verified | "READ FIRST — one task, one commit" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L8]; "the single most violated rule" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L10-L11] | |
| 33 | 2 | `freewilly-roadmap-docs` drives batches with `/loop` | verified | "For any batch of ≥2 tasks, drive it with the" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L25-L27] | |
| 34 | 2 | `freewilly-roadmap-docs` has a self-check | verified | "Self-check before starting task N+1" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L28-L31] | |
| 35 | 2 | `freewilly-roadmap-docs`: "A new block is the last resort" | verified | "A new block is the last resort" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L75] | |
| 36 | 2 | The `roadkeep` skill is vendored | verified | "the roadkeep skill is a vendored copy" [freewilly@c1c2eaf:.gitignore#L2-L3] | |
| 37 | 2 | `window-chrome`: "Found by capturing the window and comparing, not by reasoning. Do not undo them" | verified | "Found by capturing the window and comparing, not by reasoning. Do not undo them" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L34] | |
| 38 | 2 | `window-chrome` requires a byte-identical PNG before and after | verified | "Always capture before and after" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L49]; "byte-identical" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L52-L60] | |
| 39 | 2 | `agent-budget.json` is 17.8 KB | corrected | `git cat-file -s c1c2eaf:agent-budget.json` = 17552 bytes | `agent-budget.json` is 17,552 bytes (17.6 KB) at the pin [freewilly@c1c2eaf:agent-budget.json] |
| 40 | 2 | `agent-budget.json` is the token budget for the agent-facing CLI output, read by `AgentBudgetTests.cs` | verified | "Ceilings on what the agent surface costs, read by AgentBudgetTests" [freewilly@c1c2eaf:agent-budget.json#L5]; the test locates the file [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/AgentBudgetTests.cs#L41] | |
| 41 | 2 | "a build that made a response more expensive fails … the commit that raises one says what the tokens bought" | verified | "so a build that made" [freewilly@c1c2eaf:agent-budget.json#L5] "a response more expensive fails instead of mentioning it" [freewilly@c1c2eaf:agent-budget.json#L6] (two JSON strings); "the commit that raises one says what the tokens bought" [freewilly@c1c2eaf:agent-budget.json#L7]. The text is in agent-budget.json, not in AgentBudgetTests.cs | |
| 42 | 2 | Tokens are estimated as chars/4 | verified | "characters / 4, rounded up" [freewilly@c1c2eaf:agent-budget.json#L15] | |
| 43 | 2 | Baseline task: 6 calls, 11,711 tokens | verified | [freewilly@c1c2eaf:agent-budget.json#L48-L49] | |
| 44 | 2 | Shaped surface: 4 calls, 812 tokens | verified | [freewilly@c1c2eaf:agent-budget.json#L83-L85] | |
| 45 | 2 | A future MCP head is capped at `maxTools: 6`, `maxSchemaTokens: 1100` | verified | [freewilly@c1c2eaf:agent-budget.json#L256-L257] | |
| 46 | 2 | `install-roadkeep.cmd` fixes the engine path because "Every distinct command path is a fresh authorization prompt" | verified | "Every distinct command path is a fresh authorization prompt" [freewilly@c1c2eaf:install-roadkeep.cmd#L12] | |
| 47 | 2 | and because of an ImportError from a half-edited checkout | verified | "ImportError from" [freewilly@c1c2eaf:install-roadkeep.cmd#L18]; "a half-edited working tree" [freewilly@c1c2eaf:install-roadkeep.cmd#L19] | |
| 48 | 2 | `89371b8` introduced it | verified | "vendor the engine into .roadkeep and always run that copy" [freewilly@89371b8]; its diff creates install-roadkeep.cmd | |
| 49 | 3 | The task prefix is DD | verified | [freewilly@c1c2eaf:roadkeep.toml#L1] | |
| 50 | 3 | Ledger: 276 shipped, 4 retired | verified | Of the lines of `git show c1c2eaf:docs/CHANGELOG.md`, 276 carry ✅ and 4 carry 🗑 [freewilly@c1c2eaf:docs/CHANGELOG.md] | |
| 51 | 3 | The roadmap is drained, with 8 empty blocks | verified | Blocks A to H with no task line under any [freewilly@c1c2eaf:docs/ROADMAP.md#L5-L19] | |
| 52 | 3 | 8 non-goals | verified | [freewilly@c1c2eaf:docs/ROADMAP.md#L21-L46] | |
| 53 | 3 | `docs/specs/` holds four "constitutions": DD23, DD33, DD34, DD40 | corrected | "constitution" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L6]; "constitution for the desktop surface" [freewilly@c1c2eaf:docs/specs/DD34-window-constitution.md#L6]; "constitution for the published surface" [freewilly@c1c2eaf:docs/specs/DD40-site-constitution.md#L6] | Four specs, of which three call themselves a constitution (DD23, DD34, DD40); DD33 is a decision record: "This document is the decision" [freewilly@c1c2eaf:docs/specs/DD33-mcp-is-a-second-head.md#L6] |
| 54 | 3 | DD23 is the agent-first spec with laws P1-P10 | verified | "P1 — The shell is the surface" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L67]; "P10 — Compose, don't fork" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L104] | |
| 55 | 3 | `docs/_preview/` is output only | verified | "A capture is a working artefact, never a source" [freewilly@c1c2eaf:.gitignore#L40]; ignored at [freewilly@c1c2eaf:.gitignore#L41] | |
| 56 | 4 | About 90 xUnit files, with fakes | verified | tests/FreeWilly.Preflight.Tests has 93 tracked files, 86 of which hold a Fact or Theory attribute (git grep at the pin); "xunit" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/FreeWilly.Preflight.Tests.csproj]; FakeDockerDaemon.cs, FakeMachine.cs and FakeWsl.cs are tracked there | |
| 57 | 4 | The Winwright desktop cases are outside the solution | verified | "not in FreeWilly.slnx" [freewilly@c1c2eaf:run-cases.cmd#L15]; the solution lists only the Preflight tests project [freewilly@c1c2eaf:FreeWilly.slnx] | |
| 58 | 4 | `PackagingTests.cs:272-330` (DD115) fails if `.claude/settings.json` loses the minimum tools or the guard hooks | verified | "no longer grants" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L302]; "no roadkeep guard is wired on" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L326]; the two tests span [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L272-L336] | |
| 59 | 4 | `AgentDiscoveryTests` guards the agent setup | corrected | "Shipping the surface includes shipping how it is found (DD32)" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/AgentDiscoveryTests.cs#L10] | It guards the product's shipped agent files (build/agent/SKILL.md and settings-snippet.json) and the absence of an MCP head, not the repository's `.claude/` setup [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/AgentDiscoveryTests.cs#L9-L17] |
| 60 | 4 | `PaletteTests` guards the agent setup | corrected | "One meaning, one declaration (DD34)." [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PaletteTests.cs#L8] | It guards the window palette, a rule the window-chrome skill states: "fails the build on any hex colour in any" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L25-L26] |
| 61 | 4 | CI `check.yml` builds, tests, publishes and runs the exe | verified | [freewilly@c1c2eaf:.github/workflows/check.yml#L43-L56]; [freewilly@c1c2eaf:.github/workflows/check.yml#L131-L141] | |
| 62 | 4 | `check.yml` runs one Winwright case | verified | "FullyQualifiedName~PreflightPage" [freewilly@c1c2eaf:.github/workflows/check.yml#L125-L129] | |
| 63 | 4 | `roadkeep.yml` runs lint | verified | "roadkeep lint" [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L14-L19] | |
| 64 | 4 | The engine install is checked only on a VM (`scripts/vm.ps1`) | verified | "It cannot verify the engine install." [freewilly@c1c2eaf:CONTRIBUTING.md#L34-L37]; [freewilly@c1c2eaf:.github/workflows/check.yml#L17-L20] | |
| 65 | 5 | 425 of 444 commits are conventional | verified | 425 of the 444 subjects of `git log --format=%s c1c2eaf` match type(scope): or type:; the other 19 are pull-request merges [freewilly@c1c2eaf] | |
| 66 | 5 | By type: feat 136, fix 107, docs 99, chore 46, test 22, refactor 9, ci 4 | corrected | The same count gives the seven figures as stated, plus style 1 and perf 1, which make the 425 | feat 136, fix 107, docs 99, chore 46, test 22, refactor 9, ci 4, style 1, perf 1 = 425 [freewilly@c1c2eaf] |
| 67 | 5 | Subjects follow `type(scope): DD<n> <behaviour sentence>` | verified | 325 of 444 subjects have DD and a number right after the colon, e.g. "DD112 a fold does not outlive the project it was set on" [freewilly@d01fcb3] | |
| 68 | 5 | Filing a task is its own commit | verified | "DD112-DD113 file what the container follow-ups turned up" [freewilly@c44801a] | |
| 69 | 5 | Bodies are generated bullets from `ai_commit.py` or hand prose | verified | "to write the body from the" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L33-L35]; bullets in [freewilly@646e121], prose in "Worth watching rather than fixed" [freewilly@ac7e7ec] | |
| 70 | 5 | Hand prose is used on important commits | inference | | |
| 71 | 5 | 17 Co-Authored-By trailers | verified | 17 commit messages in the pin's history carry one trailer each; e.g. "Co-Authored-By: Claude Opus 5" [freewilly@ac7e7ec] | |
| 72 | 5 | 12 commits authored by Claude came in via PR #1 from a `claude/…` branch (`7968cc5`) | verified | "alegauss/claude/bloco-h-roadmap-tmtjgk" [freewilly@7968cc5]; `git log --format=%an 7968cc5^1..7968cc5^2` lists 12 commits, all by Claude | |
| 73 | 5 | PR #1 came from a web session | inference | | |
| 74 | 6.1 | The harness rewrote `.claude/settings.json` mid-session, dropping fifteen entries, twice | verified | "Twice in one session fifteen entries vanished" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L277]; "dropping fifteen entries" [freewilly@ac7e7ec] | |
| 75 | 6.1 | The deletion rode into `46ec80f` (per `ac7e7ec`) | corrected | "the deletion rode into 46ec80f alongside DD112" [freewilly@ac7e7ec], but no commit 46ec80f exists in the repository | The deletion rode into `d01fcb3` (DD112), the parent of `ac7e7ec`, whose diff removes 15 lines from .claude/settings.json [freewilly@d01fcb3]; 46ec80f, named in the message, is not in the history of the pin |
| 76 | 6.1 | It led to the DD115 build test (`646e121`) | verified | "DD115 the committed agent configuration is guarded" [freewilly@646e121] | |
| 77 | 6.2 | Stage-everything commits sweep strays; DD117 was retired because the fix would touch a shared tool | verified | "the fix touches a commit tool every repository shares" [freewilly@c1c2eaf:docs/CHANGELOG.md#L201] | |
| 78 | 6.2 | Remedy: `.gitignore` for `__pycache__/` and `TestResults/` | verified | "run-commit.cmd stages" [freewilly@c1c2eaf:.gitignore#L43-L49] | |
| 79 | 6.3 | Lint was removed from CI (`cd630d6`) and restored (`714360e`) | verified | See rows 11 and 12: [freewilly@cd630d6], [freewilly@714360e] | |
| 80 | 6.3 | Drift "reached main unremarked" (`check.yml:12-15`) | verified | "drift arriving by any other route, which for a while reached" [freewilly@c1c2eaf:.github/workflows/check.yml#L12-L15] | |
| 81 | 6.3 | CONTRIBUTING was never updated | verified | `git log 714360e..c1c2eaf -- CONTRIBUTING.md` is empty, and the file still says "CI no longer does" [freewilly@c1c2eaf:CONTRIBUTING.md#L13-L14] | |
| 82 | 6.4 | Hand edits pass where the plugin is not loaded, so the launcher is committed | verified | "an agent falls back to editing ROADMAP.md by hand" [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L9-L13]; "the committed roadkeep-launch.py is how a cloud session gets the" [freewilly@c1c2eaf:.gitignore#L12-L15] | |
| 83 | 6.5 | Floating tool paths cost prompts and wrong versions, so the engine path is fixed | verified | "Which copy answers is not decidable by looking" [freewilly@c1c2eaf:install-roadkeep.cmd#L12-L19] | |
| 84 | 6.6 | Agents batch tasks unless forced not to, hence `/loop` and a `git status` check | verified | "is NOT permission to" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L20-L31] | |
| 85 | 6.7 | A commit without `-m` mislabels docs work | verified | "Without it the tool infers the message from the diff" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L17-L19] | |
| 86 | 6.8 | 207 em dashes, "two in every three sentences" (`0794e60`, DD184), which led to the repo writing skill | verified | "207 of them, and two in every three sentences" [freewilly@0794e60]; the same commit creates .claude/skills/ai-writing-freewilly/SKILL.md | |
| 87 | 6.9 | Typed counts go stale (`llms.txt` said 4 of 5), so counts are generated | verified | "llms.txt counted four window destinations against the five" [freewilly@0794e60]; "Counts and versions are generated, not written" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L97] | |
| 88 | 6.10 | Eye checks miss what capture comparison catches (`window-chrome` l.63-65) | corrected | "the test suite saw none of them" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L63-L65] | The source contrasts capture comparison with the test suite (L63-65) and with reasoning, not with eye checks: "Found by capturing the window and comparing, not by reasoning" [freewilly@c1c2eaf:.claude/skills/window-chrome/SKILL.md#L34] |
| 89 | 6.11 | A capture passed while photographing the guest's wallpaper (`c1c2eaf`), so the case now waits for a semantic signal | verified | "photographed the guest's WALLPAPER, and passed" [freewilly@c1c2eaf]; "the case now waits for the menu to report an entry before it copies anything" [freewilly@c1c2eaf] | |
| 90 | 6.11 | An unmeasured case is not a gate | verified | "a case nobody has run there is not a gate" [freewilly@c1c2eaf] | |
| 91 | 6.12 | The budget test failed for the wrong reason (`f514e11`, `ecaad33`, `bfa7d35`, `87cf631`) | corrected | "the budget gate that can go red for the wrong reason" [freewilly@f514e11]; "a second red run refutes the first" [freewilly@ecaad33]; "the budget records the 812 tokens the shaped task actually costs" [freewilly@bfa7d35]; "the shaped token figure stops depending on the machine" [freewilly@87cf631] | `f514e11` and `ecaad33` (DD64) record a gate that went red for the wrong reason, and `bfa7d35` (DD144) a recorded figure that left the gate red; `87cf631` (DD78) fixes the opposite defect, a band that let real growth pass: "response that grew by 100 tokens landed inside it silently" [freewilly@c1c2eaf:agent-budget.json#L109] |
| 92 | 6.12 | The remedy was deterministic fixtures and a ±15% size band | corrected | "Every figure here is asserted exactly (DD78)" [freewilly@c1c2eaf:agent-budget.json#L103]; the 0.15 tolerance [freewilly@c1c2eaf:agent-budget.json#L33-L35] was already in the file when it was created [freewilly@2f7b7c1] | The remedy was exact assertion of every figure, with machine reads and later the clock fed through a seam (DD78, DD178) [freewilly@c1c2eaf:agent-budget.json#L103-L111] [freewilly@c1c2eaf:agent-budget.json#L140-L141]; the ±15% tolerance bands only the baseline fixture sizes and dates from DD23 [freewilly@2f7b7c1] |
| 93 | 6.13 | An edit silently did not apply (DD95); a missing test was added and dead code deleted | verified | "An edit that silently did not apply" [freewilly@c1c2eaf:docs/CHANGELOG.md#L22]; "left the two helpers it replaced behind as dead code" [freewilly@c1c2eaf:docs/CHANGELOG.md#L22] | |
| 94 | 6.14 | Hand-maintained lists drift (`0731091`, DD100), replaced by reflection | verified | "replaces a hand-written list of verbs with a reflection-based approach" [freewilly@0731091] | |
| 95 | 6.15 | Wrong premises are retired, not edited: DD195, DD268, DD77, DD117 | corrected | All four are retired [freewilly@c1c2eaf:docs/CHANGELOG.md#L53] [freewilly@c1c2eaf:docs/CHANGELOG.md#L98] [freewilly@c1c2eaf:docs/CHANGELOG.md#L201] [freewilly@c1c2eaf:docs/CHANGELOG.md#L239], but not all for a wrong premise | Only DD195 (filed under a wrong heading) and DD268 ("Filed against the wrong writer") were retired as wrong filings [freewilly@c1c2eaf:docs/CHANGELOG.md#L98]; DD77 was superseded because DD86 made it moot [freewilly@c1c2eaf:docs/CHANGELOG.md#L239], and DD117 was abandoned as a decision against [freewilly@c1c2eaf:docs/CHANGELOG.md#L201] |
| 96 | 6.16 | MCP versus CLI was decided by Shio's measurement: CLI first, MCP capped | verified | "CLI first; MCP only if a shell-less client ever matters" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L120]; "Capped at six tools." [freewilly@c1c2eaf:docs/specs/DD33-mcp-is-a-second-head.md#L63] | |
| 97 | 6.16 | `DD33-mcp-is-a-second-head.md` says "~2 400 tokens across eleven tools" per turn | corrected | "2 400 tokens across eleven tools" [freewilly@c1c2eaf:docs/specs/DD33-mcp-is-a-second-head.md#L26-L27], preceded by "roughly", not "~" | The exact quote is in DD23: "~2 400 tokens across eleven tools" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L113]; DD33 says "Measured at roughly" [freewilly@c1c2eaf:docs/specs/DD33-mcp-is-a-second-head.md#L26] |
| 98 | 6.17 | A "binding" law (DD23 P10) was overridden by `4575583` without amending the spec | inference | Consistent with the sources: "It is not a second Docker CLI and never grows a" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L104-L106] still stands at the pin, and "do compose up is the first verb that creates" [freewilly@4575583] | |
| 99 | 7 | 444 commits | verified | `git rev-list --count c1c2eaf` = 444 | |
| 100 | 7 | History runs from 2026-08-12 (`acc7fc1`) to 2026-09-17 (`c1c2eaf`) | verified | `git rev-list --max-parents=0 c1c2eaf` = acc7fc1, dated 2026-08-12 [freewilly@acc7fc1]; [freewilly@c1c2eaf] | |
| 101 | 7 | Busiest day 2026-08-14, with 92 commits | verified | Grouping `git log --format=%ad --date=short c1c2eaf` by day gives 92 on 2026-08-14, next 63 on 2026-08-29 | |
| 102 | 7 | 4 skills in 6 files | verified | See row 28 | |
| 103 | 7 | 1 hook script on 3 events | verified | [freewilly@c1c2eaf:.claude/settings.json#L73-L107] | |
| 104 | 7 | 1 MCP server | verified | "mcpServers" [freewilly@c1c2eaf:.mcp.json], declaring only roadkeep | |
| 105 | 7 | 4 specs | verified | `git ls-tree --name-only c1c2eaf docs/specs/` lists 4 files | |
| 106 | 7 | 373 tracked files | verified | `git ls-tree -r --name-only c1c2eaf` lists 373 paths | |
