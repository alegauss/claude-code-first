# Field notes (verified)

These five files are the first extraction pass over the corpus, made on 2026-09-24 by
read-only research agents, one per project. They are **leads, not evidence**: every claim
in them must be checked against the pinned source before it is cited by a finding or a
rule (see the backlog task that verifies them). Paths are relative to each project's root.
The prompts that produced them, and their limits, are in
[../instruments/extraction-2026-09-24.md](../instruments/extraction-2026-09-24.md); the
protocol they are held to is [../method.md](../method.md), and the commit each project is
pinned to is in [../corpus.md](../corpus.md).

| Project | Root | Notes |
|---|---|---|
| roadkeep | `D:/git/alegauss/roadkeep` | [roadkeep.md](roadkeep.md) |
| polyweave | `D:/git/alegauss/polyweave` | [polyweave.md](polyweave.md) |
| freewilly | `D:/git/alegauss/freewilly` | [freewilly.md](freewilly.md) |
| winwright | `D:/git/alegauss/winwright` | [winwright.md](winwright.md) |
| shio | `D:/git/viglet/shio/latest` (worktree 2026.3) | [shio.md](shio.md) |

Markers used below: **(inference)** is the extracting agent's own conclusion, not a
documented fact. Numbers were read on the extraction date and move with each project.

## Verification

Each note keeps its extracted text unchanged, as the audit trail, and ends with a
**Verification** table that checks it claim by claim against the project's pinned
commit. Every claim gets one status:

| Status | Meaning |
|---|---|
| verified | the pinned source says what the claim says |
| corrected | the source supports a different or narrower claim, given in the Correction column |
| refuted | the source contradicts the claim, or nothing in it supports the claim |
| outside the pin | the claim rests on work that was not committed at the pin, so it cannot be checked there |
| inference | the extractor's own interpretation; it is kept, and never cited as fact |

The Evidence column uses the pointer grammar of [../method.md](../method.md), so
`scripts/resolve_citations.py` checks every pointer and quote in it. A count is verified
by recounting at the pin, and the Evidence column gives the command. The **error rate** of
a note is corrected plus refuted, divided by verified plus corrected plus refuted.
Findings cite the sources through these pointers, never the notes.

### Result of the first verification

Checked on 2026-09-24 with the instrument in
[../instruments/verification-2026-09-24.md](../instruments/verification-2026-09-24.md).
All 789 pointers written into the tables resolve.

| Note | Claims | Verified | Corrected | Refuted | Outside the pin | Inference | Error rate |
|---|---|---|---|---|---|---|---|
| roadkeep | 134 | 111 | 17 | 0 | 4 | 2 | 13.3% |
| polyweave | 100 | 81 | 11 | 1 | 5 | 2 | 12.9% |
| freewilly | 106 | 85 | 13 | 0 | 3 | 5 | 13.3% |
| winwright | 93 | 77 | 14 | 1 | 0 | 1 | 16.3% |
| Shio | 131 | 108 | 17 | 0 | 2 | 4 | 13.6% |
| **All** | **564** | **462** | **72** | **2** | **14** | **14** | **13.8%** |

About one checkable claim in seven that the extraction agents wrote was wrong in some
detail. Most errors are small counts off by one or a few, line numbers moved, or a
commit credited with a neighbour's change. A few changed a claim's meaning: winwright's
"no Claude co-author trailer" (33 commits carry one), polyweave's learning 5 (the cited
commit says the design was right), and freewilly's learning 1 (the cited commit does not
exist). Two claims were refuted outright.

The verifier was the same model as the extractor. As a check on the verifier, six claims
it marked verified were rechecked by hand at the pins (Shio table rows 40 and 90, roadkeep
row 30, and the polyweave commit and ledger counts and winwright's trailer count), and all
six held. That sample is too small to bound the verifier's own error rate, which is left
to the audit-accuracy work.
