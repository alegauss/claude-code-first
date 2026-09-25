# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

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
