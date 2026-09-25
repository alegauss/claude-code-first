# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

### §CCF63 A quote checked as written

Found while verifying the field notes (CCF11). `scripts/resolve_citations.py` strips
inline code spans from a line before it matches pointers, so a quote that contains a
backticked name loses those words and can no longer be checked as written; the winwright
verifier rewrote such quotes. It also compares whitespace-normalised text only, so a
quote spanning several lines of a C# `///` comment, or two JSON strings, never matches,
and verifiers split those into one pointer per line. Worse, a quote wrapped onto the
line before its pointer is not read as a quote at all, so it passes unchecked and
nothing reports it; CCF12 met this. Match the quote across a line break too. Build: skip
only pointers that lie inside a code span, rather than deleting the spans before
matching, and let the quote keep its backticks; when comparing, drop a leading comment
marker (`///`, `//`, `#`, `*`) from each source line of the range. Add test cases for
both, and re-run the resolver on the five notes, which must stay green.

### §CCF64 A resolver fast enough to run on every commit

Found while writing the validity threats (CCF12): a full run of
`scripts/resolve_citations.py` over the 795 pointers in `evidence/` took about five
minutes on the owner's machine, because every pointer spawns three to five `git`
processes (`rev-parse`, `merge-base`, `show`, `log`). Each field note that joins the
corpus, and every chapter of the spec, adds hundreds more, so the gate will soon be the
slowest thing a commit waits for and the first one skipped. Build: group pointers by
project, resolve every commit and blob through one long-lived `git cat-file --batch`
process per repository, cache the ancestor check and each file's lines by commit, and
keep the output and exit codes as they are. Measure the run before and after and record
both figures in the commit.

## Block C — Case studies and the findings register

### §CCF20 The findings register

`evidence/findings/` holds one file per finding, with a stable identifier in its own
namespace distinct from the backlog prefix, a one-sentence claim, the mechanism, every
supporting observation per project as resolvable citations, counter-evidence, the grade
on both axes, and the harness facts it depends on. Findings are synthesised across the
case studies rather than copied from one: "every-turn instruction files grow until a
gate caps them" merges roadkeep RK30, Shio's 186 KB and winwright's WW69. A generated
index lists findings by grade and topic. A finding may be withdrawn but is never
deleted, so a rule that cited it can still be traced after it falls.

### §CCF21 Resolving divergent practice

Enumerate every divergence the case studies expose. Co-Authored-By trailers are present
in Shio and freewilly, dropped by policy in roadkeep, and absent in winwright and
polyweave. The every-turn file is a pointer to agents.md in roadkeep and Shio, a
CLAUDE.md in polyweave, and absent in freewilly and winwright. Permissions range from
blanket allows with local bypass to scoped rules. CI runs full tests in roadkeep, lint
only in polyweave and the host half in winwright. Commit bodies are written by the agent
or by another model. For each divergence, record a decision through `ship --decides` in
`docs/DECISIONS.md`, with a body weighing the alternatives against the evidence, and
allow a documented deviation where the evidence cannot decide.

### §CCF22 A drift inventory

`evidence/drift.md` lists each place where two artefacts of one project state
contradictory facts at the pinned commit: freewilly's CONTRIBUTING describing a CI lint
removal that `714360e` undid; Shio's agents.md saying the suites run on every push while
suites.yml runs only on 2026.3, main, pull requests and dispatch
(evidence/cases/shio.md); Shio's build skill piping a gate into grep, which agents.md
forbids; Shio's `roadkeep.toml` header denying the vendoring that agents.md describes;
roadkeep's roadkeep.toml calling the index the cheap cut while agents.md says the prose
is what to compress (evidence/cases/roadkeep.md); polyweave's audit skill naming blocks
A to H and three governed files where the pin has J and four
(evidence/cases/polyweave.md); polyweave's five non-goals, which match at the pin (the
sixth was uncommitted, so drop it unless a later pin shows it); freewilly's ledger
listing DD118 as shipped while cd630d6 deleted its gate and 714360e never restored it
(evidence/cases/freewilly.md); and freewilly's DD23 law overridden by `4575583` without
amendment. For each: the two loci, how long the contradiction has stood, and whether any
check could have caught it. The inventory supports the rule that a fact lives in one
place, and feeds the realignment of those projects in Block H.

