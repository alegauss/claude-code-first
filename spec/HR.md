# HR The human role

## The problem

A task's ledger entry is written by the session that did the work, at the moment it
decides the work is done, so the entry records that session's claim; in three projects an entry recorded as shipped was later found not to hold
([F104](../evidence/findings/F104.md)). Some acceptance conditions cannot be computed at
all: whether a render looks right at display size is a person's call, and a case that
needs a controller cannot run on a desk without one. Where work of that kind was closed
without the person or the hardware, it rested on cases that had never run, and where the
agent chose a bar in place of a person's, the bar blocked work for a day
([F105](../evidence/findings/F105.md)). The opposite waste also occurs: behaviour verified
by hand, and by nothing the build runs, surfaced later as a defect or a new task
([F305](../evidence/findings/F305.md)). This chapter says what the agent must leave to the
person, and what it must not.

What the person does not need to spend time on follows from other chapters: formatting
planning files is the tool's job under AW-2 and PG-1, and a check the machine can run is
the machine's job under VG-8. How work that waits on a person is held in the backlog is
PG-6.

### HR-1 The agent does not close what needs a person

**An agent MUST NOT record as shipped a task whose acceptance needs a person's judgement or hardware the machine lacks, until the person or the hardware has answered.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | pending |
| Checked | by judgement |
| Findings | F105, F104 |
| Harness facts | none |
| Threat | external: both origins are projects whose product depends on physical or aesthetic inputs, and "a person" is always the one owner |
| Status | active |

Rationale: in winwright a task's cases were closed on a desk with no controller, so two of
them had never run, and the entry was corrected once a controller was plugged in and both
passed; in polyweave, work needing a person's look or an absent engine was set aside and
finished only when the person or the engine was there
([F105](../evidence/findings/F105.md), R3/S2). A ledger entry records the shipping
session's own claim, and nothing in the planning files records whether anybody else tried
the work ([F104](../evidence/findings/F104.md)), so an entry closed without the person
reads exactly like one the person accepted. The finding's origins share a property, a
product with physical or aesthetic inputs; the rule is scoped to tasks whose acceptance
needs such an input, and keeps its level. PG-6 says how such a task is held instead.

### HR-2 A person's bar, not the agent's margin

**Where a bar that no measurement fixes decides acceptance, the agent SHOULD apply a bar a person set, stored where the check reads it, and not a margin of its own choosing.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F105 |
| Harness facts | none |
| Threat | external: one project, three days of history, and a single person setting every bar |
| Status | active |

Rationale: in polyweave a bar the agent chose, recorded as "a margin nobody asked for",
blocked a port for a day. In another task a search of 109 samples found no rig that
passed all four checks; the task was deferred for a person's look, and shipped once a
person looked at the result beside the shipped sprite at display size and accepted it, at
which the bar moved to 0.41 ([F105](../evidence/findings/F105.md)). The project then filed a block to make a bar a
person sets once a value the checks read. This is one project's record, a dated incident
with no contrary observation, which admits SHOULD. Whether a stored bar is then reused
without asking again is not yet observed; see the open questions.

That an acceptance condition a gate can decide is decided by a gate before the task
closes is rule VG-8 in [VG.md](VG.md); it is not repeated here.

## Open questions

- **Who owns non-goals, priorities, releases and pushes?** polyweave's rules say its
  commits are "staged by path, never pushed", and roadkeep records non-goals, but no
  finding records a failure caused by an agent setting a priority, adding a non-goal,
  releasing or pushing on its own. A recorded incident of an agent doing one of these
  against the owner's intent, in two projects, would make it a rule.
- **Are paid or irreversible acts asked for rather than assumed?** polyweave states that
  "nothing here spends money on an agent's own judgement" ([F105](../evidence/findings/F105.md)),
  but that is an instruction, not an observation, and no project records money spent or
  an irreversible act taken without asking. The PS chapter treats what an agent may do
  without asking; an incident would settle this one.
- **Is a person's acceptance recorded against the shipped entry?** roadkeep filed a design
  for recording whether a person tried what shipped, arguing that a shipping session
  checking its own criterion is not a person using the thing
  ([F104](../evidence/findings/F104.md)). It is prose, and no project records such an
  acceptance except polyweave's commit for the task a person accepted. A project that
  records acceptances, and whether entries without one are later found untrue more often,
  would settle it.
- **Is a bar a person sets once reused without asking again?** polyweave filed a block
  for it ([F105](../evidence/findings/F105.md)) but had not shipped it at the pin. A
  second task accepted against a stored bar with no new request to the person would show
  the practice working.
- **What should the person not spend time on?** The corpus suggests three things:
  formatting planning files, which a tool refuses or accepts (AW-2); writing commit
  bodies, which the owner's commit tool generates, though a generated body misdescribes
  the change when the agent does not state its intent (D5,
  [F204](../evidence/findings/F204.md)); and reproducing measurements the agent can take
  (VG-8). No finding measures how the person's time was spent, so none of these is a rule
  about the person; time logs or session transcripts that attribute it would settle it.
