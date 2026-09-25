# PS Permissions and safety

## The problem

The projects treated permission prompts as a cost to remove. Where the committed settings
show a posture, they allow most tools by bare name with empty deny and ask lists, and the
control left in place of a prompt is a hook that refuses hand edits of the planning files
and never grants anything itself ([F402](../evidence/findings/F402.md)). Such a hook
answers only for the calls it is matched on, and every recorded gap in one let work
through with nothing saying that the guard was absent ([F301](../evidence/findings/F301.md)).
What the corpus guards is narrow: hand edits of the governed files and, in winwright, a
hand-written test harness. No committed control limits destructive shell commands,
network access or pushes, and a credential is kept out of a commit in one project by an
ignore line alone. No finding records harm done through a broad allow list, and none
records harm a prompt prevented. So this chapter does not recommend the corpus's posture,
and it cannot condemn it either. It requires what the findings carry, and leaves the rest
as open questions.

### PS-1 Name what stands in for a removed prompt

**A project that removes permission prompts, by a committed allow rule or by a local bypass, MUST name in its committed files the *guard* or *gate* that stands in for them.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 1 |
| Checked | by judgement |
| Findings | F402, F301 |
| Harness facts | H4, H6, H7 |
| Threat | construct: a local bypass is uncommitted, so outside every pin |
| Status | active |

Rationale: this is decision D3 in [../evidence/divergences.md](../evidence/divergences.md).
Prompts were removed in four projects and a refusing hook stood in for them
([F402](../evidence/findings/F402.md), R3/S2). A hook is fail-open by design and answers
only for what reaches it, so an absent, unmatched or unbuilt guard looks exactly like one
that approved, and the backstop two projects name for its gaps is a gate that runs at the
commit or in CI ([F301](../evidence/findings/F301.md), R3/S3). A reader who cannot see
which controls replace the prompts cannot tell a covered action from an uncovered one.
The rule covers a local bypass too: settings such as `settings.local.json` sit above the
shared project settings (H7) and were never committed in the corpus, so the posture a
session actually ran under is invisible unless the project writes down what compensates
for it. The breadth of the allow list itself is a documented deviation and is not
settled here (see Open questions).

### PS-2 A forbidden action is refused, not only forbidden

**An action a project forbids its agent to take SHOULD be refused by a committed deny or ask rule or by a *guard*, and not stated only in prose.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 2 |
| Checked | by judgement |
| Findings | F300, F301, F402 |
| Harness facts | H6, H7 |
| Threat | construct: a forbidden action taken and not recorded leaves no trace |
| Status | active |

Rationale: a rule stated only in prose, with nothing that reads it, was found broken by
the repository that wrote it, in two projects and by count
([F300](../evidence/findings/F300.md), R3/S3). The corpus forbids some actions only that
way: polyweave's commit rule says "staged by path, never pushed" [polyweave@6d1c136:CLAUDE.md#L62-L63],
and no committed control limits shell commands other than those naming a governed file
([F402](../evidence/findings/F402.md)). The mechanisms that do refuse are the harness's
deny and ask rules (H7) and a `PreToolUse` hook's deny (H6), each covering only what it
matches ([F301](../evidence/findings/F301.md)). F300 would admit a MUST. The keyword is
held at SHOULD because every broken rule F300 records is a rule about text (a roadmap
format, a pipe in a documented command, a punctuation mark), and no source records a
forbidden action being taken, so the finding's mechanism is carried here to a kind of rule
it was not observed on. Where a project forbids nothing in prose, this rule asks nothing
of it; what a project should forbid is an open question.

### PS-3 No credential in the working tree

**A credential SHOULD NOT be stored in a repository's working tree, ignored or not.**

| Field | Value |
|---|---|
| Keyword | SHOULD NOT |
| Level | 1 |
| Checked | by judgement |
| Findings | F200 |
| Harness facts | none |
| Threat | internal: the leaks are of one shared commit tool |
| Status | active |

Rationale: a commit tool that stages everything committed whatever else the working tree
held (run logs, bytecode, a settings file changed mid-session), and each ignore rule
written in answer closed only the pattern it named, after that pattern had leaked once
([F200](../evidence/findings/F200.md), R2/S2). freewilly keeps a credential file in its
tree and says of the ignore line that excludes it that it "is the only thing keeping it out of a commit" [freewilly@c1c2eaf:.gitignore#L22].
A credential under a name the ignore file does not match would ride into the next commit
the same way. No credential is recorded as having leaked, so the rule rests on the
mechanism F200 records for files in general, and it carries that finding's SHOULD and no
more. Storing credentials outside the tree, in the user's configuration or the
environment, removes the question of which pattern covers them.

## Open questions

- **How broad an allow list may safely be.** Shio and freewilly allow nearly every tool
  with `acceptEdits`, polyweave allows `Bash(*)`, roadkeep and winwright commit no allow
  rules ([F402](../evidence/findings/F402.md)). No finding records harm done through a
  broad list, and none records harm prevented by a prompt, so decision D3 makes the breadth
  a documented deviation. Settling it needs a record of what the prompts caught or missed:
  a log of the guards' and the harness's deny and ask answers, and of what the agent did
  next, which no project keeps ([F301](../evidence/findings/F301.md) notes the pins cannot
  say how much the hooks prevented).
- **Deny or ask rules for irreversible actions.** Destructive shell commands, network
  access, force pushes and history rewrites are guarded by nothing in the corpus. That is
  an absence of a control, and the corpus also records no incident of one of these
  actions going wrong. The grading scale admits no rule from the absence of an incident,
  so a minimum set of deny or ask rules is not required here. It would be settled by a
  recorded incident of such an action in a project run this way, or by a comparison of
  projects with and without the rules that counts prompts and harms.
- **Pushes made by the person.** Only polyweave states that commits are never pushed, in
  prose (S1), and roadkeep releases on a push to main. No source records an agent's push
  causing harm, or a push the person would have refused. A rule needs such a record, or a
  measured cost of pushes made by the agent.
- **A local bypass as a posture.** Whether any project ran under `bypassPermissions`
  cannot be seen at the pins, because local settings were never committed
  ([F402](../evidence/findings/F402.md)). PS-1 requires the compensating controls to be
  named, but whether a bypass is safe given those controls is not observable. A committed
  record of the mode each session ran under would make it a question the corpus could
  answer.
- **Whether a guard should fail open.** The projects make their guards allow on their own
  errors, and no source records a guard failing closed and blocking work
  ([F301](../evidence/findings/F301.md)). The trade rests on stated reasoning (S1). A
  recorded closed failure, or a count of silent gaps against blocked turns, would settle
  it.
