# IS Instruction surface and context economy

## The problem

What the harness loads on every turn is paid on every turn, and in the corpus it grew with
the work. Shio's every-turn file grew about nineteenfold, to 185,734 bytes, under a token
budget the same file stated in prose; roadkeep's grew to the ceiling of a gated budget and
had to be compressed or moved out ([F1](../evidence/findings/F1.md)). Moving what only some
turns need into trigger-loaded files cut the every-turn file by counted amounts
([F2](../evidence/findings/F2.md)), but the moved content kept growing where it landed
unless it had a ceiling of its own ([F3](../evidence/findings/F3.md)). Lists written into
this surface went stale in silence when what they listed changed
([F7](../evidence/findings/F7.md)), and served tool schemas were measured as a fixed cost
of every session ([F4](../evidence/findings/F4.md)), although the harness documentation now
disputes how much of that cost a session pays. The rules below bound each part of the
surface by a check rather than by a sentence.

A project need not have an every-turn file at all
([../evidence/divergences.md](../evidence/divergences.md), D2): the evidence shows costs
of the file, not of its absence. IS-1 and IS-2 apply only where one exists.

### IS-1 A gated budget on the every-turn file

**Where a project has an *every-turn file*, it MUST carry a size budget that a *gate* enforces.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 1 |
| Checked | by judgement |
| Findings | F1, F2 |
| Harness facts | H1, H2 |
| Threat | internal: the prose budget failing is seen in one case, and the gate was never seen refusing |
| Status | active |

Rationale: the every-turn file is where a finished task's reasoning is cheapest to write
down, so it grows, and it is paid on every turn together with everything it imports (H1,
H2). In Shio a budget stated in the file itself did not stop it reaching 185,734 bytes; in
roadkeep a budget held by the gate brought the file to its ceiling and turned the next
addition into a decision to compress or move content
([F1](../evidence/findings/F1.md), R3/S3). After the move roadkeep lowered the budget
rather than leave the room free ([F2](../evidence/findings/F2.md)). The budget counts
bytes as well as lines where it can, since roadkeep records that a line budget alone is met
by writing longer lines ([F1](../evidence/findings/F1.md)). The size of the budget is not
fixed here; see the open questions.

### IS-2 The every-turn file is an index

**Where a project has an *every-turn file*, it SHOULD hold only what a turn touching no specific area needs, and point to *trigger-loaded skill* bodies or files read on demand for the rest.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | by judgement |
| Findings | F2 |
| Harness facts | H1, H2, H3 |
| Threat | construct: the every-turn file was measured, not what a task reads in total |
| Status | active |

Rationale: a skill's body costs context only on the turns that use it (H3), while the
every-turn file costs it on all of them. Shio's split took its every-turn file from
185,734 to 14,433 bytes, and roadkeep moved 26 lines needed only on build or commit turns
into a skill, taking its file from 125 to 104 of 125 lines
([F2](../evidence/findings/F2.md), R3/S3). The evidence would admit MUST, but decision D2
in [../evidence/divergences.md](../evidence/divergences.md) sets this rule at SHOULD, and
no finding shows that the move reduced what a task read in total: in Shio the moved
content exceeded what it replaced ([F2](../evidence/findings/F2.md)).

### IS-3 A skill's description names its occasions

**A *trigger-loaded skill* SHOULD have a description that names the occasions and words on which it is to load.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 1 |
| Checked | by judgement |
| Findings | F2, F406 |
| Harness facts | H3 |
| Threat | external: the practice is held by a test in one project, winwright, with no before-and-after figure |
| Status | active |

Rationale: moving content into a skill saves every-turn cost only if the skill loads on the
turns that need it and not on the others. winwright filed that its shipped skill was
loaded on every turn against a budget it did not need, changed it to load on a window, and
holds it with a test asserting that the description names the occasions on which the
skill should load ([F2](../evidence/findings/F2.md)). The description is itself paid on
every turn, which winwright prices apart from the body
([F406](../evidence/findings/F406.md)). The support for naming the occasions is that one
observation, recorded at S2 with no contrary one, which admits SHOULD.

### IS-4 A ceiling for what left the every-turn file

**Every *trigger-loaded skill* body, and every file the *every-turn file* or a skill sends the agent to read, MUST carry a size ceiling of its own that a *gate* enforces.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 3 |
| Checked | by judgement |
| Findings | F3, F406 |
| Harness facts | H3 |
| Threat | construct: growth was counted, but what a task paid to read the grown files was not |
| Status | active |

