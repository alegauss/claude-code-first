# Instrument: field-note verification of 2026-09-24

The prompt that verified the five field notes claim by claim (CCF11), recorded so the
verification can be repeated and its limits read. It is the second instrument of the
[research protocol](../method.md), and it checks the output of the
[first](extraction-2026-09-24.md).

## How it was run

- **Session.** One orchestrating Claude Code session started five subagents in parallel,
  one per note, each allowed to edit only its own note.
- **Agent.** The built-in `general-purpose` subagent type, run in the background with no
  person in the loop.
- **Model.** `claude-opus-5-5`, inherited from the orchestrating session: the same model
  that did the extraction.
- **Mechanical check.** Every pointer the agents wrote was then checked by
  `scripts/resolve_citations.py`: commit, path, line range and quote. What the resolver
  cannot check is whether a verified claim was restated faithfully, or whether a claim
  was left out of the table.

## Limits

- **Same model as the extraction.** A misreading shared by extractor and verifier
  would pass. The resolver removes that risk for quotes, paths and lines, but not for
  paraphrase.
- **The verifier split the claims.** How a dense sentence is cut into atomic claims
  changes the denominator of the error rate. The tables show the cut, so a reader can
  recount.
- **Uncommitted work is unverifiable.** Claims about trees that were not committed at the
  pin are marked *outside the pin* and are not counted in the error rate.

## The prompt

The five prompts differ only in the project, its local path, its pinned commit, the
example pointer and count, and one sentence on that project's uncommitted or untracked
files. The roadkeep prompt, verbatim:

```text
You are verifying one file of preliminary research notes against its primary source, claim by claim. Precision matters more than speed: this becomes cited evidence in an academic specification, and a wrong "verified" is the worst outcome.

**Your file:** `D:/Git/alegauss/claude-code-first/evidence/field-notes/roadkeep.md`
**Project:** `roadkeep`, local repository `D:/Git/alegauss/roadkeep`
**Pinned commit:** `91754240f79a2c151eb6700f1ac4b9e5a41de04b` (short `91754240`). Every check is made AT THIS COMMIT, never at the working tree or a later HEAD: use `git -C D:/Git/alegauss/roadkeep show 91754240:<path>`, `git -C ... log 91754240 ...`, `git -C ... rev-list --count 91754240`, `git -C ... grep -n <text> 91754240 -- <path>`, and so on. The checkout may have moved on; ignore its working tree. Do not modify that repository in any way.

Read first: `D:/Git/alegauss/claude-code-first/evidence/field-notes/README.md` (the status legend, section "Verification") and the "Evidence pointers" paragraph in `D:/Git/alegauss/claude-code-first/evidence/method.md`.

**What to do**
1. Split the note into atomic claims (a quote, a line number, a file size, a count, a commit hash and what it did, a rule, a date). Dense sentences hold several claims; check each.
2. Check each claim at the pin. Quotes must match verbatim (whitespace aside). Line numbers must point at the quoted text. Commit hashes must exist in the history of the pin (`git merge-base --is-ancestor <c> 91754240`) and do what the note says. Counts must be recounted.
3. Leave the existing note text UNCHANGED. Append at the end of the file a section:

## Verification

Checked against `91754240` on 2026-09-24. <N> claims: <v> verified, <c> corrected, <r> refuted, <o> outside the pin, <i> inference. Error rate <(c+r)/(v+c+r) as a percentage, one decimal>.

| # | Section | Claim | Status | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | 1 | ... short restatement of the claim ... | verified | "exact quote" [roadkeep@91754240:agents.md#L12] | |

   - Status is exactly one of: verified, corrected, refuted, outside the pin, inference (meanings in the README).
   - Evidence uses the pointer grammar: `[roadkeep@<commit>]`, `[roadkeep@<commit>:<path>]`, `[roadkeep@<commit>:<path>#L<n>]` or `#L<n>-L<m>`. Use the pinned commit for file pointers; use the specific commit's own hash for claims about a commit. Put a quote `"..."` directly before a pointer only when the claim quotes the source; the quote must occur, whitespace aside, within those lines (or in the commit message for a bare commit pointer). Avoid `|` and `"` inside quotes (pick a quote span that has neither). For counts, write the command in inline code instead of or in addition to a pointer, e.g. `git rev-list --count 91754240` = 1946.
   - Claims about the uncommitted `gui/` tree (it was staged, not committed, at the pin) are "outside the pin".
   - "(inference)" claims: status inference, unless you find a source that states it, then verified with that source.
   - Correction column: the corrected claim, stated precisely, with its own pointer.
4. Change the title line `# roadkeep: field notes (preliminary, unverified)` to `# roadkeep: field notes (verified)`. Nothing else in the existing text changes.
5. Validate: from `D:/Git/alegauss/claude-code-first`, run `python scripts/resolve_citations.py --source shio=D:/Git/viglet/shio/latest --source winwright=D:/Git/alegauss/winwright` and make every pointer in YOUR file resolve (other files may be in progress by parallel workers; ignore their lines). Also run `npx --yes markdownlint-cli2 evidence/field-notes/roadkeep.md`. Both must be clean for your file.

Constraints: edit only your one file (use the Edit tool; Write over an existing file is refused by a hook). Do not commit, stage or touch git state in either repository. Write in English, plain and exact.

Return: the counts line, the error rate, and a list of every corrected and refuted claim with a one-line reason each.
```

In the prompt as sent, the section template in step 3 was itself inside a fenced block;
it is unfenced here so this file's own fence stays whole.
