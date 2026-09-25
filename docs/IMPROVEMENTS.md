# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

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

### §CCF73 The guide learns what a surface costs

Once the findings and rules land, the plain-language guide at the site root gains a
lesson on the agent's path: shape it to the task and measure the task, because in Shio
and freewilly the generic, id-keyed interface was the expensive route whatever its
transport; prefer a CLI verb to an MCP tool where the agent has a shell; and note that
files for authoring and a budget on the project's own sessions are still open questions.
The card links the new findings and rules, which the site test already checks resolve.
The page says eight lessons in two places and states that every figure on it is
computed; the count becomes a placeholder the build fills from the cards, so adding this
lesson cannot leave the heading stale, which is F7's failure on the page that cites F7.
