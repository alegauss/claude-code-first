# AP Agent-facing product surfaces

This chapter applies only to a project whose product is used by agents: one that ships
tools, an MCP server, a command-line surface, skills or a plugin for other agents to
call. A project whose only agent is the one that writes it has nothing to conform to
here.

## The problem

Four of the five projects ship a surface to other agents, and each found that the surface
costs the consuming agent something on every session, measured it, and held it under a
ceiling a test enforces; in Shio that test fired on real changes, which were reshaped
rather than the ceiling raised ([F406](../evidence/findings/F406.md),
[F4](../evidence/findings/F4.md)). A surface exercised only from the repository that builds
it passed there while an installing consumer met it broken or missing: a skill whose
frontmatter the loader dropped, an MCP server that served no tool, skills published and
never loaded by their own repository ([F407](../evidence/findings/F407.md)). Names and
counts written into agent-facing prose went stale when the product changed
([F7](../evidence/findings/F7.md)). Where the consuming agent had a shell, Shio shipped new
capabilities as commands rather than tools, since a tool list is paid before any call
([F8](../evidence/findings/F8.md)). Shio and freewilly benchmarked whole tasks through their
surface and through the generic interface, and found the gap in fewer reads rather than in
the transport ([F409](../evidence/findings/F409.md)). And the evidence that a tool works came from named
consumer repositories, where it found what the producer's own suite had passed
([F408](../evidence/findings/F408.md)).

### AP-1 A ceiling on what the surface costs

**Each surface a product serves to agents, its tool schemas, skill descriptions and bodies, and command responses, MUST carry a token ceiling that a *gate* enforces, raised only with its reason written beside the number or in the commit that raises it.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | profile |
| Checked | by judgement |
| Findings | F406, F4 |
| Harness facts | H3, H9 |
| Threat | internal: freewilly's budget borrows Shio's argument |
| Status | active |

