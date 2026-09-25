# CD Change discipline

## The problem

Every corpus project writes down one task per commit, and three of the four whose ledgers
can be counted still made commits that ship several tasks, from under 1 percent of ship
commits in roadkeep to about 4 percent in winwright
([F203](../evidence/findings/F203.md)). The owner's commit tool stages the whole tree, so
run logs, bytecode and a settings file the session rewrote were committed under another
task's message, and each ignore rule written in answer closed only the pattern that had
already leaked ([F200](../evidence/findings/F200.md)). The same tool has another model
write the message from the staged diff, and in Shio that message described documentation
commits as implementations ([F204](../evidence/findings/F204.md)). Tasks an agent filed
while working were retired as observations, duplicates or false premises in four projects
([F102](../evidence/findings/F102.md)). And the history cannot say which commits an agent
composed, because the co-author trailer is on 0 to about 7 percent of commits, clustered
in time ([F205](../evidence/findings/F205.md)). The rules below govern what one commit
holds, how it is staged, who states what it is, and what it files.

Where several sessions share one checkout, the rules in [CS.md](CS.md) apply as well.

### CD-1 One task per commit

**A commit that ships work SHOULD ship one task, and carry that task's code, its tests and its *ledger* entry together.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | automatically |
| Findings | F203, F206 |
| Harness facts | none |
| Threat | internal: the written rule and its loop are one origin copied across the projects |
| Status | active |

Rationale: [F203](../evidence/findings/F203.md) (R3/S3) counts, at each pin, the commits
that add two or more shipped entries to the ledger: 21 of 486 in winwright, 8 of 1,177 in
roadkeep and 3 of 281 in freewilly, all under a written rule against it. The grade would
admit a MUST, but polyweave is a contrary case, with no such commit in 110, and no source
explains the difference by a property of the cases, so the rule is one level lower. A
commit that holds one task and its ledger entry is what lets the history be read back
against the ledger by task id ([F206](../evidence/findings/F206.md), R2/S3), which is how
the counts in F203 were made. Conformance is decided from the repository: count, per
commit, the shipped entries it adds to the ledger, as F203's command does. The count is a
lower bound, since it cannot see a second task's code carried under one ledger line.

### CD-2 A batch is worked one task at a time

**When a session is asked to work several tasks, it SHOULD commit each task, after its *gate* has passed on the tree that commit holds, before it starts the next.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F203, F305 |
| Harness facts | none |
| Threat | internal: the loop remedy is one copied origin and was never seen failing a batch |
| Status | active |

Rationale: most batching commits in [F203](../evidence/findings/F203.md) name several
tasks in their subject, and in winwright 18 of the 19 that do fall within eight days; each
project's rule singles out a request to work several tasks as the occasion for batching. [F305](../evidence/findings/F305.md) (R3/S3) shows the cost of closing without a
check on the change as committed: in winwright the ship step edited the roadmap after the
run that proved the work, so "The red then lands on whoever runs next, about an entry their change never touched." [winwright@a686d44]
Working a batch as a sequence of single tasks, each committed on a passing gate, keeps
each close checkable and each red attributable to one task. The keyword is SHOULD because
the evidence is for the parts, batching and unchecked closes, and not for the loop as a
whole, which is one prescription copied between the projects and never measured.

### CD-3 Staging by path

**A commit SHOULD stage its own paths by name, unless a single session owns the checkout and the tree was checked for other changes first.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F200, F201 |
| Harness facts | none |
| Threat | construct: a stray caught before a commit leaves no trace, so the leaks are a lower bound |
| Status | active |

Rationale: this rule is decision D6 of
[../evidence/divergences.md](../evidence/divergences.md). A tool that stages everything
commits whatever the tree holds: in Shio a teed run log landed in a feature commit, and a
file named past the ignore rule written in answer landed in a later fix; in freewilly a
settings file the harness rewrote and a test's bytecode "shipped inside other changes"
([F200](../evidence/findings/F200.md), R2/S2). The ignore rules closed each pattern only
after it had leaked once, so an ignore file is not a substitute for naming the paths.
Where other sessions work in the same tree, a stage-everything commit carries their work
under its message ([F201](../evidence/findings/F201.md), R2/S2), which is why the
exception is limited to a checkout one session owns. Both findings rest on one origin, the
shared commit tool, so the keyword is SHOULD.

