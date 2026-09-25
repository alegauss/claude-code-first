# Conventions

## Conformance language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**,
**SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY** and
**OPTIONAL** in this specification are to be interpreted as described in BCP 14 (RFC 2119
and RFC 8174) when, and only when, they appear in all capitals, as shown here.

One addition applies throughout. **A keyword is also a claim about evidence.** A rule may
carry a keyword no stronger than its best-supported finding allows, as set out in
[../evidence/grading.md](../evidence/grading.md): a MUST needs recurrence in two or more
independent origins at the level of a recorded incident, or a measured incident; weaker
support gives SHOULD or MAY; and a practice supported only by prose becomes an open
question, not a rule.

## The form of a rule

Every rule is written in this form, under its chapter:

```markdown
### IS-3 A budget on the every-turn file

**The every-turn file MUST carry a size budget that a gate enforces.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | automatically |
| Findings | F1, F2 |
| Harness facts | H2 |
| Threat | internal: one prose-budget case against one gated case |
| Status | active |

Rationale: one paragraph on why, citing the findings by link.
```

- **Address.** The chapter's two-letter code and a number, such as `IS-3`. The namespace
  is separate from the backlog's `CCF` ids and from the findings' `F` ids.
- **Title.** A short name, used when the rule is cited in prose.
- **Normative sentence.** One sentence, in bold, carrying exactly one keyword. A rule
  that needs two keywords is two rules.
- **Keyword.** Repeated in the table, so a tool can read it without parsing prose.
- **Level.** The conformance level the rule belongs to. Levels are defined in the
  conformance chapter; until it exists, every rule carries `pending`.
- **Checked.** `automatically` where a script can decide conformance from the files of a
  repository, `by judgement` where a reader must.
- **Findings.** The findings the rule rests on, by id. A rule with none is not a rule.
- **Harness facts.** The ids in [../evidence/harness.md](../evidence/harness.md) the rule
  depends on, or `none`. When a Claude Code release changes one of those facts, the rules
  that name it are re-examined.
- **Threat.** The threat to validity from [../evidence/validity.md](../evidence/validity.md)
  that bears on the rule most, in a phrase.
- **Status.** `active` or `withdrawn`.
- **Rationale.** One paragraph: why the rule holds, in terms of its findings.

## Addresses are permanent

A rule is never renumbered and an address is never reused. A rule that stops holding is
**withdrawn**: its Status becomes `withdrawn`, a line under its title says why and which
rule, if any, replaces it, and the rule stays in its chapter. A project that conformed to
it, or an audit that cited it, can then still be read.

## Chapters

Each chapter file is named after its code, such as `IS.md`. It opens with **The
problem**, stated from the findings in a few sentences, then gives its rules in order,
then **Open questions**: practices the evidence could not settle, each naming what would
settle it.
