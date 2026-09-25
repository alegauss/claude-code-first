# Rule in prose

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R3/S3 |

## Intent

A budget, format or ban is written down and nothing reads the text it governs.

## Context

Shio and freewilly, each with rules held in an instruction file or a skill, and many
sessions editing the governed text, some of which never load the rule.

## Problem

A written rule is read by the session that loads it and by nothing else. Later edits, other
files carrying the same content and sessions that never load the rule are outside its reach,
and nothing fails when they drift. In both projects the repository that stated the rule was
the one found breaking it.

## Forces

- Writing a sentence is cheaper than writing a check.
- A rule that reads well feels enforced by the agent that just wrote it.
- The breakage is visible only to someone who measures it.

## Refactored solution

A broken rule was moved under a check that reads the governed text: a lint over the files
that document how a suite runs, a limit refused at the write, a test case that holds a skill
to a figure. See [Grep, then lint](../patterns/grep-then-lint.md) and
[Budget as a gate](../patterns/budget-as-a-gate.md).

## Consequences

A check reads only the files it names: Shio's pipe lint does not read its build skill, which
still pipes the suite. Each check is code to keep.

## Known uses

- Shio, where the one-sentence roadmap rule was measured at "95 active task lines averaging" [shio@821f18d74:docs/agents/agent-surface.md#L1502]
  142 words, and the pipe rule is held by a lint because "the pipeline reads better without it and nothing fails." [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L44]
- freewilly, whose skill is headed "No em dashes in published prose" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L30]
  while the pinned commit added two README lines with em dashes [freewilly@c1c2eaf:README.md#L375-L376].
- winwright, where "the skill said thirty-three while the roadmap declared thirty-seven, and nothing had gone red" [winwright@a686d44].

## Related

- Rules: [GH-1](../../GH.md), [AW-2](../../AW.md) and [AW-3](../../AW.md).
- Findings: [F300](../../../evidence/findings/F300.md), [F1](../../../evidence/findings/F1.md).
