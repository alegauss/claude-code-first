# Conformance

A project conforms at a level when it meets every rule of that level and of every level
below it. The levels are cumulative, and each is a point where a project can stop and
still be coherent: all-or-nothing conformance would stop every existing project, Shio
among them, from ever claiming any of it.

## The levels

**Level 1, governed.** The agent is told little and precisely, planning goes through
governed files, work reaches history one task per commit, and the agent does not certify
what needs a person. These rules cost a configuration file, a planning tool and a commit
habit; they need no test infrastructure.

**Level 2, gated.** Nothing is called done that a gate has not passed, gates run in CI on
every push, guards stand behind the rules the agent broke, and the configuration that
wires them is itself under a gate. These rules cost test and CI work, and they are where
most of the corpus's recorded failures were stopped.

**Level 3, measured.** What the project says about itself is generated or checked:
figures, lists, ceilings on everything read on demand, drift between copies, and
measurements taken before a change. These rules cost the most to adopt and pay off as a
project grows.

**The agent-facing profile.** The rules of chapter AP apply only to projects whose
product is used by agents. They form a profile claimed alongside a level, not a level of
their own.

## Assignment of the rules

A rule's level is set by two things: how strong its evidence is, which its keyword
already reflects, and what it costs to adopt. A rule that needs only configuration or a
habit sits low; one that needs a gate or a measurement sits higher. A SHOULD at a level
is part of that level: a project meets it, or records a waiver.

| Rule | Keyword | Level | Why this level |
|---|---|---|---|
| IS-1 | MUST | 1 | a budget in configuration and a lint; the most measured failure in the corpus |
| IS-2 | SHOULD | 1 | an editing habit on a file the project already has |
| IS-3 | SHOULD | 1 | a sentence in each skill's description |
| IS-4 | MUST | 3 | ceilings on every file read on demand need a gate per file |
| IS-5 | MUST | 3 | checking names against code needs a test that reads both |
| IS-6 | SHOULD | 3 | measuring served schemas needs the server's own output |
| PG-1 | SHOULD | 1 | adopting a planning tool and its guard |
| PG-2 | SHOULD | 1 | a habit enforced by the planning tool's schema |
| PG-3 | SHOULD | 1 | a habit: retire or restate, never rewrite |
| PG-4 | MUST | 1 | a step at shipping, where rationale would otherwise be lost |
| PG-5 | MUST NOT | 1 | criteria written with the block, read before closing it |
| PG-6 | SHOULD | 1 | a deferral instead of an open line |
| CD-1 | SHOULD | 1 | a commit habit, countable from the ledger |
| CD-2 | SHOULD | 1 | a working habit |
| CD-3 | SHOULD | 1 | a staging habit |
| CD-4 | SHOULD | 1 | a title passed by the agent |
| CD-5 | MUST NOT | 1 | a bar on filing, applied at the moment of filing |
| CD-6 | SHOULD | 1 | one sentence in the commit rules |
| HR-1 | MUST NOT | 1 | the boundary the rest of the practice trusts |
| HR-2 | SHOULD | 2 | a stored bar needs somewhere a check reads it from |
| PS-1 | MUST | 1 | naming, in committed files, what replaces the prompts removed |
| PS-2 | SHOULD | 2 | deny rules or guards for forbidden actions |
| PS-3 | SHOULD NOT | 1 | a habit and an ignore rule |
| AW-2 | MUST | 1 | the planning tool refuses over-long text at the write |
| VG-1 | MUST NOT | 2 | gates exist and run before done |
| VG-2 | MUST NOT | 2 | gate commands written without pipes |
| VG-3 | MUST | 2 | a third verdict in the gate's reporting |
| VG-5 | MUST | 2 | a CI workflow on every push |
| VG-6 | MUST | 2 | filing a red outside the change as a defect |
| VG-7 | SHOULD | 2 | an expiring exception record and its check |
| VG-8 | MUST NOT | 2 | a covering check before a task ships |
| GH-1 | MUST | 2 | a guard or gate for each rule seen broken |
| GH-2 | MUST | 2 | a CI gate behind every guard |
| GH-3 | SHOULD | 2 | guard matchers covering every route |
| GH-4 | MUST | 2 | a guard that reports when it cannot run |
| GH-5 | MUST | 2 | a test over the committed configuration |
| EP-1 | MUST | 2 | a declared tool copy and version |
| EP-2 | MUST | 2 | .gitattributes and a gate that holds it |
| EP-3 | MUST | 2 | named encodings at process boundaries |
| EP-4 | SHOULD | 2 | readers that expect a byte-order mark |
| EP-5 | MUST NOT | 2 | a byte check before an encoding defect is filed |
| EP-6 | SHOULD NOT | 2 | no heredoc edits of source |
| CS-1 | SHOULD | 2 | claims in the planning tool |
| CS-2 | SHOULD | 2 | staging limited to the claim |
| CS-3 | SHOULD | 2 | commit-time hooks that stage only their own change |
| CS-4 | MUST | 2 | a disturbed run reported as could not run |
| VG-4 | SHOULD | 3 | a roll call of discovered against reported tests |
| VG-9 | SHOULD | 3 | a measurement before a change and after it |
| GH-6 | SHOULD | 3 | a gate comparing the answering copy with its source |
| AW-1 | MUST | 3 | figures generated or checked |
| AW-3 | SHOULD | 3 | a gate over the prose a style rule governs |
| CS-5 | SHOULD NOT | 3 | measurements taken only on a quiet tree |
| AP-1 | MUST | profile | token ceilings on every served surface |
| AP-2 | MUST | profile | names in agent-facing text checked against the catalogue |
| AP-3 | MUST | profile | tests run from the published artefact |
| AP-4 | MUST | profile | adoption proved in a named consumer |
| AP-5 | MAY | profile | a placement choice, made once per capability |
| AP-6 | SHOULD | profile | a benchmark with fixtures for both paths |

## Claiming conformance

A project claims conformance in its `ccf.toml` ([deviations.md](deviations.md)): the
level, the profile if it applies, and the version of this specification it is judged
against, with a waiver for each rule it departs from on purpose. The claim holds only while an audit report, made against that version
and a stated commit of the project, backs it. A waived rule appears in the report as waived, with its reason; a departure
without a waiver is drift and appears as a failure.
