---
name: bootstrap
description: Start a new project Claude Code first, governed from its first commit. Asks the person for the day-one decisions, assembles the Claude Code First templates, wires the roadkeep guard and the planning files, sets the every-turn budgets, runs the conformance checker, and stops before the first commit. Use when asked to bootstrap a repository, start a new project Claude Code first, or set up governance in a new or empty repository.
---

# Bootstrap a new project

You perform the greenfield guide, `${CLAUDE_PLUGIN_ROOT}/adoption/greenfield.md`, in a new
or empty repository. You write files and run commands in it. You never commit and never
push: you stop before the first commit and show the person what you did.

## 1. Check the target

The target is the working directory unless the person names another. Run
`git -C <target> status --short` and `git -C <target> log --oneline -1`. If the target has
commits, or holds any of `agents.md`, `roadkeep.toml`, `ccf.toml`, `.claude/`,
`.gitignore`, `.gitattributes` or `.github/workflows/check.yml`, stop: it is not a new
project, and the brownfield guide in `${CLAUDE_PLUGIN_ROOT}/adoption/` applies. If it is
not a git repository, ask before running `git init`.

## 2. Ask for the day-one decisions

Ask these in one message, with the default in brackets, and wait for the answers. They are
the person's; do not choose them.

1. **Level**: 1, 2 or 3 [2]. This skill reaches level 2; level 3 needs gates the templates
   do not provide.
2. **Attribution**: do commits carry a trailer naming the agent? Either answer conforms
   (CD-6, divergence D1).
3. **Commit message**: the agent writes the title; does it write the body too, or does a
   tool generate the body? (CD-4, D5)
4. **Permission posture**: the templates commit no allow rules and ask before `git push`,
   `git reset --hard` and `rm -rf`. Broader, such as `Bash(*)` or `acceptEdits`? Any local
   bypass? (PS-1, D3)
5. **Language** of every artefact [English].
6. **Project name** and **task id prefix** (uppercase letters and digits), and a one-line
   description of what the project does.

## 3. Assemble the templates

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/assemble_templates.py" <target>
```

If it refuses over an existing file, stop and report it. Then copy
`${CLAUDE_PLUGIN_ROOT}/.claude/hooks/no-clobber.py` to `<target>/.claude/hooks/`.

## 4. Wire the guard and create the planning files

Run `roadkeep --version`. If roadkeep is available, in the target:

```sh
roadkeep install --committed
mv roadkeep.toml roadkeep.template.toml
roadkeep init --prefix <PREFIX> --block A
mv -f roadkeep.template.toml roadkeep.toml
roadkeep declare decisions
roadkeep declare deferred
```

`init` refuses where a configuration exists, so the template's configuration is set aside
while it writes the governed files, then restored because it carries the budgets and
limits. Never write a governed file (`docs/ROADMAP.md`, `docs/CHANGELOG.md`,
`docs/IMPROVEMENTS.md`, `docs/DECISIONS.md`, `docs/DEFERRED.md`) by hand.

If roadkeep is not available, do not imitate it. Tell the person that the guard wired in
`.claude/settings.json` has no launcher and the planning files do not exist, so PG-1 and
IS-1 cannot pass; that roadkeep is the reference planning tool, installed as the
`roadkeep` plugin or from its checkout; and that these commands are what to run once it
is. Continue with the steps that do not need it.

## 5. Replace the placeholders

Edit the files in place; the no-clobber hook refuses a `Write` over an existing file.

- `roadkeep.toml`: `prefix = "EX"` becomes the chosen prefix.
- `agents.md` and `.claude/CLAUDE.md`: `example` becomes the project name, the placeholder
  sentences become the description, and the laws are the person's or are removed. Keep
  `agents.md` an index (IS-2).
- Rename `.claude/skills/example-dev` and `example-writing` to `<name>-dev` and
  `<name>-writing`, with their `name:` lines and the pointers in `agents.md`.
- The dev skill: state the attribution choice and who writes the body. If the posture is
  broader than the template's, add the allow rules to `.claude/settings.json` and name in
  the dev skill the guards (roadkeep guard, no-clobber) and CI gates that stand in for the
  removed prompts (PS-1).
- The writing skill: the language, and any house style with the check that holds it.
- `ccf.toml`: the chosen `level`; `profile = true` only if the project ships tools, skills
  or a plugin for other agents.
- `.github/workflows/check.yml`: the `gates` job ends in a step that fails on purpose.
  If the build and test commands are known, put them there without pipes (VG-2); if not,
  leave it and say so. The lint job is the `roadkeep.yml` that `roadkeep install` wrote.

## 6. Lower the budgets

Measure `agents.md` and `.claude/CLAUDE.md` in lines and bytes, and set their entries in
`[budgets]` of `roadkeep.toml` just above that size. Then run `roadkeep lint` and fix what
it reports.

## 7. Run the checker

```sh
python "${CLAUDE_PLUGIN_ROOT}/scripts/check_conformance.py" <target>
```

Keep its verdicts as they are. Fix a failure the steps above should have prevented, and
report any other failure or `could not decide` as it stands; never turn it into a pass.

## 8. Stop and show the person

Do not stage or commit. Report:

- the decisions as recorded, and the file each landed in;
- the files written, from `git -C <target> status --short`;
- the budgets set, and the checker's verdict per rule;
- what is left to the person: the build and test commands if missing, the three level 2
  gates the templates omit (a test over `.claude/settings.json` for GH-5, a line-terminator
  gate for EP-2, named encodings for EP-3), and the first commit, staged by path, holding
  governance and no code;
- that the audit skill is the next check, once the first block has shipped.