Rationale: moving content out of the every-turn file removes it from the only check that
was counting it, and the destination receives the additions the every-turn file used to
receive. Shio's area files grew from 184,521 bytes at the split to 1,730,001 at the pin
with no ceiling found; roadkeep's skill reached 65,885 code units a turn, was split into an
orientation under a ceiling and two pages, and the two uncapped pages grew until each was
given a figure of its own ([F3](../evidence/findings/F3.md), R3/S3). A skill body is paid
in full on each turn that loads it (H3), and winwright caps its shipped skill's body for
the stated reason that it otherwise becomes the instruction file it replaced
([F406](../evidence/findings/F406.md)). A ceiling per file bounds what one turn loads;
roadkeep's answer to a page past its figure is to split the page, not to refuse the
content ([F3](../evidence/findings/F3.md)).

### IS-5 Lists in the instruction surface are checked

**A list of commands, paths, identifiers or configuration keys that the *every-turn file* or a *trigger-loaded skill* gives the agent MUST be generated from its source or checked against that source by a *gate*.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 3 |
| Checked | by judgement |
| Findings | F7, F306 |
| Harness facts | none |
| Threat | construct: a stale list is known only where someone recorded finding it |
| Status | active |

Rationale: a list typed into prose has no link to what it lists, and the change that makes
it false is made elsewhere. polyweave's audit skill listed eight blocks while the roadmap
held ten, and Shio's every-turn file said 25 mutating paths where a scan found 28; in all
five projects such a figure or enumeration was found wrong with nothing failing
([F7](../evidence/findings/F7.md), R4/S4). An agent that loads the prose trusts it, so the
stale list misleads the next session rather than failing anything. winwright's shipped
skill is tested for its names because a stale one sends an agent at something that is not
there, and the agent's configuration elsewhere broke silently until a gate read it
([F306](../evidence/findings/F306.md)). The check must read the source: winwright's
earlier check held an example to nine typed names and missed the missing key for that
reason ([F7](../evidence/findings/F7.md)).

### IS-6 A budget on served tool schemas

**A project that serves MCP tools to its own agent SHOULD hold the serialized size of their schemas under a ceiling that a *gate* enforces.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 3 |
| Checked | by judgement |
| Findings | F4, F406 |
| Harness facts | H8, H9 |
| Threat | external: a harness release decides how much of the schema a session is sent |
| Status | active |

Rationale: Shio and roadkeep measured their served tool schemas as the largest fixed cost
of a session, held them under ceilings that fail the build, and met each later addition by
trimming a description or raising the ceiling with a written reason; Shio's test failed on
a real change three tokens over, answered by a trim ([F4](../evidence/findings/F4.md),
R3/S4). The ceiling did not keep roadkeep's total from rising twelve times; what it did was
make each rise a recorded decision. The finding is contested by the harness documentation:
with tool search on, the default read on 2026-09-24, Claude Code does not send every tool
definition up front (H9). The measured sizes are not in doubt, but what a session pays for
them is, and that disagreement is a property of the harness version rather than of the
cases, so the rule stands one level below the finding's grade. The ceiling that projects
put on surfaces they ship to other agents is a separate matter
([F406](../evidence/findings/F406.md)), treated in the chapter on agent-facing product
surfaces.

## Open questions

- **Whether a project should have an every-turn file at all.** freewilly and winwright have
  none and keep their rules in skills and in comments beside the mechanisms they govern; no
  finding records a failure caused by that choice, and no source says why it was made
  ([../evidence/divergences.md](../evidence/divergences.md), D2). A recorded failure in a
  project without the file that such a file would have prevented, or a measured comparison
  of the two arrangements, would settle it.
- **How large the budget should be.** The corpus gives budgets (roadkeep's 125 lines and
  8,400 bytes) but no finding shows that one size works better than another. Measurements
  of task outcomes across projects with different budgets would settle it.
- **Whether moving content out of the every-turn file lowers what a task reads in total.**
  In Shio the moved content outweighed what it replaced, and what a session read is only in
  transcripts, which are not a source of this study ([F2](../evidence/findings/F2.md),
  [F3](../evidence/findings/F3.md)). Session transcripts counted before and after such a
  move would settle it.
- **A fact stated in one file, with the others pointing to it.** Shio's index declines to
  restate the tool's configuration because "a rule in two files is two files that can disagree" [shio@821f18d74:agents.md#L268-L269],
  and roadkeep found two figures stated in five places, both drifted
  ([F7](../evidence/findings/F7.md)). But no finding measures single-sourcing as a
  remedy that held; the practice is asserted in prose. A recorded drift between two copies
  of one rule, against its absence where the rule had one home, would settle it.
- **What served tool schemas cost a session under tool search.** F4 and F406 counted
  serialized schemas, not what reached the model's context. A measurement of the context a
  session is sent, at a stated harness version with tool search on and off, would settle
  whether IS-6 should be raised to MUST or withdrawn.