### §CCF23 Reproducible corpus metrics

A script under `tools/` that, given the corpus pins, computes for each project: commits,
active days, commits per active day, the share of conventional commits and of commits
carrying a task id, bytes and estimated tokens loaded on every turn (every-turn files,
skill descriptions, MCP schemas where measurable), ledger counts (shipped, retired,
open, deferred), test count, and the share of commits with Co-Authored-By. Its output is
data (JSON and CSV) committed with the pin it was computed at, and every figure the spec
quotes is generated from it, never typed: freewilly's `llms.txt` said four where there
were five, and Shio's agents.md said 25 where there were 28. The token estimate states
its method; freewilly divided characters by four.

## Block D — The normative specification

### §CCF24 The specification's frame

Create `spec/` with an introduction (scope, audience, how to read), a
conformance-language section adopting RFC 2119 and RFC 8174, the rule format and the
chapter list. A rule has a stable address in its own namespace, distinct from the
backlog prefix; a keyword (MUST, SHOULD, MAY); one normative sentence; a rationale
paragraph; the findings it rests on; its conformance level; and whether it is checked
automatically. Rules are never renumbered, and a withdrawn rule keeps its address with a
status. Planned chapters: instruction surface and context economy; planning governance;
change discipline; verification gates; guards and hooks; permissions and safety;
environment portability; agent-facing product surfaces; the human role; concurrent
sessions; agent-written prose. Each chapter opens with the problem it answers, stated
from the findings.

### §CCF25 A glossary of terms

`spec/glossary.md` defines each term once and links its first use: Claude-Code-first
project; every-turn file; trigger-loaded skill; governed file; ledger; rationale
section; decision record; gate, a check whose failure stops the work; guard, a hook that
refuses an action at the moment it is attempted; verdict, including the third verdict,
could not run; red-suite exception; claim; deferral; realignment; conformance level;
waiver. Where the corpus uses a term inconsistently, such as a block closed versus a
block empty, the entry says which meaning the spec adopts and cites the variants. Rules
use defined terms only, and a check reports a term that a rule uses and the glossary
lacks.

### §CCF26 Chapter: instruction surface and context economy

