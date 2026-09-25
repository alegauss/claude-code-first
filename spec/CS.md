# CS Concurrent sessions

## The problem

Several agent sessions working in one checkout share one index, one set of files and one
set of gate runs, and nothing fails when they collide. In roadkeep two sessions each
shipped a commit carrying the other's code, both green, and the same misattribution came
back twice after a remedy had shipped: through a version-bump hook that staged a whole
file another session had edited, and through a stage line the tool itself printed
([F201](../evidence/findings/F201.md)). Gates read the live tree, so another session's
uncommitted edits, or a second run of the same gate, produced reds and counts that were
not about the change: in Shio two overlapping runs reported 3 errors over 1,092 tests on a
tree that alone reported 1,894 green, and in roadkeep one run reported six failures, five
not about the code, against 1,940 passed ([F202](../evidence/findings/F202.md)). The rules
below keep each session's commit to its own work and make a gate say when the tree moved
under it.

**The limit of this chapter.** Every observation comes from one person running several
agent sessions in their own repositories. The corpus holds no evidence on teams of several
people, each with agents, sharing a repository, and nothing here should be read as covering
that case ([../evidence/validity.md](../evidence/validity.md), external validity).

### CS-1 A session claims its task and its paths

**A session working in a checkout that other sessions share SHOULD hold a *claim* naming its task and the paths its commit will own.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F201 |
| Harness facts | none |
| Threat | external: one person running several sessions, no teams |
| Status | active |

Rationale: in roadkeep the first incident, two commits each holding the other's task, was
answered the same day by a claim that "carries the paths its commit owns" [roadkeep@3655014c],
so that a second session is sent to other work and each commit knows which paths are its
own ([F201](../evidence/findings/F201.md), R2/S2). Shio's sessions reached the same
separation without a claim, by stating in each commit what another session had in flight,
as in "Hand-authored and staged by path: another session has seven Java files in flight." [shio@871410748]
The failure recurred in one project only, and whether the claim ended it is not recorded,
so the keyword is SHOULD. How long a claim lasts is an open question.

### CS-2 Staging stays inside the claim

**In a checkout that other sessions share, nothing that stages for a commit, whether the agent, a hook or a stage line a tool prints, SHOULD stage a path outside the session's *claim*.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F201, F200 |
| Harness facts | none |
| Threat | construct: an incident nobody filed leaves no trace, so whether the remedies worked is unknown |
| Status | active |

Rationale: [F201](../evidence/findings/F201.md) (R2/S2) records three routes by which one
session's commit took another's work in roadkeep: a commit staged beyond its task, a hook
that staged a whole file, and a stage line the tool printed that named a file both
sessions had touched. Only the first is the agent's own staging, so the rule covers every
stager, not the agent alone. A stage-everything tool is outside the claim by construction
([F200](../evidence/findings/F200.md)), which is why CD-3 in [CD.md](CD.md) allows it only
where one session owns the checkout. Staging by path does not separate two sessions that
edit the same file, as roadkeep's own rationale for the remedy notes and a later incident
showed (F201); that case is an open question.

### CS-3 A commit-time hook stages only what it wrote

**A hook that writes into a file while a commit is made SHOULD compute its change against the committed file and stage only that change.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F201, F301 |
| Harness facts | none |
| Threat | internal: both failures are of one hook in one project |
| Status | active |

