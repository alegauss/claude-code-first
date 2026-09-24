# Threats to validity

This document says where the study's conclusions stop. It follows the four threats that
Runeson and Höst use for case studies in software engineering: construct validity,
internal validity, external validity and reliability [1]. A rule in the specification
names the threat that bears on it most, so a reader can judge how far to trust that rule
without rereading this file.

## Construct validity

*Does the study measure what it claims to measure?*

**"Claude Code first" is defined by the repository, not by self-description.** A
repository is in scope when, from an identifiable adoption commit on, it carries an agent
instruction surface (`CLAUDE.md`, `agents.md` or `.claude/`) and its planning files are
written through agent-facing tooling. The adoption commits are listed in
[corpus.md](corpus.md).

**Authorship by an agent cannot be read from git metadata.** Almost every commit in the
corpus carries the owner's name. A `Co-Authored-By: Claude` trailer appears on some
commits in some periods and not in others (roadkeep had 76, winwright 33, per the
verification tables), so the trailer measures a habit, not authorship. That the agent
wrote the code rests on the owner's account and on the projects' own statements, such as
freewilly's skill on its own prose:
"Every word in this repository was written by a model" [freewilly@c1c2eaf:.claude/skills/ai-writing-freewilly/SKILL.md#L8].
A finding about "what
the agent did" is therefore about what was done in a repository run this way, and does
not separate the agent's contribution from the person's.

**A failure is known only if someone recorded it.** The sources are commits, ledgers and
configuration. A failure nobody wrote down leaves no trace, so the corpus
under-represents failures that were fixed silently or never noticed.

## Internal validity

*Could something other than the stated cause explain a finding?*

**The projects are not independent.** One person owns all five, and they share one
harness, one commit tool and roadkeep, which governs the planning files of all five and is
itself one of them. A practice seen in several projects may recur because it was copied,
not because each project rediscovered it. The grading scale counts recurrence by
independent origin for this reason ([grading.md](grading.md)).

**The direction of copying is traced from dates.** Shio adopted first, on 2026-03-24, and
roadkeep was built from measurements of it. Roadkeep's development guide states the
problem it solves as "In Viglet Shio: 92 roadmap lines averaging" [roadkeep@91754240:agents.md#L7].
From roadkeep, the hook launcher that `roadkeep install`
writes spread into Shio [shio@c215718bb], freewilly [freewilly@acc7fc1] and polyweave
[polyweave@c45f7b3], which makes it one origin in three repositories. The no-clobber hook
came into polyweave from pportal, a project outside the corpus. Its header names the
"repo, where this hook was written" [polyweave@6d1c136:.claude/hooks/no-clobber.py#L4].
A finding that cites a practice in
several projects states which copies it has ruled out.

**The researcher is a participant.** The person governing the study owns the five
projects and wrote roadkeep, whose rules seed many of the findings. The specification
could end up describing that person's preferences and calling them evidence. Two
safeguards are in place: every rule must cite graded findings, and the corpus projects are
audited against the finished specification (Block H), which tests whether it can find
fault with its own sources.

## External validity

*To whom do the conclusions apply?*

The corpus is narrow in ways a reader should keep in view:

- **One person.** No project has a second human contributor. Rules about review,
  handover or disagreement between people are outside the evidence.
- **One harness and one model family.** Every project was built with Claude Code and
  Claude models of 2026. A rule resting on a harness behaviour, such as plugins not
  loading on the web, may not hold in another harness or a later release.
- **One platform.** All five were developed on Windows. Findings about shells, encodings
  and line endings are Windows findings until seen elsewhere.
- **A short period.** Shio's agent history runs from 2026-03-24, and the four greenfield
  projects from 2026-07-29 to the pins on 2026-09-24. Nothing here says how the practice
  holds over years.
- **A range of sizes.** From 132 to 3,446 commits, and one brownfield project among five.
  Brownfield conclusions rest on a single case.

The non-goal "Claims beyond the corpus" binds the specification to this scope: it says
nothing about teams, other harnesses or other model families without evidence from them.

## Reliability

*Would another researcher reach the same findings?*

**The first extraction was done by agents, and it was measured.** Of the checkable claims
in the field notes, 13.8% were corrected or refuted when verified against the pins, from
12.9% to 16.3% per project ([field-notes/README.md](field-notes/README.md)). Findings
therefore cite the sources through checked pointers, never the notes.

**The verifier was the same model as the extractor.** The resolver checks every commit,
path, line range and quote mechanically. What it cannot check is paraphrase: whether a
claim marked verified restates its source faithfully. A hand recheck of six such claims
found no error, which is too small a sample to bound the verifier's error rate.

**The procedure is written down.** The protocol ([method.md](method.md)) and the exact
prompts ([instruments/](instruments/extraction-2026-09-24.md)) are recorded so the
extraction can be repeated. A repetition at the same pins by a different model or a
person is the strongest test of reliability, and it has not been done.

## References

1. P. Runeson and M. Höst. "Guidelines for conducting and reporting case study research
   in software engineering". *Empirical Software Engineering* 14(2):131-164, 2009.
   doi:10.1007/s10664-008-9102-8.
