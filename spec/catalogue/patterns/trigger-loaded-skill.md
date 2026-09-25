# Trigger-loaded skill

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R3/S3 |

## Intent

Detail needed on some turns lives in a skill whose description names the occasions on
which it loads.

## Context

roadkeep and Shio, where rules needed only when building, committing or writing a governed
file had sat in the every-turn file, and winwright, whose shipped skill loaded on every
turn against a budget it did not need.

## Problem

A rule in the every-turn file is paid on every turn. A rule in a file that nothing loads is
not read at all. The detail needs a home that loads on the turns that use it and on no
others.

## Forces

- A skill's body costs context only on the turns that load it, but its name and description
  are paid every session.
- A description too broad loads the skill everywhere; too narrow, and the turn that needs
  it goes without.
- A rule in a skill is read only by the sessions that load the skill.

## Solution

The content moves into a skill whose description names the occasions and words on which it
is to load. roadkeep moved its write path, and later its build and commit rules, into a
skill that describes itself as trigger-loaded. winwright changed its shipped skill to load
on a window rather than every turn, and a test asserts that the description names those
occasions.

## Consequences

The every-turn cost falls by the amount moved. The description is itself a fixed cost,
which winwright prices apart from the body. The body has left the budget that counted it
and grows where it lands, so it needs a ceiling of its own. A rule placed only in a skill
holds only in sessions that load it: freewilly's writing skill forbade the em dash, and its
pinned commit added two because no gate read the prose.

## Known uses

- roadkeep: "Trigger-loaded, and that is the whole reason it is a file (RK23, RK1136)." [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L8]
- winwright: "load the skill on a window rather than every turn, and measure both of its costs" [winwright@7c456e0],
  held by a test on the description [winwright@861b82e:tests/Winwright.Tests/SkillTests.cs#L45-L54].

## Related

- Resolves: [Resident encyclopedia](../anti-patterns/resident-encyclopedia.md).
- Rules: [IS-3](../../IS.md), [IS-2](../../IS.md) and [IS-4](../../IS.md).
- Findings: [F2](../../../evidence/findings/F2.md), [F3](../../../evidence/findings/F3.md),
  [F406](../../../evidence/findings/F406.md) and [F6](../../../evidence/findings/F6.md).
- Patterns: [Index, not encyclopedia](index-not-encyclopedia.md) and
  [Orientation and pages](orientation-and-pages.md).
