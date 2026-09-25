# VG Verification gates

## The problem

An agent calls work done on the evidence in front of it, and in the corpus that evidence
was often not a check. Tasks closed with no check the build runs covering the change as
committed, and the missing half came back as a new task or as a red for the next session,
in three projects ([F305](../evidence/findings/F305.md)); ledger entries recorded as shipped
were found not to hold ([F104](../evidence/findings/F104.md)). Where a gate did run, it
reported a pass over tests that never executed, over an exit status that was not the
suite's, or over the wrong object ([F302](../evidence/findings/F302.md)). Gates that ran
only when somebody chose to run them let red suites sit on the main branch for nineteen
commits ([F303](../evidence/findings/F303.md)), and gates that went red for reasons outside
the change stopped being read ([F304](../evidence/findings/F304.md)). This chapter states
what must run, what it must report, and when a red may be lived with. Figures and lists
typed into documentation are the subject of chapter AW, and a gate run in a checkout that
other sessions are writing is the subject of chapter CS.

### VG-1 Gates before done

**Work MUST NOT be called done until every *gate* that covers it has run and passed on the change as it will be committed, unless a *red-suite exception* covers the red.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | pending |
| Checked | by judgement |
| Findings | F305, F303, F104 |
| Harness facts | none |
| Threat | construct: a failure is known only if someone recorded it |
| Status | active |

Rationale: in Shio, winwright and freewilly a task was closed on a report that looked
right, a look by hand, or a run that came before the last edit, and the defect surfaced
later for whoever came next ([F305](../evidence/findings/F305.md), R3/S3). In winwright the
shipping step itself edited what the gate reads after the run that proved the work, so the
red landed on the next session twice in one session. Ledger entries written by the
shipping session recorded its own claim and were later found untrue
([F104](../evidence/findings/F104.md), R3/S3). A gate that the agent must remember to run
holds only in the sessions that remember it ([F303](../evidence/findings/F303.md)), so
running it is part of closing, and the run must be on the tree that will be committed.
The only red this rule lets through is one recorded as a *red-suite exception* (VG-7).

### VG-2 No gate through a pipe

**A *gate* MUST NOT be run, in any file that tells an agent how to run it, through a pipe or filter that can replace its exit status or discard its output.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | pending |
| Checked | automatically |
| Findings | F302, F300 |
| Harness facts | none |
| Threat | internal: the failure and its remedy are recorded in one project |
| Status | active |

