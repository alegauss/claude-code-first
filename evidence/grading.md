# Grading the evidence

Every finding carries a grade, so a reader can weigh a rule by its support without
rereading the sources. The grade has two axes, because how often something was seen and
how well it was established are different questions. A pattern seen five times in prose
is weaker than one incident measured once, and a measured incident in one project says
nothing about the other four.

## Recurrence

How widely the finding was observed, counted in **independent origins** (see below).

| Grade | Meaning |
|---|---|
| **R1** | seen once, in one project |
| **R2** | recurring within one project: at least two separate occasions, separated in time or by an attempted fix |
| **R3** | independently in two or more projects |
| **R4** | independently in all five projects |

## Strength

How the strongest supporting observation is established. An observation's strength
comes from its source, not from how confidently it is stated.

| Grade | Meaning |
|---|---|
| **S1** | asserted in prose: an instruction, a rationale or a comment says it is so |
| **S2** | recorded as an incident: a commit, a ledger entry or a decision records that it happened, and when |
| **S3** | measured: the source gives a number that was counted, such as bytes, lines, commits or a failure count |
| **S4** | encoded in a test or gate: a check fails when the finding stops holding, and it has been seen to fail |

A finding is written with both grades, as **R3/S2**. Its recurrence is the number of
independent origins among its verified observations. Its strength is the highest strength
among those observations. An unverified observation contributes to neither (see
[method.md](method.md), section 6). A finding whose sources disagree carries the mark
*contested* until the disagreement is settled, which is decided as the method describes.

## Independence

The five projects share one author, one harness and several tools: roadkeep governs the
planning files of all five, itself included; the author's commit tool is used across
them; and hooks and skills were copied from one project into the next. Recurrence is therefore not
independence, and the count follows three rules.

1. **A failure counts where it happened.** An incident recorded in each of two projects
   has two origins, even if the same remedy was then applied in both.
2. **A remedy counts where it was invented.** A hook, skill, rule or configuration copied
   from project A into project B is one origin, A, however many projects carry it. It
   gains a second origin only when B records a failure of its own that the remedy
   addressed, or changes the remedy in response to something B observed.
3. **A shared tool is one origin.** A behaviour of roadkeep, the commit tool or the
   harness seen in several projects is one observation of that tool, and counts as
   evidence about the tool, not about practice in those projects.

Where the provenance of a copy is unclear, the finding counts it once and says so.

## From grades to rules

A normative rule inherits its keyword from the findings it cites. The highest keyword a
rule may carry is set by its best-supported finding:

| Keyword | Minimum support |
|---|---|
| **MUST** / **MUST NOT** | R3 at S2 or above, or an S3 incident in any number of projects |
| **SHOULD** / **SHOULD NOT** | R2 at S2 or above, or R1 at S2 or above with no contrary observation |
| **MAY** | a verified observation of any grade that the practice worked where it was used |

A finding supported only at S1 does not admit a rule: it is recorded as an open question,
as the non-goal "A rule admitted because it sounds right" requires. A finding marked
*contested*, or one with a contrary observation in another project, admits a rule one
level below its grade, unless the difference is explained by a stated property of the
cases, such as size or greenfield against brownfield. Then the rule is scoped to that
property and keeps its level.

Harness behaviour documented by Anthropic is not graded on this scale. A rule resting on
it cites the documentation, at the version read, and is marked as documented behaviour.

## Relation to levels of evidence

Evidence-based software engineering took from medicine the idea that evidence has levels,
ranked mostly by study design: systematic reviews of controlled experiments at the top,
single case studies and expert opinion near the bottom [1]. This scale differs in three
ways:

- **Every observation here comes from case studies.** On a design-based hierarchy the
  whole corpus sits at one of the lowest levels, and nothing in this scale moves it
  higher. The scale ranks evidence *within* that level. It does not claim the strength of
  an experiment.
- **It grades mechanism, not only design.** S4 records that a check encodes the finding
  and was seen to fail. That is a property of the software under study, which no
  design-based level captures.
- **It counts origins, not reports.** A design-based hierarchy assumes independent
  studies. Here the studies share an author and tools, so recurrence is counted by
  independent origin.

## References

1. B. A. Kitchenham, T. Dybå and M. Jørgensen. "Evidence-based software engineering".
   *Proceedings of the 26th International Conference on Software Engineering (ICSE)*,
   pp. 273-281, 2004.
