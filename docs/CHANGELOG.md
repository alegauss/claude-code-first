# Shipped Ledger

## Block A — The repository follows its own rule

- ✅ **CCF1** **a session opening this repository is told nothing: no every-turn file states purpose, language or write paths** — A session opening this repository now loads agents.md through .claude/CLAUDE.md, stating the purpose, three laws on evidence, English and roadkeep writes, and the layout.
- ✅ **CCF2** **the governed docs have no guard here, so a hand edit of ROADMAP.md or IMPROVEMENTS.md passes unnoticed** — A hand edit of a governed doc is now denied by a committed PreToolUse guard naming the roadkeep command to use, on every clone, with a merge driver for the four files.
- ✅ **CCF3** **no gate runs on push, so a lint failure or a broken link in the specification reaches main unremarked** — Every push and pull request now runs roadkeep lint, an offline link check and a Markdown rule set; both new gates were seen failing locally (design superseded: lint is in roadkeep.yml).
- ✅ **CCF4** **nothing states how work is committed here, so batching, stray files and mislabelled docs commits are all possible** — Committing here is a trigger-loaded ccf-dev skill: one task per commit, staged by path, message from a file, the three gates first (design superseded: staged by path).
- ✅ **CCF5** **the every-turn files carry no size budget, so they can grow the way Shio's agents.md reached 186 KB** — agents.md and .claude/CLAUDE.md now carry line and byte budgets lint enforces, and every skill written here is capped at 700 characters of description and 6,000 of body.
- ✅ **CCF6** **a Write over an existing file is accepted silently here, the path that destroyed about 700 lines in pportal** — A Write over an existing non-empty file is now refused by a PreToolUse hook naming Edit, vendored from polyweave with its source commit in the header.

## Block B — Research method and the evidence corpus

- ✅ **CCF7** **no protocol says how evidence is gathered or judged, so a finding here cannot be reproduced or challenged** — evidence/method.md states the research questions, case design, sources, extraction queries, coding scheme and disagreement rule; the first five prompts are kept verbatim.
- ✅ **CCF8** **the corpus is named by path only, so a citation breaks as soon as a source repository moves on** — evidence/corpus.md pins each project to the full commit the notes read, each confirmed as HEAD during extraction, with remotes, work outside the pins and descriptive data.
- ✅ **CCF9** **an evidence pointer has no grammar, so nothing can check that the path, line or commit it names exists** — A pointer grammar is defined, and a tested resolver checks each pointer's project, commit, path, lines and quote against the pinned corpus in CI (design recorded in `evidence/method.md`).
- ✅ **CCF10** **claims carry no strength, so one incident in one project reads like a pattern seen in all five** — evidence/grading.md grades findings on recurrence and strength, counts copied practice once, maps grades to MUST, SHOULD and MAY, and sets itself against EBSE levels.
- ✅ **CCF11** **the field notes were extracted by agents and not one of their claims has been checked against the pinned sources** — All 564 field-note claims are marked against the pins, 789 pointers resolve, and the error rate is recorded: 13.8% overall, 12.9% to 16.3% per project.
- ✅ **CCF12** **threats to validity are unstated: one author, one harness, one model family, five projects over six months** — evidence/validity.md states the construct, internal, external and reliability threats, traces the direction of copying from dated commits, and reports the measured error rate.
- ✅ **CCF13** **the Claude Code behaviour the spec relies on is cited from memory rather than from versioned documentation** — evidence/harness.md registers 14 documented harness facts with page, date and CLI 2.1.280, and 3 observed ones with evidence, one now contradicted by the docs.
- ✅ **CCF14** **no related work is surveyed, so the spec cannot say what is new and what restates ADRs, RFC 2119 or pattern languages** — evidence/related-work.md surveys ADRs, RFC 2119, patterns, Diataxis, commits, method, Anthropic's guide and four agent studies, and names five claims with no precedent.

## Block C — Case studies and the findings register

- ✅ **CCF15** **no case study describes roadkeep: its timeline, agent surfaces, gates and the incidents that shaped them** — evidence/cases/roadkeep.md tells roadkeep's case in the shared nine sections with 121 resolving pointers, correcting the design where the pinned sources disagree.
- ✅ **CCF17** **no case study describes freewilly, the project that works without any instruction file** — evidence/cases/freewilly.md tells freewilly's case in the shared structure with 103 resolving pointers, and corrects the design on CONTRIBUTING, DD115 and the web-session commits.
- ✅ **CCF18** **no case study describes winwright, whose agent surface is shipped for other repositories to use** — evidence/cases/winwright.md tells winwright's case in the shared structure with 107 resolving pointers, and corrects the design on WW69, the reopened blocks and the red pushes.
- ✅ **CCF19** **no case study describes shio, the only project that adopted the practice after years of history** — evidence/cases/shio.md tells Shio's brownfield case in the shared structure with 114 resolving pointers, splitting before and after adoption by commit rather than by date.

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

## Block I — Governance and publication of the specification

