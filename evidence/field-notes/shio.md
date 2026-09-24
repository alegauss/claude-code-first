# shio: field notes (verified)

Extracted 2026-09-24 from worktree `D:/git/viglet/shio/latest` (2026.3); HEAD `821f18d74`.
Java/Spring + JS/React monorepo (a CMS). The only brownfield project of the five.

## 1. Instruction surface

`CLAUDE.md` 5 lines / 134 B: "All project guidelines … are in the shared agents file:
`@agents.md`". `agents.md` 291 lines / 22,064 B: Product orientation ("Every design
decision is judged by *agent cycles and tokens*", laws P1-P10); Project Structure; "Where
the detail lives" routing table to `docs/agents/*.md` and skills — "the **index** …
deliberately thin: it is loaded into every session on every turn, so P3 applies to it"
(L61-63); "Invariants that fail silently and have no lint" (L109); Build/test/commit;
Committing; Docs upkeep. Quotes: "Never pipe a gate into grep" (L150, SH354/SH788); "**A
red suite is a stop (SH579).**" (L168); "**One task → one commit, and this is the most
violated rule in the project.**" (L247); batches ≥2 via `/loop` (L250-251); "a rule in two
files is two files that can disagree" (L268-269); "a defect closes with an assertion
carrying its id (SH527)" (L223); "inventing one of these [endpoints] is the most common
wrong turn" (L102-107).

Commit messages: `run-commit.cmd` stages everything and `ai_commit.py` writes the message
with the OpenAI API, so a different model writes the message; 328 bodies start "- This
commit ...". Five commits hand-authored because "the message is a survey of what already
exists, which the diff does not contain" (`7820e57a7`).

## 2. `.claude/` and plugin

`settings.json`: allow nearly every tool unscoped; `defaultMode: acceptEdits`; guard on
SessionStart / PreToolUse / Stop; plugins roadkeep and shio. `.gitignore` L71-84 ignores
`.claude/*` except skills, settings.json, hooks. Launcher `c215718bb` (2026-08-08, authored
by "Claude" with a session URL).

Project skills: 11 (9 authored, 2 vendored), partitioned by code area, each mapping to a
`docs/agents/*.md` file via the routing table; structure: triggers in the description →
"Read docs/agents/X.md" → 3-4 numbered traps with SH ids. Sizes 41-65 lines, except
shio-replication-test 252 and shio-roadmap-docs 388. Eight created together in
`f4ffdb0d9` (2026-07-29).

Published plugin `claude-plugin/` (4 skills, 3 commands, `AGENTS.fragment.md`,
`test/plugin.test.mjs`) via `.claude-plugin/marketplace.json`. Rule from `d1853cbea`
(SH949): "a plugin skill serves a session driving an instance; a project skill serves a
session changing this source tree"; no name on both sides, enforced by test. Trigger: the
skills "were published by, and never loaded in, the repository that wrote them".

`docs/agents/`: 16 files, 1.73 MB, 22,342 lines (cli.md 376 KB, agent-surface.md 304 KB,
renderer.md 184 KB, build.md 150 KB).

## 3. Docs

ROADMAP 213 lines / 29.5 KB; CHANGELOG 1,846 lines / 1.0 MB; IMPROVEMENTS 2,966 lines /
179 KB; none hand-edited. Root `CHANGELOG.md` is a legacy release log ending 0.3.8 (2021).
`docs/specs/` 19 `SH<n>-<slug>.md` (SH74 founding concept); `docs/design/` 16 artboards.
`roadkeep.toml` 397 lines, mostly argued comments; `[limits.changelog] why = 4200` because
"233 entries predate the tool and read 1038 characters at the median". Drift: the toml
header says roadkeep is not vendored; agents.md L272-275 and the tree say it is.
`.gates/` stamps `{gate, code, red, sha, when}` written by `scripts/run-gate.mjs`,
gitignored because "a committed one would let a clone inherit a claim about a run it never
made".

## 4. Gates

