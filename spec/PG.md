# PG Planning governance

## The problem

An agent writes planning prose from everything it knows, so the prose grows past any
instruction to be brief: Shio's roadmap lines reached an average of 142 words under a
one-sentence rule, and only a limit refused at the write brought them back
([F5](../evidence/findings/F5.md), [F101](../evidence/findings/F101.md)). Filing a task
costs the agent one command and costs whoever picks it up much more, and in four projects
tasks were filed that described nothing wrong ([F102](../evidence/findings/F102.md)). A
design written before the work is a prediction, and in three projects implementation
overturned it while the symptom the task stated held ([F103](../evidence/findings/F103.md)).
Where shipping deletes a task's rationale, whatever only the rationale held goes with it,
including a block's definition of done, whose loss let a block close and reopen six times
([F106](../evidence/findings/F106.md)). And some work cannot be finished from the machine
at all, because it waits on a person or on hardware that is not there
([F105](../evidence/findings/F105.md)).

The rules below are written so that any planning tool can satisfy them. roadkeep, which
governs the planning files of all five corpus projects, is the reference implementation;
where a rule rests only on its design, the rule says so and carries the weaker keyword.

The length limit on planning prose, refused where the text is written, is rule AW-2 in
[AW.md](AW.md); the rules below govern the files that prose is written into.

### PG-1 Planning files are governed files

**Each planning file an agent writes SHOULD be a *governed file*.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | automatically |
| Findings | F100, F101 |
| Harness facts | H4, H6 |
| Threat | internal: the premise that an agent hand-edits when not refused is prose from the tool's author, and every observation is of one tool |
| Status | active |

Rationale: a limit enforced by a tool (AW-2) holds only while writes go through the tool,
and in Shio the refusal of hand edits is what keeps that write path from being bypassed
([F101](../evidence/findings/F101.md)). The refusal is one tool's design: roadkeep's guard
first matched only edit tools, left shell writes open, and then asked about every commit
that staged a governed file until staging was exempted ([F100](../evidence/findings/F100.md),
R1/S2). No project records an agent hand-editing a planning file, so the benefit is argued,
not observed, and the rule carries SHOULD. A guard covers only the calls that reach it, so
the files still need the check of AW-2 as a gate; the GH chapter treats the guard's gaps.
Whether the files are declared to a tool and a guard is wired for them can be read from
the repository's configuration.

The bar for filing a task at all, that it names something observed to be wrong or
missing, is rule CD-5 in [CD.md](CD.md), since it binds the session that files the task;
it is not repeated here.

### PG-2 The symptom, not the design

**A task line SHOULD state the observed symptom and leave the design to its *rationale section*.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | by judgement |
| Findings | F103 |
| Harness facts | none |
| Threat | internal: that the symptom line held is stated in one project, and the format is one tool's |
| Status | active |

Rationale: in three projects a design or diagnosis written before implementation was
overturned once the task was built or measured ([F103](../evidence/findings/F103.md),
R3/S3). The symptom is an observation and the design is a prediction, so the prediction is
the part that fails. The finding's grade admits MUST for the overturned designs, but the
half this rule depends on, that the stated symptom survived, is recorded only in polyweave
("the premise was false, not the observation"), and designs also survived measurement
there. The rule therefore carries SHOULD. A line that names no solution does not have to
be rewritten when the design changes, and the design lives where it can be replaced.

### PG-3 A false premise is recorded, not rewritten

**When a task's premise or design is found false, the finding SHOULD be recorded, by retiring the task with its reason or in its *ledger* entry, rather than rewritten in place.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | by judgement |
| Findings | F102, F103, F106 |
| Harness facts | none |
| Threat | internal: the silent losses are recorded by one tool of repositories it does not name |
| Status | active |

Rationale: false premises are common enough to recur in four projects, and where they
were recorded the record is a retirement that names the error, such as freewilly's tasks
filed "against the wrong writer" or with a heading naming an unrelated task
([F102](../evidence/findings/F102.md)). Designs found wrong on implementation were, in one
tool, deleted at shipping "with no trace that its reasoning had" been wrong, and the remedy
was a ledger sentence stating what the design was wrong about
([F106](../evidence/findings/F106.md), [F103](../evidence/findings/F103.md)). The silent
case is observed only in that one tool's sources, so the rule carries SHOULD. Where a task
line survives because the symptom held, amending its reason in the open is the same record
in a different place.

### PG-4 What outlives the task leaves its rationale first

