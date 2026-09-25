# Roadmap (active backlog)

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

- 🛠 **CCF48** (deps: CCF47 ✅) **starting a project Claude Code first has no ordered procedure, so the order the five learned in is repeated** — The others added the same pieces over weeks, each after an incident; an ordered bootstrap installs them before the incidents. → §CCF48
- 📋 **CCF49** (deps: CCF19 ✅, CCF47 ✅) **an existing codebase adopting the practice has no procedure, and Shio's transition lives only in its history** — Most future adopters are brownfield, and the one brownfield case shows the traps: a resident instruction file and an imported backlog. → §CCF49
- 📋 **CCF50** (deps: CCF44 ✅, CCF46 ✅, CCF47 ✅) **a project already Claude Code first that drifted has no path back except rereading the whole spec** — The owner's own projects are the first to need this: the drift inventory already lists contradictions in three of them. → §CCF50

## Block H — Validation against the corpus

- 📋 **CCF51** (deps: CCF44 ✅, CCF45 ✅) **roadkeep has never been audited against the specification, so its conformance is asserted, not measured** — Roadkeep supplied many of the rules, so its audit tests whether the spec merely describes its source or can find fault in it. → §CCF51
- 📋 **CCF52** (deps: CCF44 ✅, CCF45 ✅) **polyweave has never been audited against the specification, so its conformance is asserted, not measured** — Polyweave was governed from its first commit, so its audit tests whether early adoption leaves fewer gaps than late adoption. → §CCF52
- 📋 **CCF53** (deps: CCF44 ✅, CCF45 ✅) **freewilly has never been audited against the specification, so its conformance is asserted, not measured** — Freewilly has no instruction file and a stale contributor guide, so its audit tests the spec on a project that chose another shape. → §CCF53
- 📋 **CCF54** (deps: CCF44 ✅, CCF45 ✅) **winwright has never been audited against the specification, so its conformance is asserted, not measured** — Winwright ships a plugin to other repositories, so its audit is the first to exercise the chapter on agent-facing products. → §CCF54
- 📋 **CCF55** (deps: CCF44 ✅, CCF45 ✅) **shio has never been audited against the specification, so its conformance is asserted, not measured** — Shio is the largest and only brownfield project, with known drift between its skills and its index, so its audit is the hardest test. → §CCF55
- 📋 **CCF56** (deps: CCF51, CCF52, CCF53, CCF54, CCF55) **nothing shows the audit is accurate: its false findings and misses are unmeasured** — An audit with an unknown error rate cannot be cited as evidence of conformance, and experts will ask for that rate first. → §CCF56
- 📋 **CCF57** (deps: CCF50, CCF56) **the claim that conformance reduces cost has no before-and-after measurement on any realigned project** — The spec's value is a hypothesis until one project is measured before and after realignment on the same metrics. → §CCF57

## Block I — Governance and publication of the specification

- 📋 **CCF59** (deps: CCF10 ✅, CCF58 ✅) **no process admits new evidence or a new rule, so the spec would either freeze or grow by opinion** — Other projects will realign and report what failed, and that feedback needs a path that keeps the evidence standard intact. → §CCF59
- 📋 **CCF60** (deps: CCF41 ✅) **an agent in another repository cannot consume the spec cheaply: no llms.txt and no page per rule** — Winwright measured an agent rendering three pages to learn a tool; reading the spec must cost less than the waste it prevents. → §CCF60
- 📋 **CCF61** (deps: —) **the work has no license, no citation metadata and no statement of how it was authored** — An academic reader must know how to cite it, and that an agent wrote most of it under a person's direction and with which checks. → §CCF61
- 📋 **CCF62** (deps: CCF24 ✅) **the repository has no README telling a newcomer what the spec is, how to read it and how to adopt it** — The README is the first page an expert or an adopter opens, and today it does not exist. → §CCF62

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
