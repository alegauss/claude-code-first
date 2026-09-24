# polyweave: field notes (preliminary, unverified)

Extracted 2026-09-24 at HEAD `6d1c136`; the working tree carried uncommitted changes
(PW106 in progress, PW135/PW141, a sixth non-goal).

## 1. Instruction surface

`CLAUDE.md` 63 lines / 3,361 B, created in `26bd699`, last touched `e26bd7c`. Preamble
(what, gates, site rebuild) and five sections. Rules: gates are `python -m pytest` and
`python -m ruff check .` (L7-9); a ship is followed by `npm run build && npm test` in
`site/` with the regenerated module in the same commit (L11-14); "**The caller is an agent
in a terminal, not a person at a screen.**" (L18) — a feature "that needs a GUI, a second
round trip or a source read to use is a feature that has not landed" (L20-21); Cottony
named as the evidence source (L25-37); spec says *what*, a ≤250-word rationale says *why*
(L43-45); governed docs: "A hand edit is refused — call the CLI" (L52-53); "nothing here
spends money on an agent's own judgement" (L57-58); one local commit per task, staged by
path, never pushed, `run-commit.cmd -m` (L62-63).

Drift: `run-commit.cmd` is referenced but not in the repo (user-level tool); CLAUDE.md
says "Five constraints" while the working-tree roadmap lists six non-goals.

## 2. `.claude/`

- `settings.json`: allow `Bash(*)`; MCP roadkeep; plugin `roadkeep@alegauss`; hooks:
  SessionStart guard, PreToolUse `Write` → `no-clobber.py`, PreToolUse
  `Edit|MultiEdit|NotebookEdit|Write|Bash` → guard, Stop guard (30 s).
- `hooks/no-clobber.py` (114 lines): refuses Write over an existing non-empty file, exit 2,
  names Edit. Rationale: in pportal Write "destroyed roughly 700 lines across four
  occasions — one of them committed before anyone noticed, because the tool's own report is
  what made the loss invisible". Generated trees exempt. "Never block a turn"; "The exit
  code is the protocol"; strips the PowerShell 5.1 BOM (L63-66).
- `hooks/roadkeep-launch.py` (590 lines): committed launcher because Claude Code on the
  web has no `/plugin` (L6-14); modes guard/mcp/forward; records RK1189 and RK1116.
- `agents/scanner.md` (138 lines; Read/Grep/Glob; sonnet; effort high; read-only; output
  `path:line | issue | why it matters | how to reproduce`; does not re-report what gates
  catch; "An invented finding costs more than a missed one").
  `agents/verifier.md` (166 lines; + Bash; opus; xhigh; FINDINGS mode CONFIRMED / FALSE
  POSITIVE / UNVERIFIABLE; ROADMAP mode STILL VALID / ALREADY DONE / OUTDATED / NEEDS
  REWORDING; never writes, never spends money). (inference) cheap scan, strong verify.
- `skills/audit/SKILL.md` (174 lines): gates as baseline → one scanner per roadmap block in
  parallel (+ specs, wiring) → dedupe → verifier FINDINGS → verifier ROADMAP → reconcile
  only through roadkeep verbs; "a reconciled backlog, not a patch".
- `skills/roadkeep/` vendored (SKILL 164, asking 295, writing 607).

## 3. Docs

roadkeep: prefix PW, files roadmap/changelog/improvements/deferred. Ledger 104 ✅, 0 🗑;
47 rationale sections; `DEFERRED.md` 8 ⏸ lines ("set aside (a person's judgement)").
`docs/specs/` 13 ungoverned files; `specs/README.md` indexes each spec to the lines it
binds; "TOML for documents a person authors or reads … JSON for records a machine writes";
"the first implementation that disagrees with one is evidence about the spec, not only
about the code"; specs close with "Deliberately not here".

## 4. Gates

pytest (~1,272 test functions) + ruff; real-artefact fixtures from Cottony in LFS
(`0cacaad`, `a7b72ba`). CI: `roadkeep.yml` lint ("that exit code is the whole contract"),
`site.yml` build gate. pytest and ruff are **not** in CI (inference). 16 bodies end with a
`Gates:` trailer ("Gates: ruff clean, 1161 tests (6 new), site 30/30.").

## 5. Commits

Conventional, scope, id in title (`feat(search): … (PW105)`); ", with PWn filed";
"(PWn part)"; deferrals as `docs:`; long measured prose bodies; one author, no
Co-Authored-By. First commits used generic bullet bodies, then narrative after PW1.

## 6. Learnings

1. Write silently destroys files → hook, not rule.
2. Plugin hooks absent on the web → committed launcher.
3. A hook that fails closed is worse than none (RK1189).
4. First diagnosis wrong: em-dash corruption blamed on cp1252, real cause the reader's
   UTF-8 decode; PW71's fix reverted; symptom kept, why and design amended (`f203b0a`).
5. Designs falsified while implementing (`7024e7e`; `871a15b`: parallel 1.09 s vs serial
   0.95 s on cheap rungs, 3.7x only on the last).
6. Inherited folklore stale: EXACT solver claim not reproduced on Blender 5.2.1
   (`963b652`).
7. Two defaults for one number (`32c2f35`, 0.02 vs 0.0) → one home, refuse missing.
8. "Safe" default pointed the wrong way (`1e3b8c7`).
9. Synthetic thresholds fail on real data (`0cacaad`: IoU 0.4343 vs 0.8) → real fixtures.
10. Plausible-but-wrong constructions (`f73f124`) → read the declaration back in words.
11. Same name, different meaning (`6fec5ff`, `ab4835e`, `7024e7e`) → refuse with near
    match; units on values.
12. An agent must not self-certify a look; some work needs a person or absent hardware
    (`DEFERRED.md`; `113f220`; `5a3a26c` → `0a82ee0`) → deferred store, Block J.
13. A baseline recorded after the answer is a justification (`8917a7f`, `e26bd7c`,
    `d2ae97c`) → append-only ledger; PW114-PW116.
14. Parsing another tool's format locally drifts (`642a88c`) → ask the tool.
15. Discoverability of the agent surface (PW124-PW133: "one of 118 remedy rows had ever
    been run"; "six silent drops in twelve calls"; nothing tells a consumer the plugin
    exists; PW129 nothing bounds what `describe` costs).
16. A stage-everything commit tool catches stray files (PW135: "how Shio committed
    sh545.log").
17. Understated premise corrected by shipping a part (`5eb1a8e`).

## 7. Metrics

132 commits, 2026-09-22 (`26bd699`) → 2026-09-24; 59/54/19 per day. 2 skills, 2 agents,
2 hook scripts (4 registrations), 1 MCP server; agent surface 2,248 lines. ~105 lines
shipped in 3 days (inference).