`run-gate.mjs` (SH802) keeps the log, keeps the exit code, stamps `.gates/`, locks (SH803:
two concurrent runs "reported 3 errors over 1092 tests where the tree alone reports 1894
green"). `red-suites.json` dated, expiring exceptions tied to a task (SH579, `9b7183ddf`).
CI `suites.yml` on every push: "Eleven commits landed over the first and eight over the
second, and no commit message mentions either". Meta-tests: `agents-md-figures.test.mjs`
(SH974), `assertion-debt.test.mjs` (SH527), Java conformance lints.

Root `*.log` (~90) are gitignored (`.gitignore:63 /*.log`): gate logs with `.red.log`
copies (SH735, `38dbc6389`) and ~60 ad-hoc tee logs per task (`sh951.log`, `sh956e.log`).
The rule came from incidents: sh545.log committed in `b04ee918`; `provoke.log.progress`
in the SH778 commit (`44e6ef232`); a `.pyc` (SH46). (inference) The anti-pattern is
working-tree pollution plus stage-everything, not repository pollution.

## 5. Commits

Conventional with trailing id (`fix(agent): … (SH1083)`); ", with SH1137 filed" (47);
"part one" (51). Since 2026-03-24: 1,361/1,669 conventional; 1,148 with SH ids.
Attribution: Co-Authored-By Opus 5 ×69, Opus 5 1M ×48, Opus 4.8 ×2; "Claude" author 55
(web, 04-11..08-16); most agent commits carry no trailer because run-commit adds none.

## 6. Learnings

1. The every-turn file grew until it broke its own law: agents.md 9.8 KB (`6bf11b754`,
   03-24) → 40 KB (07-26) → 130 KB → 185,734 B (`f4ffdb0d9~1`) → 14.4 KB after the split;
   "P3 violated by the file that declares P3" (L283-285).
2. The split moved the bloat: `docs/agents/` 1.73 MB; build.md 5,238 B → 149,685 B;
   agents.md back to 22 KB; no cap on area files (partly inference).
3. Skills contradict the index: `shio-build-test/SKILL.md` L17 still pipes into grep,
   which agents.md L150 forbids; one commit since creation → no skill-vs-index check.
4. One task one commit is the most violated rule → `/loop`, self-check.
5. Roadmap lines grew into essays: "95 active task lines averaging 142 words, worst 555 —
   and six of the worst eight were written in the same session that then found the
   problem" (SH341, `490a698a0`) → roadkeep limits and guard (`af98be3f0`, 07-30).
6. Plugin guards absent on the web (`c215718bb`).
7. Half-shipped fixes: "Six corrections shipped half of themselves … At 246 commits in
   seven days … that is the system's expected output" (`14acb91ce`) → SH527.
8. Red suites ignored for nineteen commits → SH579, CI on every push.
9. Build output lies: stale `target/` "Nothing to compile" (SH282, `052550e68`); `-q`
   hides totals (SH283); `pnpm test` printed `fail 2` above `EXIT=0` when piped.
10. The gate machinery produced a false red (SH828 `77f9042f0`; SH803 `be14dab5e`: "a
    false red is worse than an absent stamp") → inconclusive state, locks.
11. Flakes lose evidence (SH735; SH778 `d726a4b8b` "provoked rather than waited for").
12. False-premise defects: SH1016 (`c952ebc33`, truncated directory listing); SH519
    (`c17ed995a`: "A filed defect that does not exist costs whoever picks it up more than
    the bug would have"); SH815 (`05c1660b9`).
13. Doc figures drift: "25 mutating paths" vs 28 (SH974, `be9fa3727`).
14. Measure before optimizing (SH1044, `c1bf9071c`: eager load 7.47 MB → 1.54 MB).
15. Testing with the repo mounted hides discoverability gaps (SH605, `7820e57a7`) → SH949.
16. Grep-then-lint: "the grep is the deliverable — it lands as a lint before the fixes"
    (SH322/SH338).

## 7. Metrics

3,446 commits, 2019-07-30 (`1379f0a8b`) → 2026-09-24. Adoption `6bf11b754` (2026-03-24,
"Add agents.md and CLAUDE.md docs"): 1,777 commits before, 1,669 after. Monthly after:
03: 22, 04: 114, 05: 14, 06: 143, 07: 220, 08: 936, 09: 237 (to 09-24); before: 1-25 per
month in 2025. Agent-native pivot `1c45eb8a3` (07-26, SH74); roadkeep adopted `af98be3f0`
(07-30). 139 commits change agents.md. Highest id SH1137.

## Verification

Checked against `821f18d74` on 2026-09-24. 131 claims: 108 verified, 17 corrected, 0 refuted, 2 outside the pin, 4 inference. Error rate 13.6%.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | Header | HEAD is `821f18d74`, dated 2026-09-24 | verified | `git log -1 --format=%cs 821f18d74` = 2026-09-24 [shio@821f18d74] | |
| 2 | Header | A Java/Spring plus JS/React monorepo, a CMS | verified | "Shio is a CMS whose primary operator is a coding agent." [shio@821f18d74:agents.md#L5]; "Backend (Spring Boot 4 + Java 21)" [shio@821f18d74:agents.md#L38]; "Frontend (React + Vite + shadcn/ui + TypeScript)" [shio@821f18d74:agents.md#L46] | |
| 3 | Header | The only brownfield project of the five | inference | The comparison rests on the other four projects. For shio alone: `git rev-list --count 6bf11b754^` = 1778 commits before the adoption commit, the first dated 2019-07-30 [shio@1379f0a8b] | |
| 4 | 1 | `CLAUDE.md` is 5 lines, 134 B | verified | `git show 821f18d74:CLAUDE.md` gives 5 lines, 134 bytes [shio@821f18d74:CLAUDE.md] | |
| 5 | 1 | `CLAUDE.md` points to the shared agents file `@agents.md` | verified | "are in the shared agents file:" [shio@821f18d74:CLAUDE.md#L3]; "@agents.md" [shio@821f18d74:CLAUDE.md#L5] | |
| 6 | 1 | `agents.md` is 291 lines, 22,064 B | verified | `git show 821f18d74:agents.md` gives 291 lines, 22064 bytes [shio@821f18d74:agents.md] | |
| 7 | 1 | Product orientation: design is judged by agent cycles and tokens | verified | "Every design decision is judged by *agent cycles and tokens*" [shio@821f18d74:agents.md#L8-L9] | |
| 8 | 1 | Ten design laws P1-P10 | verified | "The ten design laws" [shio@821f18d74:agents.md#L16]; "Compose, don't fork" [shio@821f18d74:agents.md#L29] (P10) | |
| 9 | 1 | Sections Project Structure; Build/test/commit; Committing; Docs upkeep | verified | "## Project Structure" [shio@821f18d74:agents.md#L36]; "## Build, test, commit" [shio@821f18d74:agents.md#L126]; "### Committing" [shio@821f18d74:agents.md#L237]; "## Docs upkeep" [shio@821f18d74:agents.md#L255] | |
| 10 | 1 | A "Where the detail lives" routing table to `docs/agents/*.md` and skills | verified | "Where the detail lives" [shio@821f18d74:agents.md#L59]; table [shio@821f18d74:agents.md#L65-L83] (two rows point elsewhere: `cli/conformance/` and `shio-site/README.md`) | |
| 11 | 1 | The index is deliberately thin because it loads every turn (L61-63) | verified | "it is deliberately thin: it is loaded into every session on every turn, so P3 applies to it" [shio@821f18d74:agents.md#L61-L62] | |
| 12 | 1 | Heading "Invariants that fail silently and have no lint" at L109 | verified | "Invariants that fail silently and have no lint" [shio@821f18d74:agents.md#L109] | |
| 13 | 1 | "Never pipe a gate into grep" at L150, SH354/SH788 | verified | "Never pipe a gate into" [shio@821f18d74:agents.md#L150]; "not for the log (SH354), not for the verdict" [shio@821f18d74:agents.md#L150]; "(SH788)" [shio@821f18d74:agents.md#L151] (grep is in inline code in the source) | |
| 14 | 1 | "A red suite is a stop (SH579)." at L168 | verified | "A red suite is a stop (SH579)." [shio@821f18d74:agents.md#L168] | |
| 15 | 1 | "One task → one commit, and this is the most violated rule in the project." at L247 | verified | "One task → one commit, and this is the most violated rule in the project." [shio@821f18d74:agents.md#L247] | |
| 16 | 1 | Batches of two or more tasks go through `/loop` (L250-251) | verified | "a batch of ≥2 tasks must be driven with the" [shio@821f18d74:agents.md#L250-L251] (the next line names the loop skill) | |
| 17 | 1 | "a rule in two files is two files that can disagree" at L268-269 | verified | "a rule in two files is two files that can disagree" [shio@821f18d74:agents.md#L268-L269] | |
| 18 | 1 | "a defect closes with an assertion carrying its id (SH527)" at L223 | verified | "a defect closes with an assertion carrying its id (SH527)" [shio@821f18d74:agents.md#L223] | |
| 19 | 1 | Inventing one of three nonexistent endpoints is the most common wrong turn (L102-107) | verified | "inventing one of these is the most common wrong turn" [shio@821f18d74:agents.md#L102-L107] | |
| 20 | 1 | `run-commit.cmd` stages everything; `ai_commit.py` writes the message with the OpenAI API | verified | "generates a Conventional-Commits message from the staged diff via the OpenAI API" [shio@821f18d74:agents.md#L241-L242] (L241 names the stage-all step) | |
| 21 | 1 | So a different model writes the message than the agent that made the change | verified | "via the OpenAI API" [shio@821f18d74:agents.md#L242]; the agent sessions are Claude, "Co-Authored-By: Claude Opus 5" [shio@7820e57a7] | |
| 22 | 1 | 328 commit bodies start "- This commit ..." | corrected | 328 is the number of body lines that begin with it, over all commits; `git log 821f18d74 --grep='^- This commit' --format=%h` = 326 commits | 300 commit bodies begin with "- This commit" (first body line of each commit of `git rev-list 821f18d74`); 326 bodies contain such a line; 328 lines in all [shio@821f18d74] |
| 23 | 1 | Five commits are hand-authored | verified | `git log 821f18d74 --grep='^Hand-authored' --format=%h` = 5: 871410748, 542142e0d, 7820e57a7, 84ed39aad, 0f4a906f3 [shio@7820e57a7] | |
| 24 | 1 | The five were hand-authored because the message is a survey the diff does not contain | corrected | "the message is a survey of what already exists, which the diff does not contain" [shio@7820e57a7] | That reason is given by 7820e57a7 alone; the others give "the message is a measurement the diff" [shio@84ed39aad], "the message is an argument about ordering" [shio@0f4a906f3], and another session's files in flight, "Hand-authored and staged by path" [shio@871410748] |
| 25 | 2 | `settings.json` allows nearly every tool, unscoped | verified | "Bash" [shio@821f18d74:.claude/settings.json#L8]; allow list [shio@821f18d74:.claude/settings.json#L7-L50], all bare tool names except three scoped entries | |
| 26 | 2 | `defaultMode: acceptEdits` | verified | "acceptEdits" [shio@821f18d74:.claude/settings.json#L54] | |
| 27 | 2 | Guard hook on SessionStart, PreToolUse, Stop | verified | "SessionStart" [shio@821f18d74:.claude/settings.json#L61]; "PreToolUse" [shio@821f18d74:.claude/settings.json#L72]; "Stop" [shio@821f18d74:.claude/settings.json#L84]; "roadkeep-launch.py" [shio@821f18d74:.claude/settings.json#L61-L94] | |
| 28 | 2 | Plugins roadkeep and shio enabled | verified | "roadkeep@alegauss" [shio@821f18d74:.claude/settings.json#L97]; "shio@openviglet" [shio@821f18d74:.claude/settings.json#L98] | |
| 29 | 2 | `.gitignore` L71-84 ignores `.claude/*` except skills, settings.json, hooks | verified | "/.claude/*" [shio@821f18d74:.gitignore#L76]; "!/.claude/skills/" [shio@821f18d74:.gitignore#L77]; "!/.claude/settings.json" [shio@821f18d74:.gitignore#L80]; "!/.claude/hooks/" [shio@821f18d74:.gitignore#L84] | |
| 30 | 2 | Launcher `c215718bb`, 2026-08-08 | verified | "load the guard on Claude Code on the web via a committed self-locating launcher" [shio@c215718bb]; `git log -1 --format=%as c215718bb` = 2026-08-08 | |
| 31 | 2 | Authored by "Claude" with a session URL | verified | `git log -1 --format=%an c215718bb` = Claude; "Claude-Session: https://claude.ai/code/session_012QBFfwf4nKtE2ft5bGkx7v" [shio@c215718bb] | |
| 32 | 2 | 11 project skills, 9 authored, 2 vendored | verified | `git ls-tree -r --name-only 821f18d74 -- .claude/skills` lists 11 SKILL.md files; vendored: "vendor the bento page contract" [shio@d5ce0fcca] (viglet-ds-pages) and the roadkeep skill "which ships with the plugin" [shio@821f18d74:agents.md#L267] | |
| 33 | 2 | Skills are partitioned by code area, each mapping to a `docs/agents/*.md` file via the routing table | corrected | Routing table [shio@821f18d74:agents.md#L65-L83] | The nine authored skills map to area files through the table; the two vendored skills (roadkeep, viglet-ds-pages) are not in it [shio@821f18d74:agents.md#L65-L83] |
| 34 | 2 | Skill structure: triggers in the description, then "Read docs/agents/X.md", then 3-4 numbered traps with SH ids | corrected | shio-build-test has four numbered items, one without an SH id [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L29-L48]; shio-database has four, three without [shio@821f18d74:.claude/skills/shio-database/SKILL.md#L13-L36] | Trigger descriptions and a Read pointer to the area file are common to the authored area skills, but the rule lists vary: six numbered in shio-content-files [shio@821f18d74:.claude/skills/shio-content-files/SKILL.md#L21-L34], two in shio-renderer [shio@821f18d74:.claude/skills/shio-renderer/SKILL.md#L41-L44], unnumbered in shio-console-ui and shio-content-api, and not every item carries an SH id |
| 35 | 2 | Sizes 41-65 lines, except shio-replication-test 252 and shio-roadmap-docs 388 | corrected | `git show 821f18d74:.claude/skills/roadkeep/SKILL.md` = 164 lines [shio@821f18d74:.claude/skills/roadkeep/SKILL.md] | Sizes 41-65 lines except shio-replication-test 252, shio-roadmap-docs 388 and the vendored roadkeep 164 [shio@821f18d74:.claude/skills/roadkeep/SKILL.md] |
| 36 | 2 | Eight skills created together in `f4ffdb0d9` (2026-07-29) | verified | `git log --diff-filter=A` per SKILL.md: agent-surface, build-test, console-ui, content-api, content-files, database, renderer, roadmap-docs all added by [shio@f4ffdb0d9], dated 2026-07-29 | |
| 37 | 2 | `claude-plugin/` has 4 skills, 3 commands, `AGENTS.fragment.md`, `test/plugin.test.mjs` | verified | `git ls-tree -r --name-only 821f18d74 -- claude-plugin` [shio@821f18d74:claude-plugin/AGENTS.fragment.md]; [shio@821f18d74:claude-plugin/test/plugin.test.mjs] | |
| 38 | 2 | Published via `.claude-plugin/marketplace.json` | verified | "./claude-plugin" [shio@821f18d74:.claude-plugin/marketplace.json] | |
| 39 | 2 | Rule from `d1853cbea` (SH949): plugin skill drives an instance, project skill changes the tree | verified | "split the two skill sets (SH949)" [shio@d1853cbea]; wording as quoted: "a plugin skill serves a session driving an instance; a project skill serves a session changing this source tree" [shio@821f18d74:agents.md#L90-L91] (the commit message capitalizes it) | |
| 40 | 2 | No skill name on both sides, enforced by test | verified | "No name may appear on both" [shio@821f18d74:agents.md#L93-L94] | |
| 41 | 2 | Trigger: the skills were published by, and never loaded in, the repo that wrote them | verified | "were published by, and never loaded in, the repository that wrote them" [shio@d1853cbea] | |
| 42 | 2 | `docs/agents/`: 16 files, 1.73 MB, 22,342 lines | verified | `git ls-tree -r -l 821f18d74 -- docs/agents/` = 16 files, 1730001 bytes; lines summed over `git show` = 22342 | |
| 43 | 2 | cli.md 376 KB, agent-surface.md 304 KB, renderer.md 184 KB, build.md 150 KB | verified | `git ls-tree -r -l 821f18d74 -- docs/agents/`: 375711, 304495, 184336, 149685 bytes [shio@821f18d74:docs/agents/cli.md] | |
| 44 | 3 | ROADMAP 213 lines, 29.5 KB | verified | 213 lines, 29511 bytes [shio@821f18d74:docs/ROADMAP.md] | |
| 45 | 3 | CHANGELOG 1,846 lines, 1.0 MB | verified | 1846 lines, 1000042 bytes [shio@821f18d74:docs/CHANGELOG.md] | |
| 46 | 3 | IMPROVEMENTS 2,966 lines, 179 KB | verified | 2966 lines, 178920 bytes [shio@821f18d74:docs/IMPROVEMENTS.md] | |
| 47 | 3 | None of the three is hand-edited | verified | "and never by" [shio@821f18d74:agents.md#L263] (the rule; history not audited) | |
| 48 | 3 | Root `CHANGELOG.md` is a legacy release log ending 0.3.8 (2021) | verified | "## 0.3.8 (Oct 10, 2021)" [shio@821f18d74:CHANGELOG.md#L1] | |
| 49 | 3 | `docs/specs/` has 19 `SH<n>-<slug>.md` files | verified | `git ls-tree --name-only 821f18d74 -- docs/specs/` = 19 [shio@821f18d74:docs/specs/SH74-agent-native-cms.md] | |
| 50 | 3 | SH74 is the founding concept | verified | "this one is the constitution" [shio@821f18d74:docs/specs/SH74-agent-native-cms.md#L7] | |
| 51 | 3 | `docs/design/` holds 16 artboards | corrected | `git ls-tree -r --name-only 821f18d74 -- docs/design/` = 16 files, 15 of them `.dc.html` | 15 artboards (`*.dc.html`) plus `canvas.json` [shio@821f18d74:docs/design/canvas.json] |
| 52 | 3 | `roadkeep.toml` 397 lines, mostly argued comments | verified | 397 lines, 345 of them comment lines [shio@821f18d74:roadkeep.toml] | |
| 53 | 3 | `[limits.changelog] why = 4200` | verified | "[limits.changelog]" [shio@821f18d74:roadkeep.toml#L344]; "why = 4200" [shio@821f18d74:roadkeep.toml#L350] | |
| 54 | 3 | Because "233 entries predate the tool and read 1038 characters at the median" | verified | "233 entries predate the tool and read 1038" [shio@821f18d74:roadkeep.toml#L345]; "characters at the median" [shio@821f18d74:roadkeep.toml#L346] (one sentence across two comment lines) | |
| 55 | 3 | The toml header says roadkeep is not vendored | verified | "roadkeep is not vendored here and there is no path to a checkout" [shio@821f18d74:roadkeep.toml#L8] | |
| 56 | 3 | agents.md L272-275 says it is vendored | verified | "The engine is vendored" [shio@821f18d74:agents.md#L272]; "git-ignored, reproduced by" [shio@821f18d74:agents.md#L273] | |
| 57 | 3 | The tree says it is vendored | corrected | The engine is git-ignored, so no vendored copy is in any commit | At the pin the tree carries the installer and an ignore rule, not the engine: ".roadkeep/" [shio@821f18d74:.gitignore#L106]; [shio@821f18d74:install-roadkeep.cmd] |
| 58 | 3 | `.gates/` stamps hold `{gate, code, red, sha, when}` | verified | "red: code !== 0," [shio@821f18d74:scripts/gate-stamp.mjs#L235-L241] (record fields gate, code, red, sha, when) | |
| 59 | 3 | Written by `scripts/run-gate.mjs` | verified | "stamp(ROOT, key, code);" [shio@821f18d74:scripts/run-gate.mjs#L88] (through gate-stamp.mjs) | |
| 60 | 3 | `.gates/` is gitignored because a committed stamp would lie | verified | "a committed one would let a clone" [shio@821f18d74:.gitignore#L124]; "inherit a claim about a run it never made" [shio@821f18d74:.gitignore#L125] (one sentence across two comment lines); "/.gates/" [shio@821f18d74:.gitignore#L126] | |
| 61 | 4 | `run-gate.mjs` (SH802) keeps the log and the exit code | verified | "SH802 — one runner over the gate table" [shio@821f18d74:scripts/run-gate.mjs#L6]; "the exit code is not swallowed" [shio@821f18d74:scripts/run-gate.mjs#L8-L9] | |
| 62 | 4 | It stamps `.gates/` | verified | [shio@821f18d74:scripts/run-gate.mjs#L86-L91] | |
| 63 | 4 | It locks (SH803): two concurrent runs "reported 3 errors over 1092 tests where the tree alone reports 1894 green" | verified | "SH803 — one run of a gate at a time" [shio@821f18d74:scripts/run-gate.mjs#L49]; "reported 3 errors over 1092 tests where the tree alone reports 1894" [shio@821f18d74:scripts/run-gate.mjs#L57] (the word green follows in the next string literal) | |
| 64 | 4 | `red-suites.json` holds dated, expiring exceptions tied to a task (SH579, `9b7183ddf`) | verified | "dated, time-boxed, and pointing at the open task that removes it" [shio@821f18d74:red-suites.json#L2]; "a red suite is a stop" [shio@9b7183ddf] | |
| 65 | 4 | CI `suites.yml` runs on every push | corrected | [shio@821f18d74:.github/workflows/suites.yml#L19-L21] | It runs on push to branches 2026.3 and main, on pull requests and by dispatch: "branches:" [shio@821f18d74:.github/workflows/suites.yml#L20] |
| 66 | 4 | Quote: eleven commits over the first red suite and eight over the second, unmentioned | verified | "Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4]; "mentions either" [shio@821f18d74:.github/workflows/suites.yml#L5] (one sentence across two comment lines) | |
| 67 | 4 | Meta-test `agents-md-figures.test.mjs` (SH974) | verified | "no figure from one of them belongs in prose uncited" [shio@821f18d74:agents.md#L219-L220]; "(SH974)" [shio@821f18d74:agents.md#L219] | |
| 68 | 4 | Meta-test `assertion-debt.test.mjs` (SH527) | verified | "A rule nobody can check is a preference, so" [shio@821f18d74:agents.md#L229-L230]; "assertion-debt.test.mjs" [shio@821f18d74:agents.md#L230] | |
| 69 | 4 | Java conformance lints | verified | "ShAgentP1ConformanceTest" [shio@821f18d74:agents.md#L211]; "ShStatelessReachabilityLintTest" [shio@821f18d74:agents.md#L214] | |
| 70 | 4 | About 90 root `*.log` files exist | outside the pin | Untracked working-tree files; `/*.log` is ignored, so no commit holds them | |
| 71 | 4 | They are gitignored by `.gitignore:63 /*.log` | verified | "/*.log" [shio@821f18d74:.gitignore#L63] | |
| 72 | 4 | Gate logs get `.red.log` copies (SH735, `38dbc6389`) | verified | "a green re-run no longer erases the red run a flake needed (SH735)" [shio@38dbc6389]; "shio-flake.red.log" [shio@821f18d74:.gitignore#L129] | |
| 73 | 4 | About 60 ad-hoc tee logs per task (`sh951.log`, `sh956e.log`) | outside the pin | Untracked working-tree files | |
| 74 | 4 | `sh545.log` was committed in `b04ee918` | verified | "which is how sh545.log landed in b04ee918" [shio@821f18d74:.gitignore#L62]; `git show --stat b04ee9187` adds sh545.log [shio@b04ee9187] | |
| 75 | 4 | `provoke.log.progress` landed in the SH778 commit, `44e6ef232` | corrected | "so it landed in the SH778 commit" [shio@44e6ef232] | The SH778 commit that added it is d726a4b8b (`git show --stat d726a4b8b` adds provoke.log.progress) [shio@d726a4b8b]; 44e6ef232 removed it and ignored it [shio@44e6ef232] |
| 76 | 4 | A `.pyc` reached a commit (SH46) | verified | "one .pyc reached a commit that way (SH46's)" [shio@821f18d74:.gitignore#L117] | |
| 77 | 4 | The anti-pattern is working-tree pollution plus stage-everything, not repository pollution | inference | Marked (inference) in the note; the related source names the stage-everything cause: "stages everything, so a" [shio@821f18d74:.gitignore#L60-L61] | |
| 78 | 5 | Subjects are conventional with a trailing id, e.g. `fix(agent): … (SH1083)` | verified | "fix(agent): the REST batch refuses an op field it does not know (SH1083)" [shio@821f18d74] | |
| 79 | 5 | ", with SH1137 filed" appears in 47 subjects | corrected | "with SH1137 filed" [shio@6b29c549c]; `git log 821f18d74 --format=%s`: 47 subjects contain filed at all | 40 subjects match `, with SH[0-9]+.*filed`; 47 is the count of subjects containing the word filed [shio@821f18d74] |
| 80 | 5 | "part one" appears in 51 subjects | corrected | `git log 821f18d74 --format=%s`: 51 subjects contain the substring part, any case | 6 subjects say part one; 40 mark an id as partial (`SH[0-9]+[ ,]+part`), e.g. "(SH1063, part one)" [shio@7c9f0ac42] |
| 81 | 5 | Since 2026-03-24, 1,361 of 1,669 commits are conventional | corrected | `git log 6bf11b754^..821f18d74 --format=%s` gives 1668 subjects, 1361 of type(scope): form | 1,361 of 1,668 commits from the adoption commit on [shio@6bf11b754]; 1,669 comes from `--since=2026-03-24`, which git reads with the current time of day and so includes one earlier commit of that date |
| 82 | 5 | 1,148 of those subjects carry SH ids | verified | `git log 6bf11b754^..821f18d74 --format=%s`: 1148 contain `SH[0-9]+` | |
| 83 | 5 | Co-Authored-By Opus 5 ×69 | verified | `git log 821f18d74 --format=%B`: 69 lines "Co-Authored-By: Claude Opus 5" without suffix [shio@7820e57a7] | |
| 84 | 5 | Co-Authored-By Opus 5 1M ×48 | verified | 48 lines "Co-Authored-By: Claude Opus 5 (1M context)" [shio@c17ed995a] | |
| 85 | 5 | Co-Authored-By Opus 4.8 ×2 | verified | 2 lines "Co-Authored-By: Claude Opus 4.8" [shio@c215718bb] | |
| 86 | 5 | "Claude" is the author of 55 commits, from the web, 2026-04-11 to 2026-08-16 | verified | `git log 821f18d74 --author='^Claude' --format=%h` = 55, first c652a2cba 2026-04-11 [shio@c652a2cba], last daecef641 2026-08-16 [shio@daecef641]; all 55 carry a claude.ai/code session URL | |
| 87 | 5 | Most agent commits carry no trailer because run-commit adds none | inference | 119 trailers against 1668 commits since adoption; no source states that run-commit adds none; commit tool described at [shio@821f18d74:agents.md#L239-L245] | |
| 88 | 6 | agents.md was 9.8 KB at `6bf11b754` (03-24) | verified | `git cat-file -s 6bf11b754:agents.md` = 9843 [shio@6bf11b754] | |
| 89 | 6 | 40 KB on 07-26 | verified | `git cat-file -s db3edb114:agents.md` = 40375, dated 2026-07-26 [shio@db3edb114] | |
| 90 | 6 | Then 130 KB | verified | `git cat-file -s 2424f20e1:agents.md` = 130166 (2026-07-28) [shio@2424f20e1] | |
| 91 | 6 | 185,734 B at `f4ffdb0d9~1` | verified | `git cat-file -s f4ffdb0d9~1:agents.md` = 185734 [shio@490a698a0] | |
| 92 | 6 | 14.4 KB after the split | verified | `git cat-file -s f4ffdb0d9:agents.md` = 14433 [shio@f4ffdb0d9] | |
| 93 | 6 | "P3 violated by the file that declares P3" (L283-285) | verified | "P3 violated by the file that declares P3" [shio@821f18d74:agents.md#L283-L285] | |
| 94 | 6 | build.md grew from 5,238 B to 149,685 B | verified | `git cat-file -s f4ffdb0d9:docs/agents/build.md` = 5238 [shio@f4ffdb0d9]; 149685 at the pin [shio@821f18d74:docs/agents/build.md] | |
| 95 | 6 | agents.md back to 22 KB | verified | 22064 bytes [shio@821f18d74:agents.md] | |
| 96 | 6 | No cap on area files | inference | Marked partly inference in the note; not checked against every lint | |
| 97 | 6 | `shio-build-test/SKILL.md` L17 still pipes into grep, which agents.md L150 forbids | verified | "-Dskip.npm=true 2>&1" [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L17] (piped into grep on that line); "Never pipe a gate into" [shio@821f18d74:agents.md#L150] | |
| 98 | 6 | One commit since the skill's creation, so no skill-vs-index check | corrected | `git log --format=%h 821f18d74 -- .claude/skills/shio-build-test/SKILL.md` = f4ffdb0d9 only [shio@f4ffdb0d9] | The file has a single commit, its creation in f4ffdb0d9, and no change since [shio@f4ffdb0d9]; that no check exists is inference |
| 99 | 6 | The most violated rule led to `/loop` and a self-check | verified | "request to run them one at a time" [shio@821f18d74:agents.md#L250]; "Self-check before starting task N+1" [shio@821f18d74:.claude/skills/shio-roadmap-docs/SKILL.md#L25] | |
| 100 | 6 | Roadmap lines grew to 95 lines averaging 142 words, worst 555 (SH341, `490a698a0`) | verified | "six of the worst eight were written in the same session that then found the problem" [shio@821f18d74:docs/agents/agent-surface.md#L1502-L1503] (the source bolds 142; the text was added by the SH338-SH341 commit, "make the roadmap a queue again" [shio@490a698a0]) | |
| 101 | 6 | Then roadkeep limits and guard (`af98be3f0`, 07-30) | verified | "adopt roadkeep as the owner of ROADMAP, CHANGELOG and IMPROVEMENTS" [shio@af98be3f0] | |
| 102 | 6 | Plugin guards are absent on the web (`c215718bb`) | verified | "never installs marketplace plugins" [shio@c215718bb] | |
| 103 | 6 | Half-shipped fixes quote (`14acb91ce`), then SH527 | verified | "Six corrections shipped half of themselves" [shio@14acb91ce]; "At 246 commits in seven days" [shio@14acb91ce]; "system's expected output" [shio@14acb91ce] | |
| 104 | 6 | Red suites ignored for nineteen commits, then SH579 | verified | "the third state cost nineteen commits" [shio@821f18d74:agents.md#L171] | |
| 105 | 6 | Then CI on every push | corrected | [shio@821f18d74:.github/workflows/suites.yml#L19-L21] | CI on push to branches 2026.3 and main and on pull requests [shio@821f18d74:.github/workflows/suites.yml#L20] |
| 106 | 6 | Stale `target/` "Nothing to compile" (SH282, `052550e68`) | verified | "mvn compile can report success on code that does not compile" [shio@052550e68]; "Nothing to compile" [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L30] | |
| 107 | 6 | `-q` hides totals (SH283) | verified | "suppresses surefire" [shio@821f18d74:agents.md#L146-L147] | |
| 108 | 6 | `pnpm test` printed fail 2 above EXIT=0 when piped | verified | "above" [shio@821f18d74:agents.md#L155-L156] (the quoted command outputs are in inline code) | |
| 109 | 6 | The gate machinery produced a false red (SH828, `77f9042f0`) | verified | "was stamped as the suite's colour, twice (SH828)" [shio@77f9042f0] | |
| 110 | 6 | SH803 `be14dab5e`: "a false red is worse than an absent stamp" | verified | "a false red is worse than an absent stamp" [shio@be14dab5e] | |
| 111 | 6 | Then an inconclusive state and locks | verified | "recorded as INCONCLUSIVE rather than red (SH828)" [shio@821f18d74:scripts/run-gate.mjs#L94]; "one run of a gate at a time" [shio@821f18d74:scripts/run-gate.mjs#L49] | |
| 112 | 6 | Flakes lose evidence (SH735) | verified | "a green re-run no longer erases the red run a flake needed" [shio@38dbc6389] | |
| 113 | 6 | SH778 `d726a4b8b` "provoked rather than waited for" | verified | "provoked rather than waited for (SH778)" [shio@d726a4b8b] | |
| 114 | 6 | SH1016 (`c952ebc33`) had a false premise from a truncated directory listing | verified | "directory listing truncated before it" [shio@c952ebc33] | |
| 115 | 6 | SH519 (`c17ed995a`) quote on filed defects that do not exist | verified | "A filed defect that does not exist costs whoever picks it up more than the bug would have" [shio@c17ed995a] | |
| 116 | 6 | SH815 (`05c1660b9`) had a false premise | verified | "SH815's premise was the same mistake" [shio@05c1660b9] | |
| 117 | 6 | Doc figures drift: "25 mutating paths" vs 28 (SH974, `be9fa3727`) | verified | "25 mutating paths" [shio@be9fa3727]; "The scan finds twenty-eight roots" [shio@be9fa3727] | |
| 118 | 6 | Measure before optimizing (SH1044, `c1bf9071c`: eager load 7.47 MB to 1.54 MB) | verified | "The console's eager load falls from 7,473,483 raw" [shio@c1bf9071c]; "1,542,579" [shio@c1bf9071c] | |
| 119 | 6 | Testing with the repo mounted hides discoverability gaps (SH605, `7820e57a7`), then SH949 | verified | "the reader with the repository mounted is not the reader who installs (SH605)" [shio@7820e57a7]; "split the two skill sets (SH949)" [shio@d1853cbea] | |
| 120 | 6 | Grep-then-lint quote (SH322/SH338) | verified | "(SH322)" [shio@821f18d74:agents.md#L204]; "it lands as a lint" [shio@821f18d74:agents.md#L205]; "(SH338)" [shio@821f18d74:agents.md#L207] (the source bolds the deliverable and italicizes before) | |
| 121 | 7 | 3,446 commits | verified | `git rev-list --count 821f18d74` = 3446 | |
| 122 | 7 | From 2019-07-30 (`1379f0a8b`) to 2026-09-24 | verified | "the first commit" [shio@1379f0a8b], the only root, dated 2019-07-30; the pin is dated 2026-09-24 [shio@821f18d74] | |
| 123 | 7 | Adoption `6bf11b754` (2026-03-24, "Add agents.md and CLAUDE.md docs") | verified | "Add agents.md and CLAUDE.md docs" [shio@6bf11b754] | |
| 124 | 7 | 1,777 commits before adoption, 1,669 after | corrected | `git rev-list --count 6bf11b754^` = 1778; `git rev-list --count 6bf11b754^..821f18d74` = 1668 | 1,778 commits before the adoption commit and 1,668 from it on [shio@6bf11b754]; the note's split is `--before`/`--since=2026-03-24`, which git reads with the current time of day, so it moved one same-day commit (a8d1c8e7e) across [shio@a8d1c8e7e] |
| 125 | 7 | Monthly after adoption, 03: 22 | corrected | `git log 6bf11b754^..821f18d74 --format=%ad` gives 4 commits in 2026-03 | 4 commits in March 2026 from the adoption on; 22 is all of March 2026 [shio@6bf11b754] |
| 126 | 7 | Monthly after: 04: 114, 05: 14, 06: 143, 07: 220, 08: 936, 09: 237 | verified | `git log 6bf11b754^..821f18d74 --format=%ad --date=format:%Y-%m` counted per month | |
| 127 | 7 | Before adoption, 1-25 commits per month in 2025 | corrected | `git log 821f18d74 --since=2025-01-01 --until=2026-01-01 --format=%ad` per month: 9, 0, 1, 25, 6, 11, 7, 10, 20, 12, 11, 16 | 0-25 per month in 2025; February had none [shio@821f18d74] |
| 128 | 7 | Agent-native pivot `1c45eb8a3` (07-26, SH74) | verified | "reorient Shio as an agent-native CMS (SH74" [shio@1c45eb8a3]; dated 2026-07-26 | |
| 129 | 7 | roadkeep adopted in `af98be3f0` (07-30) | verified | "adopt roadkeep as the owner of ROADMAP, CHANGELOG and IMPROVEMENTS" [shio@af98be3f0]; dated 2026-07-30 | |
| 130 | 7 | 139 commits change agents.md | verified | `git log --format=%h 821f18d74 -- agents.md` = 139 | |
| 131 | 7 | Highest id SH1137 | verified | "SH1137" [shio@821f18d74:docs/ROADMAP.md#L107]; no higher id in ROADMAP, CHANGELOG or IMPROVEMENTS | |
