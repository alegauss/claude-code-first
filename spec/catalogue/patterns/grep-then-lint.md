# Grep, then lint

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S4 |

## Intent

Every current breach of a rule is found by a search first, and the search lands as a lint
with the fixes, so the build repeats the count.

## Context

Shio, whose index names the practice (SH322, SH338), and the em-dash passes in Shio and
freewilly; in each a rule had been stated in prose and was found broken by the repository
that stated it.

## Problem

A rule found broken is usually fixed where it was seen and restated. The next breach arrives
through a file nobody looked at, and nothing fails.

## Forces

- The fixes are the visible deliverable; the check looks like overhead.
- A count made once is stale by the next session.
- A lint must read the files the rule governs, and that list is easy to get wrong.

## Solution

The search that finds the breaches becomes a check that reads the governed text. Shio
removed 262 em dashes from its site and made the site lint refuse the mark; restoring one as
a control, the rule fired and named the file.

## Consequences

The rule holds where the lint reads. freewilly made the same pass without a lint, removing
201 dashes and writing a skill, and its pinned commit added two more. The lint covers only
the files it names: Shio's lint on how to run its suite reads two files, and the build skill,
not among them, still pipes the suite into a filter. A lint on a style enforces a choice
the project made, and a lint can go red for a true and irrelevant reason, as winwright's
name check did until it was narrowed.

## Known uses

- Shio: "it lands as a lint" [shio@821f18d74:agents.md#L205], and "Verified by restoring one dash: the rule fires and names the file." [shio@821f18d74:docs/agents/blueprints.md#L853-L854]
- Shio: the pipe lint reads "The two files that document how to run this suite." [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L53]
- freewilly: a skill "records the rule so the next session does not restore the dashes" [freewilly@0794e60],
  and with no gate the dashes came back [freewilly@c1c2eaf:README.md#L375-L376].

## Related

- Resolves: [Rule in prose](../anti-patterns/rule-in-prose.md) and
  [Piped gate](../anti-patterns/piped-gate.md).
- Rules: [GH-1](../../GH.md), [AW-3](../../AW.md) and [VG-2](../../VG.md).
- Findings: [F6](../../../evidence/findings/F6.md), [F300](../../../evidence/findings/F300.md)
  and [F304](../../../evidence/findings/F304.md).
- Patterns: [Generated figure](generated-figure.md).
