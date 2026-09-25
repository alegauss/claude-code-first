---
name: adopt
description: Adopt Claude Code First in an existing codebase, following the brownfield adoption guide. Inventories the instructions, skills, settings, backlog, ledgers and gates already there and reports before writing anything, proposes a level and waivers for the person to decide, merges the templates by hand without overwriting any file, and runs the conformance checker. Use when asked to adopt Claude Code First, the specification or its templates in a repository that already has history, for brownfield adoption, or to bring an existing project under Claude Code First.
---

# Adopt Claude Code First in an existing repository

You carry out `${CLAUDE_PLUGIN_ROOT}/adoption/brownfield.md` in the repository the user
names, else the working directory. Read that guide first; the rules it cites are in
`${CLAUDE_PLUGIN_ROOT}/spec/`, the levels in `spec/conformance.md` and the waiver format
in `spec/deviations.md`.

Four limits hold throughout:

- **Nothing is overwritten.** An existing file is changed only by a merge the person has
  approved for that file.
- **The person decides** the level, each waiver, and every change to an existing file.
- **You never push**, and you commit only when the person asks, one task per commit,
  staged by path.
- **You invent no history.** A figure you report comes from a command you ran.

## 1. Inventory, and write nothing

Record `git -C <target> rev-parse HEAD`, `git rev-list --count HEAD` and the first
commit's date. Then list, with bytes and lines for each file:

- every-turn files: every `CLAUDE.md`, `.claude/CLAUDE.md`, `agents.md` or `AGENTS.md`,
  and what each imports;
- skills and commands under `.claude/`, and anything under `.claude-plugin/`, as two
  separate lists;
- `.claude/settings.json` and `.mcp.json`: allow, deny and ask rules, and each hook with
  its matcher;
- planning and history files (roadmaps, changelogs, design documents), each with
  `git log -1 --format=%cs -- <path>`;
- test and lint commands, and each workflow under `.github/workflows/` with its `on:`
  triggers;
- the commit tool, whether it stages everything, and `git status --short`.

If roadkeep is available, measure the backlog without writing: `roadkeep adopt <roadmap>`,
`roadkeep adopt --ledger <changelog>` and `roadkeep adopt --sections <rationale>`.

## 2. Report and propose

Show the person the inventory, then propose:

- **a level**, 1 or 2, with the rules of that level the inventory shows unmet;
- **waivers** for what the history cannot meet, each with rule, reason, owner, date, and
  `expires` or `task`;
- **legacy limits** for old ledger or roadmap entries that exceed a limit, stated for that
  file only, with the measurement behind each;
- **legacy files** to keep in place and mark as superseded;
- **each existing file** the templates would touch, and what the merge would add.

Stop here until the person answers. Record what they decide and apply only that.

## 3. Assemble the templates into a scratch folder

`assemble_templates.py` refuses to overwrite an existing file, so never run it on the
target. Assemble into an empty folder outside the target:

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/assemble_templates.py" <scratch>
```

Copy a file into the target only where the target has none. For each file the target
already has, show the person the merge you propose (the entries to add and the lines to
change) and apply it only on their approval for that file. Never pass `--force`. Replace
`example`, `EX` and the placeholder text with the project's names.

## 4. Carry out the guide's steps

In the guide's order, each only as far as the person approved:

1. Index and budget: move detail out of the every-turn file into skills or area files,
   keeping its content, and set budgets in `roadkeep.toml` just above the sizes reached.
2. Backlog: `roadkeep init --existing`, then limits from the measurement, with legacy
   limits and their reasons beside them. Declare the deferred store.
3. Legacy files: add the approved mark saying which file replaced each.
4. Guards: `roadkeep install --committed`, merging hook entries into existing settings
   by hand. Write the commit rules, the attribution choice included.
5. Gates: the project's existing test and lint commands in CI on every push, without
   pipes; a known red becomes an expiring exception, not a disabled suite. Record the
   baseline figures in the adoption commit body.
6. If the repository publishes skills, keep its project skills apart from them and load
   the published plugin in its own settings.

Run `roadkeep lint` after each step that touches a governed file.

## 5. Declare and check

Write `ccf.toml` with the chosen level, `spec_version`, `profile`, and the approved
waivers. Then run:

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/check_conformance.py" <target>
```

Report its verdicts as they are. A failure is fixed if the person approved the fix, or
proposed as a waiver; never turn `could not decide` into a pass. The checker decides six
rules. Say that the rest need the audit skill, best run after the first governed tasks
ship.

## 6. Hand over

End with: the files created, the files merged with the person's approval, the level
claimed, the waivers, the checker's verdicts, and what is left for the person. Leave the
changes uncommitted unless the person asked for commits, and do not push.