**Where shipping deletes a *rationale section*, what in it outlives the task MUST first be moved into the code it explains, the *ledger* entry or a *decision record*.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 1 |
| Checked | by judgement |
| Findings | F106 |
| Harness facts | none |
| Threat | internal: both losses are one tool's behaviour, recorded by the researcher's own tool |
| Status | active |

Rationale: shipping deleted a task's rationale, and twice what only the rationale held was
lost with it: that a design had been wrong, and a block's definition of done, counted at
131 entries and six reopenings ([F106](../evidence/findings/F106.md), R2/S3). A measured
incident admits MUST. The rule is conditional because the loss is caused by deletion at
shipping, which is roadkeep's design and not something the evidence recommends: deleting
keeps the file small, and the cost of the alternative was never observed. A tool that does
not delete rationale meets the rule trivially. The reasons are not destroyed, since
history keeps them, but no later session reads history before deciding.

### PG-5 A block closes on its criteria

**A *block* MUST NOT be declared closed because nothing under it is open.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | 1 |
| Checked | by judgement |
| Findings | F106 |
| Harness facts | none |
| Threat | internal: the six reopenings were measured in a repository the source does not name, by the researcher's own tool |
| Status | active |

Rationale: a block that carried 131 recorded entries was declared closed and reopened six
times, "every close a count reaching zero", because its definition of done had lived in a
rationale section that shipping deleted ([F106](../evidence/findings/F106.md), R2/S3). The
reopenings were not in winwright, which adopted the remedy on its first day with this
reason and records no reopened block; they are recorded in roadkeep's sources of a
repository using it. A block is finished, in the glossary's sense, when nothing is open,
and that state does not say the block's purpose was met. A block closes when criteria
written for it, kept where shipping does not delete them (PG-4), are met. roadkeep keeps
them as a list that a ship never deletes, and winwright pairs each criterion with the case
that demonstrates it.

### PG-6 Waiting work is deferred with its reason

**A task that waits on a person's judgement or on hardware the machine lacks SHOULD be recorded as a *deferral* with its reason, not left open.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | by judgement |
| Findings | F105 |
| Harness facts | none |
| Threat | external: the practice is seen in one project whose product depends on physical and aesthetic inputs |
| Status | active |

Rationale: polyweave declared a deferred store when a task could not be finished from the
machine, set work aside with its reason, and brought it back when the missing thing
arrived: a task deferred because an engine was not installed returned the same morning,
"now that there is a Godot", and a task deferred for a person's look shipped the next
day once a person had looked ([F105](../evidence/findings/F105.md)). A recorded reason
makes waiting a state the backlog holds, so the next pick moves on instead of retrying.
The finding is R3/S2, but its second origin, winwright, closed such work rather than
deferring it, so the deferral itself is seen in one project on several occasions and the
rule carries SHOULD. That the agent must not close such work is HR-1.

## Open questions

- **Are decision records superseded rather than deleted?** roadkeep's decisions file
  states that "a decision is superseded once, and both entries stay", but no finding
  records a decision lost by deletion or recovered by supersession; it is one tool's
  prose. A recorded incident in which a later session reversed a constraint because its
  decision had been deleted, or was stopped by a superseded one, would settle it.
- **Are non-goals read before work is proposed?** No finding observes a task filed
  against a non-goal. The nearest evidence is a duplicate filed "without reading Block E's
  open lines" ([F102](../evidence/findings/F102.md)), which concerns open tasks, not
  non-goals. A recorded filing that contradicted a stated non-goal, in two projects, would
  make it a rule.
- **Should rationale be deleted at shipping at all?** Deletion keeps the rationale file
  small and caused both losses in [F106](../evidence/findings/F106.md); the alternative
  was never tried in the corpus. A project that keeps shipped rationale, measured for its
  size and for what later sessions read from it, would settle which costs more.
- **Should a guard refuse shell writes to planning files?** [F100](../evidence/findings/F100.md)
  records that answering them with a prompt cost prompts on every staging commit, and
  that an approved shell write leaves no record of its author. How often the guard
  refused or asked, and what the agent then did, is recorded nowhere; counts from session
  transcripts would settle it.
- **Does a ledger entry need correcting when later work undoes it?** In freewilly an entry
  true when written was untrue at the pin, because a later commit removed what it
  described ([F104](../evidence/findings/F104.md)). No source records harm from the stale
  entry, so it is not yet a rule; a session misled by an entry that later work had undone
  would settle it.
