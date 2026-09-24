# Roadmap (active backlog)

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

- 🛠 **CCF7** (deps: —) **no protocol says how evidence is gathered or judged, so a finding here cannot be reproduced or challenged** — An academic specification is only as strong as the method behind it, and today that method is five agent prompts nobody recorded. → §CCF7
- 📋 **CCF8** (deps: —) **the corpus is named by path only, so a citation breaks as soon as a source repository moves on** — Every source project commits daily, and a line number without a commit cannot be found again within a week. → §CCF8
- 📋 **CCF9** (deps: CCF8) **an evidence pointer has no grammar, so nothing can check that the path, line or commit it names exists** — Shio's figures in agents.md drifted from 25 to 28 unnoticed until a test demanded a source; citations here need the same check. → §CCF9
- 📋 **CCF10** (deps: CCF7) **claims carry no strength, so one incident in one project reads like a pattern seen in all five** — Expert readers weigh a rule by its support; without a grade they must reread the sources to learn it. → §CCF10
- 📋 **CCF11** (deps: CCF8, CCF9) **the field notes were extracted by agents and not one of their claims has been checked against the pinned sources** — The notes already mix quotes with inferences, and every later finding would inherit whatever error they carry. → §CCF11
- 📋 **CCF12** (deps: CCF7) **threats to validity are unstated: one author, one harness, one model family, five projects in three months** — A specification consulted by experts must say where its conclusions stop, or it will be read as general law. → §CCF12
- 📋 **CCF13** (deps: —) **the Claude Code behaviour the spec relies on is cited from memory rather than from versioned documentation** — Several lessons are harness facts, such as plugins absent on the web or settings rewritten mid-session, that a release can change. → §CCF13
- 📋 **CCF14** (deps: —) **no related work is surveyed, so the spec cannot say what is new and what restates ADRs, RFC 2119 or pattern languages** — An academic reader first asks what a work adds to what already exists, and without a survey the answer is an assertion. → §CCF14

## Block C — Case studies and the findings register

- 📋 **CCF15** (deps: CCF11) **no case study describes roadkeep: its timeline, agent surfaces, gates and the incidents that shaped them** — Roadkeep is both a corpus project and the tool three others govern with, so its lessons are the most copied and the easiest to overweight. → §CCF15
- 📋 **CCF16** (deps: CCF11) **no case study describes polyweave, the one project governed from its very first commit** — Polyweave shipped about a hundred tasks in three days, so it shows a mature practice applied from day one, with the least history. → §CCF16
- 📋 **CCF17** (deps: CCF11) **no case study describes freewilly, the project that works without any instruction file** — Freewilly has no every-turn file and a drained backlog, so it tests which rules survive when nothing is loaded by default. → §CCF17
- 📋 **CCF18** (deps: CCF11) **no case study describes winwright, whose agent surface is shipped for other repositories to use** — Winwright designs for an agent that is not its author, which makes it the corpus's evidence on agent-facing products. → §CCF18
- 📋 **CCF19** (deps: CCF11) **no case study describes shio, the only project that adopted the practice after years of history** — Shio had 1,777 commits before adoption, so its transition is the corpus's only record of adopting late. → §CCF19
- 📋 **CCF20** (deps: CCF10, CCF15, CCF16, CCF17, CCF18, CCF19) **lessons are scattered over five ledgers, so one is counted five times and a contradiction not at all** — A specification cites findings, not anecdotes, and the register is where five observations become one graded claim. → §CCF20
- 📋 **CCF21** (deps: CCF20) **the projects disagree on attribution, instruction files, permissions and CI scope, and nothing settles it** — A divergence left open becomes either silence in the spec or a rule chosen by whoever edited it last. → §CCF21
- 📋 **CCF22** (deps: CCF15, CCF16, CCF17, CCF18, CCF19) **the drift already present in the corpus is uncatalogued, though each case shows prose rules decaying** — A stale contributor guide, a skill contradicting its index and a config contradicting agents.md are the failure this spec must prevent. → §CCF22
- 📋 **CCF23** (deps: CCF8) **no cross-project metrics exist, so claims about scale, cadence and context cost are adjectives** — Figures such as bytes loaded per turn or commits per active day mean something only when computed the same way for all five. → §CCF23

## Block D — The normative specification

