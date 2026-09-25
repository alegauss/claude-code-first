# Versioning

The specification is versioned so that a conformance claim or an audit report can say
which text it was judged against. A claim without a version becomes false the day a rule
tightens.

## The version number

The version follows semantic versioning, applied to the normative content:

| Change | Class |
|---|---|
| a new MUST or MUST NOT rule, a keyword made stronger, a rule moved to a lower level | major |
| a new SHOULD, SHOULD NOT or MAY rule, a keyword made weaker, a rule moved to a higher level, a rule withdrawn, a new chapter | minor |
| wording, rationale, evidence, tooling | patch |

A change that makes more projects fail is major; one that adds guidance or relaxes a
rule is minor; one that changes no obligation is a patch.

**Before 1.0**, a major change bumps the minor number, as semantic versioning allows for
0.x releases. Version 1.0 waits for the validation block, in which the specification is
audited against the projects it came from: until then, the 0 says that the rules have not
been tested against the corpus.

## Where the version lives

In one place: the `version` field of `.claude-plugin/plugin.json`. The conformance
checker writes it into every report, and a project's `ccf.toml` names the version it
claims ([deviations.md](deviations.md)).

## Release notes

`python scripts/release_notes.py <previous-tag>` compares the rule registry,
[rules.toml](rules.toml), and the decision records between the previous release and the
working tree. It prints the notes (each rule added, removed, strengthened, weakened,
moved or reworded, and each decision recorded) and the class of the change. With
`--check` it fails when the version in the manifest is smaller than that class requires,
so a release cannot understate what it changes. The notes are kept with the release, not
in the backlog ledger, which records work, not versions.
