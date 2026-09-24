# roadkeep: field notes (preliminary, unverified)

Extracted 2026-09-24 at HEAD `91754240`. Caveat: the working tree held an uncommitted,
staged merge of `gui/` (RK1697, 564 files); nothing under `gui/` was yet in history.

## 1. Instruction surface

- `.claude/CLAUDE.md` (10 lines, 77 words) is a pointer: "All project guidelines … are in
  the shared agents file: `@../agents.md`". It lives under `.claude/` because the repo is
  the plugin, and a root CLAUDE.md ships in the plugin payload (RK323,
  `docs/CHANGELOG.md:1028`). Budgeted: `".claude/CLAUDE.md" = { lines = 12, bytes = 800 }`
  in `roadkeep.toml [budgets]`.
- `agents.md` (113 lines, 1,120 words) is the one every-turn file; budget
  `{ lines = 125, bytes = 8400 }` (`roadkeep.toml:249`), enforced by the gate. 106 commits
  touch it. Sections: preamble with the measured problem (Shio: "92 roadmap lines averaging
  142 words", "agents.md at 186 KB"; "*The saving is the analysis, not the characters.*");
  six laws (L16-27: "a change breaking one is wrong even if requested"; L1 "Schema enforced
  where the text is created; lint is only the backstop"; L4 "The tool never writes prose";
  L5 "Query instead of read"); layout index with no task numbers, held against `src/` by a
  test; conformance fixture ("roadkeep lint must pass on docs/"); the write path and the
  build/commit rules delegated to skills ("nothing here repeats it"); binding non-goals
  ("What loads every turn is only what a turn touching no governed file needs").

## 2. `.claude/` and plugin distribution

- Committed: `.claude/CLAUDE.md`, `.claude/settings.json` (181 B: `enabledMcpjsonServers`,
  one additional directory; no hooks, no allow rules), `.claude/skills/roadkeep-dev/SKILL.md`
  (trigger words: pytest, commit, stage, heredoc, version bump, run-commit, ship, file a
  task; "Trigger-loaded, and that is the whole reason it is a file (RK23, RK1136)").
- `.claude/settings.local.json` (ignored globally): `defaultMode: bypassPermissions`,
  `skipDangerousModePermissionPrompt: true`, blanket allow. (inference) Governance rests on
  hooks and the gate, not on permissions.
- The repo is the plugin; "a push to main is the release" (`gate.yml`).
  `.claude-plugin/plugin.json` v0.2.491; `marketplace.json` (RK26); plugin MCP in
  `.claude-plugin/mcp.json` vs checkout MCP in `.mcp.json` (split after RK81: "The MCP
  server is declared and no tool reaches the client").
- `hooks/hooks.json`: `roadkeep.py guard` on SessionStart (10 s), PreToolUse
  `Edit|MultiEdit|NotebookEdit|Write|Bash` (10 s), Stop (30 s). `hooks/roadkeep-launch.py`
  (590 lines) is the committed launcher for environments without the plugin (RK1108).
- `skills/roadkeep/`: `SKILL.md` orientation (165 lines) + `writing.md` (607) + `asking.md`
  (295) (RK1437). `tests/test_skill.py:136,155`: `ORIENTATION_MAX = 13_000`,
  `PAGE_MAX = {"writing.md": 54_000, "asking.md": 26_000}` UTF-16 units.
- `commands/` add/lint/pick/ship (22-29 lines; `ship.md`: "a number retyped here is one
  that goes stale"). MCP surface "63,594 at 64 tools"; per-tool description cap
  `characters = 2850` (`[tools]`).
- Guard design (`src/roadkeep/guarding.py:1-60`): Edit/Write on a governed file denied with
  the command to call instead ("a refusal that names no alternative is a refusal an agent
  works around"); Bash answered with ask (RK128); never emits allow ("Silence is the
  allow"); every failure allows; always exits 0. Stop runs lint + `attested` (RK175).

## 3. Planning docs

| File | Lines | Convention |
|---|---|---|
| `docs/ROADMAP.md` | 164 | unshipped work only; one sentence what + why + pointer, ≤320 chars, symptom never a solution; lowest-numbered task with deps shipped |
| `docs/CHANGELOG.md` | 1,238 | ledger: 1,171 ✅, 25 🗑 |
| `docs/IMPROVEMENTS.md` | 214 | rationale for unshipped sections only; deleted on ship |
| `docs/DECISIONS.md` | 945 | ADR-like one-sentence decisions, 49 bodies (RK1361); superseded never deleted (RK1274) |

Limits "the P90 of the lines that already read well, which is an agent attention budget
and not a style rule". `[reads]` caps query output (`brief = 3300`, `list = 40000`,
`show = 28000`). `[validation]` asks whether a person tried what shipped (RK1692).

## 4. Gates

`gate.yml`: lint via `uses: ./`; pytest on 3.11 and 3.13 with `fetch-depth: 0` (history is
a fixture, RK39); `claude plugin validate --strict` pinned to CLI 2.1.220 (RK335); same
check on the channel, non-gating. `.pre-commit-hooks.yaml` for adopters; `action.yml`
("A gate that runs only on a developer's machine is not a gate", RK17);
`.githooks/pre-commit` bumps the patch version, never blocks (RK153). 5,106 test functions;
xdist default (RK457); round-trip property test over Shio's and Turing's corpora at pinned
revisions, skipped in CI.

## 5. Commits

1,946 commits (1,938 by the owner, 4 by "Claude" 2026-08-01..08). 1,938 conventional
(docs 702, feat 560, fix 411, test 127, refactor 96, perf 27, chore 12, ci 3); 1,655 carry
an RK id; the id placement changed four times. One task per commit, ship output in the
same commit (`roadkeep-dev/SKILL.md`); filing is a separate docs commit (`9ecfa187`).
`run-commit.cmd -m` (user-level tool). 75 commits carry Co-Authored-By (07-31..09-01), none
after; the staged gui skill forbids attribution and push and requires staging by path and
`-F` messages (RK1474). (inference) attribution dropped by policy around 2026-09.

## 6. Learnings

1. Terse instructions do not survive an author who knows more than the line allows
   (IMPROVEMENTS §0.1) → format enforced at write time.
2. Every-turn rules spend the budget they protect (RK23; RK1136 `b12d28b5`: "26 lines of
   the every-turn file are needed only on a turn that builds or commits") → skills.
3. A budget written as a sentence is not enforced (RK30; `[budgets]` comment) → gate
   limits, lowered after content moved out.
4. Reversal: "compress the prose first" (RK203) was wrong; the index was 36 percent
   (RK1094 `c6464dd6`).
5. The skill was too big: "names all 44 verbs and costs 65k units a turn" (RK1437
   `0d756a9a`) → orientation + pages, test-capped (RK1643).
6. MCP schemas are an every-turn cost (RK1059; ceiling 2600 → 2800 → 2850 each argued;
   RK1601: 2,437 units guidance vs 9,939 schema per connect).
7. Query output can exceed the transport (RK1455: 117,815 refused) → `[reads]` ceilings.
8. An agent bypasses a format with one Edit "because Edit is cheaper than reading a
   --help" (`guarding.py:4-6`, RK22) → deny naming the command; Bash first unmatched then
   ask (RK128); prompts on git add/log removed (RK1689 `054faeed`).
9. "File what you noticed" never ends: "5 tasks shipped and 10 filed … a loop told to stop
   when nothing remains could never stop", 3 of 10 real (`35fc90c2`) → "A task that
   revealed nothing wrong files nothing".
10. Heredoc edits corrupt source (RK1091 `a39c73fd`) → banned.
11. Mixed line endings: "45 modules end CRLF and 11 end LF" (RK1132 `bca89fdb`) →
    `.gitattributes`, test, anchored patches.
12. Concurrent sessions commit each other's work (RK280, RK1117, RK1120, RK320) → claims
    with paths, printed `git add --` lines, stage by path.
13. A self-re-arming hook (RK398) → compare against the index; never block.
14. Stale plugin version = stale session (RK153) → patch bump per commit.
15. Silent loader failures (RK331 YAML frontmatter; RK81; RK323) → `claude plugin validate
    --strict` in CI.
16. A drifted vendored skill is trusted (RK234: "78 lines behind") → SessionStart notice.
17. Premises go stale inside designs (RK310, RK416, RK1486) → `reversals`,
    `--superseded-design`.
18. `Write` clobbers files: ~700 lines in pportal over four occasions
    (`gui/.claude/hooks/no-clobber.py`, staged) → PreToolUse refusal naming Edit.
19. Retirements recorded as learnings (25, e.g. RK133).

## 7. Metrics

1,946 commits, 2026-07-29 (`020d8413`) → 2026-09-24 (`91754240`), 45 active days, peak
134 on 2026-08-03. 64 MCP tools; 4 commands; 2 committed skills; 5,106 tests; highest id
RK1704; plugin 0.2.491.
