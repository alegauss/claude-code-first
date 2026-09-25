# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

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
