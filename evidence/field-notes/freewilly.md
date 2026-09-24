# freewilly: field notes (preliminary, unverified)

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