Rationale: roadkeep's version-bump hook staged two whole files, so "an unrelated edit to either rides into the next commit" [roadkeep@91754240:docs/CHANGELOG.md#L572],
and did so with an edit another session had made; the fix is that "It stages only what it wrote (RK320)." [roadkeep@91754240:.githooks/pre-commit#L15]
([F201](../evidence/findings/F201.md), R2/S2). The same hook, reading the working copy
rather than what was committed, "re-armed itself for ever", and was
"measured over eight commits, the checkout reaching 0.1.392 while HEAD said 0.1.388" [roadkeep@91754240:.githooks/pre-commit#L22]
without blocking anything ([F301](../evidence/findings/F301.md)). A file that every commit
touches, such as a version, is where concurrent sessions meet, so the hook's change is
computed from the committed state and staged alone. Both failures are one hook's, in one
project, so the keyword is SHOULD.

### CS-4 A disturbed gate run is not a verdict on the change

**A *gate* whose run was disturbed by other work in the checkout, whether another session's edits or another run of the same gate, MUST report the *verdict* could not run, not passed or failed.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | by judgement |
| Findings | F202, F304 |
| Harness facts | none |
| Threat | internal: Shio's overlapping runs came from one session's background job, not from two sessions |
| Status | active |

Rationale: a gate reads the live tree and has no notion of whose edits it is reading
([F202](../evidence/findings/F202.md), R3/S3). Shio measured two overlapping runs of one
gate, which "reported 3 errors over 1092 tests where the tree alone reports 1894" [shio@821f18d74:scripts/run-gate.mjs#L57]
green, and twice on one day a commit had to argue that its reds were another session's
uncommitted work; roadkeep measured a run with six failures, five not about the code,
where "nothing in the output said so" [roadkeep@91754240:tests/conftest.py#L14]. Each
project made the run detect the condition, by different means: one run per gate at a time
in Shio, a snapshot taken at collection and a fingerprint naming
the file that moved in roadkeep. A red that is not about the change trains everyone to
ignore the next true one ([F304](../evidence/findings/F304.md), R3/S3). Two independent
origins, each measured, admit a MUST. The means are not fixed here; the verdict is. The
pins record no occasion on which a lock or a fixture was seen to refuse or skip a real
run.

### CS-5 No measurement on a moving tree

**A count or timing that a rule, a decision or a finding will cite SHOULD NOT be taken while another session has uncommitted work in the checkout.**

| Field | Value |
|---|---|
| Keyword | SHOULD NOT |
| Level | pending |
| Checked | by judgement |
| Findings | F202 |
| Harness facts | none |
| Threat | internal: the observations are measurements set aside, not wrong ones found later |
| Status | active |

Rationale: the mechanism that turns a gate red for another session's work also moves any
number taken from the tree ([F202](../evidence/findings/F202.md), R3/S3). Both projects
that measured the collision set measurements aside for it: Shio postponed a census because
it "would have been a moving target under it" [shio@1dcd16a1e], and roadkeep discarded its
own timing sweep as not a measurement because the tree moved under every run. The finding
would admit a MUST, but these observations are avoidances; no source records a wrong
number that was cited and later found to come from a moving tree, so the rule is one level
lower.

## Open questions

- **How long a claim lasts.** roadkeep's claims expire, so that a session that stopped
  does not hold its task for ever. No finding records a stale claim that blocked work or an
  expired claim that let two sessions collide, so neither the expiry nor its length is a
  rule. A recorded incident of either would settle it.
- **Two sessions editing the same file.** Staging by path does not separate two sessions'
  edits to one file ([F201](../evidence/findings/F201.md)). The corpus records the
  failure but no remedy seen to work, such as a separate worktree per session or a claim
  that refuses a second session a path already claimed. A comparison of either against
  shared-checkout incidents would settle it.
- **Merging planning files by entry.** roadkeep ships a merge driver that merges its
  planning files entry by entry rather than line by line. No finding records a planning
  file corrupted or conflicted by a text merge, so it admits no rule. A recorded merge
  that lost or duplicated an entry would settle it.
- **Generated files beyond the version bump.** CS-3 rests on one hook's failures. Whether
  other files every commit regenerates need the same reconciliation against the index is
  not recorded. A second project's failure of that kind would settle it.
- **Teams.** Every observation here is of one person running several sessions. Whether
  claims and path-scoped staging hold when several people, each with agents, share a
  repository and a remote is outside the evidence. A corpus project with a second human
  contributor would be needed.
