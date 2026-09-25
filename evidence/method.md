# Research protocol

This protocol states how evidence for the specification is gathered, coded and judged, so
that a second researcher can repeat an extraction and challenge a finding. It is the
method behind every finding the specification cites. A change to it is a backlog task,
and the finding it affects says which version of the protocol produced it.

## 1. Research questions

- **RQ1.** Which practices do projects developed with Claude Code as the primary author
  converge on, and where do they diverge?
- **RQ2.** Which failures recur across those projects, and which mechanisms stopped them
  from recurring?
- **RQ3.** Which of those practices hold in every case, and which depend on a property of
  one project, such as its size, its age at adoption or what it ships?

## 2. Design

The study is a multiple-case study in the sense of Yin [1], conducted and reported
following the guidelines of Runeson and Höst for case study research in software
engineering [2]. It is exploratory for RQ1 and RQ2 and descriptive for RQ3. Each case is
analysed on its own first; the cross-case analysis then looks for literal replication (the
same practice or failure in several cases) and theoretical replication (a difference
between cases that a stated property of the cases explains).

**Unit of analysis.** A software repository developed with Claude Code as its primary
author, under the governance of a person who decides what is built and accepts the
result. The repository is analysed as a whole, including its history; a single session or
a single commit is a data point within it, not a unit.

**Cases.** Five repositories, all governed by the same person, listed with their roots in
[field-notes/README.md](field-notes/README.md): roadkeep, polyweave, freewilly, winwright
and Shio. They were chosen because they are the full set of that person's projects run
this way at the time of the study, which makes the sample a convenience sample. What that
does to the reach of the conclusions is stated with the threats to validity (CCF12).

## 3. Data sources

Four sources are read in every case, so that a claim can be checked against a source of
another kind (data source triangulation [2]):

| Source | What it holds | Why it is read |
|---|---|---|
| Git history | commits, messages, diffs, dates, authorship | what was done, in what order, and how it was explained at the time |
| Governed planning files | roadmap, changelog, rationale, decisions, deferred lines | what was planned, shipped, reversed or set aside, with the stated reason |
| Agent configuration | CLAUDE.md, agents.md, `.claude/` settings, hooks, skills, `.mcp.json`, plugin manifests | what the agent was told, and what was enforced instead of told |
| Tests and CI | test suites, workflows, gate scripts | which rules a machine checks, and when a check was added |

Session transcripts are not a source in the first extraction. They are local to one
machine and are not part of any repository, so a claim resting on one could not be
checked by a reader.

Every source is read at a pinned commit. The pins are recorded per case in
[corpus.md](corpus.md), and an evidence pointer names the commit it was read at. A
pointer without a commit is a lead, not evidence.

**Evidence pointers.** A pointer names a project from the corpus, a commit in the history
of that project's pin, and optionally a path and a line range at that commit:

| Form | Points at |
|---|---|
| `[shio@821f18d74]` | a commit, such as the one that introduced a rule |
| `[shio@821f18d74:agents.md]` | a file at that commit |
| `[shio@821f18d74:agents.md#L247]` | one line of it |
| `[shio@821f18d74:agents.md#L247-L251]` | a range of lines |

A quoted string directly before a pointer is a quote the pointer vouches for, as in
`"the most violated rule in the project" [shio@821f18d74:agents.md#L247]`. It must occur,
whitespace aside, in those lines, in the file when no range is given, or in the commit
message for a bare commit. `scripts/resolve_citations.py` checks every pointer under
`evidence/`, `spec/` and `adoption/` against the corpus, and a pointer that does not resolve fails the
build. Pointers written inside code, as in this table, are examples and are not checked.

## 4. Extraction procedure

One extraction covers one case and answers the same seven questions in the same order:

1. The agent instruction surface: every-turn files, their structure and size, and the
   rules they state.
2. The `.claude/` directory and any plugin surface the project ships to other
   repositories.
3. The governed planning files and their configuration.
4. The quality gates: tests, lint, CI, hooks that refuse an action.
5. The commit conventions.
6. Learnings, mistakes and reversals, each recorded as claim, evidence and consequence.
7. Metrics: commit count, first and last commit date, instruction file sizes, and the
   number of skills, hooks and tools.

For question 6 the extractor searches commit messages with `git log --grep` for each of
these keywords, then reads the planning files and any design documents for the same
subjects: *revert, reverse, wrong, mistake, regress, undo, supersede, drift, token, cost,
context, budget, clobber, audit, flaky, red, gate, adoption*. For question 5 the
extractor reads `git log --oneline -60` and the bodies of a sample of those commits. For
question 7 the counts come from `git rev-list --count HEAD`, the dates from the first and
last commit, and the sizes from the files at the pinned commit.

## 5. Coding scheme

The extraction yields **observations**. Each observation is one record with these fields:

| Field | Content |
|---|---|
| Claim | one sentence stating what was observed |
| Source | the case and the commit the source was read at |
| Locus | a path with a line or line range, or a commit hash |
| Mechanism | what produced the observed effect: a rule, a hook, a gate, a habit, a tool behaviour |
| Consequence | what followed: an incident, a cost, a change of practice |
| Kind | *fact* when the source states it, *inference* when the extractor concluded it |

An inference is never promoted to a fact by being repeated. It becomes a fact only when a
source is found that states it.

A **finding** groups the observations that support one claim across cases. It carries
their loci, the cases it holds in, the cases that contradict it, and a grade on the scale
in [grading.md](grading.md). Findings, not observations, are what the specification's rules cite.

## 6. Verification

Every observation is checked against its source at the pinned commit before any finding
may cite it (CCF11). The check gives one of three outcomes: *verified*, *corrected* (the
source supports a narrower or different claim, which replaces the original) or
*refuted*. The proportion corrected and refuted is reported as the error rate of the
extraction that produced the observations.

## 7. Disagreement

When two extractions, or an extraction and its verification, disagree:

1. Both return to the source at the pinned commit. Where the source states the matter,
   the source decides.
2. Where the disagreement is one of interpretation, both readings are recorded in the
   finding, and the finding is graded as contested until more evidence settles it.
3. An agent does not settle an interpretive disagreement about its own extraction. The
   person governing the study decides, and the decision is recorded with the finding.

## 8. Instruments

An instrument is the exact prompt or procedure that produced an extraction, kept
verbatim so the extraction can be repeated and its biases read.

- [instruments/extraction-2026-09-24.md](instruments/extraction-2026-09-24.md): the five
  prompts behind the field notes. Its limits are stated there: read-only, one pass per
  case, one model, and prompts that carried the orchestrator's expectations.
- [instruments/verification-2026-09-24.md](instruments/verification-2026-09-24.md): the
  prompt that verified those notes claim by claim against the pins, and what the
  resolver could and could not check of its output.

## References

1. R. K. Yin. *Case Study Research and Applications: Design and Methods*, 6th ed. SAGE,
   2018.
2. P. Runeson and M. Höst. "Guidelines for conducting and reporting case study research
   in software engineering". *Empirical Software Engineering* 14(2):131-164, 2009.
   doi:10.1007/s10664-008-9102-8.
