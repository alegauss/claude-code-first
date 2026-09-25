---
name: realign
description: Realign a project that has drifted from the Claude Code First specification, starting from an audit report. Classifies each failure with the person as drift, divergence or obsolescence, drafts one task per drifted rule, files tasks or writes waivers only when the owner asks, and re-audits after each level. Use when asked to realign a drifted project, bring a project back to conformance, act on an audit, or turn audit failures into tasks.
---

# Realign a project against Claude Code First

You turn an audit report into work the owner can decide on. The owner decides what is
filed, what is waived and what code changes. You propose; you never file a task, write a
waiver, change code or push on your own initiative. The guide this skill follows is
`${CLAUDE_PLUGIN_ROOT}/adoption/realignment.md`; the rules are in
`${CLAUDE_PLUGIN_ROOT}/spec/rules.toml` and the chapters in `${CLAUDE_PLUGIN_ROOT}/spec/`.

## 1. Get a report

Use the audit report the person gives you (the JSON, not only its rendering). With none,
run the `audit` skill first, at the level in the target's `ccf.toml` or the level the
person names, and keep its JSON as the baseline. Check it with
`python "${CLAUDE_PLUGIN_ROOT}/scripts/report.py" validate <report.json>`.

Before classifying, set two kinds of verdict apart:

- `could not run`: it blocks the level until resolved. Say what the check needed.
- `fail` on an expired waiver: the owner renews it or files the work it waited for.

## 2. Classify each failure with the person

For every `fail`, read the rule's statement in its chapter and the report's locus and
evidence, then propose one class with the reason:

| Class | Test | Outcome |
|---|---|---|
| drift | the project's own files already state the rule, or it meant to conform | one task per rule |
| divergence | a deliberate choice the owner would make again | a waiver in `ccf.toml` |
| obsolescence | the case the rule rests on has changed, such as a harness release | a report upstream, and a waiver meanwhile |

Drift is the default for a failure the project's own instructions forbid. Divergence and
obsolescence are the person's call: ask, and record their answer, never your guess. A
departure the specification already allows, such as having no every-turn file (decision
D2), needs no waiver; say so.

## 3. Draft the tasks

Draft, do not file, one task per drifted rule: several loci failing one rule are one
task. For each draft give:

- a line stating the symptom the audit saw, not the design (PG-2), naming something wrong
  (CD-5);
- a rationale holding the rule's address and a link to its chapter, the locus and the
  evidence from the report, and the check that will hold the fix (GH-1);
- the rule's level.

Order the drafts by level, lowest first. Show them to the person with the level each
belongs to, and say which recipe in the guide applies (splitting an every-turn file,
moving a procedure into a skill, pinning line endings). A missing committed launcher is
an open question in the specification, not drift: draft nothing for it.

## 4. File only on the owner's request

File a task only when the owner asks for it in this session, and only the tasks they
name. File through the target's own planning tool, never by editing its planning files.
With roadkeep, run it from the target:

```sh
roadkeep add "<symptom>" --section "<title>" --section-body-file <path>
roadkeep lint
```

File the lowest failing level only; leave the levels above as drafts until it is reached,
since its fixes change what they find. If the target has no planning tool, give the
drafts as text and stop.

## 5. Waivers only with approval

Write a waiver into the target's `ccf.toml` only when the owner approves its wording. It
needs `rule`, `reason`, `owner`, `date`, and `expires` or `task`
(`${CLAUDE_PLUGIN_ROOT}/spec/deviations.md`); the checker refuses one without them. For
obsolescence, the reason cites the upstream report. Show the entry before writing it.

## 6. Report obsolescence upstream

For each failure the person classed as obsolete, draft a report for the specification's
maintainers: the rule's address, the project and commit, what changed, and the
measurement or source that shows it. Hand it to the person to send.

## 7. Re-audit after each level

When the owner says the tasks of a level are done, run the `audit` skill again at that
level, then compare:

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/report.py" diff <older.json> <newer.json>
```

Say whether `achieved_level` rose, which rules changed verdict, and any that went from
`pass` to `fail`, which is new drift for step 2. Save the report and its rendering where
the owner says, such as `docs/audits/<date>-<commit>.json`, and commit them only if the
owner asks. Then offer the next level's drafts.

## Limits

You do not change the target's code, gates or configuration to make a rule pass, even
when the fix is small; that is a task for the owner to file and work. You never push. A
scanner reads a sample, so a clean re-audit bounds what it examined, not the repository.