Rules to derive and grade from the findings: the every-turn file is an index with a
budget that a gate enforces (roadkeep RK30; Shio's 186 KB; winwright WW69); procedures
are trigger-loaded skills whose descriptions name their trigger words; a skill is an
orientation plus reference pages opened on demand, each with a ceiling (RK1437, RK1643);
every artefact a skill names is checked against the code (winwright
`SkillTests.cs:16-18`); a fact lives in one file and the others point to it (winwright's
roadmap-docs skill; Shio agents.md L268-269); moving text out of the every-turn file
does not lift the obligation to bound it (Shio's `docs/agents/` at 1.73 MB); and MCP
tool schemas count as every-turn cost (RK1059; freewilly DD33).

### §CCF27 Chapter: planning governance

Rules stated so that another tool could satisfy them, with roadkeep named as the
reference implementation: planning files are written through a tool that enforces their
schema, and a hand edit is refused (roadkeep L1; Shio's lines averaging 142 words,
SH341); a task states a falsifiable symptom, never a solution; rationale is bounded and
deleted when the work ships; decisions outlive the work and are superseded, not deleted;
a block is finished by stated criteria, not by an empty count (winwright's six
reopenings); non-goals are read before work is proposed; work waiting on a person or on
absent resources is deferred, not left open (polyweave `DEFERRED.md`); a false premise
is restated or retired, never silently rewritten (freewilly DD195, DD268). Separate what
the evidence makes a MUST from what only one tool's design motivates.

### §CCF28 Chapter: change discipline

Rules: one task, one commit, carrying the code, the tests and the planning-file writes
together (Shio L247; roadkeep's dev skill); a batch is worked one task at a time with a
check in between (the `/loop` practice; freewilly's self-check); staging is by path, or
the working tree is kept clean by ignore rules before any stage-everything tool runs
(Shio `b04ee918`, `44e6ef232`; freewilly DD117; roadkeep RK280); the commit title states
intent rather than being inferred from the diff; follow-up work discovered is named in
the commit and filed, while a task that revealed nothing files nothing (roadkeep
`35fc90c2`); the commit says whether downstream adopters are affected (winwright
`7a37e95`). Attribution and who writes commit bodies follow the recorded divergence
decisions.

### §CCF29 Chapter: verification gates

Rules: the agent runs the project's gates before committing, and a red gate stops the
work (Shio SH579); a gate's exit code and full log are kept and never filtered through a
pipe (Shio agents.md L150-155, where `fail 2` printed above `EXIT=0`); a check that
could not run is a third verdict, never a pass (winwright's skill, L71); discovered and
executed tests are compared (winwright WW117: 352 of 374); a known red suite is an
expiring exception tied to a task (Shio `red-suites.json`); CI runs on every push, and
runs only checks whose verdict somebody can act on (winwright `7a37e95`); a defect
closes with an assertion carrying its id (Shio SH527); figures and lists in
documentation are generated or tested (Shio SH974; freewilly DD100); and measurement
comes before building (winwright `5012473`; Shio SH1044).

### §CCF30 Chapter: guards and hooks

Rules: a rule an agent is observed breaking moves from prose into a guard (roadkeep
RK22, where Edit was "cheaper than reading a --help"; polyweave's no-clobber hook); a
refusal names the command to use instead; a guard never blocks a turn on its own failure
and never emits an allow that would override the user's permissions (roadkeep
`guarding.py`); guards are committed together with a launcher, so they load where
plugins do not, such as the web (RK1108; Shio `c215718bb`); a guard shipped to others
fails loudly on a missing build (winwright WW221); the wiring of guards and permissions
is protected by a test, because the harness can rewrite settings (freewilly DD115,
`ac7e7ec`); and a vendored copy that drifted from its source is detected (RK234;
winwright `a18dd8d`).

### §CCF31 Chapter: permissions and safety

The corpus shows blanket allows and `bypassPermissions` in local settings (roadkeep,
freewilly), with safety carried by guards, gates and review of commits. The chapter must
not endorse this by default. It weighs what the guards are shown to prevent (hand edits,
clobbering writes, hand-written harnesses) against what nothing in the corpus guards:
destructive shell commands, network access, secrets, and pushes, which polyweave and
roadkeep forbid only in prose. It states a minimum: committed settings with explicit
deny or ask rules for irreversible actions; a local bypass allowed only as a documented
deviation naming its compensating controls; no secrets in the repository; and pushes
made by the person. Anthropic's documentation on permission modes and sandboxing is
cited through the harness register.

### §CCF32 Chapter: environment portability

Rules: nothing the practice relies on may exist only in a user-level install, so
plugins, engines and hooks reach a web session through committed files (RK1108; Shio
`c215718bb`; freewilly's launcher); tool versions are pinned and a stale copy is
detected (RK153, RK234; freewilly `89371b8`); line endings are pinned by
`.gitattributes` and tested (RK1132: 45 modules ending CRLF and 11 ending LF); encoding
is judged on bytes before a defect is filed (Shio SH519; polyweave `f203b0a`); source is
never edited through a heredoc (RK1091); and PowerShell 5.1 adds a byte-order mark to
piped input (polyweave's no-clobber, L59-62, corrected by CCF11). The first rule rests
on observation O3 in evidence/harness.md, which the documentation now contradicts (H10:
synced plugins load in cloud sessions); test a plugin in a cloud session before writing
it. Each rule names the platform facts it depends on through the harness register.

### §CCF33 Chapter: agent-facing product surfaces

An optional chapter, applying only where a project's product is used by agents. Rules:
the input format reaches the agent as a schema, never as prose to type from memory
(winwright WW66); every response and tool schema has a token budget held by a test, and
raising one is argued in its commit (freewilly `agent-budget.json`; roadkeep's tool and
read ceilings); an unknown name is refused with the near matches (polyweave PW128); a
remedy names a command that exists (PW127); the product's own skills are loaded by its
own repository and kept apart from project skills (Shio SH949); discoverability is
tested with the published artefacts alone, never with the source mounted (Shio SH605);
agents are given Markdown twins and `llms.txt` rather than rendered pages (winwright
WW495); and adoption is proved by code deleted in a consumer (WW86).

### §CCF34 Chapter: the human role

Rules: the person owns non-goals, priorities, releases and pushes; a judgement of
quality with no measurable bar belongs to the person, is recorded as a verdict against
the shipped entry (roadkeep `validate`, RK1692) and is never inferred by the agent
(polyweave's sixth non-goal; `113f220`); work waiting on a person or on absent hardware
is deferred with its reason, never left open or faked (polyweave `DEFERRED.md`;
`5a3a26c` then `0a82ee0`); a bar a person sets once is stored and reused (polyweave
Block J); and paid or irreversible acts are asked for, not assumed. The chapter also
says what the person should not spend time on: formatting planning files, writing commit
bodies, and reproducing measurements the agent can take.

### §CCF35 Chapter: concurrent sessions

Rules: a session claims the task it works on and the paths it owns, and a claim expires
(roadkeep's claims, held for 60 minutes); staging is limited to the claimed paths
(RK280, RK1117, RK320); gates that share state take a lock, and a run that could not
complete is inconclusive rather than red (Shio SH803, where two concurrent runs reported
3 errors over 1,092 tests on a tree that alone reported 1,894 green; SH828); planning
files merge by entry rather than by text (roadkeep's merge driver); and version bumps or
generated files that every commit touches are reconciled against the index (RK398).
State the limit: the corpus has one person running several sessions, and no evidence on
teams of several people with agents.

### §CCF36 Chapter: agent-written prose

Rules: a project written by an agent declares its writing rules in a trigger-loaded
skill (freewilly's writing skill, created after the agent defended the old style itself,
`0794e60`); counts and versions in prose are generated or tested (freewilly DD157,
DD159; Shio SH974); length limits on planning prose are enforced where the text is
written, not reviewed afterwards (roadkeep's founding rationale; Shio SH341); commit
bodies record what was measured and how, rather than restating the diff (winwright's
shift from generic bullets to measured prose; Shio `7820e57a7`); and the project's
language is declared. Rules about truthfulness, such as generated figures, are graded
separately from rules about style.

## Block E — Patterns and anti-patterns

### §CCF37 The pattern form

Adopt a form derived from Alexander and from the anti-pattern literature: name; one-line
intent; context (which projects, under which conditions); problem; forces; solution, or
for an anti-pattern the refactored solution; consequences, including costs; known uses
with citations; related rules and findings; grade. Names are short noun phrases a
reviewer can say aloud, such as "resident encyclopedia" or "deny with a door". A
template file and a check that every entry has every section. Patterns describe and
rules prescribe: an entry never uses RFC 2119 keywords, and each links to the rules that
make it normative.

### §CCF38 The anti-pattern catalogue

Candidates from the field notes, each to be confirmed by findings: resident encyclopedia
(an every-turn file that grows, Shio's 186 KB); moved bloat (a split that relocates
size, Shio's 1.73 MB `docs/agents/`); rule in prose (a budget or ban only written down,
roadkeep RK30); stage everything (logs and bytecode in commits); batch commit; absent
guard (plugin hooks missing on the web); silent green (tests that never ran counted as
passed); piped gate; permanent red; typed figure; self-certified look; filing treadmill
(roadkeep `35fc90c2`); clobbering write; false-premise defect (Shio SH519); heredoc
edit; drifted copy (a vendored skill behind its source); folklore threshold (polyweave
`963b652`). Each links to the pattern that resolves it.

### §CCF39 The pattern catalogue

Candidates: pointer instruction file; index, not encyclopedia; trigger-loaded skill;
orientation and pages; write-time schema; deny with a door; committed launcher; budget
as a gate; third verdict; roll call; red-suite ledger; assertion carries its id; grep
then lint (Shio SH322); generated figure; capture comparison (freewilly's window skill);
scanner and verifier (polyweave's agents); deferred for judgement; proof by deletion
(winwright WW86); measure first; claim with paths. Each entry names the anti-pattern it
resolves and the cost it adds, because several of them, guards and budgets especially,
create friction that the corpus also records (roadkeep RK1689 removed prompts that no
allow rule could pre-empt).

## Block F — Conformance and the audit

### §CCF40 Conformance levels

Cumulative levels, each a coherent stopping point. Level 1, governed: an every-turn
index with a budget, governed planning files, one task per commit. Level 2, gated:
guards committed and portable, gates run before commit and in CI, the third verdict,
red-suite discipline. Level 3, measured: generated figures, context-cost budgets,
discoverability tested, drift checks between artefacts. Every rule is assigned a level,
justified by its grade and its adoption cost. A project states its level and the spec
version, and the claim is backed by an audit report. The optional chapter on
agent-facing products is a profile, not a level.

### §CCF41 A machine-readable rule registry

`spec/rules.toml`, in TOML because people author it (polyweave's convention: TOML for
documents a person writes, JSON for records a machine writes), carries for each rule:
the address, chapter, keyword, level, a one-line statement, its findings, the kind of
check (automatic, assisted or manual), the detector's identifier where one exists, and
the harness facts it depends on. The chapters remain the normative text; the registry is
generated from them or tested against them, so the two cannot disagree. A query tool
answers questions such as which level 2 rules are not automated, or which rules depend
on plugin loading, without reading the chapters.

### §CCF42 The traceability gate

A CI check that fails when a rule cites no finding; when a MUST rests on findings below
the admission grade; when a finding cites no resolvable primary evidence; when a finding
is cited by nothing and not marked as background; or when a pattern links a rule that
does not exist. It generates a traceability matrix, rule to findings to citations to
projects, as a committed artefact regenerated in the same commit as any change, the way
polyweave regenerates its site module. The matrix is the first thing an expert reviewer
reads.

### §CCF43 A deterministic conformance checker

A script depending on nothing beyond its language's standard library (roadkeep's
zero-dependency rule) that, run in a target repository, evaluates each automatic rule:
every-turn files present and within a declared budget; guards wired in committed
settings for the required events; a committed launcher; ignore rules covering logs and
caches; a CI workflow running the declared gates on push; governed planning files
present and linting clean; line endings pinned by `.gitattributes`. It writes the report
format, and exits non-zero when a rule at the claimed level fails. It is tested against
fixture repositories built for each rule, one passing and one failing.

### §CCF44 The audit skill and its agents

Ship a Claude Code plugin from this repository with an audit skill and two agents
modelled on polyweave's: a read-only scanner per chapter, on a cheaper model, with a
fixed output of rule, locus, observation and evidence, since "an invented finding costs
more than a missed one"; and a verifier on a stronger model that classifies each finding
as confirmed, false positive or unverifiable. The skill runs the deterministic checker
first and never re-reports what the checker covers, and it loads only the rules for the
claimed level. Its output is the report; filing tasks into the adopter's backlog is a
separate, explicit step through the adopter's own roadkeep. The skill's description and
body are budgeted as the spec requires of others.

### §CCF45 The audit report format

A JSON schema with a Markdown rendering: the spec version; the audited repository and
commit; the claimed and achieved level; for each rule a verdict (pass, fail, waived, not
applicable, could not run) with its locus and evidence; a summary by chapter; and the
versions of the checker and the skill. Could not run is a verdict of its own, never
folded into pass. Reports are committed in the audited project under a declared path so
that its history shows the trend, and a diff tool compares two reports.

### §CCF46 Recorded deviations

A file on the adopter's side, for example `ccf.toml`, lists each waived rule with a
reason, an owner, a date, and either an expiry or a tracking task, the shape of Shio's
`red-suites.json` (SH579). The checker and the audit read it: a waived rule reports
waived, and an expired waiver reports fail. The same file declares the claimed level and
the spec version. A waiver is also evidence for this specification, since a rule that
most adopters waive is a rule to revisit (Block I).

## Block G — Adoption and realignment

### §CCF47 Reference templates

`templates/` holds a minimal conforming file per artefact, each with a comment block
citing the rules it implements: an `agents.md` skeleton and the `.claude/CLAUDE.md`
pointer; `.claude/settings.json` with guards and explicit deny rules; the hook launcher
and the no-clobber hook, vendored with their source commit; `.gitignore` and
`.gitattributes` fragments; a `roadkeep.toml` with budgets and criteria enabled; CI
workflows; a dev skill for committing and a writing skill; and a `ccf.toml` declaring
the level and the spec version. The templates are tested: the checker passes on a
repository assembled from them.

### §CCF48 Greenfield bootstrap

`adoption/greenfield.md` and a skill that performs it: the order in which to install the
pieces so that each protects the next, with guards before the first planning file, gates
before the first feature, and budgets from the first every-turn file; the decisions the
person makes on day one (language, level, attribution, permission posture); and the
first audit. Polyweave, governed from its first commit, is the reference case, but its
speed must be measured by the corpus metrics before it is quoted, and compared fairly:
it inherited a mature toolchain that the other projects had to build.

### §CCF49 Brownfield adoption

`adoption/brownfield.md`, derived from the Shio case study: inventory the existing
instructions and documentation before writing any; start with an index and a budget
rather than one large file (Shio's growth to 185 KB and its later split); import an
existing backlog through roadkeep's `adopt`, accepting legacy limits explicitly (Shio's
changelog limit of 4,200 characters for 233 entries that predate the tool); keep legacy
artefacts marked as such (Shio's root CHANGELOG ending in 2021); add gates that measure
before the agent's first feature; and keep project skills apart from any published ones.
Each step names the rule it satisfies and the level it reaches.

### §CCF50 Realignment procedure

`adoption/realignment.md` and a skill: run the audit; classify each failure as drift
(the project meant to conform), divergence (a deliberate choice, to be waived with a
reason) or obsolescence (the rule no longer fits, to be reported upstream to this
specification); file the drift as tasks in the project's own backlog through its
roadkeep, one per rule, with the rule's address in the rationale; order them by level,
so the project reaches a stable level before attempting the next; and re-audit after
each level, committing the report. Migrations with a known recipe, such as splitting an
every-turn file, moving a procedure into a skill, or committing a launcher, get a guide
each.

## Block H — Validation against the corpus

### §CCF51 Audit: roadkeep

Run the deterministic checker and the audit skill against the project's current head and
commit the report under `validation/`. Each failure is classified as drift, divergence
or obsolescence. Realignment tasks are offered to the owner; filing them into that
project's backlog is the owner's decision, and the report records which were accepted.
The audit's own cost, in tokens and wall time, is recorded as data for the audit design.
Expected tension: rules derived from roadkeep may pass trivially, which is circularity
rather than validation, so the report lists the rules for which roadkeep was the only
source.

### §CCF52 Audit: polyweave

Run the deterministic checker and the audit skill against the project's current head and
commit the report under `validation/`. Each failure is classified as drift, divergence
or obsolescence. Realignment tasks are offered to the owner; filing them into that
project's backlog is the owner's decision, and the report records which were accepted.
The audit's own cost, in tokens and wall time, is recorded as data for the audit design.
Expected from the field notes: pytest and ruff run only locally, and CLAUDE.md counts
non-goals differently from the roadmap. Compare the findings with what polyweave's own
audit skill reports on the same head, since both use a scanner and a verifier.

### §CCF53 Audit: freewilly

Run the deterministic checker and the audit skill against the project's current head and
commit the report under `validation/`. Each failure is classified as drift, divergence
or obsolescence. Realignment tasks are offered to the owner; filing them into that
project's backlog is the owner's decision, and the report records which were accepted.
The audit's own cost, in tokens and wall time, is recorded as data for the audit design.
Expected: CONTRIBUTING describing a CI lint removal that was undone; the absence of an
every-turn file, a divergence to classify under the recorded decision rather than assume
to be a failure; and the local bypass of permissions. The report says whether the spec's
rules would have caught the harness trimming settings, which freewilly caught with its
own test.

### §CCF54 Audit: winwright

Run the deterministic checker and the audit skill against the project's current head and
commit the report under `validation/`. Each failure is classified as drift, divergence
or obsolescence. Realignment tasks are offered to the owner; filing them into that
project's backlog is the owner's decision, and the report records which were accepted.
The audit's own cost, in tokens and wall time, is recorded as data for the audit design.
Include the product-surface profile. Of interest: no instruction file, justified by a
test; CI deliberately limited to the host half of the suite; skill budgets already
enforced. Record where winwright is stricter than the specification, since a stricter
practice in the corpus is a candidate for raising a SHOULD to a MUST.

### §CCF55 Audit: shio

Run the deterministic checker and the audit skill against the project's current head and
commit the report under `validation/`. Each failure is classified as drift, divergence
or obsolescence. Realignment tasks are offered to the owner; filing them into that
project's backlog is the owner's decision, and the report records which were accepted.
The audit's own cost, in tokens and wall time, is recorded as data for the audit design.
Audit the `latest` worktree. Expected: `docs/agents/` without a size cap; the build
skill contradicting agents.md on piping gates; the stale `roadkeep.toml` header; about
sixty ad hoc log files in the working tree. Measure whether loading only the rules of
the claimed level keeps the audit of a repository this size within budget.

### §CCF56 Measuring audit accuracy

For a sample of rules across all five projects, the person records a verdict
independently of the audit. Compute agreement per rule and overall, with Cohen's kappa
where the sample allows, and list every disagreement with its cause: an ambiguous rule,
a checker defect, a missing fixture, or the person's own error. Run the audit twice on
the same commit to measure its repeatability, since the verifier is a model. Ambiguous
rules are rewritten and defects become tasks. `validation/accuracy.md` reports the
numbers with the sample size and its limits.

### §CCF57 Measuring the effect of realignment

Pick one project whose owner accepted realignment tasks; Shio is the likely case because
of its size. Before realignment, record with the corpus metrics script: bytes loaded on
every turn, drift findings, days with a red suite, stray files committed, and commits
per task. After the realignment ships and a comparable period passes, record the same.
Report the differences with the confounders stated: the project changes for other
reasons, the models change, and the person learns. This is an observational measurement,
not an experiment, and the report says so.

## Block I — Governance and publication of the specification

### §CCF58 Versioning the specification

Semantic versioning for the normative content: a new MUST or a stricter level is a major
change; a new SHOULD, MAY or chapter is minor; editorial and evidence-only changes are
patches. Tagged releases carry notes generated from the decision records and from the
rule registry's diff, kept separate from the backlog ledger. Every conformance claim and
audit report names the version. Version 1.0 waits for the validation block, so that 0.x
signals rules not yet tested against the corpus.

### §CCF59 Changing the specification

A proposal form, in the manner of a lightweight RFC or PEP: the rule text, the findings
that support it with their grades, the projects it affects, its level, and the expected
cost to adopters. An accepted proposal lands as a task here and as a decision record.
Evidence may come from outside the original corpus: a new project joins through the same
protocol and is pinned. A rule is deprecated before it is withdrawn, and a rule most
adopters waive is reviewed. The process runs through this repository's roadkeep, so the
history of every rule can be queried.

### §CCF60 Publishing for agents and people

A static site with one addressable page per rule and per finding, a Markdown twin for
each page, and an `llms.txt` listing them (winwright WW495). The rule registry is
published as data, so the audit plugin can fetch one version's rules without the prose.
Every page shows the spec version and the evidence grade. The site is generated in CI
from the repository, and nothing on it is edited by hand.

### §CCF61 License, citation and authorship

A license for the text (for example CC BY 4.0) and one for code and templates (for
example MIT), chosen by the owner and recorded as a decision; `CITATION.cff` with the
author, title, version and date; and an authorship statement describing the method:
Claude Code as primary author under the owner's governance, and the checks that guard
the result (the resolver, the traceability gate, the measured audit accuracy). The
reader can then judge the work by the standard it asks of others.

### §CCF62 A README as the entry point

A short README: what Claude Code first means here, in one paragraph; the three audiences
(adopters, auditors and researchers) and where each starts; the repository layout (spec,
evidence, patterns, conformance, adoption, templates, validation); the current version
and the corpus's conformance status; and how to cite. It links rather than restates, so
it stays small, and its figures come from the generated metrics.
