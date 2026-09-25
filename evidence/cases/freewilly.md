# Case study: freewilly

## 1. Context

freewilly is a free Docker desktop for Windows, written in C# on .NET with WPF: the tray project sets "UseWPF" [freewilly@c1c2eaf:src/FreeWilly.Tray/FreeWilly.Tray.csproj#L8].
It is a greenfield case. Its first commit, `acc7fc1` on 2026-08-12, is also its adoption
commit: it adds the roadkeep launcher hook, `.claude/settings.json`, the vendored roadkeep
skill and the lint workflow in one change [freewilly@acc7fc1]. The pin is `c1c2eaf`, dated
2026-09-17 [freewilly@c1c2eaf]. At the pin, `git rev-list --count c1c2eaf` gives 444
commits, `git log --format=%cd --date=short c1c2eaf | sort -u | wc -l` gives 21 active
days, and `git ls-tree -r --name-only c1c2eaf | wc -l` gives 373 tracked files.

`git log --format=%an c1c2eaf | sort | uniq -c` gives four author names: two spellings of
the owner's name (395 and 19 commits), Claude (12) and dependabot[bot] (18). The house
writing skill states the premise directly: "Every word in this repository was written by a model" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L8].

## 2. Agent surface

**No every-turn instruction file.** `git ls-tree -r --name-only c1c2eaf` lists no
`CLAUDE.md` and no `AGENTS.md`, in any case. The closest thing to a human-facing rule book
is `CONTRIBUTING.md`, 40 lines long [freewilly@c1c2eaf:CONTRIBUTING.md#L1-L40], which
addresses contributors rather than the agent.

**Rules as comments where they are enforced.** Much of the project's rationale sits beside
the mechanism it explains. `.gitignore` is commented throughout
[freewilly@c1c2eaf:.gitignore#L1-L49]: it records that "settings.json IS committed" [freewilly@c1c2eaf:.gitignore#L9]
and why the hook is committed, since "the plugin never installs on Claude Code on the web" [freewilly@c1c2eaf:.gitignore#L12].
It also carries a credential rule where the credential file is excluded: the ignore line "is the only thing keeping it out of a commit" [freewilly@c1c2eaf:.gitignore#L22].
The same pattern holds in `install-roadkeep.cmd` [freewilly@c1c2eaf:install-roadkeep.cmd#L4-L42],
`run-cases.cmd` [freewilly@c1c2eaf:run-cases.cmd#L1-L15], `winwright.json`
[freewilly@c1c2eaf:winwright.json#L1-L7], the CI header
[freewilly@c1c2eaf:.github/workflows/check.yml#L1-L20] and the tests, as in DD115 below.
The sources do not support the stronger statement that rules live *only* in comments: the
skills carry the process rules, and the one-task, one-commit rule is stated there as "the single most violated rule" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L10-L11].
That comment placement is a deliberate house practice, rather than a habit, is an
interpretation.

**Skills.** `git ls-tree -r --name-only c1c2eaf .claude/skills` lists six files in four
skills: `ai-writing-freewilly`, `freewilly-roadmap-docs`, `window-chrome`, and a vendored
roadkeep skill ("the roadkeep skill is a vendored copy" [freewilly@c1c2eaf:.gitignore#L2-L3]).

**Hooks and MCP.** One committed script, `.claude/hooks/roadkeep-launch.py`, runs as `guard`
on SessionStart, PreToolUse and Stop [freewilly@c1c2eaf:.claude/settings.json#L73-L107].
Its docstring states why it exists: "Claude Code on the web has no" [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L9-L10]
plugin command, so the plugin's guard never loads there. It also states "Three rules keep it from ever making things worse" [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L38],
among them "Never block a turn." [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L48] and "Never reach the network." [freewilly@c1c2eaf:.claude/hooks/roadkeep-launch.py#L50].
One MCP server, roadkeep, is declared, through the same launcher [freewilly@c1c2eaf:.mcp.json].

**Settings and permissions.** The committed settings set "acceptEdits" [freewilly@c1c2eaf:.claude/settings.json#L4]
as the default mode and allow 42 entries, starting with bare `Bash` and `PowerShell`
[freewilly@c1c2eaf:.claude/settings.json#L5-L48]; the `deny` and `ask` lists are empty
[freewilly@c1c2eaf:.claude/settings.json#L49-L50]. The roadkeep plugin is enabled
[freewilly@c1c2eaf:.claude/settings.json#L62-L64] and `ROADKEEP_HOME` points at the
vendored engine [freewilly@c1c2eaf:.claude/settings.json#L109-L111].

The design asked what stood in for permission prompts under a local bypass. The bypass
itself cannot be examined: `.claude/*` is ignored and only `skills/`, `settings.json` and
`hooks/` are negated [freewilly@c1c2eaf:.gitignore#L7-L15], and `git log c1c2eaf --format=%h
-- .claude/settings.local.json` returns nothing, so no local settings file was ever
committed. Any claim about a `bypassPermissions` mode is outside the pin. What the pin does
show is that the project treated prompts as a cost to remove and put three committed
controls in their place: a broad allow list, a PreToolUse guard on
`Edit|MultiEdit|NotebookEdit|Write|Bash` [freewilly@c1c2eaf:.claude/settings.json#L85-L95]
whose job is to refuse hand edits of the governed files, and a build test that fails when
either is weakened (DD115, section 6). The install script records the cost it was avoiding: "Every distinct command path is a fresh authorization prompt" [freewilly@c1c2eaf:install-roadkeep.cmd#L12].
The only purpose the pin states for the guard is that one: "roadkeep denies a hand-edit of ROADMAP, CHANGELOG and IMPROVEMENTS through this" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L311]
hook. No committed control is described as limiting other shell commands.

**A token budget on the product's agent-facing output.** `agent-budget.json` is not about
the development agent. It holds "Ceilings on what the agent surface costs, read by AgentBudgetTests" [freewilly@c1c2eaf:agent-budget.json#L5],
where the agent surface is the product's own CLI for agents. Tokens are estimated as "characters / 4, rounded up" [freewilly@c1c2eaf:agent-budget.json#L15].
The canonical task, "bring the stack up and say why the api container is not answering" [freewilly@c1c2eaf:agent-budget.json#L40],
is recorded at 6 calls and 11,711 tokens through the raw transport
[freewilly@c1c2eaf:agent-budget.json#L47-L50] and at 4 calls and 812 tokens through the
shaped surface [freewilly@c1c2eaf:agent-budget.json#L82-L86]. A ceiling may be raised, but "the commit that raises one says what the tokens bought" [freewilly@c1c2eaf:agent-budget.json#L7].
A future MCP head is capped at six tools and 1,100 schema tokens
[freewilly@c1c2eaf:agent-budget.json#L256-L257].

## 3. Planning governance

The backlog is governed by roadkeep with the prefix DD [freewilly@c1c2eaf:roadkeep.toml#L1],
in `docs/ROADMAP.md`, `docs/CHANGELOG.md` and `docs/IMPROVEMENTS.md`; there is no decisions
file (`git ls-tree --name-only c1c2eaf docs/`). CONTRIBUTING says a hand edit of these "is refused rather than reviewed" [freewilly@c1c2eaf:CONTRIBUTING.md#L11-L12].
At the pin the roadmap is drained: blocks A to H carry no task line
[freewilly@c1c2eaf:docs/ROADMAP.md#L5-L19]. `git show c1c2eaf:docs/CHANGELOG.md | grep -c
'^- ✅'` gives 276 shipped entries and the same count for the retired mark gives 4.

Filing is its own commit, separate from shipping, as in "DD112-DD113 file what the container follow-ups turned up" [freewilly@c44801a].
Retirement is used when a filing was wrong or moot rather than editing it: DD117 was
abandoned because "the fix touches a commit tool every repository shares" [freewilly@c1c2eaf:docs/CHANGELOG.md#L201].
Four documents under `docs/specs/` hold longer-lived design; DD23, for example, fixes the
order "CLI first; MCP only if a shell-less client ever matters" [freewilly@c1c2eaf:docs/specs/DD23-agent-first-freewilly.md#L120].

The ledger is not always true at the pin. DD118 is recorded as shipped with "The gate runs the vendored engine beside the action it floats on and prints both versions" [freewilly@c1c2eaf:docs/CHANGELOG.md#L202],
but the lint workflow at the pin only calls the published action
[freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L13-L19]
(`git grep -c roadkeep.py c1c2eaf -- .github/workflows/roadkeep.yml` finds nothing), and the
test that held DD118 was deleted in `cd630d6` [freewilly@cd630d6] and not restored.

## 4. Gates

**CI.** `check.yml` runs on every push and pull request on `windows-latest`; it builds,
tests, publishes the single-file executable and runs it
[freewilly@c1c2eaf:.github/workflows/check.yml#L22-L56]
[freewilly@c1c2eaf:.github/workflows/check.yml#L131-L141]. Of the desktop cases it runs one,
filtered to the preflight page [freewilly@c1c2eaf:.github/workflows/check.yml#L125-L129].
`roadkeep.yml` runs `roadkeep lint` [freewilly@c1c2eaf:.github/workflows/roadkeep.yml#L14-L19].

**Tests that guard the agent configuration.** Two tests in `PackagingTests.cs` read the
committed settings [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L272-L336].
The first asserts a floor of allowed tools, "A floor and not the whole list" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L281],
failing with a message that the file "no longer grants" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L302]
the tool. The second fails if "no roadkeep guard is wired on" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L326]
any of the three hook stages. The budget file is read by `AgentBudgetTests`
[freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/AgentBudgetTests.cs#L41].

**Local only.** The cases outside the solution are run by hand: they are "not in FreeWilly.slnx" [freewilly@c1c2eaf:run-cases.cmd#L15].
The engine install is checked on a virtual machine and not in CI: "It cannot verify the engine install." [freewilly@c1c2eaf:CONTRIBUTING.md#L34].

**What is not checked.** The em-dash rule of the writing skill has no gate. At the pin
`git grep -c -P '\x{2014}' c1c2eaf -- README.md` reports 2 lines, against none at
`c1c2eaf^`: the pinned commit itself added two em dashes to the README
[freewilly@c1c2eaf:README.md#L375-L376]. Nothing checks that a ledger entry still describes
the tree (DD118, section 3), and nothing checks that CONTRIBUTING describes CI (section 6).

## 5. Commit practice

`git log --format=%s c1c2eaf | grep -cE '^[a-z]+(\([^)]*\))?: '` gives 425 of 444
conventional subjects; the other 19 are pull-request merges. With `: DD[0-9]+` appended to
the pattern the count is 325: most subjects name the task, as in "DD112 a fold does not outlive the project it was set on" [freewilly@d01fcb3].
The process skill fixes the unit under the heading "one task, one commit" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L8],
and a request for several tasks "is NOT permission to" [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L20]
batch them. Commits go through `run-commit.cmd`, which stages everything and has
`ai_commit.py` write the body [freewilly@c1c2eaf:.claude/skills/freewilly-roadmap-docs/SKILL.md#L33-L35].
Many bodies are therefore generated bullet lists, as in `646e121` [freewilly@646e121]; some
are hand-written prose, as in `ac7e7ec` [freewilly@ac7e7ec].

**Attribution.** `git log --format=%B c1c2eaf | grep -c '^Co-Authored-By:'` gives 17. Twelve
of them come from one pull request. Pull request #1 merged the branch "alegauss/claude/bloco-h-roadmap-tmtjgk" [freewilly@7968cc5]
on 2026-08-13, and `git log --format=%an 7968cc5^1..7968cc5^2` lists 12 commits, all with
the author name Claude, dated +0000; `git log --format=%ad --date=iso c1c2eaf` shows 414
commits at -0300 and 30 at +0000, which are these 12 and the 18 by dependabot. Each
carries "Co-Authored-By: Claude Opus 4.8" [freewilly@915e22e] and a session link, "Claude-Session: https://claude.ai/code/session_" [freewilly@915e22e].
Each also ships one task, DD40 to DD51, as in "DD40 the workspace, and the landing page ported into it" [freewilly@ba66593].
That these commits came from a Claude Code on the web session is an interpretation: it is
consistent with the claude.ai/code link, the author name and the time zone, but no source
at the pin says so.

## 6. Timeline

- **2026-08-12.** Adoption: the launcher, committed settings and lint workflow arrive with
  the first commit [freewilly@acc7fc1].
- **2026-08-13.** Pull request #1, twelve commits authored by Claude, is merged
  [freewilly@7968cc5].
- **2026-08-14, 15:35.** The engine is vendored under a fixed path, "vendor the engine into .roadkeep and always run that copy" [freewilly@89371b8],
  because floating paths cost a prompt each and one checkout failed with an ImportError
  [freewilly@c1c2eaf:install-roadkeep.cmd#L12-L19].
- **2026-08-14, 17:09.** The DD112 commit also removes 15 lines from
  `.claude/settings.json` [freewilly@d01fcb3], including `Task`, `SendMessage` and
  `CronCreate`. Nothing in that task called for it.
- **2026-08-14, 17:11.** The entries are restored. The message states "The harness rewrote .claude/settings.json mid-session" [freewilly@ac7e7ec]
  and names the carrier as "the deletion rode into 46ec80f alongside DD112" [freewilly@ac7e7ec];
  no commit `46ec80f` exists, and the carrier was `d01fcb3`, the parent of `ac7e7ec`. It was
  the second trim in that session, and "the first was caught before a commit" [freewilly@ac7e7ec].
  Mechanism produced: DD115, filed eight minutes later [freewilly@5e41114].
- **2026-08-14, 18:08.** "DD115 the committed agent configuration is guarded" [freewilly@646e121].
  The test comment records the incident: "Twice in one session fifteen entries vanished from" [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L277]
  the allow list. The ledger frames the cause as settings that are "rewritten by whatever session is open" [freewilly@c1c2eaf:docs/CHANGELOG.md#L199];
  neither source establishes which component did the rewriting, and none records the
  harness version. `git log c1c2eaf -- .claude/settings.json` shows no change to the file
  after `ac7e7ec`.
- **2026-08-14, 18:18 to 18:28.** The same evening produces DD116, where "ROADKEEP_HOME arrives unexpanded" [freewilly@c1c2eaf:docs/CHANGELOG.md#L200]
  [freewilly@d1f00b9]; DD117, filed and retired [freewilly@74fd721], its stray-file half
  closed by a `.gitignore` rule because "run-commit.cmd stages" [freewilly@c1c2eaf:.gitignore#L47]
  everything; and DD118, which adds the vendored engine to the lint gate [freewilly@956e91e].
- **2026-08-19.** The lint workflow is deleted, "workflow as it is no longer needed" [freewilly@cd630d6],
  together with the DD118 test. The same commit rewrites CONTRIBUTING to say "Run it yourself before pushing" [freewilly@c1c2eaf:CONTRIBUTING.md#L13]
  and that the lint gate "every push was removed" [freewilly@c1c2eaf:CONTRIBUTING.md#L31-L32].
  No task id and no reason beyond that phrase is given.
- **2026-08-25.** DD184: "207 of them, and two in every three sentences" [freewilly@0794e60],
  counting em dashes across the site copy, the README and `llms.txt`. The same commit creates
  the writing skill, which "records the rule so the next session does not restore the dashes" [freewilly@0794e60];
  the skill's heading is "No em dashes in published prose" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L30].
  DD185 later removed 62 of the 64 in the strings the product prints [freewilly@f2e6617]
  [freewilly@c1c2eaf:docs/CHANGELOG.md#L295].
- **2026-08-29.** Lint returns: "put lint back in CI" [freewilly@714360e]. The CI header now
  says drift arriving by other routes is caught, "drift arriving by any other route, which for a while reached" [freewilly@c1c2eaf:.github/workflows/check.yml#L15]
  main. CONTRIBUTING was not updated: `git log --oneline 714360e..c1c2eaf -- CONTRIBUTING.md`
  prints nothing, and at the pin it still says "CI no longer does" [freewilly@c1c2eaf:CONTRIBUTING.md#L13-L14]
  and counts "Two workflows" [freewilly@c1c2eaf:CONTRIBUTING.md#L21], while
  `git ls-tree --name-only c1c2eaf .github/workflows/` lists four.
- **2026-09-17.** The pinned commit records a screen capture that "photographed the guest's WALLPAPER, and passed" [freewilly@c1c2eaf];
  the case now waits for the menu to report an entry, and CI is filtered away from it
  because "a case nobody has run there is not a gate" [freewilly@c1c2eaf].

## 7. Metrics

From [../corpus.md](../corpus.md): 444 commits, first commit and adoption both `acc7fc1` on
2026-08-12, 21 active days, greenfield. Grouping `git log --format=%ad --date=short c1c2eaf`
by day gives 92 commits on 2026-08-14, the busiest day, and 63 on 2026-08-29, the next.
The agent surface at the pin is four skills in six files, one hook script on three events,
one MCP server and four specs (`git ls-tree --name-only c1c2eaf docs/specs/`). The Preflight
test project has 93 tracked files (`git ls-tree -r --name-only c1c2eaf
tests/FreeWilly.Preflight.Tests | wc -l`).

The project measured two things itself. The agent budget records 11,711 tokens for the
baseline task and 812 for the shaped surface (section 2), and `git log --format=%h c1c2eaf --
agent-budget.json | wc -l` gives 18 commits to the budget file. DD184 counted 207 em
dashes before removing 201 of them [freewilly@c1c2eaf:docs/CHANGELOG.md#L293].

## 8. What is particular to this case

- The project is itself a product for agents. Its budget file measures what an agent pays
  to use the product, which is a different object from the development harness, and the
  two should not be conflated when this case is compared with others.
- There is no every-turn instruction file, so the agent meets the project's rules through
  skill descriptions, hook messages, test failures and comments, not through a file loaded
  at every turn.
- The DD115 incident reached a commit through a commit tool that stages everything, as the
  test comment says [freewilly@c1c2eaf:tests/FreeWilly.Preflight.Tests/PackagingTests.cs#L278-L279].
  The project chose not to change that shared tool and retired DD117 in favour of DD115 and
  a `.gitignore` rule [freewilly@c1c2eaf:docs/CHANGELOG.md#L201]. That the trim would
  otherwise have stayed in the working tree is an interpretation.
- Some committed rationale was carried in from another repository. The install script says "NEITHER this repository nor freewilly is a Python" [freewilly@c1c2eaf:install-roadkeep.cmd#L30]
  project, naming freewilly as if it were a different repository; reading this as a copied
  comment is an interpretation.
- The history is short and dense: five weeks, with 92 commits on the day of the settings
  incident.

## 9. Open questions

- What rewrote `.claude/settings.json` on 2026-08-14, and in which harness version? The
  commit attributes it to the harness; the test and the ledger attribute it to an open
  session. Neither is measured.
- What, if anything, was set in `.claude/settings.local.json`, and in which sessions? No
  version of the file was committed.
- Why was the lint workflow removed on 2026-08-19? The commit says only that it was no
  longer needed.
- Was pull request #1 produced in a Claude Code on the web session, and did the committed
  launcher guard it? The trailer links a session but records no environment.
- Has the DD115 test ever failed? No change to the settings file after `ac7e7ec` is in the
  history, so the pin shows no occasion on which it could have.
