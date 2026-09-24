# shio: field notes (preliminary, unverified)

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
