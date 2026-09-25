# The pinned corpus

Every citation in this repository into a corpus project is read at the commit pinned
here. A source project keeps committing, and a line number with no commit behind it
cannot be found again within a week. The protocol that uses these pins is
[method.md](method.md).

**Re-pinning** moves a project to a later commit. It is a deliberate act, done as its own
backlog task with its own changelog entry, and every citation into that project is
re-checked against the new commit in the same task. A citation never names a commit other
than its project's pin without saying so.

## Pins

| Project | Remote | Branch read | Pinned commit | Commit date |
|---|---|---|---|---|
| roadkeep | `github.com/alegauss/roadkeep` | `main` | `91754240f79a2c151eb6700f1ac4b9e5a41de04b` | 2026-09-24 17:23 −03:00 |
| polyweave | `github.com/alegauss/polyweave` | `main` | `6d1c1363270a0fe40c5a08e009ee9b5bac5c68e9` | 2026-09-24 17:47 −03:00 |
| freewilly | `github.com/alegauss/freewilly` | `main` | `c1c2eaf4694a03df85f8a8eeb83a7de03886b056` | 2026-09-17 18:09 −03:00 |
| winwright | `github.com/alegauss/winwright` | `main` | `861b82e2cb7d0864cf2dc41799f04f4de3ec0e6e` | 2026-09-21 21:42 −03:00 |
| Shio | `github.com/ShioCMS/shio` | `2026.3` (worktree) | `821f18d74e9760cdd6e50b66f21138dfec15a033` | 2026-09-24 17:52 −03:00 |

These are the commits the first extraction read
([instruments/extraction-2026-09-24.md](instruments/extraction-2026-09-24.md)), which ran
from 17:59 to 18:04 −03:00 on 2026-09-24. Each was confirmed as the checkout's HEAD in that
window: it is dated before the window opened, and the next commit on its branch is dated
after it closed (roadkeep `5c8529a8` at 18:22, polyweave `347ab20` at 18:04:33, Shio
`92b882459` at 18:16; freewilly and winwright had no later commit).

## Work outside the pins at extraction

Two checkouts held uncommitted work that the extractors could read and a later reader of
the pinned commit cannot. An observation drawn from it is not evidence until it is found
in a commit, which then needs a re-pin or a citation that names that commit explicitly.

- **roadkeep**: a staged merge of `gui/` (RK1697, 564 files), nothing of it yet in
  history. It was committed as `5c8529a8` at 18:22, after the extraction.
- **polyweave**: uncommitted changes for PW106, PW135 and PW141 and a sixth non-goal.
  PW106 was committed as `347ab20` at 18:04:33, at the end of the extraction.

This list comes from the field notes, which recorded the state of each tree when it was
read. The other three notes record no uncommitted work, which is not proof there was none.

## Descriptive data

Counted at the pinned commit. *Adoption* is the first commit that touches `CLAUDE.md`,
`agents.md`, `AGENTS.md` or `.claude/`. *Active days* are distinct committer dates. The
commit and active-day counts below match the generated [metrics](metrics/README.md), which
hold further figures computed the same way for all five projects.

| Project | Language | What it is | First commit | Adoption | Commits | Active days | Kind |
|---|---|---|---|---|---|---|---|
| roadkeep | Python | a CLI and Claude Code plugin that owns the writes to a project's planning files | 2026-07-29 | `00a59e0e`, 2026-07-29 | 1,946 | 45 | greenfield |
| polyweave | Python | a Claude Code plugin for making 3D assets on Blender, Godot and a generative mesh service | 2026-09-22 | `26bd699`, 2026-09-22 | 132 | 3 | greenfield |
| freewilly | C# (.NET, WPF) | a free Docker desktop for Windows | 2026-08-12 | `acc7fc1`, 2026-08-12 | 444 | 21 | greenfield |
| winwright | C# (.NET) | a library and Claude Code plugin that drives a Windows desktop application from a test | 2026-08-21 | `fd4162f`, 2026-08-21 | 708 | 23 | greenfield |
| Shio | Java (Spring), JavaScript (React) | a content management system | 2019-07-30 | `6bf11b754`, 2026-03-24 | 3,446 | 515 | brownfield |

Greenfield means adoption came within the first hour of the project's history. Shio had
1,778 commits before its adoption commit and 1,668 from it to the pin, over 83 active
days.

## How the figures were produced

With `<c>` the pinned commit and `<a>` the adoption commit, from each checkout:

```sh
git log -1 --format='%H %cI' <c>                        # the pin and its date
git log --reverse --ancestry-path --format='%h %cI' <c>..HEAD | head -1   # the next commit
git rev-list --count <c>                                # commits
git log --reverse --format='%h %cI' <c> | head -1       # first commit
git log --format=%cd --date=short <c> | sort -u | wc -l # active days
git log --reverse --format='%h %cI' <c> -- CLAUDE.md .claude agents.md AGENTS.md | head -1
git rev-list --count <a>^                               # commits before adoption
```
