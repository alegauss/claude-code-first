# Decisions

## Block A — The repository follows its own rule

- ✅ **CCF2** **the governed docs have no guard here, so a hand edit of ROADMAP.md or IMPROVEMENTS.md passes unnoticed** — The roadkeep engine is vendored per machine into an ignored .roadkeep/ and reached by a committed launcher; committing the engine would make every upgrade a diff here.

### §CCF2 Where the roadkeep engine lives

Three ways to reach the engine were weighed. Relying on the installed plugin alone
leaves Claude Code on the web unguarded, because plugins do not load there (roadkeep
RK1108). Committing the engine under `.roadkeep/` would pin it for every clone, but
every upgrade would then be an 86-file diff in a repository whose subject is not
roadkeep. The chosen shape matches polyweave and freewilly: a committed launcher, an
engine copied per machine by `roadkeep install --vendor`, and `.roadkeep/` in
`.gitignore`. The cost is that two machines may pin different engine versions; `lint`
names that as `engine.disagreement`.

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

- ✅ **CCF21** **the projects disagree on attribution, instruction files, permissions and CI scope, and nothing settles it** — Divergent practice is settled in one register, evidence/divergences.md, capped by the grades of its findings; a practice no evidence decides is a documented deviation, not a rule.

### §CCF21 One register for divergent practice

The design asked for one decision record per divergence, each written by `ship
--decides`. A ship records one decision, so seven divergences would have meant seven
filler tasks. The alternative taken is one register, `evidence/divergences.md`, with an
entry per divergence (D1-D7) that names what each project does at its pin, the findings
that bear on it, and a decision capped by the grading scale. Where the corpus holds no
failure on either side, the decision allows a documented deviation instead of inventing
a rule. The register also corrects two premises of the design: roadkeep's attribution
change was an intermittent trailer that stopped, not a stated policy, and winwright does
carry trailers on 33 commits.

## Block D — The normative specification

- ✅ **CCF70** **no rule says when a capability belongs on a CLI verb rather than on an MCP tool list** — A CLI verb over an MCP tool stays a MAY scoped to agents with a shell until the cost of a tool list under tool search is measured; winwright's typed input is excluded, not a reason to lower it.

### §CCF70 A CLI verb or an MCP tool

Proposed by the owner as "a CLI is better than MCP". Weighed: F8 (R2/S2) admits SHOULD,
from three Shio decisions that kept a capability off the tool list because its agent had
a shell; freewilly's policy is a stated copy and adds no origin. Against it, winwright
serves MCP tools so a structured input arrives as the loader's schema, which the rule
excludes by scope, since the difference is the kind of input and not the shell. Shio's
first law puts MCP first for clients without a shell, which the rule keeps. H9 disputes
the cost the choice avoids, as it does for IS-6, so the rule stands one level lower, at
MAY. A measurement of what a tool list costs a session with tool search on and off
re-opens it.

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

## Block I — Governance and publication of the specification

- ✅ **CCF61** **the work has no license, no citation metadata and no statement of how it was authored** — The text is licensed CC BY 4.0 and the code, including the plugin, templates, scripts and CI, MIT, chosen by the owner so adopters can copy templates without a share-alike duty.