- 📋 **CCF24** (deps: CCF10) **the specification has no frame: no chapter order, no rule addresses and no conformance keywords** — Chapters written before the frame exists would each invent a rule format, and no reader could cite a rule by address. → §CCF24
- 📋 **CCF25** (deps: CCF24) **terms such as every-turn file, governed file, gate, guard, ledger and verdict are used without definitions** — The five projects use the same words with different meanings, and a spec whose terms drift cannot be conformed to. → §CCF25
- 📋 **CCF26** (deps: CCF20, CCF24) **no normative chapter says what may load on every turn and what must be trigger-loaded instead** — Context economy is the most strongly supported finding, measured in three projects, and it still has no rule. → §CCF26
- 📋 **CCF27** (deps: CCF20, CCF24) **no normative chapter says how an agent plans, records and closes work** — Every project converged on governed roadmap, ledger and rationale files after prose limits failed, and that convergence needs stating. → §CCF27
- 📋 **CCF28** (deps: CCF20, CCF21, CCF24) **no normative chapter says how an agent turns finished work into commits** — One task per commit is called the most violated rule in two projects, and stray files reached commits in three. → §CCF28
- 📋 **CCF29** (deps: CCF20, CCF24) **no normative chapter says what an agent must run, keep and report before calling work done** — Silent greens, piped exit codes and suites red for nineteen commits recur across the corpus, each costing more than a gate would. → §CCF29
- 📋 **CCF30** (deps: CCF13, CCF20, CCF24) **no normative chapter says which rules must be enforced by hooks rather than by instructions** — Every rule the corpus enforces reliably is a hook or a gate, and every rule left to prose recurs as an incident. → §CCF30
- 📋 **CCF31** (deps: CCF21, CCF30) **no normative chapter states a permission and safety posture, and the corpus runs with prompts bypassed** — Two projects bypass permission prompts locally; whether guards and gates compensate is a claim to test, not to recommend. → §CCF31
- 📋 **CCF32** (deps: CCF13, CCF20, CCF24) **no normative chapter covers where a session runs: web versus local, shells, encodings and line endings** — Plugins absent on the web, mixed line endings, cp1252 mojibake and heredoc corruption each cost sessions in more than one project. → §CCF32
- 📋 **CCF33** (deps: CCF20, CCF24) **no normative chapter covers projects that ship tools, skills or plugins for other agents to use** — Four of five projects ship an agent surface, and their lessons on schemas, budgets and discoverability are the most measured. → §CCF33
- 📋 **CCF34** (deps: CCF20, CCF24) **no normative chapter says what the person decides and what an agent must never certify for itself** — Polyweave and roadkeep both found an agent judging its own output to be the weakest point, yet the boundary is not stated. → §CCF34
- 📋 **CCF35** (deps: CCF20, CCF24) **no normative chapter covers several agent sessions working in one repository at once** — Sessions committing each other's code and concurrent gate runs reporting false reds were measured in roadkeep and Shio. → §CCF35
- 📋 **CCF36** (deps: CCF20, CCF24) **no normative chapter covers the prose an agent writes, though model-written prose was measurably detectable** — 207 em dashes in freewilly and stale typed counts in three projects show that agent prose needs rules just as code does. → §CCF36

## Block E — Patterns and anti-patterns

- 📋 **CCF37** (deps: CCF24) **no form fixes how a pattern or anti-pattern is written, so entries would mix problem, remedy and evidence** — A catalogue can be searched and compared only when every entry answers the same questions in the same order. → §CCF37
- 📋 **CCF38** (deps: CCF20, CCF37) **the recurring failures have no names, so a reviewer cannot say which one a project is committing** — A name turns a long explanation into a word two people share, and the corpus holds at least a dozen failures seen more than once. → §CCF38
- 📋 **CCF39** (deps: CCF20, CCF37) **the practices that resolved those failures are described only inside the projects that invented them** — An adopter needs the remedy in a portable form, stripped of the project it was found in, with its evidence still attached. → §CCF39

## Block F — Conformance and the audit

