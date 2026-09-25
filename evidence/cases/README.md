# Case studies

One case study per corpus project, each with the same sections in the same order, so a
reader can compare projects without rereading them. They are the within-case half of the
analysis in [../method.md](../method.md). The cross-case half, where observations from
several cases become one graded finding, is the findings register.

| Case | Kind | File |
|---|---|---|
| roadkeep | greenfield | [roadkeep.md](roadkeep.md) |
| freewilly | greenfield | [freewilly.md](freewilly.md) |
| winwright | greenfield | [winwright.md](winwright.md) |
| Shio | brownfield | [shio.md](shio.md) |

## The shared structure

1. **Context.** Domain, language, size, dates, greenfield or brownfield, and the pin.
2. **Agent surface.** What the agent is given, as built at the pin: every-turn file,
   skills, hooks, MCP servers, plugin surface, settings.
3. **Planning governance.** How work is planned, recorded and closed.
4. **Gates.** What checks the work, where each check runs (locally, in CI, as a hook),
   and what it does not check.
5. **Commit practice.** The unit of a commit, the message conventions, attribution.
6. **Timeline.** Dated incidents in order, each with the rule or mechanism it produced.
   This is the core of each case: what went wrong, and what changed because of it.
7. **Metrics.** The descriptive figures from [../corpus.md](../corpus.md), and any
   measurement the project itself recorded.
8. **What is particular to this case.** The properties that might explain a difference
   from the other four, and so bound any finding drawn from it.
9. **Open questions.** What the evidence at the pin cannot answer.

## How a case study cites

Every factual statement carries a pointer in the grammar of
[../method.md](../method.md), checked by `scripts/resolve_citations.py`, or a `git`
command run at the pin whose output it reports. A quote sits on the same line as its
pointer, so the resolver checks it. Most pointers come from the verification tables in
[../field-notes/](../field-notes/README.md), where each was already checked; the
corrected form is used wherever the table corrected a note. A statement that is the
author's interpretation says so. A case study states what happened in one project and
does not generalise: that is the findings register's job.
