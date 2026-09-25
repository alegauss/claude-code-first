# Roadmap (active backlog)

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

- 📋 **CCF69** (deps: —) **no finding records putting capabilities on a CLI rather than an MCP tool list where the consuming agent has a shell** — Shio decided it three times on the tool list's cost, freewilly copied it and winwright chose MCP for a typed schema, so a CLI-over-MCP claim needs its scope graded. → §CCF69

## Block D — The normative specification

- 📋 **CCF70** (deps: CCF69) **no rule says when a capability belongs on a CLI verb rather than on an MCP tool list** — F4 prices the tool list and IS-6 caps it, but neither says where a new capability should land, and the corpus decided that repeatedly and not always the same way. → §CCF70
- 📋 **CCF71** (deps: —) **the files-over-APIs and the per-project session token budget claims are recorded nowhere as open questions** — Both are argued in the corpus and measured in none of it, so the non-goal on rules that sound right sends them to their chapters' open questions. → §CCF71
- 📋 **CCF72** (deps: CCF68 ✅) **no rule asks a product to benchmark canonical tasks through its agent surface against the generic path** — AP-1 bounds each surface's size, but a regression in what a whole task costs, or in the gap to the generic path, passes every per-surface ceiling. → §CCF72

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

## Block I — Governance and publication of the specification

- 📋 **CCF73** (deps: CCF70, CCF71, CCF72) **the guide's lessons say nothing about what an agent-facing surface costs, and the page types its lesson count** — The guide is the site's way in, and a reader should meet the corrected claims on REST, CLI, files and budgets there, with a count the build computes. → §CCF73

## Done when — Block A

- **A hand edit of a governed file is denied in a fresh session** The guard is the
  reason the rest of the backlog can be trusted, so it is checked by trying the edit,
  not by reading the settings.
- **CI fails a push that breaks lint or a link** Shown by a deliberately broken commit
  on a branch, since a gate never seen to fail is not known to work.
- **Every every-turn file is within a budget the gate enforces** The budget is a number
  in configuration that lint checks, not a sentence in a file.

## Done when — Block B

- **Every field-note claim is marked verified, corrected or refuted** Findings may cite
  sources only after the notes they were drawn from have been checked, and the error
  rate is recorded.
- **The resolver passes on every citation in the repository** A pointer that does not
  resolve at its pinned commit is a build failure, not a warning.
- **Method, corpus pins, grading, validity and harness facts are written** These five
  documents are what an expert reads before trusting any finding.

## Done when — Block C

- **Each of the five projects has a case study with the shared structure** The same
  sections in the same order let a reader compare projects without rereading them.
- **Every finding has a two-axis grade and a resolvable citation** A finding without a
  grade or a source cannot support a rule.
- **Every divergence between projects has a decision record** The spec takes a side, or
  records why the evidence cannot decide, for each practice the projects disagree on.

## Done when — Block D

- **Every rule has an address, a keyword, a level and cited findings** A rule missing
  any of the four cannot be conformed to, audited or traced.
- **Every term a rule uses has a glossary entry** Undefined terms are where two readers
  of one rule reach different verdicts.

## Done when — Block E

- **Every catalogue entry follows the form and links at least one rule** A pattern that
  makes nothing normative, or an anti-pattern no rule prevents, is a story rather than a
  specification artefact.

## Done when — Block F

- **The traceability gate runs in CI and passes** The evidence chain from rule to source
  is checked on every push.
- **The checker passes and fails its fixture repositories as designed** Each automatic
  rule is shown to detect its failure and to accept its conforming case.

## Done when — Block G

- **A repository built from the templates passes the checker** Templates that do not
  conform would spread non-conformance to every project that starts from them.
- **Greenfield, brownfield and realignment each have a guide and a skill** Each path an
  adopter can arrive by has an ordered procedure an agent can carry out.

## Done when — Block H

- **All five corpus projects have a committed audit report** The specification is judged
  against the projects it came from before it is offered to others.
- **Audit accuracy is reported with its sample size and limits** Conformance claims cite
  an audit whose error rate is known.

## Done when — Block I

- **Version 1.0 is tagged with release notes and citation metadata** A tagged, citable
  release is what an expert or an adopter can refer to.
- **Every rule is published on its own page with its grade** People and agents can link
  to, and read, one rule without the rest.

## Done when — CCF56

- **Audit accuracy is measured against a person** Agreement and kappa over the 35
  sampled rules, and one repeated audit, are reported in validation/accuracy.md.

## Done when — CCF57

- **roadkeep-after.json exists and the notes compare it with roadkeep-before.json** Both
  windows are written by scripts/window_metrics.py, so the comparison is between files a
  rerun reproduces.

## Non-goals

- **A rule admitted because it sounds right** Every MUST, SHOULD or MAY traces to graded
  findings or to documented harness behaviour; a practice with no evidence is recorded
  as an open question, not as a rule.
- **A manual of Claude Code features** The spec cites the official documentation for
  what the harness does and states only practice; restating the manual would go stale
  with each release.
- **One tool made mandatory** Requirements are written so another tool could satisfy
  them; roadkeep and the audit plugin are reference implementations, never the
  requirement itself.
- **Editing an adopter's repository** The audit reports and offers tasks; filing them,
  or changing code in another project, is that project owner's decision and is never
  done on their behalf.
- **Claims beyond the corpus** Nothing is asserted about teams, other harnesses or other
  model families without evidence from them; the scope is stated in the validity
  threats, not implied.
