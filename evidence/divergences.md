# Divergences between the projects

Where the five projects do the same thing differently, the specification must take a
side or say why it cannot. A divergence left open becomes silence in the specification,
or a rule chosen by whoever edited it last. Each entry below names the practice, what each
project does at its pin, the findings that bear on it, and the decision. The decision
caps the keyword a rule on it may carry, following [grading.md](grading.md).

Where the evidence cannot decide, the decision says so and allows a **documented
deviation**: a project may choose either way if it records the choice and its reason
where the agent reads it. That is a decision too, and it is the honest one when the
corpus holds no failure on either side.

## D1 Attribution of agent-written commits

**What the projects do.** A `Co-Authored-By: Claude` trailer appears on some commits in
some periods: 76 roadkeep commits up to 2026-09-01 and none after, 33 in winwright, a
few in freewilly and Shio, none in polyweave. No project states a policy for it at its
pin. Commits the web harness makes are authored as "Claude"; the rest carry the owner's
name.

**Evidence.** [F205](findings/F205.md) (R2/S3): git metadata does not show which commits
an agent composed; the trailer is on a few percent of commits, unevenly. No finding
records a failure caused by the presence or absence of a trailer.

**Decision.** The specification does not use git attribution as evidence of authorship,
and it requires none. A project **SHOULD** state, where its agent reads its commit rules,
whether commits carry attribution, so the choice is deliberate rather than habitual.
Either choice is conforming.

## D2 The every-turn instruction file

**What the projects do.** roadkeep and Shio keep a short `CLAUDE.md` that imports
`agents.md`; polyweave keeps its rules in `CLAUDE.md`; freewilly and winwright have no
every-turn file in any commit and keep their rules in skills and in comments beside the
mechanisms they govern.

**Evidence.** [F1](findings/F1.md) (R3/S3): an every-turn file grows until a gate refuses
the next addition. [F2](findings/F2.md) (R3/S3): moving what only some turns need into
trigger-loaded files cut the every-turn cost by a measured amount. No finding records a
failure caused by having no every-turn file, and no source says why freewilly and
winwright chose none.

**Decision.** Having an every-turn file is not required: the evidence shows costs of the
file, not of its absence. Where a project has one, it **MUST** carry a size budget that
a gate enforces (F1, F2), and it **SHOULD** be an index that points to trigger-loaded
detail. A project without one is conforming and records that choice.

## D3 Permission posture

**What the projects do.** Shio and freewilly commit broad allow lists with `acceptEdits`;
polyweave allows `Bash(*)`; roadkeep and winwright commit no allow rules. Local settings
that bypass prompts are not committed anywhere, so they are outside every pin.

**Evidence.** [F402](findings/F402.md) (R3/S2): permission prompts were treated as a cost
to remove, and a hook that refuses named writes stood in for them.
[F301](findings/F301.md) (R3/S3): a guard hook refuses only the calls that reach it, and
its recorded gaps failed silently. No finding records harm done through a broad allow
list, and none records harm prevented by a prompt.

**Decision.** The evidence cannot decide how broad an allow list may safely be. A project
**MUST** name, in committed configuration or its commit rules, which hooks or gates stand
in for the prompts it has removed, because F301 shows a guard's gaps pass silently
otherwise. The breadth of the allow list itself is a documented deviation, and the
permissions chapter (CCF31) treats it as a claim to test, not to recommend.

## D4 What CI runs

**What the projects do.** roadkeep's CI runs its governed-docs lint, its full pytest
suite, "python -m pytest -q" [roadkeep@91754240:.github/workflows/gate.yml#L58], and a
plugin validation pinned to a CLI version. polyweave's CI runs the roadkeep lint and a
site build, but not pytest or ruff. winwright runs only the host half of its suite in CI,
the VMware guest half being impossible on a hosted runner. freewilly runs build, tests and
launch checks on a Windows runner. Shio runs its suites on pushes to two branches, on pull
requests and on demand.

**Evidence.** [F303](findings/F303.md) (R3/S3): a gate that did not run on every push let
red suites and drift reach the main branch unremarked. [F304](findings/F304.md) (R3/S3):
gates went red for reasons outside the change, and a red nobody could act on was
ignored.

**Decision.** A gate that decides whether work is done **MUST** run in CI on every push to
the branches work lands on (F303). A gate that cannot run there, such as a suite needing
hardware a hosted runner lacks, is a documented deviation that names the gate, the
reason, and where it does run. A red in CI that nobody can act on is itself a defect to
file, not a state to live with (F304).

## D5 Who writes the commit message

**What the projects do.** Where a project uses the owner's commit tool, as roadkeep and
Shio do by their own rules, the tool writes the body with another vendor's model from the
staged diff and the agent passes at most the title. Some commits, in Shio and in this
repository, are written whole by the agent that did the work. How much of each project's
history came from each path is not measured.

**Evidence.** [F204](findings/F204.md) (R2/S2): a message generated from the staged diff by
another model misdescribes the change, most visibly on documentation commits.

**Decision.** The agent that did the work **SHOULD** state the commit's intent (at least
its title) rather than leave it to a model that sees only the diff (F204). A generated
body is conforming.

## D6 How a commit is staged

**What the projects do.** The owner's commit tool stages everything. roadkeep answers a
claim with the `git add --` line for that task's paths; polyweave's rules name both
staging by path and the commit tool; this repository stages by path only. Shio's sessions
staged by path, against their own written rule, whenever another session had files in
the tree.

**Evidence.** [F200](findings/F200.md) (R2/S2): a tool that stages everything commits
whatever else the tree holds. [F201](findings/F201.md) (R2/S2): sessions sharing one
checkout commit each other's work unless each stages only its own paths.

**Decision.** A commit **SHOULD** stage its own paths by name. Staging everything is
conforming only where a single session owns the checkout and the tree was checked first.

## D7 The em dash and other house style

**What the projects do.** freewilly and Shio treat the em dash as a mark of generated
prose and rule it out; polyweave, winwright and roadkeep keep it on purpose.

**Evidence.** [F6](findings/F6.md) (R3/S4): the density was counted in two projects, and a
writing rule without a lint did not keep the dash out. [F300](findings/F300.md) (R3/S3): a
rule stated only in prose, with no check that reads it, was found broken by the project
that wrote it.

**Decision.** The specification takes no side on house style: which punctuation a project
allows is a documented choice. What it takes a side on is enforcement. A style rule a
project declares **SHOULD** be checked by a gate, since unchecked prose rules were found
broken (F300, F6).
