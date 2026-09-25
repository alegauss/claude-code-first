---
name: audit
description: Audit a repository against the Claude Code First specification at a claimed conformance level. Runs the deterministic checker, then one scanner per chapter and a verifier for the rules that need judgement, and writes a report. Use when asked to audit, check conformance, or measure drift against Claude Code First.
---

# Audit against Claude Code First

You produce a report. You do not change the audited repository, and you do not file
tasks into its backlog: that is a separate step the owner asks for, through the owner's
own planning tool.

The specification ships with this plugin at `${CLAUDE_PLUGIN_ROOT}`: the rules in
`spec/rules.toml`, the chapters in `spec/*.md`, the levels in `spec/conformance.md`.

## 1. Settle the target and the level

The target is the repository in the working directory unless the user names another.
The level is the one the user claims, 1 to 3; if none is given, audit at level 1 and say
so. Record the target's commit with `git -C <target> rev-parse HEAD` and the plugin's
version from `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`.

## 2. Run the checker first

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/check_conformance.py" <target> --level <N> --report <report.json>
```

Keep its verdicts as they are. Never re-examine a rule the checker decided, and never
turn its `could not decide` into a pass or a fail: carry it to the report.

## 3. Select the rules that need judgement

Read `${CLAUDE_PLUGIN_ROOT}/spec/rules.toml` and keep the rules whose `level` is at or
below the claimed level, plus `profile` if the target ships a surface for other agents,
and whose `detector` is empty. Group them by `chapter`. Load nothing else of the
specification into this session.

## 4. One scanner per chapter

Start the `scanner` agent once per chapter group, in parallel. Give each: the target
path, the chapter file `${CLAUDE_PLUGIN_ROOT}/spec/<CHAPTER>.md`, and the addresses of
its selected rules. Each returns findings as `rule | locus | observation | evidence`.

## 5. Verify

Start the `verifier` agent once with every scanner finding and the target path. It
classifies each as confirmed, false positive or unverifiable. Only confirmed findings
count against conformance.

## 6. Write the report

Add a verdict to `<report.json>` for every rule you selected, in the form of
`${CLAUDE_PLUGIN_ROOT}/spec/report.md`: a confirmed finding is `fail` with its locus and
evidence, a rule with no finding is `pass`, an unverifiable finding is `could not run`,
and `by` is `verifier`. Recompute `achieved_level` from the verdicts, then run
`python "${CLAUDE_PLUGIN_ROOT}/scripts/report.py" validate <report.json>` and `render`
it to Markdown. Save both where the user asks, or print the rendering.

State the limits in the report: a scanner reads a sample of the repository, and a
verifier that could not reproduce a finding says so rather than guessing.
