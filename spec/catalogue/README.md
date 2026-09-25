# Patterns and anti-patterns

The catalogue names what recurred in the corpus, so that a reviewer can say in two words
which failure a project is committing and which practice resolved it. **Patterns describe
and rules prescribe**: an entry here never uses the RFC 2119 keywords, and each links to
the rules in the chapters that make it normative. A pattern with no rule behind it is a
story, and the catalogue does not keep stories.

The form follows the pattern languages of Alexander and of Gamma et al., and the
anti-pattern form of Brown et al., in which a recurring solution with bad consequences
is paired with the refactored solution that replaces it (see
[../../evidence/related-work.md](../../evidence/related-work.md)).

## Where entries live

- `patterns/<name>.md`, one practice that resolved a recurring problem.
- `anti-patterns/<name>.md`, one recurring failure and what replaced it.

The file name is the entry's name in lower case with hyphens, such as
`anti-patterns/resident-encyclopedia.md`. `scripts/check_catalogue.py` holds every entry
to the form below, and CI runs it.

## The form

Names are short noun phrases a reviewer can say aloud. Every entry has this title line,
this table and these sections, in this order:

```markdown
# <Name>

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

One line.

## Context

Which projects, under which conditions.

## Problem

## Forces

The pressures that make the problem hard, as a list.

## Solution

## Consequences

What it costs as well as what it gains.

## Known uses

Where it was seen, each with a pointer to the pinned source.

## Related

The rules that make it normative, and the findings it rests on, by link.
```

An anti-pattern has `anti-pattern` as its Kind and **Refactored solution** in place of
**Solution**: the practice that replaced the failure where it was seen. The Grade is the
grade of the best finding the entry rests on.