### CD-4 The title states the intent

**The agent that did the work SHOULD write the commit's title, stating the intent of the change and the id of the task it ships, rather than leave the title to a model that sees only the staged diff.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F204, F206 |
| Harness facts | none |
| Threat | construct: the misdescriptions are found cases, not a rate |
| Status | active |

Rationale: this rule is decision D5 of
[../evidence/divergences.md](../evidence/divergences.md). A message generated from the
staged diff by another model titled two documentation-only commits in Shio as
implementations, "feat: implement typed TypeScript DSL for post-types authoring" [shio@24da11f44]
among them, and wrote a body that contradicted the text its own commit added
([F204](../evidence/findings/F204.md), R2/S2). The diff of a document about a feature reads
like the feature; only the agent that made the change knows which it was. Naming the task
id in the subject is the convention in all five projects and joins each commit to its
ledger entry ([F206](../evidence/findings/F206.md), R2/S3). A generated body under a title
the agent wrote is conforming, as D5 decides, and so is a message the agent wrote whole.

### CD-5 A filing names something wrong

**A session MUST NOT file a task that names nothing wrong or missing.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | pending |
| Checked | by judgement |
| Findings | F102 |
| Harness facts | none |
| Threat | construct: a retirement is a lower bound, and a rate was measured in one session only |
| Status | active |

Rationale: in four projects, tasks filed during work were retired as observations,
duplicates or false premises, and in the one session that was measured, "Three of those ten qualified" [roadkeep@91754240:.claude/skills/roadkeep-dev/SKILL.md#L47]
([F102](../evidence/findings/F102.md), R3/S3). A filing costs the agent one command and
costs whoever picks it up a diagnosis, and a loop told to stop when nothing remains cannot
stop if each task files more than it ships. An observation that is not a defect or a gap
belongs in the commit body. The rule does not require a task to file anything: one that
revealed nothing wrong files nothing. Filings made from a hurried reading, a truncated
listing or open lines not read, inherit its error (F102), so a session checks what it
names before it files it.

### CD-6 Attribution is a stated choice

**A project SHOULD state, where its agent reads its commit rules, whether commits carry attribution to the agent.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F205 |
| Harness facts | none |
| Threat | construct: authorship by an agent cannot be read from git metadata |
| Status | active |

Rationale: this rule is decision D1 of
[../evidence/divergences.md](../evidence/divergences.md). The co-author trailer is on 0
to about 7 percent of commits in projects where an agent is the primary author, clustered
in time: 76 roadkeep commits up to 2026-09-01 and none of the 423 after it, 24 of
winwright's 33 on one day, none in polyweave ([F205](../evidence/findings/F205.md),
R2/S3). No project at its pin states a policy, so the trailer records how a commit was
made, not who made the change. No finding records harm from either choice, so the
specification requires neither attribution nor its absence; it asks only that the choice
be deliberate and written where the agent reads it. Either answer is conforming.

## Open questions

- **Naming follow-up work in the commit.** Commits in polyweave and winwright name the
  tasks they filed, as in "refactor(site): one C# reader for every generator (WW502), with WW507 filed" [winwright@3f5009b]
  ([F206](../evidence/findings/F206.md)). The corpus shows the convention in use but no
  failure where it was absent, so it admits no rule. A recorded case of a filing that
  could not be traced to the work that revealed it would settle it.
- **Saying whether downstream adopters are affected.** winwright's commits sometimes state
  their effect on repositories that consume the tool. No finding records an adopter
  harmed by a commit that did not say so; [F407](../evidence/findings/F407.md) shows
  consumers meeting a broken surface, but not that a note in the commit would have
  prevented it. An incident in which an adopter took up a breaking change unannounced
  would settle it.
- **How often a generated body misdescribes.** CD-4 governs the title. Whether the body a
  model writes from the diff is wrong often enough to require the agent to write it too is
  not known: [F204](../evidence/findings/F204.md) gives found cases, not a rate. A
  systematic comparison of generated bodies with their diffs would settle it.
- **Checking the tree before a stage-everything commit.** CD-3 allows staging everything
  where one session owns the checkout and the tree was checked first. No source records
  how that check was made or whether it caught a stray; the recorded remedies are ignore
  rules, which leaked ([F200](../evidence/findings/F200.md)). A count of strays caught by
  such a check, against strays that leaked, would settle what the check must be.
