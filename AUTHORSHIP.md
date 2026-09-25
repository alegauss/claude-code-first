# How this work was written

Most of the text, the evidence registers and the tooling in this repository were
written by Claude Code, under the direction and governance of its owner, who chose what
to build, set the backlog, and accepts the result. It is itself a Claude Code first
project, and it asks to be judged by the standard it sets for others.

## What the agent did, and what the person did

- **The agent** extracted the field notes, verified them against the pinned sources,
  wrote the case studies, the findings, the chapters and the scripts, and committed each
  task. Much of the extraction, verification and drafting ran as parallel subagents, each
  confined to its own files; their prompts are kept verbatim in
  [evidence/instruments/](evidence/instruments/extraction-2026-09-24.md).
- **The person** decided the scope, the corpus and the backlog, and makes the decisions
  this repository reserves for a person: the licenses, releases, pushes, and any
  interpretive disagreement about the evidence
  ([evidence/method.md](evidence/method.md), section 7).

## What guards the result

A reader need not trust the agent's reading. These checks run on every push:

- **Every pointer to a source resolves.** `scripts/resolve_citations.py` checks each
  pointer's commit, path, line range and quote against the pinned corpus.
- **Every rule traces to evidence that admits it.** `scripts/traceability.py` fails a rule
  whose keyword is stronger than its best finding allows, and a finding with no source.
- **The extraction's error rate was measured.** 13.8% of the checkable claims the first
  extraction wrote were corrected or refuted when verified
  ([evidence/field-notes/README.md](evidence/field-notes/README.md)); later work found
  three errors in the verification itself, and says so.
- **Where the conclusions stop is stated.** One author, one harness, one model family,
  five projects on one platform: [evidence/validity.md](evidence/validity.md).

What is not yet measured is the accuracy of the audit that judges other projects against
this specification. Until it is, a conformance verdict from the audit is a claim to check,
not a result.
