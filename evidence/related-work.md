# Related work

What this specification borrows, where it departs from existing work, and which of its
claims found no precedent. The last group carries the burden of evidence: nothing
already published supports it, so its support must come from the corpus alone. The
entries are grouped by what they contribute. BibTeX for every entry is in
[references.bib](references.bib), keyed as cited here.

Web sources were read on 2026-09-24.

## Recording decisions

**Architecture decision records** [nygard2011; madr]. Nygard proposed a short record per
decision with its context, the decision, a status and its consequences, kept in the
repository, and marked superseded, with a pointer to its replacement, when a later
decision replaces it. MADR gives the record a fixed Markdown template. The corpus's `DECISIONS.md`, written only when a task
ships and corrected by supersession rather than editing, is the same idea. **Departure:**
in the corpus a decision is written only as a side effect of shipping a task, by a tool
that refuses a hand edit, because an agent writing prose directly was the failure being
guarded against. ADR practice assumes a human author and gives no such enforcement.

## Normative language

**RFC 2119 and RFC 8174** [rfc2119; rfc8174]. These define MUST, SHOULD and MAY for
Internet standards, and RFC 8174 limits that meaning to the words in capitals. The
specification adopts both unchanged. **Extension:** here a keyword is capped by the
evidence behind the rule ([grading.md](grading.md)), so a MUST is a claim about support
as well as about obligation. The RFCs say nothing about why a requirement is justified.

## Patterns and anti-patterns

**Pattern languages** [alexander1977; gamma1994] and **anti-patterns** [brown1998].
Alexander's form gives each pattern a name, a context, the forces in tension and a
resolution, linked to the patterns around it. Gamma et al. brought the form to software
design, and Brown et al. popularised the anti-pattern: a recurring solution with bad
consequences, paired with a refactored solution. The catalogue in Block E follows this
lineage. **Departure:** every entry here must cite graded findings, where the classic
catalogues cite the authors' experience of known uses.

## Documentation

**Diátaxis** [diataxis] separates documentation into tutorials, how-to guides, reference
and explanation, because each serves a different need of the reader. The corpus reaches
a similar split for a different reader, the agent. Every-turn files are kept as short
indexes, detail moves to skills loaded on demand, and rationale lives in files the agent
queries rather than reads. **Departure:** Diátaxis sorts by the reader's purpose. The
corpus sorts by when the text is loaded and what it costs in context, which has no
counterpart in documentation for people.

## Commit conventions

**Conventional Commits** [conventionalcommits] fixes the shape of a commit title (a type,
an optional scope, a description) so tools can read history. All five projects use it
for most of their commits, though not all: 1,361 of Shio's 1,668 commits since adoption
conform (see the verification table in [field-notes/shio.md](field-notes/shio.md)).
**Extension:** the corpus adds the task id to the title, one task per commit, and the
planning files changed in the same commit, so the history links each change to its plan.
Conventional Commits says nothing about how much work a commit holds.

## Case study method and evidence

**Case study research** [yin2018; runeson2009] supplies the design (a multiple-case study
with replication logic) and the validity framework used here ([method.md](method.md),
[validity.md](validity.md)). **Evidence-based software engineering** [kitchenham2004]
supplies the idea of grading evidence. Where and why the scale here departs from a
design-based hierarchy is stated in [grading.md](grading.md).

## Anthropic's guidance on Claude Code

**Best practices for Claude Code** [anthropic-bp]. The official guide already states
several things the corpus found for itself: that "CLAUDE.md is loaded every session, so
only include things that apply broadly", that domain knowledge belongs in skills, which
load on demand, that "Unlike CLAUDE.md instructions which are advisory, hooks are
deterministic and guarantee the action happens", and that Claude needs a check it can
run to verify its work. **Relation:** on these points the specification is not new. What
it adds is evidence of what happened in five repositories when a practice was followed or
not, measured at pinned commits, and rules for matters the guide leaves open: planning
files, the unit of a commit, several sessions sharing one checkout, and what an agent must
not certify about its own work. The guide's behavioural statements are harness facts and
are cited through [harness.md](harness.md) rather than restated.

## Empirical studies of coding agents in real repositories

**Agent manifests** [chatlatanagulchai2025; chatlatanagulchai2025readmes; santos2025].
Chatlatanagulchai et al. analysed 253 `CLAUDE.md` files from 242 repositories and found
shallow structures dominated by operational commands, implementation notes and
architecture. The same group then studied 2,303 agent context files from 1,925
repositories, found functional concerns (tests, implementation, architecture) far more
often than security or performance, and observed that the files evolve like
configuration code, through frequent small additions. Santos et al. examined 328
configuration files from Claude Code projects and the concerns they specify.
**Relation:** these studies describe what instruction files contain across many
repositories, with no view of outcomes. This study is the complement: five repositories
followed through their history, with what went wrong recorded next to the rule that
followed. The "frequent, small additions" they measure is the growth mechanism the
corpus shows unchecked in Shio's 185.7 KB `agents.md` and checked by budgets elsewhere.

**Agent-authored pull requests** [watanabe2025]. Watanabe et al. studied 567 pull requests
made with Claude Code across 157 open-source projects: 83.8% were merged, against 91.0%
for human pull requests, and 45.1% of the merged ones needed human revision. **Relation:**
their unit is a pull request to someone else's project, reviewed by that project's
maintainers. Here the unit is a repository whose whole development runs through the
agent under one person's governance, a setting that pull-request studies do not see.

## Claims with no precedent found

The survey above found no published precedent for the following. Each therefore rests
on the corpus alone and is graded as such when it becomes a finding.

1. **Governing the planning files through a tool that refuses a hand edit**, so that an
   agent cannot write a task line or a rationale outside a schema.
2. **Counting recurrence by independent origin** when the cases share an author and
   tools, so that a practice copied between projects counts once.
3. **Budgets on every-turn files enforced by a gate**, as opposed to advice to keep them
   short, which the official guide gives.
4. **Rules for several agent sessions committing in one checkout**: claims on tasks,
   staging by path, and the failures that motivated them.
5. **Measuring the error rate of agent-extracted research** against pinned sources, as
   done for the field notes (13.8%).

"No precedent found" is a statement about this survey, not about the literature. A reader
who knows of one is asked to report it, and the claim is then re-graded.
