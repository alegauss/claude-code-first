# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

### §CCF68 A task-shaped path against the generic API

The owner reviewed the specification against Shio and proposed that REST is the worst
way for Claude Code to work, because it consumes the most tokens. The corpus measured
something close to that, and it contradicts the transport part. Shio's SH112 runs four
canonical jobs twice, once over the agent surface and once over the same instance's
id-keyed console and CDA endpoints, and asserts calls, tokens and both ratios against
ceilings in token-budgets.properties. The token advantage measured 3.8x to 23.3x, and
fell to 2.1x to 12.1x when the console's own REST reads stopped serializing entities
(SH117, SH120, SH176); the file concludes that a large part of the advantage was never
the protocol. SH164 then attributed what remained: the lint and path addressing carry
it, batching buys turns rather than bytes. The agent surface that won is itself REST.
freewilly measured one canonical task at 6 calls and 11,711 tokens over the Docker
Engine API against 4 calls and 812 tokens through its shaped verbs, and notes that the
Docker CLI prints several times the Engine API's payload for the same entity. The
finding is that the generic, id-keyed interface is the expensive path whatever its
transport, and it goes in the F400 block with both origins counted under the copy rule,
since freewilly adapts Shio's laws but built its own baseline.

### §CCF69 A CLI verb against an MCP tool

The owner proposed that a CLI is better than MCP. F4 already records that served tool
schemas were measured and held under ceilings, and that freewilly chose a CLI on the
strength of Shio's measurement, but no finding states the placement decision itself or
its limits. At the pins, Shio kept three capabilities off its MCP tool list on the same
argument: instance memory in SH114, because a tool schema is paid on every turn of every
session and a coding agent has a shell; the handoff report in SH104, whose consumer is a
human; and raster snapshots in SH265, which stay in the CLI where the agent has a shell.
freewilly's DD23 and DD33 decide CLI first and MCP only for a client with no shell, and
say the measurement is borrowed, so they add no origin. Against it, Shio's own first law
orders every capability MCP before files and CLI, for clients without a shell, and
winwright serves MCP tools so that the input format arrives as the loader's own schema
after agents typed keys from memory (WW66). H9 contests the per-turn cost. The finding
is written in the F1 to F99 block with Shio as its origin, freewilly as a copy and
winwright as contrary, scoped to a consuming agent that has a shell.

## Block D — The normative specification

### §CCF70 Where a capability lands

The owner proposed that a CLI is better than MCP. The finding CCF69 writes supports a
narrower rule: where the consuming agent has a shell, offer a capability as a CLI verb,
and add an MCP tool only for a client without one, or where a schema is what keeps the
input correct. The keyword is set by that finding's grade after the contrary observation
is weighed. winwright's choice is explained by a stated property, an input that is a
structured document its loader validates, so the rule is scoped to exclude it rather
than lowered for it. H9 is named, because with tool search on by default the per-turn
cost that makes the argument is disputed, and a change there re-opens the rule. The rule
sits in the AP chapter, since in the corpus it was decided for surfaces served to
agents, and cross-refers IS-6 for a tool list a project serves to its own agent.

### §CCF71 Two claims the corpus argues and never measured

The owner proposed two more corrections. First, that an agent manipulating files is
better served locally. Shio's P4 says files beat APIs for authoring because Edit, Write
and Grep are the agent's cheapest tools, and it acted on that: content projects to a
git-diffable tree (SH86), templates project as files so Grep reaches them (SH191), and
shio read was not built because grep over a pulled tree is cheaper than a request
(SH288). No commit at the pin measures authoring through files against authoring through
the API; SH164's projection pair is field projection, not files. The cost is recorded: a
two-way sync with a three-way merge, and SH519, a false defect produced by a local
read-modify-write that decoded through cp1252. This goes in AP's open questions with
what would settle it. Second, that every project must hold its own development to a
token budget checked by tests. The corpus bounds what loads every turn (IS-1) and what a
product serves (AP-1), but no project measures what its own Claude Code sessions
consume, and transcripts are not a source of this study. This goes in IS's open
questions beside the one on moved content.

### §CCF72 Benchmark the task, not only the surface

The owner asked that every project be built around token consumption, with tests that
fail when the project's progression overruns the tokens intended. AP-1 and IS-6 already
cap what each surface costs, per tool list, skill and response. What they cannot see is
a task that got more expensive because it now takes more calls, each within its ceiling.
Shio and freewilly answered that with a canonical-task benchmark: named tasks run
through the agent surface and through the generic interface, with calls and tokens
asserted against ceilings and the ratio against a floor, and wall clock recorded but
never asserted. Shio lowered its floors when the baseline improved rather than defend
them, and isolated each benchmark's database after shared fixtures made one measurement
an input to another (SH315). The rule belongs in the AP chapter at profile level,
admitted by the finding CCF68 writes. Its scope is the evidence's: products whose
surface agents consume, not every project, since no corpus project benchmarks the
sessions that build it. That wider claim goes to the open question CCF71 records.

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

### §CCF56 Measuring audit accuracy

For a sample of rules across all five projects, the person records a verdict
independently of the audit. Compute agreement per rule and overall, with Cohen's kappa
where the sample allows, and list every disagreement with its cause: an ambiguous rule,
a checker defect, a missing fixture, or the person's own error. Run the audit twice on
the same commit to measure its repeatability, since the verifier is a model. Ambiguous
rules are rewritten and defects become tasks. `validation/accuracy.md` reports the
numbers with the sample size and its limits.

### §CCF57 Measuring the effect of realignment

Pick one project whose owner accepted realignment tasks; Shio is the likely case because
of its size. Before realignment, record with the corpus metrics script: bytes loaded on
every turn, drift findings, days with a red suite, stray files committed, and commits
per task. After the realignment ships and a comparable period passes, record the same.
Report the differences with the confounders stated: the project changes for other
reasons, the models change, and the person learns. This is an observational measurement,
not an experiment, and the report says so.

## Block I — Governance and publication of the specification

### §CCF73 The guide learns what a surface costs

Once the findings and rules land, the plain-language guide at the site root gains a
lesson on the agent's path: shape it to the task and measure the task, because in Shio
and freewilly the generic, id-keyed interface was the expensive route whatever its
transport; prefer a CLI verb to an MCP tool where the agent has a shell; and note that
files for authoring and a budget on the project's own sessions are still open questions.
The card links the new findings and rules, which the site test already checks resolve.
The page says eight lessons in two places and states that every figure on it is
computed; the count becomes a placeholder the build fills from the cards, so adding this
lesson cannot leave the heading stale, which is F7's failure on the page that cites F7.