Rationale: a shell pipeline reports its last command's status, so in Shio a failing test
run printed an exit status of 0, and an earlier pipe lost a failure that occurred in one
run of six, whose failing class is still unknown because the line "went into a pipe nobody kept" [shio@821f18d74:shio-app/src/test/java/com/viglet/shio/ShTestCommandDocLintTest.java#L33]
([F302](../evidence/findings/F302.md), R3/S3). Shio's remedy is a runner that keeps the
whole output and the suite's own exit code, and a lint over the files that document the
suite. The lint does not read the build skill, which at the pin still pipes the suite into
a filter ([F300](../evidence/findings/F300.md)), so the rule covers every file an agent
reads for the command: instruction files, skills, contributing guides and CI. A script can
decide conformance by reading those files.

### VG-3 Could not run is not a pass

**A *gate* MUST report a check that did not execute with the third *verdict*, could not run, and never count it as passed.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | by judgement |
| Findings | F302, F304 |
| Harness facts | none |
| Threat | construct: a green is the absence of a reported failure |
| Status | active |

Rationale: in winwright, Shio and freewilly a gate went green over work that had not run:
a dying test host, a stale build directory, a vacuous check, a capture of the wrong window
([F302](../evidence/findings/F302.md), R3/S3). Each project answered by making "did not
run" distinct from a pass or by waiting for the positive signal before judging. The same
separation answers a false red: Shio records a failed clean as inconclusive rather than
red ([F304](../evidence/findings/F304.md)). A check that can only say passed or failed
turns "did not run" into "passed". winwright's shipped skill states the rule for its own
product's checks: "A check that could not run is a third verdict and never a pass" [winwright@861b82e:skills/winwright/SKILL.md#L71].

### VG-4 A roll call of the tests

**A test *gate* SHOULD compare the tests its runner discovered with the tests that reported a result, and report any difference as could not run.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F302 |
| Harness facts | none |
| Threat | internal: the remedy was invented in one project and not recorded failing |
| Status | active |

Rationale: winwright measured a dying test host still printing a pass, "measured here at 352 of 374, a green covering twenty-two tests that" [winwright@861b82e:.github/workflows/ci.yml#L42]
never ran, and answered with a roll call of what discovery listed against what the results
file recorded ([F302](../evidence/findings/F302.md), R3/S3). The failure the finding grades
would admit a MUST, but the roll call is one project's remedy among several, and no source
records it catching a real run, so the rule carries SHOULD. It is the concrete form of
VG-3 for a test suite.

### VG-5 CI on every push

**A *gate* that decides whether work is done MUST run in CI on every push to the branches work lands on.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | automatically |
| Findings | F303, F304 |
| Harness facts | none |
| Threat | internal: two origins, one of them uncounted |
| Status | active |

Rationale: in Shio every workflow was dispatch-only, and two suites stayed red at the head
of the branch while "Eleven commits landed over the first and eight over the second, and no commit message" [shio@821f18d74:.github/workflows/suites.yml#L4]
mentioned either; freewilly deleted its lint workflow and drift reached main until it came
back ([F303](../evidence/findings/F303.md), R3/S3). Both restored the gate to every push.
This follows decision D4 in [../evidence/divergences.md](../evidence/divergences.md). A
gate that cannot run on a hosted runner, such as winwright's suite half that needs an
interactive desk ([F304](../evidence/findings/F304.md)), is a *documented deviation* that
names the gate, the reason, and where it does run. A script can decide conformance from
the workflow files' triggers and the gates they call.

### VG-6 A red about something else is a defect

**A *gate* that goes red for a cause outside the change MUST be filed as a defect of the gate and fixed, by narrowing what it concludes or where it runs, rather than rerun until it passes.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | pending |
| Checked | by judgement |
| Findings | F304 |
| Harness facts | none |
| Threat | internal: the three remedies differ, so the rule states the aim, not the mechanism |
| Status | active |

Rationale: in Shio, winwright and freewilly a gate went red for a concurrent run, a build
that never started, a runner without the needed desktop, or a non-deterministic figure
([F304](../evidence/findings/F304.md), R3/S3). winwright's CI was red for twenty-odd pushes
and never about the tree, and its workflow now runs only the half a hosted runner can
answer, because a permanently red badge is one nobody reads. Shio's runner allows one run
per gate and records a failed setup as inconclusive; freewilly made its figures
deterministic. None of them told the agent to rerun. A red that means nothing costs a
diagnosis every time and then hides the true red beside it, which is why D4 calls it a
defect to file, not a state to live with.

### VG-7 An expiring exception for a known red

**A *gate* that is to stay red while other work continues SHOULD be covered by a *red-suite exception* that a check turns red once it expires.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F303, F304 |
| Harness facts | none |
| Threat | internal: the exception ledger is one project's remedy |
| Status | active |

Rationale: the red suites that nobody mentioned for nineteen commits in Shio were red with
no record that anyone knew ([F303](../evidence/findings/F303.md), R3/S3). Shio's answer,
with SH579, is a ledger of dated exceptions whose test works "so a forgotten exception goes red instead of quiet" [shio@821f18d74:red-suites.json#L2].
A red that nobody can act on is ignored ([F304](../evidence/findings/F304.md)), and an
exception tied to the task that will fix it gives the red an owner and an end. The problem
is graded R3/S3, but the ledger is one project's remedy and no source records it firing,
so the rule carries SHOULD.

### VG-8 A closing check

**A task that changes behaviour MUST NOT be recorded as shipped until a check that a *gate* runs covers that behaviour as committed.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | pending |
| Checked | by judgement |
| Findings | F305, F104 |
| Harness facts | none |
| Threat | construct: Shio's own reading ties the failures to its commit rate |
| Status | active |

Rationale: six corrections in Shio shipped half of themselves, three of them shipping the
report and leaving the behaviour; in freewilly DD75 shipped, "so the new behaviour was verified by hand and by nothing the build runs" [freewilly@c1c2eaf:docs/CHANGELOG.md#L22];
each project answered by making a check part of closing
([F305](../evidence/findings/F305.md), R3/S3). The ledger records the shipping session's
own claim, so without a check nothing tells a true entry from an untrue one
([F104](../evidence/findings/F104.md), R3/S3). Shio's form of the remedy, SH527, closes a
defect with an assertion carrying its id so the unasserted ones can be computed; whether
that form catches what it is built for is an open question below. Where the check cannot
run on the machine, because it needs hardware or a person's judgement, the task is not
closed by the agent: that is the subject of chapter HR.

### VG-9 Measure before building

**A change made to improve a measurable quantity SHOULD be preceded by a measurement of that quantity, and kept only if a second measurement shows the gain.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | pending |
| Checked | by judgement |
| Findings | F103, F102 |
| Harness facts | none |
| Threat | internal: designs also survived measurement, and no rate is known |
| Status | active |

Rationale: in three projects a design or diagnosis written before implementation was
overturned once it was built or measured ([F103](../evidence/findings/F103.md), R3/S3).
winwright built, measured and reverted WW249: "take the per-code-unit send back out, the rate did not move" [winwright@5012473],
and retired two filed tasks whose premise did not survive a measurement taken before
building ([F102](../evidence/findings/F102.md)). F103 also records a design that
measurement confirmed, so the evidence shows that measuring settles the question, not that
designs usually fail; the rule carries SHOULD for that reason.

## Open questions

- **Does an assertion carrying the defect's id catch an unasserted close?** Shio's SH527
  computes the defects closed without such an assertion, but its first run misread its own
  declaration as the evidence ([F302](../evidence/findings/F302.md)), and no source records
  it catching a real close. VG-8 therefore requires a covering check, not this form of it.
  A record of the debt test failing on a real unasserted close, in Shio or elsewhere, would
  settle it.
- **Is a gate result written into the commit message worth requiring?** polyweave records
  "Gates:" lines on 18 of 132 commits and runs its code gates only locally
  ([F303](../evidence/findings/F303.md)); no failure is recorded either way, so the practice
  has no observed outcome. A project that compares self-reported gate lines with CI runs of
  the same commits would settle it.
- **Does a gate that runs only on the author's machine, with no incident, conform?**
  polyweave and winwright's desk half both do so without a recorded red landing, and
  neither has an audit that would find one ([F303](../evidence/findings/F303.md)). VG-5
  treats this as a *documented deviation*. An audit of such a project's history against a
  later CI run would show whether reds landed unremarked.
