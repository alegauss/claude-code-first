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
- ✅ **CCF64** **the citation resolver takes about five minutes over 795 pointers, so it will be the gate a commit skips first** — The resolver reads each corpus through one git cat-file batch process and the pin's ancestry set: 1,972 pointers take 1.5 s, down from 273 s.
- ✅ **CCF63** **the resolver cannot check a quote that holds inline code or runs across comment-prefixed source lines** — A quote is now checked as written: it may wrap onto the line before its pointer, keep backticks and run across comment lines, and a wrapped quote no longer passes unread.

## Block C — Case studies and the findings register

- ✅ **CCF15** **no case study describes roadkeep: its timeline, agent surfaces, gates and the incidents that shaped them** — evidence/cases/roadkeep.md tells roadkeep's case in the shared nine sections with 121 resolving pointers, correcting the design where the pinned sources disagree.
- ✅ **CCF17** **no case study describes freewilly, the project that works without any instruction file** — evidence/cases/freewilly.md tells freewilly's case in the shared structure with 103 resolving pointers, and corrects the design on CONTRIBUTING, DD115 and the web-session commits.
- ✅ **CCF18** **no case study describes winwright, whose agent surface is shipped for other repositories to use** — evidence/cases/winwright.md tells winwright's case in the shared structure with 107 resolving pointers, and corrects the design on WW69, the reopened blocks and the red pushes.
- ✅ **CCF19** **no case study describes shio, the only project that adopted the practice after years of history** — evidence/cases/shio.md tells Shio's brownfield case in the shared structure with 114 resolving pointers, splitting before and after adoption by commit rather than by date.
- ✅ **CCF16** **no case study describes polyweave, the one project governed from its very first commit** — evidence/cases/polyweave.md tells polyweave's case in the shared structure with 112 resolving pointers, measuring throughput from the ledger and correcting the design on 871a15b.
- ✅ **CCF20** **lessons are scattered over five ledgers, so one is counted five times and a contradiction not at all** — evidence/findings/ holds 37 graded findings across five topics, each merging observations by independent origin with resolving pointers, and a generated index CI checks.
- ✅ **CCF21** **the projects disagree on attribution, instruction files, permissions and CI scope, and nothing settles it** — evidence/divergences.md settles seven divergences against graded findings, allowing a documented deviation where evidence cannot decide (design superseded: one register).
- ✅ **CCF22** **the drift already present in the corpus is uncatalogued, though each case shows prose rules decaying** — evidence/drift.md inventories nine verified contradictions inside corpus projects at their pins, with dates, days standing and whether a check could catch each.
- ✅ **CCF23** **no cross-project metrics exist, so claims about scale, cadence and context cost are adjectives** — scripts/corpus_metrics.py computes commits, cadence, commit conventions, ledgers, every-turn bytes and tests for all five pins into committed data, methods stated.

## Block D — The normative specification

- ✅ **CCF24** **the specification has no frame: no chapter order, no rule addresses and no conformance keywords** — spec/ has its frame: scope, audience and chapter list in README.md, and in conventions.md the RFC 2119 keywords tied to evidence grades, the rule form and permanent addresses.
- ✅ **CCF25** **terms such as every-turn file, governed file, gate, guard, ledger and verdict are used without definitions** — spec/glossary.md defines 18 terms, settling the corpus's two senses of a block, and a CI check fails any italic term in a rule sentence that has no entry.
- ✅ **CCF26** **no normative chapter says what may load on every turn and what must be trigger-loaded instead** — spec/IS.md states six rules on the instruction surface, each capped by its findings: a gated budget on any every-turn file, bounded skills and read-on-demand files, checked name lists.
- ✅ **CCF36** **no normative chapter covers the prose an agent writes, though model-written prose was measurably detectable** — spec/AW.md states three rules on agent prose: generated or checked figures (MUST, F7), length limits refused at the write (MUST), and gated style rules (SHOULD, per D7).
- ✅ **CCF28** **no normative chapter says how an agent turns finished work into commits** — spec/CD.md states six rules on turning work into commits: one task per commit, a gate between tasks, staging by path, the agent's own title, no empty filings, and a stated attribution policy.
- ✅ **CCF27** **no normative chapter says how an agent plans, records and closes work** — spec/PG.md states six planning rules satisfiable by any tool: governed files, symptom-first tasks, recorded false premises, rationale moved before deletion, criteria-closed blocks and deferral.
- ✅ **CCF33** **no normative chapter covers projects that ship tools, skills or plugins for other agents to use** — spec/AP.md states four rules for products agents use: gated token ceilings, names checked against the catalogue, tests from the published artefact, adoption proved in a consumer.
- ✅ **CCF29** **no normative chapter says what an agent must run, keep and report before calling work done** — spec/VG.md states nine rules on what must run and pass before work is done, from gates on the committed change to the third verdict, CI on every push and expiring red exceptions.

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

## Block I — Governance and publication of the specification

