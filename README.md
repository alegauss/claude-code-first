# Claude Code First

An evidence-based specification of how to run a software project in which Claude Code is
the primary author of the code and a person governs what is built. Each rule rests on
graded findings from five projects run this way, and each finding on pointers into their
pinned sources, which a gate checks on every push. The specification says what a project
must do so that an agent's work can be trusted and kept, and how far that claim is
supported.

## Where to start

- **Adopting it** on a new project: [adoption/greenfield.md](adoption/greenfield.md), the
  [templates](templates/README.md), and the [conformance levels](spec/conformance.md).
  On an existing codebase, or to bring a drifted project back, see the other guides in
  [adoption/](adoption/).
- **Auditing a repository** against it: install this repository as a Claude Code plugin
  and run its `audit` skill, which reports against [spec/report.md](spec/report.md).
  `scripts/check_conformance.py` decides the rules a script can decide, without the
  plugin.
- **Judging it as research**: the [traceability matrix](spec/traceability.md) from rules to
  findings to sources, the [method](evidence/method.md), the
  [grading scale](evidence/grading.md), the [findings](evidence/findings/index.md), the
  [threats to validity](evidence/validity.md) and [how it was written](AUTHORSHIP.md).

## Layout

| Folder | What is in it |
|---|---|
| [spec/](spec/README.md) | the specification: conventions, the chapters, conformance, reports, versioning |
| [spec/catalogue/](spec/catalogue/README.md) | named patterns and anti-patterns, each linked to its rules |
| [evidence/](evidence/method.md) | the protocol, the pinned corpus, field notes, case studies, findings, metrics |
| [adoption/](adoption/) | how to adopt the practice, or realign to it |
| [templates/](templates/README.md) | conforming files to start from |
| `skills/`, `agents/`, `.claude-plugin/` | the audit plugin |
| `scripts/` | the gates and tools, standard library only |
| `docs/` | this repository's own backlog, ledger and decisions |

## Status

The specification is at a 0.x version: its rules have not yet been tested by auditing the
five projects they came from, which version 1.0 waits for
([spec/versioning.md](spec/versioning.md)). The current version is the `version` in
[.claude-plugin/plugin.json](.claude-plugin/plugin.json). The figures about the corpus
are generated, never typed: see [evidence/metrics/](evidence/metrics/README.md). No
license has been chosen yet.

## Citing it

Cite it with [CITATION.cff](CITATION.cff), naming the version you read.
