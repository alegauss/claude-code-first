# Claude Code First: a specification

This specification states how to run a software project in which Claude Code is the
primary author of the code and a person governs what is built. Every rule in it rests on
graded findings from five such projects, or on documented behaviour of the harness, and
says which.

## Scope

It covers the repository practices that decide whether an agent's work can be trusted
and kept: what the agent is told and what that costs, how work is planned and closed, how
it becomes commits, what checks it before it is called done, which rules are enforced by
the harness rather than by instructions, permissions, where sessions run, projects that
ship tools for other agents, what the person must decide, several sessions in one
repository, and the prose agents write.

It does not cover:

- **Features of Claude Code.** The official documentation is cited, not restated; the
  facts a rule depends on are in [../evidence/harness.md](../evidence/harness.md).
- **One tool.** roadkeep and the audit plugin are reference implementations. A rule is
  written so that another tool could satisfy it.
- **Teams, other harnesses or other model families.** The evidence comes from one person,
  one harness and one model family; [../evidence/validity.md](../evidence/validity.md)
  states where the conclusions stop.
- **Changing an adopter's repository.** An audit against this specification reports and
  proposes; the project's owner decides.

## Who it is for

- **Researchers and experts**, who will want the method before any rule:
  [../evidence/method.md](../evidence/method.md), the
  [grading scale](../evidence/grading.md), the [findings](../evidence/findings/index.md)
  and the [threats to validity](../evidence/validity.md).
- **People adopting it**, on a new project or an existing one, who will want the rules
  and the level to aim for.
- **Agents**, who read one rule at a time and need each to stand on its own.

## How to read it

Start with [conventions.md](conventions.md): the conformance keywords, the form of a rule
and how rules are addressed. Then read the chapters in any order; each opens with the
problem it answers, stated from the findings, and each rule links the findings it rests
on. A reader who doubts a rule follows its findings to their observations, and the
observations to the pinned sources.

## Chapters

| Code | Chapter | Answers |
|---|---|---|
| IS | [Instruction surface and context economy](IS.md) | what an agent is told on every turn, and what that costs |
| PG | Planning governance | how work is planned, recorded and closed |
| CD | Change discipline | how finished work becomes commits |
| VG | Verification gates | what must run, and pass, before work is called done |
| GH | Guards and hooks | which rules the harness enforces rather than instructions |
| PS | Permissions and safety | what an agent may do without asking, and what stands in for asking |
| EP | Environment portability | where a session runs: web or local, shells, encodings |
| AP | Agent-facing product surfaces | projects that ship tools, skills or plugins for other agents |
| HR | The human role | what the person decides, and what an agent must not certify |
| CS | Concurrent sessions | several agent sessions in one repository |
| AW | Agent-written prose | the prose an agent writes, and how it is kept true |

The chapters are written from the findings register and appear here as they are
completed.
