# Claim with paths

| Field | Value |
|---|---|
| Kind | pattern |
| Grade | R2/S2 |

## Intent

A session sharing a checkout holds a claim naming its task and the paths its commit owns,
and stages only those paths.

## Context

roadkeep and Shio, where several agent sessions worked in one checkout and the owner's commit
tool stages the whole tree. Every observation is of one person running several sessions; no
team is in the evidence.

## Problem

Sessions in one tree share one index. Whatever stages the whole tree, or a whole file, takes
the other session's edits under its own message, and both commits are green.

## Forces

- The shared commit tool is written to stage everything.
- The agent is not the only stager: hooks and stage lines a tool prints stage too.
- Two sessions can edit the same file.

## Solution

roadkeep answered its first incident the same day with a claim that carries the paths its
commit owns, so a second session is sent to other work and each commit knows its own paths.
Its version hook now stages only what it wrote, and its stage line names what no claim
accounts for. Shio's sessions reached the same separation without a claim, staging by path
and saying so in the message.

## Consequences

Staging by path breaks Shio's written rule to commit through the stage-everything tool, and
the agent then writes the message too. It does not separate two sessions editing one file,
which a later roadkeep incident showed, and misattribution came back twice after the first
remedy, through a hook and through a printed stage line. Whether the claim ended the
incidents is not recorded, and how long a claim lasts is an open question.

## Known uses

- roadkeep: "sessions, two commits, each holding the other's work, both green" [roadkeep@64195176:docs/IMPROVEMENTS.md#L129],
  answered by "a claim carries the paths its commit owns" [roadkeep@3655014c].
- roadkeep: "It stages only what it wrote (RK320)." [roadkeep@91754240:.githooks/pre-commit#L15]
- Shio: "Hand-authored and staged by path: another session has seven Java files in flight." [shio@871410748]

## Related

- Resolves: [Stage everything](../anti-patterns/stage-everything.md).
- Rules: [CS-1](../../CS.md), [CS-2](../../CS.md), [CS-3](../../CS.md) and [CD-3](../../CD.md).
- Findings: [F201](../../../evidence/findings/F201.md) and
  [F200](../../../evidence/findings/F200.md).
