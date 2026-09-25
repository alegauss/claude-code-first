# GH Guards and hooks

## The problem

A rule that lives only in an instruction file is read by the session that loads it and by
nothing else. In the corpus such rules were found broken by the repositories that wrote
them ([F300](../evidence/findings/F300.md)), and budgets stated in prose did not hold
([F1](../evidence/findings/F1.md), [F5](../evidence/findings/F5.md)). The projects moved
those rules into hooks and gates. Hooks brought their own failure: a guard refuses only
the calls that reach it, in sessions where it loaded and could run, and every recorded gap
let work through with nothing saying the guard was not guarding
([F301](../evidence/findings/F301.md)). The configuration that wires guards was itself
lost without an error ([F306](../evidence/findings/F306.md),
[F401](../evidence/findings/F401.md)), and where several copies of a shared tool could
answer, sessions ran a stale one ([F403](../evidence/findings/F403.md)). This chapter
states when a rule leaves prose, and what keeps a guard honest about its own reach. What
an agent may do without asking is the subject of chapter PS.

### GH-1 A broken rule leaves prose

**A rule that the project has seen broken MUST be enforced by a *guard* or a *gate* that reads what the rule governs, not left in prose alone.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F300, F1, F5, F6 |
| Harness facts | none |
| Threat | internal: the researcher wrote the tool that moved several of these rules |
| Status | active |

Rationale: in Shio and freewilly a rule stated only in prose was measured broken, each
time by the repository that stated it: Shio's roadmap lines ran to 142 words under a
one-sentence rule, and freewilly's writing skill forbade the em dash while the pinned
commit added two to the README ([F300](../evidence/findings/F300.md), R3/S3). A budget on
the every-turn file stated in prose did not stop it growing about nineteenfold, while a
gated one held ([F1](../evidence/findings/F1.md)); planning prose outran an instruction to
be brief until a limit was refused at write time ([F5](../evidence/findings/F5.md)); a
writing rule without a lint did not keep the em dash out ([F6](../evidence/findings/F6.md)).
Shio's index states the principle: "A rule nobody can check is a preference, so" [shio@821f18d74:agents.md#L229].
The rule is conditioned on a breach seen, because no project records an agent breaking the
rules its guards were written against before they were written (see the open questions).
A check that reads a typed copy of the rule rather than the governed text reproduces the
fault ([F7](../evidence/findings/F7.md)), so the check reads what the rule governs.

### GH-2 A gate behind every guard

**Every rule a *guard* enforces MUST also be checked by a *gate* that runs in CI.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F301, F303 |
| Harness facts | H4, H6 |
| Threat | external: one harness and one release window |
| Status | active |

Rationale: a `PreToolUse` guard answers only for the tools it is matched on, in sessions
where it is installed and able to run (H4, H6), and in four projects a gap in it (a tool
not matched, a session where it did not load, a clone where it was not built) let work
through silently ([F301](../evidence/findings/F301.md), R3/S3). The backstop two projects
name is a gate elsewhere: roadkeep's guard says "the gate is the backstop for the barrier" [roadkeep@91754240:src/roadkeep/guarding.py#L31],
and when freewilly deleted its lint workflow the hooks were the only guard and drift
reached main by other routes until the lint came back ([F303](../evidence/findings/F303.md)).
A gate in CI sees the result whatever route produced it, and whether or not the session
had its guard.

### GH-3 Match every route to the change

**A *guard* SHOULD be matched on every tool through which the agent can make the change it refuses, the shell included.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 2 |
| Checked | by judgement |
| Findings | F100, F301 |
| Harness facts | H4, H6 |
| Threat | internal: the gap and its fix are one tool's, seen from its adopters |
| Status | active |

Rationale: roadkeep's guard first matched only `Edit` and `Write`, and a shell command
writing the same file got silence until the guard also matched `Bash`
([F100](../evidence/findings/F100.md), R1/S2; [F301](../evidence/findings/F301.md)). A
shell command names a path without saying what it does with it, so the guard can only ask
there, and asking on every command that names a governed path also asked on `git add`,
which the tool then exempted. That cost is why the rule carries SHOULD and leaves the
answer on the shell (ask, or refuse a recognised write) to the project. The finding is one
tool's history, R1 at S2 with no contrary observation, which admits SHOULD.

### GH-4 A guard that cannot run says so

**A *guard* that is wired but cannot run, such as one whose build or engine is missing, MUST say in the session that it is not guarding.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F301, F403 |
| Harness facts | H5 |
| Threat | construct: a silent gap is known only once someone noticed it |
| Status | active |