- 📋 **CCF40** (deps: Block D) **conformance has no levels, so a project cannot say how far it adopts the spec or what to do next** — All-or-nothing conformance would stop every brownfield project, Shio included, from ever claiming any of it. → §CCF40
- 📋 **CCF41** (deps: CCF40) **rules exist only as prose, so no tool can list them, filter them by level or check a repository against them** — An audit that must reread the whole spec to learn what to check spends the context the spec tells projects to save. → §CCF41
- 📋 **CCF42** (deps: CCF9, CCF41) **traceability is unchecked: a rule citing no finding, or a finding citing no evidence, would pass** — Being evidence-based is what sets this spec apart, so a broken trace must fail a build, not wait for a reader to notice. → §CCF42
- 📋 **CCF43** (deps: CCF41) **automatable rules have no checker, so each audit rederives by reading what a script could measure** — Budgets, hook wiring, ignore rules and CI presence are facts about files, and paying for an agent's judgement on them is waste. → §CCF43
- 📋 **CCF44** (deps: CCF43) **the rules that need judgement cannot be audited without an agent reading the whole spec** — Polyweave's scanner and verifier pair shows that a cheap scan plus a strong verification finds more, with fewer false findings. → §CCF44
- 📋 **CCF45** (deps: CCF41) **an audit report has no fixed format, so two audits of one project cannot be compared over time** — Realignment is measured by the difference between two audits, which needs the same fields, the spec version and the commit audited. → §CCF45
- 📋 **CCF46** (deps: CCF41) **a deliberate deviation from a rule cannot be recorded, so it reads as drift in every audit** — Shio's red-suite ledger shows exceptions work when dated, tied to a task and expiring; unrecorded ones become permanent. → §CCF46

## Block G — Adoption and realignment

- 📋 **CCF47** (deps: Block D, CCF40) **a new project has no starting kit, so each of the five wrote its own settings, hooks and skills** — Five hand-written copies of one launcher and one skill have already drifted apart; templates carry the rules and their evidence. → §CCF47
- 📋 **CCF48** (deps: CCF47) **starting a project Claude Code first has no ordered procedure, so the order the five learned in is repeated** — The others added the same pieces over weeks, each after an incident; an ordered bootstrap installs them before the incidents. → §CCF48
- 📋 **CCF49** (deps: CCF19, CCF47) **an existing codebase adopting the practice has no procedure, and Shio's transition lives only in its history** — Most future adopters are brownfield, and the one brownfield case shows the traps: a resident instruction file and an imported backlog. → §CCF49
- 📋 **CCF50** (deps: CCF44, CCF46, CCF47) **a project already Claude Code first that drifted has no path back except rereading the whole spec** — The owner's own projects are the first to need this: the drift inventory already lists contradictions in three of them. → §CCF50

## Block H — Validation against the corpus

- 📋 **CCF51** (deps: CCF44, CCF45) **roadkeep has never been audited against the specification, so its conformance is asserted, not measured** — Roadkeep supplied many of the rules, so its audit tests whether the spec merely describes its source or can find fault in it. → §CCF51
- 📋 **CCF52** (deps: CCF44, CCF45) **polyweave has never been audited against the specification, so its conformance is asserted, not measured** — Polyweave was governed from its first commit, so its audit tests whether early adoption leaves fewer gaps than late adoption. → §CCF52
- 📋 **CCF53** (deps: CCF44, CCF45) **freewilly has never been audited against the specification, so its conformance is asserted, not measured** — Freewilly has no instruction file and a stale contributor guide, so its audit tests the spec on a project that chose another shape. → §CCF53
- 📋 **CCF54** (deps: CCF44, CCF45) **winwright has never been audited against the specification, so its conformance is asserted, not measured** — Winwright ships a plugin to other repositories, so its audit is the first to exercise the chapter on agent-facing products. → §CCF54
- 📋 **CCF55** (deps: CCF44, CCF45) **shio has never been audited against the specification, so its conformance is asserted, not measured** — Shio is the largest and only brownfield project, with known drift between its skills and its index, so its audit is the hardest test. → §CCF55
- 📋 **CCF56** (deps: CCF51, CCF52, CCF53, CCF54, CCF55) **nothing shows the audit is accurate: its false findings and misses are unmeasured** — An audit with an unknown error rate cannot be cited as evidence of conformance, and experts will ask for that rate first. → §CCF56
- 📋 **CCF57** (deps: CCF50, CCF56) **the claim that conformance reduces cost has no before-and-after measurement on any realigned project** — The spec's value is a hypothesis until one project is measured before and after realignment on the same metrics. → §CCF57

## Block I — Governance and publication of the specification

