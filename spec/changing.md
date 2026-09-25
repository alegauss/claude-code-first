# Changing the specification

Rules change as evidence arrives: other projects will adopt the specification, realign
to it and report what failed. This page is the path that evidence takes, so that the
specification neither freezes nor grows by opinion.

## A proposal

A change to a rule, or a new one, starts as a proposal, in the manner of a lightweight
RFC. It is filed as an issue or a pull request against this repository and carries:

```markdown
# Proposal: <one line>

- **Rule**: the address it changes, or "new", and the chapter.
- **Text**: the normative sentence as it would read, with its keyword.
- **Findings**: the findings it rests on, with their grades; or the new observations,
  with pointers, from which a finding would be written.
- **Level**: the conformance level it belongs to, and why.
- **Who it affects**: which corpus projects meet it today, and which would not
  (`python scripts/check_conformance.py`, or an audit report, for each).
- **Cost to adopters**: what a project has to build or change to meet it.
- **Class**: major, minor or patch, as spec/versioning.md defines them.
```

## From proposal to rule

1. **The evidence is checked first.** A rule needs findings at the grade its keyword
   requires ([../evidence/grading.md](../evidence/grading.md)); a proposal whose support
   is a practice that sounds right becomes an open question in its chapter, not a rule.
2. **New evidence enters through the protocol.** Observations from a project outside the
   corpus are extracted and verified as [../evidence/method.md](../evidence/method.md)
   describes, and the project is pinned in [../evidence/corpus.md](../evidence/corpus.md)
   before any finding cites it. Its independence from the existing cases is counted, not
   assumed.
3. **An accepted proposal becomes a task** in this repository's backlog, and the change
   ships as that task's commit: the finding, the chapter, the regenerated registry and
   matrix, and a decision record stating what was decided and what was weighed. The
   gates in CI refuse a rule whose keyword its findings do not admit.
4. **The version moves** as `scripts/release_notes.py --check` requires.

Because every step runs through the backlog, the history of a rule can be read back:
`roadkeep origin <task>` names the commit that shipped it, and the decision records say
why.

## Deprecation and withdrawal

A rule is **deprecated** before it is **withdrawn**: its Status becomes `deprecated` for
at least one minor release, with a line under its title saying why and what replaces it,
so that projects claiming a level have time to follow. It is then withdrawn in place, and
its address is never reused ([conventions.md](conventions.md)).

## When adopters waive a rule

A waiver is evidence ([deviations.md](deviations.md)). When audit reports show that most
of the projects claiming a rule's level waive it, the rule is reviewed as if a proposal
had been filed against it: its findings are re-read, its level and keyword reconsidered,
and the outcome recorded as a decision either way.
