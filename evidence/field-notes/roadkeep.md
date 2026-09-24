# roadkeep: field notes (verified)

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

## Verification

Checked against `91754240` on 2026-09-24. 134 claims: 111 verified, 17 corrected, 0 refuted, 4 outside the pin, 2 inference. Error rate 13.3%.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | intro | The extraction was made at HEAD 91754240, dated 2026-09-24 | verified | [roadkeep@91754240]; `git show -s --format=%ad 91754240` = Thu Sep 24 17:23:05 2026 -0300 | |
| 2 | intro | The working tree held an uncommitted, staged merge of gui/ (RK1697, 564 files) | outside the pin | the staged tree is not in any commit; RK1697 itself is only an open idea at the pin, "roadkeep-gui is a second repository" [roadkeep@91754240:docs/ROADMAP.md#L47] | |
| 3 | intro | Nothing under gui/ was in history at the pin | verified | `git log --oneline 91754240 -- gui` returns no commit | |
| 4 | 1 | .claude/CLAUDE.md is 10 lines and 77 words | verified | `git show 91754240:.claude/CLAUDE.md` through `wc -l -w` = 10 77 [roadkeep@91754240:.claude/CLAUDE.md] | |
| 5 | 1 | .claude/CLAUDE.md is a pointer to the shared agents file, via @../agents.md | verified | "All project guidelines, conventions and design laws are in the shared agents file:" [roadkeep@91754240:.claude/CLAUDE.md#L3-L5] | |
| 6 | 1 | It lives under .claude/ because the repo is the plugin and a root CLAUDE.md ships in the payload (RK323) | verified | "this repository is the plugin, so every root file ships in the payload" [roadkeep@91754240:.claude/CLAUDE.md#L7-L9] | |
| 7 | 1 | docs/CHANGELOG.md:1028 is the RK323 entry | verified | "The published payload carries this repository's own CLAUDE.md" [roadkeep@91754240:docs/CHANGELOG.md#L1028] | |
| 8 | 1 | .claude/CLAUDE.md is budgeted at 12 lines and 800 bytes in roadkeep.toml [budgets] | verified | "lines = 12, bytes = 800" [roadkeep@91754240:roadkeep.toml#L253] | |
| 9 | 1 | agents.md is 113 lines and 1,120 words | verified | `git show 91754240:agents.md` through `wc -l -w` = 113 1120 [roadkeep@91754240:agents.md] | |
| 10 | 1 | agents.md is the one every-turn file | corrected | "Files loaded on every turn, and what each may cost (RK30)" [roadkeep@91754240:roadkeep.toml#L235] | [budgets] declares two every-turn files, agents.md and the .claude/CLAUDE.md pointer that imports it [roadkeep@91754240:roadkeep.toml#L249-L253]; agents.md is the one that carries the rules |
| 11 | 1 | agents.md budget is 125 lines and 8400 bytes, at roadkeep.toml:249 | verified | "lines = 125, bytes = 8400" [roadkeep@91754240:roadkeep.toml#L249] | |
| 12 | 1 | The budget is enforced by the gate | verified | "held by" [roadkeep@91754240:agents.md#L112]; lint exits 1 on an "over-budget every-turn file" [roadkeep@91754240:agents.md#L83] | |
| 13 | 1 | 106 commits touch agents.md | verified | `git log --oneline 91754240 -- agents.md` counted with `wc -l` = 106 | |
| 14 | 1 | The preamble measures Shio at 92 roadmap lines averaging 142 words | verified | "92 roadmap lines averaging" [roadkeep@91754240:agents.md#L7] (142 words is bold on the same line) | |
| 15 | 1 | The preamble measures an agents.md at 186 KB | verified | "186 KB" [roadkeep@91754240:agents.md#L8] | |
| 16 | 1 | The preamble says the saving is the analysis, not the characters | verified | "The saving is the analysis, not the characters." [roadkeep@91754240:agents.md#L11-L12] | |
| 17 | 1 | The six laws sit at L16-27 | verified | "The six laws" [roadkeep@91754240:agents.md#L16-L27] | |
| 18 | 1 | A change breaking a law is wrong even if requested | verified | "a change breaking one is wrong even if requested" [roadkeep@91754240:agents.md#L18] | |
| 19 | 1 | L1: schema enforced where the text is created; lint is only the backstop | verified | "is only the backstop" [roadkeep@91754240:agents.md#L22] (the source bolds and code-formats parts of the line) | |
| 20 | 1 | L4: the tool never writes prose | verified | "never writes prose" [roadkeep@91754240:agents.md#L25] | |
| 21 | 1 | L5: query instead of read | verified | "Query instead of read" [roadkeep@91754240:agents.md#L26] | |
| 22 | 1 | The layout index carries no task numbers | corrected | "so it carries no task numbers" [roadkeep@91754240:agents.md#L36-L37] | Only the src/roadkeep/ part carries none; the rows after it cite ids, as in "and the launcher an adopter commits where no plugin can be (RK1108)" [roadkeep@91754240:agents.md#L61] |
| 23 | 1 | The layout index is held against src/ by a test | verified | "holds agents.md's Layout" [roadkeep@91754240:tests/test_checkout.py#L120]; "def test_every_module_is_named_in_the_layout_index" [roadkeep@91754240:tests/test_linting.py#L212] | |
| 24 | 1 | Conformance fixture: roadkeep lint must pass on docs/ | verified | "must pass on" [roadkeep@91754240:agents.md#L79] | |
| 25 | 1 | The write path is delegated to a skill, and nothing here repeats it | verified | "nothing here repeats it" [roadkeep@91754240:agents.md#L96] | |
| 26 | 1 | The build and commit rules are delegated to a skill | verified | "Nothing here repeats it." [roadkeep@91754240:agents.md#L101-L105] | |
| 27 | 1 | Non-goals are binding; only what a turn touching no governed file needs loads every turn | verified | "What loads every turn is only what a turn touching no governed file needs." [roadkeep@91754240:agents.md#L111] | |
| 28 | 2 | Committed under .claude/: CLAUDE.md, settings.json, skills/roadkeep-dev/SKILL.md | verified | `git ls-tree -r --name-only 91754240 -- .claude` lists exactly these three | |
| 29 | 2 | .claude/settings.json is 181 bytes | verified | `git cat-file -s 91754240:.claude/settings.json` = 181 | |
| 30 | 2 | settings.json holds enabledMcpjsonServers and one additional directory; no hooks, no allow rules | verified | "additionalDirectories" [roadkeep@91754240:.claude/settings.json#L5-L9]; the file has no hooks or allow key | |
| 31 | 2 | The roadkeep-dev skill's trigger words include pytest, commit, stage, heredoc, version bump, run-commit, ship, file a task | verified | "Trigger words: pytest, run the tests, commit, stage, git add, heredoc, version bump, run-commit, ship, file a task, add --block." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L3] | |
| 32 | 2 | The skill says it is a file only because it is trigger-loaded (RK23, RK1136) | verified | "Trigger-loaded, and that is the whole reason it is a file (RK23, RK1136)." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L8] | |
| 33 | 2 | .claude/settings.local.json is globally ignored and sets bypassPermissions, skipDangerousModePermissionPrompt and a blanket allow | outside the pin | the file is not committed and the repository's .gitignore does not name it [roadkeep@91754240:.gitignore] | |
| 34 | 2 | Governance rests on hooks and the gate, not on permissions | inference | the extractor's reading; no source states it | |
| 35 | 2 | The repo is the plugin, and a push to main is the release | verified | "This repository *is* the plugin, so a push to main is the release." [roadkeep@91754240:.github/workflows/gate.yml#L12] | |
| 36 | 2 | .claude-plugin/plugin.json is version 0.2.491 | verified | "0.2.491" [roadkeep@91754240:.claude-plugin/plugin.json#L4] | |
| 37 | 2 | marketplace.json was published under RK26 | verified | "publish a marketplace so /plugin install reaches the plugin (RK26)" [roadkeep@fa8e6dd3] | |
| 38 | 2 | Plugin MCP in .claude-plugin/mcp.json and checkout MCP in .mcp.json, split after RK81 | verified | "The MCP server is declared and no tool reaches the client" [roadkeep@91754240:docs/CHANGELOG.md#L978]; "./.claude-plugin/mcp.json" [roadkeep@91754240:.claude-plugin/plugin.json#L20] | |
| 39 | 2 | hooks.json runs roadkeep.py guard on SessionStart (10 s), on PreToolUse for Edit, MultiEdit, NotebookEdit, Write and Bash (10 s), and on Stop (30 s) | verified | [roadkeep@91754240:hooks/hooks.json#L3-L35] | |
| 40 | 2 | hooks/roadkeep-launch.py is 590 lines | verified | `git grep -c "" 91754240 -- hooks/roadkeep-launch.py` = 590 | |
| 41 | 2 | The launcher is the committed one for environments without the plugin (RK1108) | verified | "install --committed writes a launcher the repository carries" [roadkeep@91754240:docs/CHANGELOG.md#L1067] | |
| 42 | 2 | skills/roadkeep/ holds SKILL.md (165 lines), writing.md (607) and asking.md (295) | verified | `git grep -c "" 91754240 -- skills/roadkeep` = 165, 607, 295 | |
| 43 | 2 | The orientation and pages split is RK1437 | verified | "The skill is an orientation of 11k units" [roadkeep@91754240:docs/CHANGELOG.md#L1099] | |
| 44 | 2 | tests/test_skill.py:136 sets ORIENTATION_MAX = 13_000 | verified | "ORIENTATION_MAX = 13_000" [roadkeep@91754240:tests/test_skill.py#L136] | |
| 45 | 2 | tests/test_skill.py:155 sets PAGE_MAX to 54_000 for writing.md and 26_000 for asking.md | verified | "PAGE_MAX = {" [roadkeep@91754240:tests/test_skill.py#L155] | |
| 46 | 2 | The ceilings are in UTF-16 units | verified | "in UTF-16 code units" [roadkeep@91754240:tests/test_skill.py#L128]; "in UTF-16 code units (RK1643)" [roadkeep@91754240:tests/test_skill.py#L138] | |
| 47 | 2 | commands/ holds add, lint, pick and ship, 22 to 29 lines each | verified | `git grep -c "" 91754240 -- commands` = 29, 25, 23, 22 | |
| 48 | 2 | ship.md: a number retyped here is one that goes stale | verified | "a number retyped here is one that goes stale." [roadkeep@91754240:commands/ship.md#L21-L22] | |
| 49 | 2 | MCP surface is 63,594 units at 64 tools | corrected | "the reading here is 63,594 at 64 tools" [roadkeep@91754240:roadkeep.toml#L98] is RK1364's reading, raised many times after | At the pin the reading is 69,544 against a ceiling of 69,665: "session = 69665" [roadkeep@91754240:roadkeep.toml#L232], "69544" [roadkeep@91754240:roadkeep.toml#L227]; `roadkeep cost --tools` on an export of the pin reports 67 tools, 69544 of 69665 held |
| 50 | 2 | The per-tool description cap is characters = 2850 in [tools] | verified | "characters = 2850" [roadkeep@91754240:roadkeep.toml#L95] | |
| 51 | 2 | The guard denies Edit and Write on a governed file and names the command instead | verified | "a refusal that names no alternative is a refusal an agent works around" [roadkeep@91754240:src/roadkeep/guarding.py#L14-L15] | |
| 52 | 2 | Bash is answered with ask (RK128) | verified | "is matched and answered with" [roadkeep@91754240:docs/CHANGELOG.md#L989]; [roadkeep@91754240:src/roadkeep/guarding.py#L32] | |
| 53 | 2 | The guard never emits allow | verified | "Silence is the allow." [roadkeep@91754240:src/roadkeep/guarding.py#L24] | |
| 54 | 2 | Every failure allows | verified | "Every failure allows." [roadkeep@91754240:src/roadkeep/guarding.py#L28] | |
| 55 | 2 | The guard always exits 0 | verified | "always exits 0" [roadkeep@91754240:src/roadkeep/guarding.py#L45-L47] | |
| 56 | 2 | Stop runs lint and attested (RK175) | verified | "and, since RK175," [roadkeep@91754240:src/roadkeep/guarding.py#L39-L41] | |
| 57 | 3 | docs/ROADMAP.md is 164 lines | corrected | `git grep -c "" 91754240 -- docs/ROADMAP.md` = 163 | docs/ROADMAP.md is 163 lines [roadkeep@91754240:docs/ROADMAP.md] |
| 58 | 3 | ROADMAP holds unshipped work only, one sentence what + why + pointer, at most 320 characters, symptom never a solution, picking the lowest-numbered task whose deps shipped | verified | "never a solution name" [roadkeep@91754240:docs/ROADMAP.md#L17-L21]; "the lowest-numbered task whose" [roadkeep@91754240:docs/ROADMAP.md#L21] | |
| 59 | 3 | docs/CHANGELOG.md is 1,238 lines | verified | `git grep -c "" 91754240 -- docs/CHANGELOG.md` = 1238 | |
| 60 | 3 | The ledger holds 1,171 ✅ entries | corrected | `git grep -c "^- ✅" 91754240 -- docs/CHANGELOG.md` = 1170 | 1,170 ✅ entries; the 1,171st ✅ is in the header note [roadkeep@91754240:docs/CHANGELOG.md#L7] |
| 61 | 3 | The ledger holds 25 🗑 entries | corrected | `git grep -c "^- 🗑" 91754240 -- docs/CHANGELOG.md` = 24 | 24 🗑 entries; the 25th 🗑 is inside the RK125 sentence [roadkeep@91754240:docs/CHANGELOG.md#L865] |
| 62 | 3 | docs/IMPROVEMENTS.md is 214 lines | corrected | `git grep -c "" 91754240 -- docs/IMPROVEMENTS.md` = 188 | docs/IMPROVEMENTS.md is 188 lines [roadkeep@91754240:docs/IMPROVEMENTS.md] |
| 63 | 3 | IMPROVEMENTS is rationale for unshipped sections only, deleted on ship | verified | "When a section ships, delete it here." [roadkeep@91754240:docs/IMPROVEMENTS.md#L3-L5] | |
| 64 | 3 | docs/DECISIONS.md is 945 lines | verified | `git grep -c "" 91754240 -- docs/DECISIONS.md` = 945 | |
| 65 | 3 | DECISIONS holds ADR-like one-sentence decisions | verified | "an ADR is kept by hand or not at all" [roadkeep@91754240:docs/DECISIONS.md#L7]; "a decision is one sentence" [roadkeep@91754240:docs/DECISIONS.md#L19] | |
| 66 | 3 | DECISIONS carries 49 bodies (RK1361) | verified | `git grep -c "^### §" 91754240 -- docs/DECISIONS.md` = 49; "no verb deletes a body while the entry stands" [roadkeep@91754240:docs/DECISIONS.md#L19] | |
| 67 | 3 | A superseded decision is never deleted (RK1274) | verified | "A decision is superseded once, and both entries stay" [roadkeep@91754240:docs/DECISIONS.md#L8] | |
| 68 | 3 | Limits are the P90 of the lines that already read well | verified | "the P90 of the lines that already read well, which is an agent attention budget" [roadkeep@91754240:roadkeep.toml#L48] | |
| 69 | 3 | [reads] caps query output at brief = 3300, list = 40000, show = 28000 | verified | "brief = 3300" [roadkeep@91754240:roadkeep.toml#L303]; "list = 40000" [roadkeep@91754240:roadkeep.toml#L309]; "show = 28000" [roadkeep@91754240:roadkeep.toml#L322] | |
| 70 | 3 | [validation] asks whether a person tried what shipped (RK1692) | verified | "Whether a person tried what shipped (RK1692)" [roadkeep@91754240:roadkeep.toml#L335] | |
| 71 | 4 | gate.yml runs lint through the action itself | verified | "uses: ./" [roadkeep@91754240:.github/workflows/gate.yml#L33] | |
| 72 | 4 | pytest runs on 3.11 and 3.13 | verified | "3.11" [roadkeep@91754240:.github/workflows/gate.yml#L43] | |
| 73 | 4 | Tests check out with fetch-depth: 0 because history is a fixture (RK39) | verified | "fetch-depth: 0" [roadkeep@91754240:.github/workflows/gate.yml#L51]; "(RK39), and this repository's own past is" [roadkeep@91754240:.github/workflows/gate.yml#L46] | |
| 74 | 4 | claude plugin validate --strict is pinned to CLI 2.1.220 (RK335) | verified | "2.1.220" [roadkeep@91754240:.github/workflows/gate.yml#L71]; "named here rather than left to a channel (RK335)" [roadkeep@91754240:.github/workflows/gate.yml#L66] | |
| 75 | 4 | The same check runs on the channel, non-gating | verified | "continue-on-error: true" [roadkeep@91754240:.github/workflows/gate.yml#L119] | |
| 76 | 4 | .pre-commit-hooks.yaml exists for adopters | verified | "An adopting project adds" [roadkeep@91754240:.pre-commit-hooks.yaml#L1] | |
| 77 | 4 | action.yml: a gate that runs only on a developer's machine is not a gate (RK17) | verified | "A gate that runs only on a developer's machine is not a gate" [roadkeep@91754240:action.yml#L3]; [roadkeep@91754240:docs/CHANGELOG.md#L518] | |
| 78 | 4 | .githooks/pre-commit bumps the patch version and never blocks (RK153) | verified | "Bump the patch version on every commit (RK153)." [roadkeep@91754240:.githooks/pre-commit#L2]; "It never blocks a commit." [roadkeep@91754240:.githooks/pre-commit#L12] | |
| 79 | 4 | 5,106 test functions | corrected | `git grep -h -E "def test_" 91754240 -- tests` counted with `wc -l` = 5104 | 5,104 test functions [roadkeep@91754240:tests]; pytest collects 5,658 items from an export of the pin |
| 80 | 4 | xdist runs by default (RK457) | verified | [roadkeep@91754240:pyproject.toml#L90]; "The suite runs parallel by default" [roadkeep@91754240:docs/CHANGELOG.md#L611] | |
| 81 | 4 | A round-trip property test runs over Shio's and Turing's corpora at pinned revisions and skips in CI | verified | "Shio's and Turing's at the revision" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L24-L26]; "which is what CI does" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L26] | |
| 82 | 5 | 1,946 commits | verified | `git rev-list --count 91754240` = 1946 | |
| 83 | 5 | 1,938 commits by the owner | corrected | `git log 91754240 --format=%an` grouped: 1938 Alexandre Oliveira, 3 Alê Oliveira, 4 Claude, 1 github-actions[bot] | 1,941 commits by the owner's address (1,938 as Alexandre Oliveira, 3 as Alê Oliveira) [roadkeep@91754240] |
| 84 | 5 | 4 commits by Claude, 2026-08-01 to 08-08 | verified | `git log 91754240 --author=Claude` = 4 commits, 7b653977 and 2c55aa18 (08-01), 7944b1a7 and 372c52a7 (08-08) | |
| 85 | 5 | 1,938 conventional subjects | verified | `git log 91754240 --format=%s` matched against type(scope): = 1938 of 1946; the other 8 are merges and three Add commits | |
| 86 | 5 | docs 702, feat 560, fix 411, test 127, refactor 96, perf 27, chore 12, ci 3 | verified | same subject count, grouped by type | |
| 87 | 5 | 1,655 commits carry an RK id | verified | `git log 91754240 --format=%s` with an RK number = 1655 (1,668 counting whole messages) | |
| 88 | 5 | The id placement changed four times | corrected | "(RK3)" [roadkeep@7068a102]; "docs(RK1115):" [roadkeep@5345a5bb]; "feat: RK1298 -" [roadkeep@8ec64f2b]; "(RK1677)" [roadkeep@f7333f42] | Subjects show four placements in sequence, so three changes, with overlap (a docs(RK1478) subject on 2026-09-02 [roadkeep@f3e85d69]): a trailing (RKn) from 2026-07-29, a type(RKn) scope from 2026-08-12, type: RKn - from 2026-08-23, and a trailing (RKn) after a named scope from 2026-09-11 |
| 89 | 5 | One task per commit, with ship output in the same commit | verified | "One task → one commit, the instant it is validated." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L61-L62] | |
| 90 | 5 | Filing is a separate docs commit, as in 9ecfa187 | verified | "docs: file block J, validation, with RK1690-RK1694" [roadkeep@9ecfa187] | |
| 91 | 5 | Commits go through run-commit.cmd -m, a user-level tool | verified | "from the repo root" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L65]; no run-commit file is in the tree (`git ls-tree -r --name-only 91754240`) | |
| 92 | 5 | 75 commits carry Co-Authored-By, 07-31 to 09-01 | corrected | `git log 91754240 -i --grep=Co-Authored-By` = 76 | 76 commits carry the trailer, from 40847570 on 2026-07-29 [roadkeep@40847570] to 595894af on 2026-09-01 [roadkeep@595894af] |
| 93 | 5 | No Co-Authored-By commit after 2026-09-01 | verified | the newest match of `git log 91754240 -i --grep=Co-Authored-By` is 595894af, 2026-09-01 07:18 [roadkeep@595894af] | |
| 94 | 5 | The staged gui skill forbids attribution and push and requires staging by path and -F messages (RK1474) | outside the pin | the gui/ skill was staged, not committed | |
| 95 | 5 | Attribution was dropped by policy around 2026-09 | inference | the extractor's reading; no committed source states the policy | |
| 96 | 6 | Terse instructions do not survive an author who knows more than the line allows (IMPROVEMENTS §0.1), so the format is enforced at write time | verified | "An instruction to be terse does not survive the moment its author knows more than the line allows." [roadkeep@91754240:docs/IMPROVEMENTS.md#L23-L24] | |
| 97 | 6 | Every-turn rules spend the budget they protect (RK23) | verified | "Rules resident every turn spend the budget they exist to protect" [roadkeep@91754240:docs/CHANGELOG.md#L970] | |
| 98 | 6 | RK1136 (b12d28b5): 26 lines of the every-turn file are needed only on a turn that builds or commits | verified | the quote is the RK1136 ledger entry, "26 lines of the every-turn file are needed only on a turn that builds or commits" [roadkeep@91754240:docs/CHANGELOG.md#L667]; the commit says "Moved 26 lines of content from the every-turn file" [roadkeep@b12d28b5] | |
| 99 | 6 | A budget written as a sentence is not enforced (RK30, [budgets] comment), so gate limits, lowered after content moved out | verified | "This budget lived in prose at" [roadkeep@91754240:roadkeep.toml#L235]; "Lowered when the skill took the rules" [roadkeep@91754240:roadkeep.toml#L240] | |
| 100 | 6 | RK203 said compress the prose first | verified | "the measurement says compress the prose first" [roadkeep@91754240:docs/CHANGELOG.md#L546] | |
| 101 | 6 | The reversal: the index was 36 percent (RK1094, c6464dd6) | verified | "the index is 36 percent and the cheap cut, not the prose" [roadkeep@91754240:docs/CHANGELOG.md#L657]; "The index is now identified as 36% of the bytes" [roadkeep@c6464dd6] | |
| 102 | 6 | RK1437 (0d756a9a): the skill names all 44 verbs and costs 65k units a turn | verified | "the skill names all 44 verbs and costs 65k units a turn" [roadkeep@91754240:docs/CHANGELOG.md#L1099]; "the skill is an orientation and the reference is two pages beside it" [roadkeep@0d756a9a] | |
| 103 | 6 | Remedy: orientation plus pages, test-capped (RK1643) | verified | "Each page carries its own figure beside the orientation's" [roadkeep@91754240:docs/CHANGELOG.md#L824] | |
| 104 | 6 | MCP schemas are an every-turn cost (RK1059) | verified | "the largest every-turn surface is measured and held by nothing" [roadkeep@91754240:docs/CHANGELOG.md#L645] | |
| 105 | 6 | The per-tool ceiling went 2600, 2800, 2850, each raise argued | verified | "Raised from 2600" [roadkeep@91754240:roadkeep.toml#L82]; "Raised from 2800" [roadkeep@91754240:roadkeep.toml#L87]; "characters = 2850" [roadkeep@91754240:roadkeep.toml#L95] | |
| 106 | 6 | RK1601: 2,437 units of guidance against 9,939 of schema per connect | verified | "2,437 code units on the turns that open a page, against 9,939 of schema every session pays at connect" [roadkeep@91754240:docs/CHANGELOG.md#L803] | |
| 107 | 6 | Query output can exceed the transport (RK1455: 117,815 refused), hence [reads] ceilings | verified | "RK1455 measured one at 117,815 refused" [roadkeep@91754240:roadkeep.toml#L307] | |
| 108 | 6 | guarding.py:4-6: an agent bypasses the format because Edit is cheaper than reading a --help (RK22) | verified | "is cheaper than reading a" [roadkeep@91754240:src/roadkeep/guarding.py#L4-L6] (the source code-formats Edit and --help); "(RK22)" [roadkeep@91754240:src/roadkeep/guarding.py#L1] | |
| 109 | 6 | Bash was first unmatched, then answered with ask (RK128) | verified | "It used not to be matched at all" [roadkeep@91754240:src/roadkeep/guarding.py#L32-L33] | |
| 110 | 6 | Prompts on git add and git log were removed (RK1689, 054faeed) | verified | "stop asking about git staging or reading a governed file (RK1689)" [roadkeep@054faeed] | |
| 111 | 6 | The rule that never ends was named File what you noticed | corrected | "The rule that produced it was" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L43] | The rule was archive what the task revealed, read as anything I noticed [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L43-L44]; the note's wording is a paraphrase in quotation marks |
| 112 | 6 | 5 tasks shipped and 10 filed; a loop told to stop when nothing remains could never stop | verified | "a loop told to stop when nothing remains could never stop" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L42-L43] (10 filed is bold in the source) | |
| 113 | 6 | 3 of the 10 filings were real | verified | "Three of those ten qualified" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L47] | |
| 114 | 6 | 35fc90c2 introduced the rule that a task that revealed nothing wrong files nothing | verified | "A task that revealed nothing wrong files nothing." [roadkeep@35fc90c2:.claude/skills/roadkeep-dev/SKILL.md#L41]; `git log 91754240 -S` on that sentence returns only 35fc90c2, whose message does not mention it | |
| 115 | 6 | Heredoc edits corrupt source (RK1091, a39c73fd), so they are banned | verified | "source edits do not go through a heredoc (RK1091)" [roadkeep@a39c73fd]; "Never edit source through a shell heredoc." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L30] | |
| 116 | 6 | RK1132: 45 modules end CRLF and 11 end LF | verified | "45 modules end CRLF and 11 end LF" [roadkeep@91754240:docs/CHANGELOG.md#L664] | |
| 117 | 6 | The .gitattributes and test remedy is commit bca89fdb | corrected | "name .gitattributes where the rule it exists for is stated" [roadkeep@bca89fdb] | The remedy landed in 05cc307d, "declare one line terminator and hold it against a mixed file" [roadkeep@05cc307d], which added .gitattributes; bca89fdb only names it in the committing section |
| 118 | 6 | Remedy includes anchored patches | verified | "Anchor on bytes, not on a guess." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L34] | |
| 119 | 6 | Concurrent sessions commit each other's work (RK280, RK1117, RK1120, RK320) | verified | "Two sessions each ship a commit carrying the other's code" [roadkeep@91754240:docs/CHANGELOG.md#L121]; RK1117 [roadkeep@91754240:docs/CHANGELOG.md#L195], RK1120 [roadkeep@91754240:docs/CHANGELOG.md#L196], RK320 [roadkeep@91754240:docs/CHANGELOG.md#L572] | |
| 120 | 6 | Remedy: claims with paths, printed git add lines, staging by path | verified | "Run that line, then commit." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L69-L73] | |
| 121 | 6 | A self-re-arming hook (RK398): compare against the index, never block | verified | "re-armed itself for ever" [roadkeep@91754240:.githooks/pre-commit#L19-L25]; "It never blocks a commit." [roadkeep@91754240:.githooks/pre-commit#L12] | |
| 122 | 6 | Stale plugin version means stale session (RK153), hence a patch bump per commit | verified | "A checkout whose plugin version never moves is one the session keeps running the old copy of" [roadkeep@91754240:docs/CHANGELOG.md#L987] | |
| 123 | 6 | Silent loader failures (RK331, RK81, RK323), hence claude plugin validate --strict in CI | verified | "RK331 shipped broken" [roadkeep@91754240:.github/workflows/gate.yml#L9-L12] | |
| 124 | 6 | A drifted vendored skill is trusted (RK234, 78 lines behind), hence a SessionStart notice | verified | "78 lines behind" [roadkeep@91754240:src/roadkeep/guarding.py#L57-L59]; "notice names a vendored copy that drifted" [roadkeep@91754240:docs/CHANGELOG.md#L872] | |
| 125 | 6 | Premises go stale inside designs (RK310, RK416, RK1486), hence reversals and --superseded-design | verified | "A design section can carry a stale premise" [roadkeep@91754240:docs/CHANGELOG.md#L130]; "reversals" [roadkeep@91754240:src/roadkeep/serving.py#L783]; "--superseded-design" [roadkeep@91754240:src/roadkeep/briefing.py#L411] | |
| 126 | 6 | Write clobbered about 700 lines in pportal over four occasions; a staged no-clobber hook refuses it | outside the pin | gui/.claude/hooks/no-clobber.py was staged, not committed | |
| 127 | 6 | 25 retirements recorded as learnings, such as RK133 | corrected | `git grep -c "^- 🗑" 91754240 -- docs/CHANGELOG.md` = 24 | 24 retirements, RK133 among them [roadkeep@91754240:docs/CHANGELOG.md#L35] |
| 128 | 7 | History runs 2026-07-29 (020d8413) to 2026-09-24 (91754240) | verified | `git rev-list --max-parents=0 91754240` = 020d8413, 2026-07-29 13:08 [roadkeep@020d8413] | |
| 129 | 7 | 45 active days | verified | `git log 91754240 --format=%ad --date=short` has 45 distinct dates | |
| 130 | 7 | Peak of 134 commits on 2026-08-03 | verified | same listing, grouped by date: 134 on 2026-08-03, next 128 on 2026-09-06 | |
| 131 | 7 | 64 MCP tools | corrected | "64 tools" [roadkeep@91754240:roadkeep.toml#L98] is RK1364's reading | 67 tools: `roadkeep cost --tools` on an export of the pin reports 67 tool(s) and the handshake |
| 132 | 7 | 4 commands and 2 committed skills | verified | `git ls-tree -r --name-only 91754240` lists commands/add, lint, pick, ship and the two SKILL.md files, skills/roadkeep and .claude/skills/roadkeep-dev | |
| 133 | 7 | 5,106 tests | corrected | see claim 79 | 5,104 test functions, 5,658 collected items [roadkeep@91754240:tests] |
| 134 | 7 | The highest id is RK1704 | corrected | `git grep -ohE "RK[0-9]+" 91754240` highest real id = RK1703 (RK9999 is a test fixture) | RK1703 [roadkeep@91754240:docs/ROADMAP.md#L53] |