Rationale: the guards in the corpus allow on any failure of their own, so an absent,
unmatched or broken guard looks exactly like one that approved
([F301](../evidence/findings/F301.md), R3/S3). winwright's guard, on a fresh clone with no
build, exited 1 and never 2 (H5), and a "guard that is not there refuses nothing" [winwright@861b82e:README.md#L113]; its fix
kept the hook non-blocking and made it name the missing build. roadkeep's launcher stood
down on a stale registry row and both guards were absent at once, and freewilly's hooks ran
a sibling engine because a variable arrived unexpanded
([F403](../evidence/findings/F403.md)). The rule does not require the guard to block: a
message costs nothing and turns the silent gap the findings record into one the session
can see. A guard that never loaded cannot speak for itself; GH-2 covers that case.

### GH-5 The agent configuration under a gate

**The committed agent configuration, including the wiring of every *guard*, MUST be checked by a *gate* that fails when an entry is lost.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F306, F401 |
| Harness facts | H7, H11, H13 |
| Threat | external: the component that rewrote the settings is not established |
| Status | active |

Rationale: in roadkeep, freewilly and Shio a part of the agent's configuration stopped
working with no error: a skill's frontmatter the loader dropped, committed settings that
lost their allow entries, a published plugin the producing repository never loaded
([F306](../evidence/findings/F306.md), R3/S3). In freewilly the settings lost fifteen
entries twice in one session, and the second loss reached a commit about something else
([F401](../evidence/findings/F401.md), R2/S2; harness observation O1). Each project
answered with a check in its suite or CI: freewilly's DD115 tests fail when a declared
floor of granted tools or the guard's wiring on any hook event is lost, roadkeep runs
`claude plugin validate --strict` at a pinned version (H13), and Shio tests its published
skills against its project skills. Settings are layered (H7) and a cloud session reads the
committed file (H11), so the committed file is the one to hold.

### GH-6 A stale copy fails a gate

**Where a session can reach more than one copy of a tool or skill that a *guard* or a *gate* depends on, a *gate* SHOULD fail when the copy that answers is stale against its source or is not the intended one.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 3 |
| Checked | by judgement |
| Findings | F403 |
| Harness facts | none |
| Threat | internal: no failing check is recorded as having held |
| Status | active |

Rationale: in winwright, freewilly and roadkeep's adopters a session ran or read a copy of
a shared engine or skill that was stale or not the intended one, and nothing failed
([F403](../evidence/findings/F403.md), R3/S3). winwright's vendored skill drifted twice;
the second time the session-start notice reported it and the agent wrote "I read past it every time" [winwright@a18dd8d],
at a counted cost of five refusal round-trips. A notice is therefore shown not to be
enough, which points at a check that fails. The finding would admit a MUST, but the one
failing check recorded, freewilly's DD118, was deleted with its workflow and did not come
back, so no source shows such a gate holding; the rule carries SHOULD until one does.

## Open questions

- **Does a refusal that names the command to use instead change what the agent does
  next?** roadkeep's guard was built to name the command, but no source records how often a
  guard denied or asked, or what the agent did after ([F100](../evidence/findings/F100.md)).
  A count of refusals and of the call that followed each, from session transcripts, would
  settle it.
- **Should a guard be written before any breach is seen?** No project records an agent
  hand-editing a governed file; the premise that it will is stated in roadkeep's rationale
  and was checked by the tool's author, not observed in a session
  ([F100](../evidence/findings/F100.md)). The polyweave no-clobber hook answers an incident
  in pportal, outside the corpus. A recorded breach in a project without the guard would
  settle it; until then GH-1 applies only after a breach.
- **Should a guard fail open?** Every guard in the corpus allows on its own failure, but
  the reason is the projects' stated reasoning (S1): no source records a guard failing
  closed and blocking work ([F301](../evidence/findings/F301.md)). An observed closed
  failure, or a count of guard errors in sessions, would settle it. GH-4 holds either way.
- **Should a guard never answer allow?** roadkeep's guard treats silence as the allow and
  never grants anything, so it cannot override the user's permissions
  ([F402](../evidence/findings/F402.md)). That is a design statement with no incident of a
  hook's allow granting what the user had not. An incident, in or outside the corpus, would
  settle it; chapter PS takes up permissions.
- **Must guards be carried by a launcher committed to the repository?** In August 2026 a
  guard shipped in a plugin did not load in a web session, and Shio committed a launcher so
  that it would ([F400](../evidence/findings/F400.md), R1/S2); the launcher was copied into
  three more projects. The documentation read on 2026-09-24 contradicts the premise: a
  plugin enabled for the claude.ai account loads in cloud sessions as a synced plugin (H10;
  harness observation O3). A cloud session on a current release, with the plugin synced
  and without the launcher, that shows whether the guard loads, including for a plugin
  installed from a project marketplace, would settle it.
