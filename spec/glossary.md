# Glossary

Each term the rules use is defined once, here. In a rule's normative sentence a defined
term is written in italics, such as *every-turn file*, and `scripts/check_glossary.py`
fails the build when an italic term in a rule has no entry below. Where the corpus uses a
term in more than one sense, the entry says which one this specification adopts.

## Claude-Code-first project

A repository in which Claude Code is the primary author of code and documentation and a
person governs what is built and accepts the result. Identified by the repository, not by
self-description: from an adoption commit on, it carries an agent instruction surface and
plans its work through agent-facing tooling (see
[../evidence/validity.md](../evidence/validity.md), construct validity).

## every-turn file

A file the harness loads into the agent's context at the start of every session and keeps
there for every turn: `CLAUDE.md` in the locations the harness reads, and every file it
imports with an `@path` line. Its whole size is paid on every turn.

## trigger-loaded skill

A skill whose name and description are in context from the start but whose body is loaded
only when the skill is used. Its description is paid every turn; its body only on the
turns that need it.

## governed file

A planning file whose writes go through a tool that enforces its format, and whose hand
edits a hook refuses: in the corpus, the roadmap, ledger, rationale and decision files that
roadkeep owns.

## ledger

The governed file that records what has shipped, one entry per closed task, with the
outcome in one sentence. It is append-only in practice: an entry is corrected by a new
entry, not by editing history.

## rationale section

The design prose for one open task, kept in a governed file and deleted when the task
ships. What in it must outlive the work is moved, at shipping, into the code it explains
or into a decision record.

## decision record

A durable statement of a constraint and the alternative it rejected, written when the task
that settled it ships, and replaced only by a later decision that supersedes it.

## block

A named group of tasks in the roadmap. The corpus uses two states that are easy to
confuse: a block is **finished** when the ledger records entries under it and nothing is
open, and **empty** when its heading exists but no task was ever filed under it. This
specification uses both words in those senses.

## gate

A check whose failure stops the work: a test suite, a lint, a build or a script, run
before work is called done and, where it can be, in CI on every push. A check whose
failure only produces a warning is not a gate.

## guard

A hook that refuses an action at the moment the agent attempts it, such as a hand edit of
a governed file, and names the action to take instead. A guard acts before the change
exists; a gate acts after.

## verdict

The result a check reports: **passed**, **failed**, or the third verdict, **could not
run**, for a check that did not execute and so says nothing about the work. A check that
cannot report the third verdict turns "did not run" into "passed".

## red-suite exception

A recorded, dated permission for a named gate to stay red, tied to the task that will make
it green, and expiring. Without one, a red gate stops the work.

## claim

A marker that one session is working on one task, with the paths its commit will own, so
that a second session is sent elsewhere and each commit stages only its own paths. A claim
expires; it is not a lock.

## deferral

Setting an open task aside, with its reason, because it needs something absent: a person's
judgement, hardware, an account. A deferred task keeps its identifier and returns when the
thing it needs is present. It is not a retirement.

## realignment

Bringing a project that once followed this specification, and drifted, back into
conformance, starting from an audit that lists what drifted.

## conformance level

A named subset of the rules that a project can claim to meet in full. The three levels,
governed, gated and measured, are cumulative and are defined in
[conformance.md](conformance.md).

## waiver

A recorded, deliberate deviation from one rule: the rule's address, the reason, the date
and, where the deviation is temporary, when it ends. A deviation with a waiver is a
decision; one without is drift.

## documented deviation

A choice between practices that the evidence cannot decide, recorded where the agent reads
it. Unlike a waiver, it departs from no rule; the specification leaves the choice open
([../evidence/divergences.md](../evidence/divergences.md)).
