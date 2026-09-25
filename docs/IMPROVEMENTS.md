# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

### §CCF74 Session cost as evidence

The owner asked whether a project's token budget can be measured and checked as the
project progresses. The IS open question says the count would come from session
transcripts, which method.md excludes because they are local to one machine and pinned
by no commit. They do carry the figures: every assistant request in the JSONL under
~/.claude/projects records its input, cache writes, cache reads and output, and
claude-code-usage's measure-usage.mjs already reads them, folding subagents into the
task that spawned them. What is missing is attribution to backlog work, which
task-cost.mjs in that repository adds by assigning each request to the first commit
after it and summing per id. The method change admits a session-cost aggregate as
evidence on four conditions: it is produced by a named tool at a named commit, from a
stated date range, it holds no prompt or content, and it is committed here with the
command that made it, so the aggregate is pinned even though its source is not. Its
observations grade at S3 at best, with a validity threat that no one else can rerun it.
The harness facts it rests on, the transcript's usage fields, go into harness.md with
the documentation read. The first aggregate covers Shio and roadkeep, and the IS open
question is revised by what it shows.

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

### §CCF75 Files against the API, measured

CCF71 recorded Shio's "files beat APIs for authoring" as an open question and named what
would settle it: one canonical authoring task benchmarked both ways, in calls and
tokens. Shio's SH1141 builds that benchmark in its CLI suite, against the fake server
the content commands are tested with, counting only what reaches the agent's context on
each path, including the Read the harness requires before an Edit. Once it lands, its
figures are cited at the commit that holds them, which is past Shio's pin, and the
citation says so, as corpus.md requires; a re-pin is its own task and is not needed for
one pointer. If the file path is cheaper by a margin the test holds, the result becomes
a finding at R1 and the open question is replaced by a pointer to it; if it is not, the
open question is rewritten to say what was measured and what it showed, which is itself
a correction to Shio's P4. Either way the guide's lesson on the agent's path is checked
against the result.

## Block I — Governance and publication of the specification
