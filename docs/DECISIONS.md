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

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

## Block I — Governance and publication of the specification

