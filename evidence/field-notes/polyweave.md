# polyweave: field notes (verified)

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

## Verification

Checked against `6d1c136` on 2026-09-24. 100 claims: 81 verified, 11 corrected, 1 refuted, 5 outside the pin, 2 inference. Error rate 12.9%.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | intro | The working tree carried uncommitted changes (PW106 in progress, PW135/PW141, a sixth non-goal) | outside the pin | Uncommitted work is not in `6d1c136`; the highest task id in its docs is PW122 (`git grep -h -o -E 'PW[0-9]+' 6d1c136 -- docs`) | |
| 2 | 1 | CLAUDE.md is 63 lines and 3,361 bytes | verified | `git cat-file -s 6d1c136:CLAUDE.md` = 3361; 63 lines, last one [polyweave@6d1c136:CLAUDE.md#L63] | |
| 3 | 1 | CLAUDE.md was created in 26bd699 | verified | `git log --diff-filter=A --format=%h 6d1c136 -- CLAUDE.md` = 26bd699 [polyweave@26bd699] | |
| 4 | 1 | CLAUDE.md was last touched in e26bd7c | corrected | e26bd7c changes only docs/DEFERRED.md, docs/ROADMAP.md, roadkeep.toml and site/src/lib/roadmap.generated.ts [polyweave@e26bd7c] | Last touched in 3771c41 (2026-09-22): `git log -1 --format=%h 6d1c136 -- CLAUDE.md` = 3771c41 [polyweave@3771c41] |
| 5 | 1 | A preamble (what, gates, site rebuild) and five sections | verified | Preamble [polyweave@6d1c136:CLAUDE.md#L1-L14]; five level-2 headings at L16, L23, L39, L50, L60, e.g. "One task, one commit" [polyweave@6d1c136:CLAUDE.md#L60] | |
| 6 | 1 | The gates are python -m pytest and python -m ruff check . (L7-9) | verified | "and the gates are" [polyweave@6d1c136:CLAUDE.md#L7-L9] | |
| 7 | 1 | A ship is followed by npm run build and npm test in site/, with the regenerated module in the same commit (L11-14) | verified | "the regenerated module goes in the same commit" [polyweave@6d1c136:CLAUDE.md#L11-L14] | |
| 8 | 1 | Quote of the bold caller rule (L18) | verified | "The caller is an agent in a terminal, not a person at a screen." [polyweave@6d1c136:CLAUDE.md#L18] | |
| 9 | 1 | Quote of the not-landed rule (L20-21) | verified | "that needs a GUI, a second round trip or a source read to use is a feature that has not landed" [polyweave@6d1c136:CLAUDE.md#L20-L21] | |
| 10 | 1 | Cottony is named as the evidence source (L25-37) | verified | "Nearly every symptom in the backlog was measured in" [polyweave@6d1c136:CLAUDE.md#L25-L37] | |
| 11 | 1 | The spec says what; a rationale capped at 250 words says why (L43-45) | verified | "is capped at 250 words and says" [polyweave@6d1c136:CLAUDE.md#L43-L45] | |
| 12 | 1 | Governed docs: quote on hand edits (L52-53) | verified | "A hand edit is refused — call the CLI" [polyweave@6d1c136:CLAUDE.md#L52-L53] | |
| 13 | 1 | Quote on spending money (L57-58) | verified | "nothing here spends money on an agent's own judgement" [polyweave@6d1c136:CLAUDE.md#L57-L58] | |
| 14 | 1 | One local commit per task, staged by path, never pushed, via run-commit.cmd -m (L62-63) | verified | "staged by path, never pushed" [polyweave@6d1c136:CLAUDE.md#L62-L63] | |
| 15 | 1 | run-commit.cmd is referenced but is not in the repository | verified | Referenced at [polyweave@6d1c136:CLAUDE.md#L63] and [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L161]; `git ls-tree -r --name-only 6d1c136` lists no such file | |
| 16 | 1 | run-commit.cmd is a user-level tool | outside the pin | Nothing at the pin says where the tool lives; the claim rests on the user's own setup, not on the repository | |
| 17 | 1 | CLAUDE.md says 'Five constraints' | verified | "Five constraints bind this project" [polyweave@6d1c136:CLAUDE.md#L57] | |
| 18 | 1 | The working-tree roadmap lists six non-goals | outside the pin | At the pin the roadmap lists five non-goals, which agrees with CLAUDE.md [polyweave@6d1c136:docs/ROADMAP.md#L107-L122] | |
| 19 | 2 | settings.json allows Bash(*) | verified | "Bash(*)" [polyweave@6d1c136:.claude/settings.json#L5] | |
| 20 | 2 | settings.json enables the roadkeep MCP server | verified | [polyweave@6d1c136:.claude/settings.json#L11], declared in [polyweave@6d1c136:.mcp.json] | |
| 21 | 2 | settings.json enables the plugin roadkeep@alegauss | verified | "roadkeep@alegauss" [polyweave@6d1c136:.claude/settings.json#L59] | |
| 22 | 2 | Hooks: SessionStart guard; PreToolUse Write to no-clobber.py; PreToolUse on Edit, MultiEdit, NotebookEdit, Write, Bash to guard; Stop guard with a 30 s timeout | verified | [polyweave@6d1c136:.claude/settings.json#L13-L52]; the Stop timeout is 30 at [polyweave@6d1c136:.claude/settings.json#L52] | |
| 23 | 2 | hooks/no-clobber.py is 114 lines | verified | `git show 6d1c136:.claude/hooks/no-clobber.py` has 114 lines [polyweave@6d1c136:.claude/hooks/no-clobber.py#L114] | |
| 24 | 2 | no-clobber refuses Write over an existing non-empty file, exits 2, names Edit | verified | "Refuse" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L1]; "DENY = 2" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L43]; "So this refuses the call and names" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L11] | |
| 25 | 2 | Rationale quote: pportal Write destroyed roughly 700 lines across four occasions | corrected | The source writes a double hyphen where the note has an em dash [polyweave@6d1c136:.claude/hooks/no-clobber.py#L4-L6] | Verbatim: "destroyed roughly 700 lines across four occasions -- one of them committed before anyone noticed, because the tool's own report is what made the loss invisible" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L5-L6] |
| 26 | 2 | Generated trees are exempt | verified | "Trees whose contents are generated, vendored or scratch" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L29-L41] | |
| 27 | 2 | Rule quote: Never block a turn | verified | "Never block a turn." [polyweave@6d1c136:.claude/hooks/no-clobber.py#L16] | |
| 28 | 2 | Rule quote: The exit code is the protocol | verified | "The exit code is the protocol." [polyweave@6d1c136:.claude/hooks/no-clobber.py#L19] | |
| 29 | 2 | no-clobber strips the PowerShell 5.1 BOM at L63-66 | corrected | L63-66 are the except branch and the tool_name check [polyweave@6d1c136:.claude/hooks/no-clobber.py#L63-L66] | The BOM strip is at L59-62: "PowerShell 5.1 prepends one when" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L59-L62] |
| 30 | 2 | hooks/roadkeep-launch.py is 590 lines | verified | `git show 6d1c136:.claude/hooks/roadkeep-launch.py` has 590 lines [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L590] | |
| 31 | 2 | The launcher is committed because Claude Code on the web has no /plugin (L6-14) | verified | "Claude Code on the web has no" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L6-L14] | |
| 32 | 2 | The launcher's modes are guard, mcp and forward | verified | "return _forward(argv)" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L578-L586] | |
| 33 | 2 | The launcher records RK1189 and RK1116 | verified | "reported from (RK1189)" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L55]; "forwarded to that engine (RK1116)" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L70] | |
| 34 | 2 | scanner.md is 138 lines; tools Read, Grep, Glob; model sonnet; effort high | verified | "tools: Read, Grep, Glob" [polyweave@6d1c136:.claude/agents/scanner.md#L4-L6]; 138 lines [polyweave@6d1c136:.claude/agents/scanner.md#L138] | |
| 35 | 2 | The scanner is read-only | verified | "You fix nothing, edit nothing and run nothing" [polyweave@6d1c136:.claude/agents/scanner.md#L9-L10] | |
| 36 | 2 | The scanner's output is one line per finding: path:line, issue, why it matters, how to reproduce | verified | [polyweave@6d1c136:.claude/agents/scanner.md#L14-L18] | |
| 37 | 2 | The scanner does not re-report what the gates catch | verified | "do not re-report it" [polyweave@6d1c136:.claude/agents/scanner.md#L30] | |
| 38 | 2 | Quote on invented findings | verified | "An invented finding costs more than a missed one" [polyweave@6d1c136:.claude/agents/scanner.md#L10-L11] | |
| 39 | 2 | verifier.md is 166 lines; adds Bash; model opus; effort xhigh | verified | "tools: Read, Grep, Glob, Bash" [polyweave@6d1c136:.claude/agents/verifier.md#L4-L6]; 166 lines [polyweave@6d1c136:.claude/agents/verifier.md#L166] | |
| 40 | 2 | FINDINGS mode: CONFIRMED, FALSE POSITIVE, UNVERIFIABLE; ROADMAP mode: STILL VALID, ALREADY DONE, OUTDATED, NEEDS REWORDING | verified | "STILL VALID, ALREADY DONE, OUTDATED or NEEDS REWORDING" [polyweave@6d1c136:.claude/agents/verifier.md#L3] | |
| 41 | 2 | The verifier never writes | verified | "Modify no file." [polyweave@6d1c136:.claude/agents/verifier.md#L14] | |
| 42 | 2 | The verifier never spends money | verified | "And never a call that spends." [polyweave@6d1c136:.claude/agents/verifier.md#L25] | |
| 43 | 2 | (inference) Cheap scan, strong verify | inference | Consistent with sonnet for the scanner and opus for the verifier [polyweave@6d1c136:.claude/agents/scanner.md#L5] [polyweave@6d1c136:.claude/agents/verifier.md#L5]; no file states the principle | |
| 44 | 2 | skills/audit/SKILL.md is 174 lines | verified | `git show 6d1c136:.claude/skills/audit/SKILL.md` has 174 lines [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L174] | |
| 45 | 2 | Audit pipeline: gates as baseline, one scanner per roadmap block in parallel plus specs and wiring rows, dedupe, verifier FINDINGS, verifier ROADMAP, reconcile only through roadkeep | verified | "The gates first — the baseline" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L17]; "Partition by the roadmap's blocks" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L50]; [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L73-L82]; "Deduplicate" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L84]; "in FINDINGS mode" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L90]; "in ROADMAP mode" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L99]; "Reconcile, through roadkeep only" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L113] | |
| 46 | 2 | Quote: a reconciled backlog, not a patch | verified | "a reconciled backlog, not a patch" [polyweave@6d1c136:.claude/skills/audit/SKILL.md#L7-L8] | |
| 47 | 2 | skills/roadkeep/ is vendored: SKILL 164, asking 295, writing 607 lines | verified | `git show 6d1c136:<path>` has 164, 295 and 607 lines [polyweave@6d1c136:.claude/skills/roadkeep/SKILL.md#L164] [polyweave@6d1c136:.claude/skills/roadkeep/asking.md#L295] [polyweave@6d1c136:.claude/skills/roadkeep/writing.md#L607] | |
| 48 | 3 | roadkeep prefix PW; files roadmap, changelog, improvements, deferred | verified | "prefix = " [polyweave@6d1c136:roadkeep.toml#L1]; "deferred = " [polyweave@6d1c136:roadkeep.toml#L10-L14] | |
| 49 | 3 | The ledger holds 104 shipped (✅) lines | corrected | `git grep -c ✅ 6d1c136 -- docs/CHANGELOG.md` = 103 [polyweave@6d1c136:docs/CHANGELOG.md] | 103 ✅ lines in the ledger at the pin [polyweave@6d1c136:docs/CHANGELOG.md] |
| 50 | 3 | The ledger holds 0 retired (🗑) lines | verified | `git grep -c 🗑 6d1c136 -- docs` finds no match | |
| 51 | 3 | 47 rationale sections | corrected | `git grep -c '^### §PW' 6d1c136 -- docs/IMPROVEMENTS.md` = 26 [polyweave@6d1c136:docs/IMPROVEMENTS.md] | 26 rationale sections, §PW118 to §PW113 in file order [polyweave@6d1c136:docs/IMPROVEMENTS.md#L13] [polyweave@6d1c136:docs/IMPROVEMENTS.md#L529] |
| 52 | 3 | DEFERRED.md holds 8 ⏸ lines | verified | `git grep -c ⏸ 6d1c136 -- docs/DEFERRED.md` = 8 [polyweave@6d1c136:docs/DEFERRED.md#L19-L26] | |
| 53 | 3 | The deferred lines read 'set aside (a person's judgement)' | corrected | PW36 gives a different reason [polyweave@6d1c136:docs/DEFERRED.md#L19] | 7 of the 8 read "set aside (a person's judgement)" [polyweave@6d1c136:docs/DEFERRED.md#L20-L26]; PW36 reads "set aside (Nobody has recorded that baseline yet.)" [polyweave@6d1c136:docs/DEFERRED.md#L19] |
| 54 | 3 | docs/specs/ holds 13 ungoverned files | verified | `git ls-tree --name-only 6d1c136 docs/specs/` lists 13 files; "Nothing governs them" [polyweave@6d1c136:docs/specs/README.md#L8] | |
| 55 | 3 | specs/README.md indexes each spec to the lines it binds | verified | "Lines it binds" [polyweave@6d1c136:docs/specs/README.md#L20-L33] | |
| 56 | 3 | Quote on TOML for documents and JSON for records | verified | "TOML for documents a person authors or reads" [polyweave@6d1c136:docs/specs/README.md#L37]; "JSON for records a machine writes" [polyweave@6d1c136:docs/specs/README.md#L38] | |
| 57 | 3 | Quote on the first disagreeing implementation | verified | "the first implementation that disagrees with one is evidence about the spec, not only about the code" [polyweave@6d1c136:docs/specs/README.md#L16-L17] | |
| 58 | 3 | Specs close with 'Deliberately not here' | corrected | Of the 13 files only context.md closes that way; most end otherwise, e.g. "Conventions" [polyweave@6d1c136:docs/specs/geometry.md] | Only context.md has "Deliberately not here" [polyweave@6d1c136:docs/specs/context.md#L41]; README.md has "Deliberately not specced yet" [polyweave@6d1c136:docs/specs/README.md#L44] and acceptance-spec.md "What this file deliberately cannot say" [polyweave@6d1c136:docs/specs/acceptance-spec.md#L173] |
| 59 | 4 | About 1,272 pytest test functions | corrected | `git grep -h -E 'def test_' 6d1c136 -- tests` yields 1,266 lines | 1,266 test functions under tests/ at the pin |
| 60 | 4 | Real-artefact fixtures from Cottony, stored in LFS (0cacaad, a7b72ba) | verified | "LFS was activated properly here" [polyweave@0cacaad]; "route mesh and capture binaries through LFS" [polyweave@a7b72ba] | |
| 61 | 4 | CI roadkeep.yml runs lint; quote on the exit code | verified | "exit code is the whole contract" [polyweave@6d1c136:.github/workflows/roadkeep.yml#L4]; "name: roadkeep lint" [polyweave@6d1c136:.github/workflows/roadkeep.yml#L15] | |
| 62 | 4 | CI site.yml is a build gate | verified | "The gate is the build" [polyweave@6d1c136:.github/workflows/site.yml#L7] | |
| 63 | 4 | (inference) pytest and ruff are not in CI | verified | `git grep -n -e pytest -e ruff 6d1c136 -- .github` finds no match; "so this is the whole CI" [polyweave@6d1c136:.github/workflows/site.yml#L1] | |
| 64 | 4 | 16 commit bodies end with a Gates: trailer | verified | `git log 6d1c136 --grep=Gates:` finds 18 commits; in 16 the last non-blank body line begins with Gates: (in f203b0a it ends a sentence line, in 898d788 it is mid-body) | |
| 65 | 4 | Example trailer quote | verified | "Gates: ruff clean, 1161 tests (6 new), site 30/30." [polyweave@fae7981] | |
| 66 | 5 | Titles are conventional, with a scope and the id, e.g. feat(search) ending (PW105) | verified | All 132 titles in `git log 6d1c136 --format=%s` open with a conventional type, 108 with a scope, 122 name a PW id; "feat(search): search one rig against a whole family and name the conflict (PW105)" [polyweave@6d1c136] | |
| 67 | 5 | Titles use ', with PWn filed' | verified | 18 titles in `git log 6d1c136 --format=%s` carry it; "(PW1), with PW37 filed" [polyweave@8d1c9ab] | |
| 68 | 5 | Titles use '(PWn part)' | verified | 13 titles carry it; "(PW56 part)" [polyweave@5eb1a8e] | |
| 69 | 5 | Deferrals are committed as docs: | verified | All 6 'set aside' titles are docs:, e.g. "docs: set the port aside until somebody records what it replaces (PW36)" [polyweave@e26bd7c] | |
| 70 | 5 | Bodies are long, measured prose | verified | e.g. "Interpreter start is 0.85s" [polyweave@871a15b] | |
| 71 | 5 | One author | verified | `git log 6d1c136 --format=%an` gives Alexandre Oliveira for all 132 commits | |
| 72 | 5 | No Co-Authored-By | verified | `git log 6d1c136 -i --grep=co-authored-by` finds no commit | |
| 73 | 5 | The first commits used generic bullet bodies, then narrative after PW1 | corrected | Bullet bodies also appear after PW1: [polyweave@8d762a2] [polyweave@3771c41] [polyweave@91937d4] | The four commits before PW1 have bullet bodies [polyweave@26bd699] [polyweave@2a251b7] [polyweave@031af19] [polyweave@c45f7b3]; from PW1 [polyweave@8d1c9ab] bodies are narrative, except three later bullet bodies (8d762a2, 3771c41, 91937d4) |
| 74 | 6 | L1: Write silently destroys files, so a hook, not a rule | verified | "which is why this is a hook" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L96-L97]; "reports" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L3] | |
| 75 | 6 | L2: plugin hooks are absent on the web, so a committed launcher | verified | "This file is committed to the adopting repository" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L9-L17] | |
| 76 | 6 | L3: a hook that fails closed is worse than none (RK1189) | corrected | RK1189 is the MCP server standing down and reading as a crash, not a hook failing closed: "standing down there was the defect this was reported from (RK1189)" [polyweave@6d1c136:.claude/hooks/roadkeep-launch.py#L54-L59] | The worse-than-none rule is in no-clobber.py and carries no RK id: "A hook that denies on its own bug is worse than no hook" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L16-L18] |
| 77 | 6 | L4: em-dash corruption blamed on cp1252; the real cause was the reader's UTF-8 decode | verified | "What reads the pipe decodes UTF-8" [polyweave@f203b0a] | |
| 78 | 6 | L4: PW71's fix reverted | verified | "The ASCII semicolon PW71 put in that sentence an hour ago is reverted" [polyweave@f203b0a] | |
| 79 | 6 | L4: symptom kept, why and design amended (f203b0a) | verified | "kept its symptom, which was accurate, and had its why amended and its design rewritten" [polyweave@f203b0a] | |
| 80 | 6 | L5: a design falsified while implementing (7024e7e) | verified | "measuring it is what settled the line the other way" [polyweave@7024e7e] | |
| 81 | 6 | L5: 871a15b measured parallel 1.09 s against serial 0.95 s on cheap rungs, 3.7x only on the last | verified | "0.95s serial vs 1.09s parallel" [polyweave@871a15b]; "3.7x" [polyweave@871a15b]; the pair is the sphere rung, and preview also loses | |
| 82 | 6 | L5: 871a15b is a design falsified while implementing | refuted | The measurement confirmed the design: "Which is what the design predicted" [polyweave@871a15b] | |
| 83 | 6 | L6: the EXACT solver claim did not reproduce on Blender 5.2.1 (963b652) | verified | "That does not reproduce on Blender 5.2.1" [polyweave@963b652] | |
| 84 | 6 | L7: two defaults for one number (0.02 vs 0.0), then one home and a refusal when missing (32c2f35) | verified | "was 0.02 in the config defaults and 0.0" [polyweave@32c2f35]; "Config.tolerances() is the one home now" [polyweave@32c2f35] | |
| 85 | 6 | L8: a 'safe' default pointed the wrong way (1e3b8c7) | verified | "the safe way to be wrong" [polyweave@1e3b8c7]; "It is backwards" [polyweave@1e3b8c7] | |
| 86 | 6 | L9: synthetic thresholds fail on real data, IoU 0.4343 vs 0.8, so real fixtures (0cacaad) | verified | "silhouette IoU of 0.4343" [polyweave@0cacaad]; "The synthetic tests clear 0.8" [polyweave@0cacaad] | |
| 87 | 6 | L10: plausible-but-wrong constructions, so read the declaration back in words (f73f124) | verified | "looked entirely reasonable while being written" [polyweave@f73f124]; "read a shape back in words before building it" [polyweave@f73f124] | |
| 88 | 6 | L11: same name, different meaning (6fec5ff, ab4835e, 7024e7e), answered by refusal with a near match and units on values | corrected | 6fec5ff is about names the renderer lacks: "neither of which the renderer has" [polyweave@6fec5ff]; the same-name case is not refused: "This does not refuse the mistake and does not claim to" [polyweave@7024e7e] | Same name, different meaning is ab4835e and 7024e7e: "Three more constants are worse than missing" [polyweave@ab4835e], answered by units on values, "rig.UNITS holds it" [polyweave@7024e7e]; the near-match refusal answers an absent name, "near match named" [polyweave@6fec5ff] |
| 89 | 6 | L12: some work needs a person or absent hardware (DEFERRED.md; 113f220; 5a3a26c then 0a82ee0), so a deferred store and Block J | verified | "a call for somebody looking at" [polyweave@113f220]; "Godot is not installed on this machine" [polyweave@5a3a26c]; "now that there is a Godot" [polyweave@0a82ee0]; "That needed a deferred store" [polyweave@e26bd7c]; "A bar a person sets once" [polyweave@6d1c136:docs/DEFERRED.md#L30] | |
| 90 | 6 | L13: a baseline recorded after the answer is a justification (8917a7f, e26bd7c, d2ae97c), so an append-only ledger; PW114-PW116 | verified | "a baseline recorded once the answer is known is not a baseline but a justification" [polyweave@8917a7f]; "the ledger is append-only" [polyweave@8917a7f]; "a baseline recorded once the answer is known is a justification" [polyweave@e26bd7c]; "the hand search it replaces was never timed" [polyweave@d2ae97c]; §PW114-§PW116 at [polyweave@6d1c136:docs/IMPROVEMENTS.md#L299-L350] | |
| 91 | 6 | L14: parsing another tool's format locally drifts, so ask the tool (642a88c) | verified | "so the answer is asked for" [polyweave@642a88c] | |
| 92 | 6 | L15: discoverability quotes from PW124-PW133 | outside the pin | No PW id above PW122 and neither quote occurs at the pin (`git grep -n 'six silent drops' 6d1c136` finds nothing) | |
| 93 | 6 | L16: PW135 on a stage-everything commit tool and sh545.log | outside the pin | `git grep -n sh545 6d1c136` finds nothing; PW135 is not at the pin | |
| 94 | 6 | L17: an understated premise corrected by shipping a part (5eb1a8e) | verified | "which is a sharper version of the symptom than the line stated" [polyweave@5eb1a8e] | |
| 95 | 7 | 132 commits | verified | `git rev-list --count 6d1c136` = 132 | |
| 96 | 7 | From 2026-09-22 (26bd699) to 2026-09-24 | verified | 26bd699 is the root, 2026-09-22 [polyweave@26bd699]; the pin is dated 2026-09-24 [polyweave@6d1c136] | |
| 97 | 7 | 59, 54 and 19 commits per day | verified | `git log 6d1c136 --format=%ad --date=short` counted per day: 59 on 09-22, 54 on 09-23, 19 on 09-24 | |
| 98 | 7 | 2 skills, 2 agents, 2 hook scripts (4 registrations), 1 MCP server | verified | `git ls-tree -r --name-only 6d1c136 .claude` lists skills audit and roadkeep, agents scanner and verifier, hooks no-clobber.py and roadkeep-launch.py; four hook entries [polyweave@6d1c136:.claude/settings.json#L13-L52]; one server [polyweave@6d1c136:.mcp.json] | |
| 99 | 7 | The agent surface is 2,248 lines | verified | The eight files under .claude/ other than settings.json total 114 + 590 + 138 + 166 + 174 + 164 + 295 + 607 = 2,248 lines | |
| 100 | 7 | (inference) About 105 lines shipped in 3 days | inference | The ledger holds 103 ✅ lines at the pin (row 49) [polyweave@6d1c136:docs/CHANGELOG.md] | |
