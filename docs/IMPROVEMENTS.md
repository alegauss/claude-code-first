# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

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