Rationale: Shio, roadkeep, freewilly and winwright each measured what their surface costs a
consuming agent and held it under a ceiling read by a test or lint
([F406](../evidence/findings/F406.md), R3/S4). Shio's tool-list test failed on a real
change, "3 tokens over its 2200 ceiling" [shio@821f18d74:docs/CHANGELOG.md#L22], and a
description was trimmed instead. The ceiling did not stop growth in roadkeep, where the
session ceiling was raised twelve times; what it did was make each raise a written
decision with the task that paid for it ([F4](../evidence/findings/F4.md), R3/S4), which
is why the reason is part of the rule. The two costs are priced apart because a skill's
description is paid every session and its body only when used (H3). H9 bears on tool
schemas: with tool search on, the documented default, not every definition is sent up
front, so a schema ceiling measures serialized size, which is not in doubt, rather than a
cost every session is certain to pay. A change to H9 re-opens that part.

### AP-2 Names in agent-facing text are checked against the build

**Every command, tool or configuration key that a product's agent-facing text names MUST be checked by a *gate* against the product's own catalogue of names.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | profile |
| Checked | by judgement |
| Findings | F7, F306, F403 |
| Harness facts | none |
| Threat | reliability: the S4 control run is winwright's alone |
| Status | active |

Rationale: a count or list typed into prose went stale in all five projects when what it
described changed, and stayed true only where it was generated or checked
([F7](../evidence/findings/F7.md), R4/S4). In winwright the README's configuration example
had been missing a key since the verb that reads it shipped, and a gate over the example
had not seen it because it checked names somebody typed; the check that replaced it reads
the build's own catalogue of keys and was seen to fail when the key was taken out again.
winwright's shipped skill is under a names test because a stale name "sends an agent confidently at something that is not there" [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L16-L18]
([F306](../evidence/findings/F306.md)). The cost of the opposite was counted: a session
working from a stale skill that lacked one command made five refusal round-trips
([F403](../evidence/findings/F403.md)). A refusal or error message that names a remedy is
agent-facing text in this sense, so the command it names is checked like any other.

### AP-3 Tested as installed

**A product's agent surface MUST be exercised from its published artefact, loaded the way an installing consumer loads it, and not only from the source checkout.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | profile |
| Checked | by judgement |
| Findings | F407, F306 |
| Harness facts | H8, H13; O2 (observed) |
| Threat | construct: defects are known only where a consumer reported them |
| Status | active |

Rationale: roadkeep's published plugin shipped a skill whose frontmatter the loader dropped
in silence (O2), an MCP server from which no tool reached the client, and its own
`CLAUDE.md` in the payload; Shio published four skills its own settings never loaded, so
"every breakage in them arrived as somebody else's report" [shio@d1853cbea]
([F407](../evidence/findings/F407.md), R3/S2). Inside its own checkout a session reaches
the producer's files by other routes, the repository's `.mcp.json` (H8), docs and a
repo-local skill, so it does not see what a consumer sees. The remedies load the artefact
as published: roadkeep runs `claude plugin validate --strict` in CI at a pinned version
(H13), and Shio enables its own published plugin in its committed settings
([F306](../evidence/findings/F306.md), R3/S3). Discoverability is the same question: Shio
named the gap that "the reader with the repository mounted is not the reader who installs (SH605)" [shio@7820e57a7],
so a test of whether an agent finds the surface counts only when it runs without the
source on disk.

### AP-4 Adoption is proved in a consumer

**A claim that a consumer has adopted the product MUST be proved by a counted change in a named consumer repository, such as the lines of its own replacement deleted or its checks passing on the product.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | profile |
| Checked | by judgement |
| Findings | F408 |
| Harness facts | none |
| Threat | internal: the consumers are the same person's projects |
| Status | active |

Rationale: winwright, polyweave and roadkeep each took their evidence from a named
consumer and recorded adoption as a counted change there
([F408](../evidence/findings/F408.md), R3/S3). winwright closed adoption by deleting the
consumer's own harness: 285 lines in pportal, and in claude-tray a harness whose size
winwright's records give as both 3,004 and 2,732 lines. It requires "the number of lines removed is reported rather than described" [winwright@861b82e:docs/ROADMAP.md#L137];
polyweave's real artefacts from Cottony overturned a threshold its synthetic tests passed;
roadkeep's premise was counted in Shio and its launcher's defects were found there.
Deleting a consumer's replacement is a test the producer cannot pass by construction. The
proof was sometimes overstated, and winwright corrected its pportal entry the same day
because two cases had never run, so a counted change is necessary and is not by itself
sufficient: the cases it counts must have run.

### AP-5 A capability for agents with a shell may land as a command

**Where the agents that consume a capability have a shell, a product MAY offer it as a command-line verb rather than as an MCP tool, keeping MCP tools for clients without a shell and for input that is a structured document a served schema validates.**

| Field | Value |
|---|---|
| Keyword | MAY |
| Level | profile |
| Checked | by judgement |
| Findings | F8, F4 |
| Harness facts | H9 |
| Threat | external: a harness release decides how much of a tool list a session is sent |
| Status | active |

Rationale: Shio shipped three capabilities as CLI verbs and not as tools, because "a tool schema is paid on every turn of every session (P3) and a coding agent has a shell" [shio@821f18d74:docs/CHANGELOG.md#L392]
([F8](../evidence/findings/F8.md), R2/S2), and the cost it names is the tool-list size
Shio and roadkeep measured and held by a gate ([F4](../evidence/findings/F4.md), R3/S4).
A verb costs context only when it runs. The scope is the evidence's. Shio's own first law
still puts MCP first for clients without a shell, and winwright serves MCP tools because
its input is a structured document whose schema refuses a mistyped key, after agents typed
flag names from memory; the rule excludes that input rather than being lowered for it. It
stands at MAY, one level below the SHOULD that F8's grade admits, because the harness
disputes the cost the choice avoids: with tool search on by default, not every tool
definition is sent up front (H9), the same dispute that holds IS-6 below its finding. F8
has one origin, as freewilly's "CLI first" is a stated copy of Shio's. A measurement of what a tool list costs a session under
tool search would settle whether it should rise. For a tool list a project serves to its
own agent, IS-6 holds the list's size whichever way this choice goes.

### AP-6 Canonical tasks benchmarked against the generic path

**A product whose surface agents consume SHOULD benchmark named canonical tasks through that surface and through the generic interface the same tasks would otherwise use, with a *gate* that fails when a task's calls or tokens pass their ceiling or its ratio to the generic path falls below its floor.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | profile |
| Checked | by judgement |
| Findings | F409 |
| Harness facts | none |
| Threat | construct: each baseline was written by the author of the surface it is compared with |
| Status | active |

Rationale: AP-1 caps each surface, but a task that got dearer by taking more calls, each
under its ceiling, passes every one of them. Shio and freewilly each ran named tasks both
ways and held the result by a test ([F409](../evidence/findings/F409.md), R3/S4), and
freewilly's assertion "caught it on the commit" [freewilly@c1c2eaf:agent-budget.json#L113-L114]
that widened one response by 43 tokens. The generic path is the point of the comparison:
Shio found that a single number per task "could no longer distinguish" [shio@821f18d74:docs/CHANGELOG.md#L478]
a cheaper protocol from a wasteful console, and that its token advantage fell by more than
half when its own REST reads were fixed. So a ratio is reported with its baseline, and its
floor drops with a better baseline rather than being defended. What the benchmark measures
is the shape of the path, not its transport, since Shio's shaped surface is HTTP as well.
Both projects learned to isolate the inputs, since shared fixtures and a date in a fixture
turned the gate red with no regression to blame, and neither asserts wall clock. The rule
is a SHOULD although F409 admits MUST: roadkeep and winwright ship surfaces to agents with
no such benchmark and no failure recorded against its absence, and building one costs a
fixture for the generic path as well as the shaped one.

## Open questions

- **The input format as a schema.** winwright gave its MCP tools the loader's own schema
  so that "a misspelled key is not a thing the caller can send" [winwright@861b82e:README.md#L93],
  answering a problem it named as field names typed from memory (WW66). This is one
  project's design, recorded in its case file and in no graded finding, and no incident of
  a mistyped key reaching a loader is recorded against it. A finding with a recorded
  failure of a prose-described format, in more than one project, would admit a rule.
- **Refusing an unknown name with the near matches.** No finding records either the
  practice or a failure it would have prevented. It needs one.
- **Keeping product skills apart from project skills.** Shio's SH949 holds that no name may
  be both a plugin skill and a project skill, with a test ([F407](../evidence/findings/F407.md)).
  The test is not recorded as having failed, and no collision of names is recorded, so the
  separation is a stated design (S1) beside the incident that AP-3 answers. A recorded
  collision, or the test failing on a real change, would settle it.
- **Markdown twins and `llms.txt` instead of rendered pages.** freewilly argues that an
  agent cannot discover its surface and winwright that an agent renders three pages to learn
  what the tool is; both are argued from design, not from an observed session
  ([F407](../evidence/findings/F407.md), counter-evidence). freewilly's `llms.txt` itself
  went stale when a destination was added ([F7](../evidence/findings/F7.md)), which
  argues that such a file needs AP-2's check, not that it helps. A measured session that
  finds the surface with and without the twin would settle it.
- **What a tool schema costs under tool search.** The ceilings in AP-1 count serialized
  schema size. With tool search on by default (H9), what a session actually pays for the
  schema is not measured anywhere in the corpus. A count of the tokens that reach the model
  with tool search on and off would say whether the schema ceiling should stay as strict as
  the others.
- **Files instead of an API for authoring.** Shio's law is "Files beat APIs for authoring" [shio@821f18d74:agents.md#L23],
  and it projects content to a text tree (SH86) and declined a read command because
  "grep is cheaper than a request (P4), so read would be a worse version of a file" [shio@821f18d74:docs/CHANGELOG.md#L1086].
  No commit at the pin measures authoring through files against authoring through the API:
  the benchmark in [F409](../evidence/findings/F409.md) runs both paths over HTTP, and its
  projection pair projects fields, not files. The cost is recorded instead: a two-way sync
  with a three-way merge, and a false defect that a local read-modify-write produced when it
  decoded through the wrong code page, "the mojibake was mine, not the CLI's" [shio@c17ed995a].
  One canonical authoring task benchmarked both ways, in calls and tokens, would settle it.
