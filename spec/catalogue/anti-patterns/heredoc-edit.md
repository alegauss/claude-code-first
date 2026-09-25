# Heredoc edit

| Field | Value |
|---|---|
| Kind | anti-pattern |
| Grade | R4/S3 |

## Intent

Source is written through a shell heredoc or a scripted edit, and bytes change on the way.

## Context

Agents editing source on Windows through a shell, a codec or a line-ending boundary. The
heredoc form is recorded in roadkeep; the wider boundary failure, text changing bytes in
silence, is recorded in all five projects.

## Problem

The shell between the agent and the file interprets what passes through it: escapes, quotes,
line terminators, a byte-order mark, a code page. The file on disk differs from what the agent
wrote, and the process that wrote it sees nothing wrong. Often only a parser, or a reader much
later, notices.

## Forces

- A heredoc writes a whole file in one command.
- The corruption is invisible in a terminal that renders the bytes as intended.
- The edit tools and the shell handle line terminators differently, so an edit anchored on one
  terminator matches nothing in a file that uses the other.

## Refactored solution

Source was edited through the edit tools, never through a heredoc; line terminators were
declared in `.gitattributes` and held by a test; and byte-level checks walked the tree for
damage such as UTF-8 read as Windows-1252.

## Consequences

The byte-level checks catch only the damage they are written for: winwright's walk had to be
widened when damage beside a correct character was invisible to it.

## Known uses

- roadkeep: "three heredoc edits corrupted a test file's string literals and only the parser noticed" [roadkeep@91754240:docs/CHANGELOG.md#L655],
  answered by "Never edit source through a shell heredoc." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L30]
- Shio: "restore LF in diff.mjs after a scripted edit flipped it to CRLF" [shio@237cec023].
- winwright: "two committed source files carry a double-encoded em-dash, one of them in shipped documentation" [winwright@861b82e:docs/CHANGELOG.md#L503].

## Related

- Rules: [EP-6](../../EP.md), [EP-2](../../EP.md) and [EP-3](../../EP.md).
- Findings: [F404](../../../evidence/findings/F404.md).
