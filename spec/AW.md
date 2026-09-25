# AW Agent-written prose

## The problem

In a project run this way the agent writes most of the prose: skills, READMEs, planning
files, commit messages. Three failures recur in it. A count or list typed into a sentence
went stale in silence in all five projects when what it described changed
([F7](../evidence/findings/F7.md)). Planning prose ran well past an instruction to be
brief, and only a limit refused at the write bounded it
([F5](../evidence/findings/F5.md)). And a writing rule stated only in a skill, with no
check reading the prose, was broken by the project that wrote it
([F6](../evidence/findings/F6.md), [F300](../evidence/findings/F300.md)).

The chapter grades rules about whether prose is true apart from rules about how it reads.
A wrong figure misleads the next session; a house style is a choice. The specification
takes no side on style, such as whether the em dash is allowed
([../evidence/divergences.md](../evidence/divergences.md), D7); it takes a side on how a
style a project chose is enforced.

### AW-1 Figures in prose are generated or checked

**A count, version or enumeration that prose states about the present state of the project MUST be generated from its source or checked against that source by a *gate*.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | by judgement |
| Findings | F7 |
| Harness facts | none |
| Threat | construct: a stale figure is known only where someone recorded finding it, so the cases found are a lower bound |
| Status | active |

Rationale: a number typed into a sentence is true when written and has no link to what it
counts, and an agent that later loads the prose trusts it. In all five projects such a
figure was found wrong after what it described changed, with nothing failing: freewilly's
`llms.txt` counted four window destinations against five, and its contributing guide names
two workflows where four are in the tree; winwright's README example lacked a key since the
verb that added it shipped ([F7](../evidence/findings/F7.md), R4/S4). The remedies that
held generated the figure from its source or checked the sentence against a measurement,
and winwright's check was seen to fail on a control. A check built from a typed list
reproduces the fault, so the check must read the source. The rule covers claims about the
present, not records of a moment such as a ledger entry's count on the day a task shipped.

### AW-2 Length limits on planning prose are refused at the write

**Prose an agent writes into a planning file MUST be held to a length limit that the write path refuses, not only to an instruction to be brief.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | by judgement |
| Findings | F5, F101 |
| Harness facts | none |
| Threat | internal: Shio's before and after is not controlled, since a rewrite preceded the limit by two days |
| Status | active |

Rationale: the agent writing a line knows the whole analysis behind it, and an instruction
to be brief competes with all of it. Under a one-sentence rule stated in prose, Shio's
roadmap held 95 active lines averaging 142 words, the worst 555, six of the worst eight
written in the session that then found the problem; in winwright, with limits refused at
the write, one rationale section still took five refusals before it fit
([F5](../evidence/findings/F5.md), R3/S3). After the limit, Shio's open task lines at the
pin average 52 words with none above 61 ([F101](../evidence/findings/F101.md), which
counts the same Shio failure and adds no origin). The refusal, not the instruction, is what
held the length. A refusal costs a round trip in which the text is sent again, and a limit
bounds length, not content ([F5](../evidence/findings/F5.md)).

### AW-3 A declared house style is checked by a gate

**A rule on the style of prose that a project declares SHOULD be checked by a *gate* that reads the prose it governs.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F6, F300 |
| Harness facts | none |
| Threat | internal: the judgement that the em dash is a defect has one origin, a writing skill shared across projects |
| Status | active |

Rationale: a rule in a skill is read only by a session that loads the skill, while a lint
reads every file it covers. freewilly removed 201 em dashes from its published prose and
wrote a skill so the next session would not restore them; with no gate reading the prose,
its pinned commit added two more ([F6](../evidence/findings/F6.md), R3/S4). Shio's site
lint refuses the mark and was recorded firing when one dash was restored as a control
([F6](../evidence/findings/F6.md)). More widely, a rule stated only in prose with no check
reading the text it governs was found broken in two projects by the project that wrote it
([F300](../evidence/findings/F300.md), R3/S3). The findings would admit MUST, but decision
D7 in [../evidence/divergences.md](../evidence/divergences.md) sets this rule at SHOULD.
Which style a project chooses is a documented choice; the rule applies only to a style it
has declared.

## Open questions

- **Declaring the writing rules in a trigger-loaded skill.** freewilly records its writing
  rules in a skill, and the one observation of that arrangement is that the rule did not
  hold without a gate ([F6](../evidence/findings/F6.md)). No finding shows where writing
  rules are best declared; the placement of detail in general is IS-2. Evidence that
  sessions which loaded the skill wrote prose closer to its rules than those that did not
  would settle it.
- **Commit bodies that record what was measured and how.** Shio marks five commits as
  hand-authored because the message carried a measurement or argument the diff did not
  contain, and a message generated from the diff misdescribed documentation commits
  ([F204](../evidence/findings/F204.md), R2/S2). Who states a commit's intent is decided in
  D5 ([../evidence/divergences.md](../evidence/divergences.md)); no finding shows that
  recording measurements in the body helped anyone who later read it. A recorded case in
  which a later session or audit depended on a measured body, or failed for lack of one,
  would settle it.
- **Declaring the project's language.** Every project in the corpus writes in English, and
  no finding records prose in another language reaching a repository or causing a failure.
  Such an incident, or a project whose agent wrote in a mix of languages without a declared
  rule, would settle it.
- **Figures in prose about the past.** AW-1 excludes records of a moment, such as a ledger
  entry's count. Whether such a record should carry the commit or date it was measured at
  rests on no finding; a case of a dated record misread as current would settle it.
