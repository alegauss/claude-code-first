# Write-time schema

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

A length or format rule on planning prose is refused by the tool that writes it, not stated
as an instruction.

## Context

Shio, whose roadmap lines grew under a one-sentence rule stated in prose, and winwright,
whose drafts exceeded limits already in force. The limits are roadkeep's, a shared tool
that governs the planning files of all five projects.

## Problem

The agent writing a line knows the whole analysis behind it, and an instruction to be brief
competes with all of it. Later sessions read every extra word back.

## Forces

- The line is where the next reader looks, so the author puts the design there.
- The long form has a proper home, the rationale section, one step further away.
- A refusal costs a round trip in which the text is sent again.

## Solution

The planning files are written through a tool that holds each field to a limit and refuses
the write that crosses it, and hand edits of those files are refused so the write path
cannot be bypassed. roadkeep sets each limit from lines that already read well.

## Consequences

Shio's roadmap went from 95 active lines averaging 142 words, the worst 555, to open lines
averaging 52 words with none above 61 at the pin, although a rewrite two days before the
limit leaves the comparison uncontrolled. Each refusal is a round trip: one winwright
rationale section took five. The limit bounds length, not content, and it bent for old
text, since Shio's ledger limit was set high for entries written before the tool. The
refusal of hand edits it depends on covers only the calls its guard matches, and widening
that guard cost prompts on every staging commit until staging was exempted.

## Known uses

- Shio: "six of the worst eight were written in the same session that then found the problem" [shio@821f18d74:docs/agents/agent-surface.md#L1502-L1503],
  later held at "line = 320" [shio@821f18d74:roadkeep.toml#L339].
- winwright: "five refusal round-trips over the 250-word limit, each re-sending the whole paragraph" [winwright@a18dd8d].
- roadkeep: "An instruction to be terse does not survive the moment its author knows more than the line allows." [roadkeep@91754240:docs/IMPROVEMENTS.md#L23-L24]

## Related

- Resolves: [Rule in prose](../anti-patterns/rule-in-prose.md).
- Rules: [AW-2](../../AW.md) and [PG-1](../../PG.md).
- Findings: [F5](../../../evidence/findings/F5.md), [F101](../../../evidence/findings/F101.md)
  and [F100](../../../evidence/findings/F100.md).
- Patterns: [Budget as a gate](budget-as-a-gate.md).
