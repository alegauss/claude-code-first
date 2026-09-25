# Case study: Shio

## 1. Context

Shio is a content management system: "Shio is a CMS whose primary operator is a coding agent." [shio@821f18d74:agents.md#L5]. The backend is "Backend (Spring Boot 4 + Java 21)" [shio@821f18d74:agents.md#L38] and the console is "Frontend (React + Vite + shadcn/ui + TypeScript)" [shio@821f18d74:agents.md#L46].

It is the one brownfield case. The history starts on 2019-07-30 [shio@1379f0a8b], and the
first commit to touch an agent file is "Add agents.md and CLAUDE.md docs" [shio@6bf11b754],
dated 2026-03-24. `git rev-list --count 6bf11b754^` gives 1778 commits before that commit
and `git rev-list --count 6bf11b754^..821f18d74` gives 1668 from it to the pin. The pin is
`821f18d74` on the `2026.3` worktree, dated 2026-09-24 [shio@821f18d74].

## 2. Agent surface

**Every-turn file.** `CLAUDE.md` holds five lines and imports "@agents.md" [shio@821f18d74:CLAUDE.md#L5]. `agents.md` is 291 lines; `git cat-file -s 821f18d74:agents.md` gives 22064 bytes. It calls itself an index and states why it must stay small: "it is deliberately thin: it is loaded into every session on every turn, so P3 applies to it" [shio@821f18d74:agents.md#L61-L62], P3 being "Tokens are a measured budget" [shio@821f18d74:agents.md#L22]. A routing table sends each code area to a file under `docs/agents/` and to a skill [shio@821f18d74:agents.md#L65-L84].

**Skills.** `git ls-tree -r --name-only 821f18d74 -- .claude/skills | grep -c SKILL.md`
gives 11. Nine are authored for this tree and are named in the routing table; the
`roadkeep` skill "ships with the plugin" [shio@821f18d74:agents.md#L267], and
`viglet-ds-pages` was vendored in [shio@d5ce0fcca]. The ignore file calls the skills
directory "lazy-loaded half of agents.md" [shio@821f18d74:.gitignore#L72].

**Settings, hooks and MCP.** `.claude/settings.json` sets "acceptEdits" [shio@821f18d74:.claude/settings.json#L54], allows almost every tool by bare name [shio@821f18d74:.claude/settings.json#L7-L50], and runs one committed launcher, "roadkeep-launch.py" [shio@821f18d74:.claude/settings.json#L61-L94], on SessionStart, PreToolUse and Stop. It enables "roadkeep@alegauss" [shio@821f18d74:.claude/settings.json#L97] and "shio@openviglet" [shio@821f18d74:.claude/settings.json#L98]. `.mcp.json` starts the roadkeep server through the same launcher [shio@821f18d74:.mcp.json].

**Published plugin.** The repository publishes a marketplace entry, "./claude-plugin" [shio@821f18d74:.claude-plugin/marketplace.json], whose plugin carries four skills (`git ls-tree -r --name-only 821f18d74 -- claude-plugin | grep -c SKILL.md` gives 4), three commands and a fragment for a consumer's agent file [shio@821f18d74:claude-plugin/AGENTS.fragment.md].

## 3. Planning governance

The backlog, ledger and rationale are governed by roadkeep, adopted in "adopt roadkeep as the owner of ROADMAP, CHANGELOG and IMPROVEMENTS" [shio@af98be3f0] on 2026-07-30. The rule at the pin is that the three files are written by the tool "and never by" hand [shio@821f18d74:agents.md#L263]; the history was not audited for hand edits.

At the pin `git cat-file -s` gives 29511 bytes for `docs/ROADMAP.md`, 1000042 for
`docs/CHANGELOG.md` and 178920 for `docs/IMPROVEMENTS.md` [shio@821f18d74:docs/CHANGELOG.md].
Larger designs go to `docs/specs/`; the SH74 spec, which set the agent-native direction, says of itself "this one is the constitution" [shio@821f18d74:docs/specs/SH74-agent-native-cms.md#L7].

Before roadkeep the roadmap had drifted into prose. The area file records the measurement: "six of the worst eight were written in the same session that then found the problem" [shio@821f18d74:docs/agents/agent-surface.md#L1502-L1503], after 95 active lines averaging 142 words. The fix was "make the roadmap a queue again" [shio@490a698a0], two days before roadkeep was adopted.

The two configuration sources disagree about how the engine arrives. `roadkeep.toml` says "roadkeep is not vendored here and there is no path to a checkout" [shio@821f18d74:roadkeep.toml#L8]; `agents.md` says "The engine is vendored" [shio@821f18d74:agents.md#L272]. The tree carries an ignore rule for `.roadkeep/` [shio@821f18d74:.gitignore#L106] and an installer [shio@821f18d74:install-roadkeep.cmd], not the engine.

## 4. Gates

**The three suites and the red-suite ledger.** The rule is "A red suite is a stop (SH579)." [shio@821f18d74:agents.md#L168]. A red gate either blocks the next commit or has an entry in `red-suites.json`: "dated, time-boxed, and pointing at the open task that removes it" [shio@821f18d74:red-suites.json#L2]. At the pin the ledger holds three entries, all tied to "SH1072" [shio@821f18d74:red-suites.json#L9] and expiring on 2026-09-28 [shio@821f18d74:red-suites.json#L11]. The rule came from an incident: "the third state cost nineteen commits" [shio@821f18d74:agents.md#L171].

**CI.** The workflow added with SH579 records the incident in its header: "Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4], and "Every other workflow in this directory is" dispatch-only [shio@821f18d74:.github/workflows/suites.yml#L5]. It runs on push to branches 2026.3 and main, on pull requests and by dispatch [shio@821f18d74:.github/workflows/suites.yml#L19-L22]. `agents.md` describes it as one that "runs two of the three on" [shio@821f18d74:agents.md#L175] every push, which is broader than the trigger. A day earlier, the SH527 commit had removed the push and pull-request triggers from two other workflows [shio@d29b83dc8]; its subject is silent on this, and its body says "Workflow configurations for GitHub Actions have been updated to trigger only on manual dispatch" [shio@d29b83dc8].

**The gate runner and its stamps.** `scripts/run-gate.mjs` is "one runner over the gate table" [shio@821f18d74:scripts/run-gate.mjs#L6], in which "the exit code is not swallowed" [shio@821f18d74:scripts/run-gate.mjs#L8-L9]. Each run writes a stamp with the gate, exit code, colour, commit and time [shio@821f18d74:scripts/gate-stamp.mjs#L235-L241] to `.gates/`, which is ignored because "a committed one would let a clone" inherit a claim about a run it never made [shio@821f18d74:.gitignore#L124]. The runner holds a lock per gate because a collision "reported 3 errors over 1092 tests where the tree alone reports 1894" [shio@821f18d74:scripts/run-gate.mjs#L57], and a run in which no suite started is "recorded as INCONCLUSIVE rather than red (SH828)" [shio@821f18d74:scripts/run-gate.mjs#L94].

**Meta-tests.** `cli/test/assertion-debt.test.mjs` enforces "a defect closes with an assertion carrying its id (SH527)" [shio@821f18d74:agents.md#L223]. `cli/test/agents-md-figures.test.mjs` fails a sentence that states an inventory figure uncited, after `agents.md` said "25 mutating paths" when "The scan finds twenty-eight roots" [shio@be9fa3727].

**What the gates do not check.** The command-documentation lint scans "The two files that document how to run this suite." [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L53], namely `agents.md` and `docs/agents/build.md` [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L54-L56]. Skills are outside it (section 6, 2026-08-17).

## 5. Commit practice

**Tool.** Commits go through a script that stages the whole tree and "generates a Conventional-Commits message from the staged diff via the OpenAI API" [shio@821f18d74:agents.md#L241-L242]; agents are told "Don't hand-author" [shio@821f18d74:agents.md#L244]. The agent that makes the change is Claude, and a model from another vendor writes the message from the diff. Agents are told to always pass `-m`, or a docs commit's prose about shipped work is "misread as" a feature [shio@821f18d74:agents.md#L252].

**Unit.** "One task → one commit, and this is the most violated rule in the project." [shio@821f18d74:agents.md#L247]. Batches of two or more tasks go through a loop skill, "a batch of ≥2 tasks must be driven with the" loop [shio@821f18d74:agents.md#L250-L251].

**Messages before and after adoption.** A subject in `type(scope): ` form counts as
conventional. `git log 6bf11b754^ --format=%s | grep -cE '^[a-z]+(\([^)]*\))?!?: '` gives 0;
the same command over `6bf11b754^..821f18d74` gives 1361 of 1668. Subjects carrying an SH
id: 0 before, 1148 after, by `grep -cE 'SH[0-9]+'` over the same ranges. A marker of the
generated style is a body line beginning "- This commit":
`git log 6bf11b754^..821f18d74 --grep='^- This commit' --format=%h | wc -l` gives 326, and
the same over `6bf11b754^` gives 0. The first such body is dated 2026-06-16 [shio@0a60e8a09]
and the last 2026-09-12. The marker undercounts generated bodies, which also open with other
verbs, as in [shio@9b7183ddf].

**Where the generated body diverges from the change.** Two cases were found in this
extraction; no systematic comparison was made. The split commit's body says "New skill files are created for each agent" [shio@f4ffdb0d9], while the eight skills it adds are named for areas of the project, not for agents [shio@821f18d74:agents.md#L65-L84]. The SH788 body says the defect was "leading to misleading results in CI workflows" [shio@c1b9e8947], while the text the same commit adds to `agents.md` says "CI is already honest about this" [shio@821f18d74:agents.md#L161] and "the trap is local" [shio@821f18d74:agents.md#L162].

**Exceptions.** `git log 821f18d74 --grep='^Hand-authored' --format=%h | wc -l` gives 5; one reason given is "the message is a survey of what already exists, which the diff does not contain" [shio@7820e57a7].

**Attribution.** `git log 821f18d74 --grep='^Co-Authored-By: Claude' --format=%h | wc -l`
gives 119, all after adoption, against 1668 commits. `git log 821f18d74 --author='^Claude' --format=%h | wc -l`
gives 55, from 2026-04-11 [shio@c652a2cba] to 2026-08-16 [shio@daecef641], each with a claude.ai
session URL; these are web sessions. The reason most commits carry no trailer is not
stated in the source.

## 6. Timeline

- **2026-03-24.** Adoption: `CLAUDE.md` and a 241-line `agents.md` [shio@6bf11b754]; `git cat-file -s 6bf11b754:agents.md` gives 9843 bytes.
- **2026-04-11.** First commit authored by Claude from a web session [shio@c652a2cba].
- **2026-07-26.** The agent-native pivot, "reorient Shio as an agent-native CMS" [shio@1c45eb8a3], authored from a web session. `agents.md` stands at 40375 bytes the same day [shio@db3edb114].
- **2026-07-28.** The roadmap is made "a queue again" [shio@490a698a0]. `agents.md` stands at 130166 bytes [shio@2424f20e1] and, by the day's last commit, 185734 bytes [shio@e73516a9f]. The file later records this as "P3 violated by the file that declares P3" [shio@821f18d74:agents.md#L283-L285].
- **2026-07-29.** The split into an index, `docs/agents/` and skills [shio@f4ffdb0d9]. `agents.md` falls to 14433 bytes; `git ls-tree -r -l f4ffdb0d9 -- docs/agents` gives 14 files and 184521 bytes, and `git ls-tree -r -l f4ffdb0d9 -- .claude/skills` gives the eight skills the commit adds, 32867 bytes. The split moved the bytes out of the every-turn file; it did not reduce them. After it, `git rev-list --count f4ffdb0d9..821f18d74 -- docs/agents` gives 777 commits, and the area files reach 1730001 bytes at the pin, while `agents.md` reaches 22064. `docs/agents/build.md` goes from 5238 bytes [shio@f4ffdb0d9] to 149685 [shio@821f18d74:docs/agents/build.md].
- **2026-07-30.** roadkeep adopted as owner of the three planning files [shio@af98be3f0].
- **2026-08-02.** A lint requires the documented test command to keep its log [shio@ddec6a424], after a failure that "went into a pipe nobody kept" [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L33].
- **2026-08-06.** "Six corrections shipped half of themselves" [shio@14acb91ce], and "At 246 commits in seven days" [shio@14acb91ce] the commit calls this the "system's expected output" [shio@14acb91ce]. SH527 is implemented the same day by the assertion-debt test [shio@d29b83dc8], which holds the debt as a list because a ceiling "lets one task pay the debt and the next spend it" [shio@821f18d74:cli/test/assertion-debt.test.mjs#L28]. Its first run misread itself: "its own declaration made all forty entries read as asserted" [shio@821f18d74:agents.md#L234-L235]. Also this day, a stage-everything commit carries `sh545.log` [shio@b04ee9187], and 56 seconds later a commit ignores `/*.log` [shio@9553233a2].
- **2026-08-07.** SH579: the red-suite ledger, its test and CI on push [shio@9b7183ddf].
- **2026-08-08.** The committed launcher, because the web harness "never installs marketplace plugins" [shio@c215718bb], so roadkeep's guard was absent there.
- **2026-08-17.** SH788 forbids piping a gate: "Never pipe a gate into" a filter [shio@821f18d74:agents.md#L150], added in [shio@c1b9e8947]. The skill created in the split still pipes the suite into a filter [shio@821f18d74:.claude/skills/shio-build-test/SKILL.md#L17]; `git log --format=%h 821f18d74 -- .claude/skills/shio-build-test/SKILL.md` lists only `f4ffdb0d9`, and the lint of 2026-08-02 does not read skills. The same day: SH802 merges four gate wrappers into one runner [shio@062fbe172]; SH803 is filed on the ground that "a false red is worse than an absent stamp" [shio@be14dab5e]; the SH778 flake is "provoked rather than waited for" [shio@d726a4b8b], and that commit carries `provoke.log.progress`, which `/*.log` did not match and which the next commit removes and ignores [shio@44e6ef232].
- **2026-08-18.** A failed clean "was stamped as the suite's colour, twice (SH828)" [shio@77f9042f0]; the runner gains the inconclusive state.
- **2026-09-13.** SH949: the repository enables its own published plugin, whose skills "were published by, and never loaded in, the repository that wrote them" [shio@d1853cbea]. The rule written into the index: "a plugin skill serves a session driving an instance; a project skill serves a session changing this source tree" [shio@821f18d74:agents.md#L90-L91]. "No name may appear on both" sides [shio@821f18d74:agents.md#L93-L94], and the plugin test checks it [shio@821f18d74:claude-plugin/test/plugin.test.mjs#L291].

**Root log files.** The ignore file says why root logs are ignored: the commit script "stages everything, so a" log named anything else is committed with the fix [shio@821f18d74:.gitignore#L60-L61]. The same happened with bytecode: "one .pyc reached a commit that way (SH46's)" [shio@821f18d74:.gitignore#L117]. Interpretation: the fault is scratch files in the working tree meeting a tool that stages everything; each ignored pattern keeps the history clean without removing the files.

## 7. Metrics

| Figure | Before adoption | From adoption to pin |
|---|---|---|
| Commits | 1778 | 1668 |
| Active days | 433 | 83 |
| Commits per active day | 4.1 | 20.1 |
| Conventional subjects | 0 | 1361 |
| Subjects with an SH id | 0 | 1148 |
| Bodies with a line beginning "- This commit" | 0 | 326 |

Active days are `git log --format=%cs <range> | sort -u | wc -l`; the two periods share
2026-03-24, so they sum to 516 against 515 over the whole history.

Monthly commits from `git log --format=%cs`, split by commit at `6bf11b754`:

| Month | Before | From adoption | Event |
|---|---|---|---|
| 2026-01 | 10 | | |
| 2026-02 | 1 | | |
| 2026-03 | 18 | 4 | `agents.md` added [shio@6bf11b754] |
| 2026-04 | | 114 | first web-session commit [shio@c652a2cba] |
| 2026-05 | | 14 | |
| 2026-06 | | 143 | |
| 2026-07 | | 220 | pivot [shio@1c45eb8a3], split [shio@f4ffdb0d9], roadkeep [shio@af98be3f0] |
| 2026-08 | | 936 | launcher [shio@c215718bb] |
| 2026-09 | | 237 | to 2026-09-24 |

Before adoption the busiest month was 2020-06, with 164 commits. By year, `git log --format=%cs 6bf11b754^ | cut -c1-4 | sort | uniq -c`
gives 93 (2019), 494 (2020), 479 (2021), 381 (2022), 17 (2023), 157 (2024), 128 (2025) and
29 (2026). August 2026 alone, the month after the pivot, split and roadkeep, has more
commits than any year of the project.

`git rev-list --count 821f18d74 -- agents.md` gives 139: 114 up to and including the split, 25 after it.

## 8. What is particular to this case

- It is brownfield: more than six years and 1778 commits of history preceded the agent files, and the pivot of 2026-07-26 redirected an existing product rather than starting one.
- The agent is itself the product's intended user, so agent-facing rules and product rules share a vocabulary; P3 governs both the product's responses [shio@821f18d74:agents.md#L22] and `agents.md` [shio@821f18d74:agents.md#L61-L62].
- The same repository is both a consumer of plugins and a publisher of one, which is what made SH949 necessary.
- Work ran from both a local machine and web sessions; the web harness lacked plugins, which is why a launcher is committed [shio@c215718bb].
- The rate after adoption is about five times the rate before, measured in commits per active day, and 936 commits fell in one month. Interpretation: rules that cite incidents at this rate, such as the half-shipped fixes at 246 commits in seven days, may depend on it.

## 9. Open questions

- How much of the area files a session reads per task cannot be told without transcripts, which are not a source. So whether 1730001 bytes of area files cost a task more or less than 185734 bytes of every-turn file did is not answered at the pin.
- No size limit on `agents.md`, the area files or the skills was found in the test and script trees at the pin. This is the result of one search, not a proof of absence.
- Other skills were not checked exhaustively against the index.
- How often the generated bodies misdescribe their diff is not measured; the two cases in section 5 are found cases, not a rate.
- How often one task, one commit was broken is not counted in any source, though `agents.md` calls it the most violated rule.
- The number and content of untracked root logs at extraction time are outside the pin.