- 📋 **CCF58** (deps: CCF24) **the specification has no version, so an audit cannot say which text it judged a project against** — Rules will change as evidence arrives, and a conformance claim without a version becomes false the day a rule tightens. → §CCF58
- 📋 **CCF59** (deps: CCF10, CCF58) **no process admits new evidence or a new rule, so the spec would either freeze or grow by opinion** — Other projects will realign and report what failed, and that feedback needs a path that keeps the evidence standard intact. → §CCF59
- 📋 **CCF60** (deps: CCF41) **an agent in another repository cannot consume the spec cheaply: no llms.txt and no page per rule** — Winwright measured an agent rendering three pages to learn a tool; reading the spec must cost less than the waste it prevents. → §CCF60
- 📋 **CCF61** (deps: —) **the work has no license, no citation metadata and no statement of how it was authored** — An academic reader must know how to cite it, and that an agent wrote most of it under a person's direction and with which checks. → §CCF61
- 📋 **CCF62** (deps: CCF24) **the repository has no README telling a newcomer what the spec is, how to read it and how to adopt it** — The README is the first page an expert or an adopter opens, and today it does not exist. → §CCF62

## Done when — Block A

- **A hand edit of a governed file is denied in a fresh session** The guard is the
  reason the rest of the backlog can be trusted, so it is checked by trying the edit,
  not by reading the settings.
- **CI fails a push that breaks lint or a link** Shown by a deliberately broken commit
  on a branch, since a gate never seen to fail is not known to work.
- **Every every-turn file is within a budget the gate enforces** The budget is a number
  in configuration that lint checks, not a sentence in a file.

## Done when — Block B

- **Every field-note claim is marked verified, corrected or refuted** Findings may cite
  sources only after the notes they were drawn from have been checked, and the error
  rate is recorded.
- **The resolver passes on every citation in the repository** A pointer that does not
  resolve at its pinned commit is a build failure, not a warning.
- **Method, corpus pins, grading, validity and harness facts are written** These five
  documents are what an expert reads before trusting any finding.

## Done when — Block C

- **Each of the five projects has a case study with the shared structure** The same
  sections in the same order let a reader compare projects without rereading them.
- **Every finding has a two-axis grade and a resolvable citation** A finding without a
  grade or a source cannot support a rule.
- **Every divergence between projects has a decision record** The spec takes a side, or
  records why the evidence cannot decide, for each practice the projects disagree on.

## Done when — Block D

- **Every rule has an address, a keyword, a level and cited findings** A rule missing
  any of the four cannot be conformed to, audited or traced.
- **Every term a rule uses has a glossary entry** Undefined terms are where two readers
  of one rule reach different verdicts.

## Done when — Block E

- **Every catalogue entry follows the form and links at least one rule** A pattern that
  makes nothing normative, or an anti-pattern no rule prevents, is a story rather than a
  specification artefact.

## Done when — Block F

- **The traceability gate runs in CI and passes** The evidence chain from rule to source
  is checked on every push.
- **The checker passes and fails its fixture repositories as designed** Each automatic
  rule is shown to detect its failure and to accept its conforming case.

## Done when — Block G

- **A repository built from the templates passes the checker** Templates that do not
  conform would spread non-conformance to every project that starts from them.
- **Greenfield, brownfield and realignment each have a guide and a skill** Each path an
  adopter can arrive by has an ordered procedure an agent can carry out.

## Done when — Block H

- **All five corpus projects have a committed audit report** The specification is judged
  against the projects it came from before it is offered to others.
- **Audit accuracy is reported with its sample size and limits** Conformance claims cite
  an audit whose error rate is known.

## Done when — Block I

- **Version 1.0 is tagged with release notes and citation metadata** A tagged, citable
  release is what an expert or an adopter can refer to.
- **Every rule is published on its own page with its grade** People and agents can link
  to, and read, one rule without the rest.

## Non-goals

- **A rule admitted because it sounds right** Every MUST, SHOULD or MAY traces to graded
  findings or to documented harness behaviour; a practice with no evidence is recorded
  as an open question, not as a rule.
- **A manual of Claude Code features** The spec cites the official documentation for
  what the harness does and states only practice; restating the manual would go stale
  with each release.
- **One tool made mandatory** Requirements are written so another tool could satisfy
  them; roadkeep and the audit plugin are reference implementations, never the
  requirement itself.
- **Editing an adopter's repository** The audit reports and offers tasks; filing them,
  or changing code in another project, is that project owner's decision and is never
  done on their behalf.
- **Claims beyond the corpus** Nothing is asserted about teams, other harnesses or other
  model families without evidence from them; the scope is stated in the validity
  threats, not implied.
