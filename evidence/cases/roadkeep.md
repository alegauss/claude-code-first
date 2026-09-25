# roadkeep: case study

## 1. Context

roadkeep is a Python command-line tool and Claude Code plugin that owns the writes to a
project's planning files, so that their format is a schema applied at insertion rather than
a convention the author must remember [roadkeep@91754240:agents.md#L3-L5]. Its problem was measured in another corpus project, Shio: "92 roadmap lines averaging" [roadkeep@91754240:agents.md#L7]
142 words against a one-sentence rule, and an `agents.md` of 186 KB.

The case is greenfield. The first commit and the adoption commit are both dated 2026-07-29
([roadkeep@020d8413], [roadkeep@00a59e0e]), and the history at the pin holds 1,946
commits over 45 active days (see [../corpus.md](../corpus.md)). The pin is `91754240`,
committed on 2026-09-24 [roadkeep@91754240]. At extraction the working tree also held a
staged, uncommitted merge of a `gui/` tree; nothing under `gui/` is in the pinned history,
so no claim below rests on it.

## 2. Agent surface

The Claude Code entry point, `.claude/CLAUDE.md`, is 10 lines and 77 words and only points
at the shared file: "All project guidelines, conventions and design laws are in the shared agents file:" [roadkeep@91754240:.claude/CLAUDE.md#L3-L5].
It sits under `.claude/` because "this repository is the plugin, so every root file ships in the payload" [roadkeep@91754240:.claude/CLAUDE.md#L7-L9].
The rules are in `agents.md`, 113 lines and 1,120 words at the pin
[roadkeep@91754240:agents.md]. It states six laws, and "a change breaking one is wrong even if requested" [roadkeep@91754240:agents.md#L18].
Its last section holds that "What loads every turn is only what a turn touching no governed file needs." [roadkeep@91754240:agents.md#L111]

Three files are committed under `.claude/`: the pointer, a 181-byte `settings.json` that
enables the project's MCP server and adds one directory, with no hooks and no allow rules
[roadkeep@91754240:.claude/settings.json], and one project skill,
`roadkeep-dev`, which says it is "Trigger-loaded, and that is the whole reason it is a file (RK23, RK1136)." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L8]

The plugin surface is the repository itself: "This repository *is* the plugin, so a push to main is the release." [roadkeep@91754240:.github/workflows/gate.yml#L12]
It ships three hooks, all running one `guard` command, on `SessionStart`, on `PreToolUse`
for `Edit|MultiEdit|NotebookEdit|Write|Bash`, and on `Stop`
[roadkeep@91754240:hooks/hooks.json#L3-L35]; a skill in three files, an orientation of 165
lines with two reference pages of 607 and 295 lines (`git grep -c "" 91754240 -- skills/roadkeep`
gives 165, 607 and 295); four slash commands (`git grep -c "" 91754240 -- commands` lists
four files); and an MCP server with a declared ceiling, "session = 69665" [roadkeep@91754240:roadkeep.toml#L232].

**The guard.** Its module docstring sets out the design. An edit or write to a governed
file is denied with the command to call instead, because "a refusal that names no alternative is a refusal an agent works around" [roadkeep@91754240:src/roadkeep/guarding.py#L14-L15].
The guard never grants anything: "Silence is the allow." [roadkeep@91754240:src/roadkeep/guarding.py#L24]
Emitting allow would override the user's permission rules, and "a guard that widens what an agent may write is worse than no guard" [roadkeep@91754240:src/roadkeep/guarding.py#L26-L27].
Its own errors never block: "Every failure allows." [roadkeep@91754240:src/roadkeep/guarding.py#L28]
The reason: "A guard that denies on its own errors turns one typo" [roadkeep@91754240:src/roadkeep/guarding.py#L29]
into a repository nobody can edit, and the commit gate is the backstop. It also "always exits 0" [roadkeep@91754240:src/roadkeep/guarding.py#L45-L47], since the
harness reads a non-zero exit as a failed hook. Two qualifications apply to the design as
the backlog states it. A `Bash` command is not denied: where it names a governed
path it is answered with ask [roadkeep@91754240:src/roadkeep/guarding.py#L32-L33]. And since
RK1689, "Git staging or reading a governed file passes the guard in silence" [roadkeep@91754240:docs/CHANGELOG.md#L1136].

## 3. Planning governance

roadkeep governs its own planning files, which serve as its conformance fixture: `roadkeep lint`
"must pass on" [roadkeep@91754240:agents.md#L79] the repository's `docs/`. At the pin
`docs/ROADMAP.md` is 163 lines [roadkeep@91754240:docs/ROADMAP.md], and an entry there is
one sentence of what, why and pointer, at most 320 characters, "never a solution name" [roadkeep@91754240:docs/ROADMAP.md#L17-L21];
work is picked as "the lowest-numbered task whose" [roadkeep@91754240:docs/ROADMAP.md#L21]
dependencies have all shipped. The ledger `docs/CHANGELOG.md` is 1,238 lines, with 1,170
shipped and 24 retired entries (`git grep -c "^- ✅" 91754240 -- docs/CHANGELOG.md` gives
1170, and the same count for the retired marker gives 24) [roadkeep@91754240:docs/CHANGELOG.md].
`docs/IMPROVEMENTS.md` holds rationale for unshipped work only: "When a section ships, delete it here." [roadkeep@91754240:docs/IMPROVEMENTS.md#L3-L5]
In `docs/DECISIONS.md`, "A decision is superseded once, and both entries stay" [roadkeep@91754240:docs/DECISIONS.md#L8].

Field limits are set at "the P90 of the lines that already read well, which is an agent attention budget" [roadkeep@91754240:roadkeep.toml#L48].
Because shipping deletes a rationale section, the incidents in section 6 are read from
`docs/IMPROVEMENTS.md` at the commits that filed them.

## 4. Gates

CI runs the repository's own lint action, "uses: ./" [roadkeep@91754240:.github/workflows/gate.yml#L33],
pytest on Python 3.11 and 3.13 with full history as a fixture [roadkeep@91754240:.github/workflows/gate.yml#L43-L51],
and `claude plugin validate --strict` at a pinned CLI version, "2.1.220" [roadkeep@91754240:.github/workflows/gate.yml#L71].
The every-turn files are held by the gate, not by prose: lint exits 1 on an "over-budget every-turn file" [roadkeep@91754240:agents.md#L83],
and the budget is "lines = 125, bytes = 8400" [roadkeep@91754240:roadkeep.toml#L249].
The trigger-loaded skill is held by a test instead, "ORIENTATION_MAX = 13_000" [roadkeep@91754240:tests/test_skill.py#L136]
in UTF-16 code units, with one ceiling per reference page from "PAGE_MAX = {" [roadkeep@91754240:tests/test_skill.py#L155].

Locally, `.githooks/pre-commit` bumps the patch version and "It never blocks a commit." [roadkeep@91754240:.githooks/pre-commit#L12]
The `Stop` hook runs lint and, since RK175, a check for governed bytes no verb wrote
[roadkeep@91754240:src/roadkeep/guarding.py#L39-L41].

What the gates do not check is stated in the sources. The round-trip property test over
Shio's and Turing's files skips when those corpora are absent, "which is what CI does" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L26].
A shell write to a governed file is put to the user rather than refused
[roadkeep@91754240:src/roadkeep/guarding.py#L32-L33]. By law L4 nothing checks the
content of a sentence, only its shape [roadkeep@91754240:agents.md#L25].

## 5. Commit practice

The rule is "One task → one commit, the instant it is validated." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L61-L62]
Commits go through a user-level tool, `run-commit.cmd -m`, for which "the title is yours and only the body is generated" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L67].
Of that tool the skill says "It stages everything." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L69]
This is why each write prints the `git add --` line for what it wrote, with the instruction
"Run that line, then commit." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L73]
Filing new tasks is its own documentation commit, as in "docs: file block J, validation, with RK1690-RK1694" [roadkeep@9ecfa187].

Subjects follow Conventional Commits in 1,938 of 1,946 commits, the remainder being merges
and three untyped commits (`git log 91754240 --format=%s`, matched against a type prefix).
The task id's place in the subject changed three times [roadkeep@7068a102] [roadkeep@5345a5bb]
[roadkeep@8ec64f2b] [roadkeep@f7333f42].

**Attribution.** A `Co-Authored-By` trailer appears on 76 commits
(`git log 91754240 -i --grep=Co-Authored-By --format=%h | wc -l` gives 76), from
2026-07-29 [roadkeep@40847570] to 2026-09-01 [roadkeep@595894af], and on none of the 423
commits after it (`git rev-list --count --after=2026-09-01T07:18:59 91754240` gives 423).
The design names this a change of attribution policy around 2026-09-01. The pinned sources
do not support that as stated. No committed file or commit message found states an attribution
policy; the words co-authored and attribution occur in the tree, outside the tests, only in
the licence and one unrelated rendering comment. The trailer was also rare before the date: 76 of
the 1,523 commits up to and including [roadkeep@595894af]
(`git rev-list --count --before=2026-09-01T07:19:00 91754240` gives 1523). The source supports only
that an intermittent trailer stopped after 2026-09-01. A rule against attribution exists in
the staged `gui/` skill the extraction saw, which is outside the pin. (Interpretation.) 69 of the 76 trailered commits have bodies with
no hyphen-led line, against 124 of all 1,523 commits to that date, counted by testing each
body with `grep -q '^- '`. The generated bodies in this history are bulleted lists, as in
[roadkeep@13272828], so the trailer may have marked commits composed without that tool
rather than a policy in force.
Four commits are authored under the name Claude, on 2026-08-01 and 2026-08-08
(`git log 91754240 --author=Claude --format=%h` gives four, among them [roadkeep@7b653977]
and [roadkeep@372c52a7]).

## 6. Timeline

- **2026-07-29, the guard.** RK22 recorded that "An agent can hand-edit the file the CLI is supposed to own" [roadkeep@91754240:docs/CHANGELOG.md#L969].
  The commit to "deny the agent's hand-edit of a governed file, naming the command instead" [roadkeep@cf99c0a9]
  added the `PreToolUse` refusal and the `Stop` lint.
- **2026-07-29, the budget.** RK30 moved the every-turn budget out of prose: "hold the every-turn file to a declared budget" [roadkeep@13272828].
  The configuration records why: the prose arrangement "that let Shio's reach 186 KB while declaring 150 lines about itself." [roadkeep@91754240:roadkeep.toml#L235-L237]
  It counts bytes as well because "a line budget alone is met by writing longer lines" [roadkeep@91754240:roadkeep.toml#L239].
- **2026-07-30, the skill.** RK23, "Rules resident every turn spend the budget they exist to protect" [roadkeep@91754240:docs/CHANGELOG.md#L970],
  moved the write path "out of the resident file and into a trigger-loaded skill" [roadkeep@24e6fcda].
- **2026-08-03, the shell.** RK128 recorded that "The guard denies Edit and Write and answers silence to a shell command writing the same file" [roadkeep@91754240:docs/CHANGELOG.md#L989],
  and the guard began answering a matching `Bash` command with ask [roadkeep@e1d8056b].
  The same day RK175 addressed that "An approved shell write leaves a valid line and no record of who wrote it" [roadkeep@91754240:docs/CHANGELOG.md#L993]
  [roadkeep@3112274d].
- **2026-08-03, the first measurement.** RK203 put a test on the layout index in `agents.md`
  [roadkeep@43d41f95], and its ledger entry concludes that "the measurement says compress the prose first" [roadkeep@91754240:docs/CHANGELOG.md#L546].
- **2026-08-04, concurrent sessions.** RK280 was filed from an observed case: "Observed, not imagined." [roadkeep@64195176:docs/IMPROVEMENTS.md#L126]
  Two commits shipping RK244 and RK279 [roadkeep@a0c6f6ca] [roadkeep@767d3ebb] each carried
  work of another task, "sessions, two commits, each holding the other's work, both green" [roadkeep@64195176:docs/IMPROVEMENTS.md#L129].
  The gap named was that "nothing denies staging a file it does not" [roadkeep@64195176:docs/IMPROVEMENTS.md#L136]
  own. The mechanism produced was "a claim carries the paths its commit owns" [roadkeep@3655014c].
- **2026-08-05, the version bump.** RK320 recorded that "another agent had edited" [roadkeep@b16ce40f:docs/IMPROVEMENTS.md#L187]
  the plugin manifest and "the key removal landed under that commit's message" [roadkeep@b16ce40f:docs/IMPROVEMENTS.md#L190],
  because the hook staged the whole file to write the version into it. The fix: "It stages only what it wrote (RK320)." [roadkeep@91754240:.githooks/pre-commit#L15]
  [roadkeep@1a4c1aef].
- **2026-08-07, the hook that re-armed itself.** The RK320 check read the hook's own bump as
  a foreign edit, so "it re-armed itself for ever" [roadkeep@91754240:.githooks/pre-commit#L20];
  RK398 made it a comparison against the index [roadkeep@33a9dc29].
- **2026-08-11, the reversal.** The file reached "budget --file agents.md answers 125 of 125, 0 left" [roadkeep@a3ecd54c].
  RK1092 added a per-section reading, and "the first reading says the Layout index is 37 percent of agents.md rather than the 23 RK203 recorded" [roadkeep@91754240:docs/CHANGELOG.md#L656].
  RK1094 reversed the advice: "the index is 36 percent and the cheap cut, not the prose" [roadkeep@91754240:docs/CHANGELOG.md#L657]
  [roadkeep@c6464dd6]. The configuration keeps the record: "the cheap cut, and it is the safe one" [roadkeep@91754240:roadkeep.toml#L246].
- **2026-08-13, back to the prose.** RK1135 compressed the file sentence by sentence
  [roadkeep@e3d27ce4] and "measured the prose and the index both at their density floor" [roadkeep@91754240:docs/CHANGELOG.md#L666].
  The same commit wrote the sentence that closes `agents.md` at the pin: "the index is a fifth of it, held by a test, so the prose is what to compress (RK203, RK1135)." [roadkeep@91754240:agents.md#L112-L113]
- **2026-08-13, the second skill.** RK1136, "26 lines of the every-turn file are needed only on a turn that builds or commits" [roadkeep@91754240:docs/CHANGELOG.md#L667],
  moved building and committing to the project skill, after which "the every-turn file dropped to 104 of 125 lines and the pointer is what stays" [roadkeep@91754240:docs/CHANGELOG.md#L667]
  [roadkeep@b12d28b5].
- **2026-08-13, the stage line.** RK1117 was measured while shipping RK1112, when a
  concurrent session had filed RK1116 [roadkeep@043da6c0:docs/IMPROVEMENTS.md#L87]:
  "Another task's filing landed under this task's" [roadkeep@043da6c0:docs/IMPROVEMENTS.md#L99]
  message. The fix makes a departure name the file it wrote that it does not explain
  [roadkeep@678e35d6], and RK1120 names the other ids that moved in a staged file
  [roadkeep@bf101979].
- **2026-08-31, the orientation.** RK1437 found that "the skill names all 44 verbs and costs 65k units a turn" [roadkeep@91754240:docs/CHANGELOG.md#L1099],
  and split it into an orientation and two pages [roadkeep@0d756a9a]; "the split landed at 11,148 against 65,885 before it" [roadkeep@91754240:tests/test_skill.py#L133].
- **2026-09-09, the pages.** RK1643 answered that "RK1437 gave the ceiling to the half that shrank and left these two unbounded" [roadkeep@91754240:tests/test_skill.py#L144]:
  each page got its own ceiling, and "a page past it is a page to split" [roadkeep@91754240:docs/CHANGELOG.md#L824].
  The commit, "give each reference page a cadence ceiling of its own" [roadkeep@d849f061],
  does not name RK1643; it is the commit that added the ledger entry
  (`git log 91754240 -S"Each page carries its own figure beside" -- docs/CHANGELOG.md` gives only `d849f061`).
- **2026-09-21, fewer prompts.** RK1689 stopped the guard asking about git staging and
  reading of governed files [roadkeep@054faeed].

## 7. Metrics

Commits number 1,946 (`git rev-list --count 91754240` gives 1946). At the pin: `agents.md` is
113 lines under a 125-line, 8,400-byte budget [roadkeep@91754240:roadkeep.toml#L249];
`.claude/CLAUDE.md` is 10 lines under "lines = 12, bytes = 800" [roadkeep@91754240:roadkeep.toml#L253];
the plugin is "0.2.491" [roadkeep@91754240:.claude-plugin/plugin.json#L4]. The test suite
holds 5,104 test functions (`git grep -h -E "def test_" 91754240 -- tests | wc -l` gives
5104). Of all subjects, 1,655 carry an RK id (`git log 91754240 --format=%s`, counted for
an RK number).

The project recorded its own context measurements, cited in section 6; RK203's index share
was "figure was ~23% of the bytes" [roadkeep@91754240:roadkeep.toml#L243]. The two readings
of that share at the pin disagree in unit and in conclusion. The test that holds it measures lines,
"assert 15 <= share <= 30, share" [roadkeep@91754240:tests/test_linting.py#L361], and the
fenced index is 35 of the file's 113 lines (`git show 91754240:agents.md | sed -n 32,66p | wc -l`
gives 35), at the test's upper bound. The configuration measures bytes and calls the index
the cheap cut [roadkeep@91754240:roadkeep.toml#L242-L248], while `agents.md` calls the
prose the thing to compress [roadkeep@91754240:agents.md#L112-L113]. The sources support the reversal of RK203 by RK1094, but RK1135 restated the RK203 advice
two days later, so at the pin the reversal is not the last word. (Interpretation.) The
difference of unit may explain the disagreement; no source says so.

## 8. What is particular to this case

**Subject and instrument.** roadkeep is one of the five cases and also the tool that writes
this specification's own governed files: this repository's development guide reserves them
to it ([../../agents.md](../../agents.md)). The project's premise was measured in Shio
[roadkeep@91754240:agents.md#L7], and by RK21 the format was carried by other repositories of
the same owner: "Turing and Dumont each carry their own roadkeep.toml" [roadkeep@3403939d].
An observation of roadkeep's format in another case is therefore not independent of this one.

**Laws are design, not findings.** The six laws in `agents.md` are the specification of one
tool, declared binding in advance [roadkeep@91754240:agents.md#L16-L27] and justified in its
own rationale [roadkeep@91754240:docs/IMPROVEMENTS.md#L35-L44]. They state what the tool was built to do, not that the practice worked; the incidents in
section 6 are the observations.
The risk for the cross-case analysis is that a rule stated with the force of "a change breaking one is wrong even if requested" [roadkeep@91754240:agents.md#L18]
is read as a result.

**The product is the governance.** The every-turn budget, for instance, is both a rule of
this repository and a check its lint ships to adopters [roadkeep@91754240:agents.md#L83].
(Interpretation.) Rules of this kind may be denser here than the project's own needs
require, because each is also a feature under test.

**Scale and speed.** The case has the most commits of the greenfield cases over 45 active
days (see [../corpus.md](../corpus.md)). Each of the three staging incidents records a
second session or agent at work in the same checkout
([roadkeep@64195176:docs/IMPROVEMENTS.md#L129], [roadkeep@043da6c0:docs/IMPROVEMENTS.md#L87],
[roadkeep@b16ce40f:docs/IMPROVEMENTS.md#L187]).

## 9. Open questions

- Whether the index or the prose is the part of `agents.md` to compress next: the sources at
  the pin give both answers (section 7).
- Why the attribution trailer stopped after 2026-09-01. The pinned history shows the stop
  but no rule; the only rule seen is outside the pin.
- Who composed which commit. The owner's name is on almost every commit and the trailer is
  intermittent, so git metadata cannot separate the agent's work from the person's.
- How often the guard's deny and ask answers fired, and what the agent did next. The
  sources read for this case hold no log of them, and session transcripts are not a source
  in this study.
- Whether the concurrency remedies (claimed paths, printed stage lines, the narrowed bump)
  ended the incidents. An incident nobody filed leaves no trace in these sources.
