# Instrument: extraction prompts of 2026-09-24

The five prompts that produced the field notes in [../field-notes/](../field-notes/README.md),
recorded verbatim from the session that ran them. They are the first instrument of the
[research protocol](../method.md).

## How they were run

- **Session.** One orchestrating Claude Code session (`4e8d498c-62e1-4aeb-bf47-225ce2764829`)
  started five subagents in parallel, one per case, between 20:59:46 and 21:00:12 UTC.
- **Agent.** The built-in `Explore` subagent type, read-only, run in the background with no
  person in the loop.
- **Model.** `claude-opus-5-5` for all five.
- **Output.** Each returned one Markdown report, edited into a field-notes file by the
  orchestrating session. The raw reports are not kept in this repository.

## Limits

- **Read-only, single pass.** Each case was read once, by one agent, with no second
  extractor to compare against. Nothing it reported was checked against the source before
  it was written down (CCF11 does that).
- **One model.** Every extraction came from the same model, so any systematic error of
  that model is shared by all five and cannot show up as a disagreement between them.
- **Prompts that carried expectations.** Each prompt gives the extractor the
  orchestrator's prior beliefs: commit counts, what a directory is thought to contain, and
  in the Shio prompt the suggestion that stray log files "may be an anti-pattern". A leading
  prompt makes confirming observations easier to find than disconfirming ones.
- **Unequal prompts.** The five differ in the files they name and in the word budget
  (about 2,000 or 2,500 words), so a difference between two field notes may come from the
  prompt rather than the project.
- **No pinned commit.** The prompts name repositories, not commits. The commits the
  extractors read were whatever each checkout held that evening, and they have to be
  recovered from the dates before the notes can be verified (CCF8).

## The prompts

### roadkeep

Subagent `agent-a7b4194ef8a011df5`, started 2026-09-24T20:59:46.798Z, 31 assistant turns.

```text
Research task (very thorough, read-only). Repo: D:/git/alegauss/roadkeep (1946 commits). This repo is one of five projects developed "Claude Code first" (Claude Code is the primary developer; the human governs). I am building a formal, evidence-based SPECIFICATION of Claude-Code-first practices. I need facts with citations, not opinions.

Extract, with file paths (and line numbers where useful) and commit hashes as evidence:
1. Agent instruction surface: CLAUDE.md / .claude/CLAUDE.md / agents.md — structure, size, what sections exist, what rules they encode. Quote the most important rules verbatim (short).
2. .claude/ contents: settings.json (permissions, hooks), skills (names, purpose, structure: SKILL.md + auxiliary files), agents, hooks scripts, .mcp.json, .claude-plugin, commands/, hooks/, skills/ at root (plugin distribution).
3. Governance of planning docs: docs/ROADMAP.md, CHANGELOG.md, IMPROVEMENTS.md, DECISIONS.md — format conventions, how tasks are written (symptom/why/deps), ship flow, and roadkeep.toml settings.
4. Quality gates: tests, lint, CI (.github/workflows), pre-commit (.githooks, .pre-commit-hooks.yaml), any "guard" hooks that deny hand edits.
5. Commit conventions (look at `git log --oneline -60` and a few bodies): one task per commit? conventional commits? attribution?
6. MOST IMPORTANT: learnings, mistakes and reversals. Search DECISIONS.md, CHANGELOG, commit messages (git log --grep for revert, reverse, wrong, mistake, regress, undo, supersede, drift, token, cost, context), and anything describing what did NOT work for an AI agent (e.g. context cost, token budgets, hand-edit drift, hooks denying edits). Summarize each learning as: claim → evidence (path/commit) → consequence.
7. Metrics you can cheaply get: commit count, date range (first/last commit date), size of CLAUDE.md in lines/words, number of skills, test count if obvious.

Output a structured report (markdown) of up to ~2500 words, sections 1-7, every claim followed by its evidence pointer. Flag anything that is inference rather than documented fact as "(inference)".
```

### polyweave

Subagent `agent-a34300d806dd4eab6`, started 2026-09-24T20:59:52.409Z, 33 assistant turns.

```text
Research task (very thorough, read-only). Repo: D:/git/alegauss/polyweave (132 commits). This repo is one of five projects developed "Claude Code first" (Claude Code is the primary developer; the human governs). I am building a formal, evidence-based SPECIFICATION of Claude-Code-first practices. I need facts with citations, not opinions.

Extract, with file paths (line numbers where useful) and commit hashes as evidence:
1. Agent instruction surface: CLAUDE.md — structure, size, sections, the rules it encodes. Quote the most important rules verbatim (short).
2. .claude/ contents: settings.json (permissions, hooks), agents (scanner.md, verifier.md — how they are used; there's an audit skill that pairs with them), hooks (no-clobber.py, roadkeep-launch.py — what they do), skills (audit, roadkeep with asking.md/writing.md), .mcp.json, .polyweave/ directory.
3. docs/: ROADMAP, CHANGELOG, IMPROVEMENTS, DEFERRED.md, docs/specs/ — format conventions and how specs are structured. roadkeep.toml settings.
4. Quality gates: tests, lint, CI (.github/workflows).
5. Commit conventions (git log --oneline -60 and a few bodies).
6. MOST IMPORTANT: learnings, mistakes and reversals. Search DEFERRED.md, CHANGELOG, specs, commit messages (git log --grep for revert, wrong, mistake, regress, undo, supersede, drift, clobber, token, cost, context, audit) and anything describing what did NOT work for an AI agent. Summarize each learning as: claim → evidence (path/commit) → consequence.
7. Metrics: commit count, first/last commit date, CLAUDE.md size in lines, number of skills/agents/hooks.

Output a structured markdown report up to ~2000 words, sections 1-7, every claim with an evidence pointer. Flag inference as "(inference)".
```

### freewilly

Subagent `agent-aeb7ec65a271386ec`, started 2026-09-24T20:59:58.254Z, 47 assistant turns.

```text
Research task (very thorough, read-only). Repo: D:/git/alegauss/freewilly (444 commits, .NET). This repo is one of five projects developed "Claude Code first" (Claude Code is the primary developer; the human governs). I am building a formal, evidence-based SPECIFICATION of Claude-Code-first practices. I need facts with citations, not opinions.

Extract, with file paths (line numbers where useful) and commit hashes as evidence:
1. Agent instruction surface: is there a CLAUDE.md anywhere (root, .claude/, src/)? CONTRIBUTING.md — structure, rules. Quote key rules verbatim (short).
2. .claude/ contents: settings.json (permissions, hooks; note there are .bak files — why?), hooks/roadkeep-launch.py, skills (ai-writing-freewilly, freewilly-roadmap-docs, roadkeep, window-chrome — purpose and structure), .mcp.json, agent-budget.json (what is it? a token/context budget?), winwright.json, install-roadkeep.cmd, run-cases.cmd.
3. docs/: ROADMAP, CHANGELOG, IMPROVEMENTS, docs/specs/, docs/_preview — conventions. roadkeep.toml settings.
4. Quality gates: tests, CI (.github/workflows), how UI/desktop is verified by an agent (winwright?).
5. Commit conventions (git log --oneline -60, a few bodies).
6. MOST IMPORTANT: learnings, mistakes and reversals. Search commit messages (git log --grep for revert, wrong, mistake, regress, undo, supersede, drift, budget, token, cost, context, flaky), CHANGELOG, specs, and anything describing what did NOT work for an AI agent. Each learning as: claim → evidence (path/commit) → consequence.
7. Metrics: commit count, first/last commit date, instruction file sizes, number of skills/hooks.

Output a structured markdown report up to ~2000 words, sections 1-7, every claim with an evidence pointer. Flag inference as "(inference)".
```

### winwright

Subagent `agent-a0dea2e7296f88ee1`, started 2026-09-24T21:00:04.223Z, 30 assistant turns.

```text
Research task (very thorough, read-only). Repo: D:/git/alegauss/winwright (708 commits, .NET; appears to be a tool for agents to drive Windows desktop UI, distributed as a Claude plugin). This repo is one of five projects developed "Claude Code first" (Claude Code is the primary developer; the human governs). I am building a formal, evidence-based SPECIFICATION of Claude-Code-first practices. I need facts with citations, not opinions.

Extract, with file paths (line numbers where useful) and commit hashes as evidence:
1. Agent instruction surface: any CLAUDE.md / agents.md? README sections aimed at agents. Quote key rules verbatim (short).
2. .claude/ contents: settings.json, skills (roadkeep, roadmap-docs), plus the plugin distribution: .claude-plugin/, hooks/, skills/ at root, .mcp.json — how a project ships an agent-facing surface (MCP server, skills) to OTHER projects.
3. docs/: ROADMAP, CHANGELOG, IMPROVEMENTS conventions; roadkeep.toml settings.
4. Quality gates: tests, CI, the many .cmd scripts (run-tests-vm, run-typing, capture-adoption, capture-walkthrough) — how an agent verifies desktop behavior; VM isolation.
5. Commit conventions (git log --oneline -60, a few bodies).
6. MOST IMPORTANT: learnings, mistakes and reversals. Search commit messages (git log --grep for revert, wrong, mistake, regress, undo, supersede, drift, token, cost, context, flaky, adoption), CHANGELOG, and anything describing what did NOT work for an AI agent (e.g. agent ergonomics of MCP tools, output size, tool descriptions). Each learning as: claim → evidence (path/commit) → consequence.
7. Metrics: commit count, first/last commit date, instruction file sizes, number of skills/hooks/MCP tools.

Output a structured markdown report up to ~2000 words, sections 1-7, every claim with an evidence pointer. Flag inference as "(inference)".
```

### shio

Subagent `agent-ad70b06864a13e63d`, started 2026-09-24T21:00:12.119Z, 38 assistant turns.

```text
Research task (very thorough, read-only). Repo: D:/git/viglet/shio/latest (3446 commits; Java/Spring + JS/React monorepo, a CMS). This is the largest of five projects developed "Claude Code first" (Claude Code is the primary developer; the human governs). I am building a formal, evidence-based SPECIFICATION of Claude-Code-first practices. I need facts with citations, not opinions. Note: this is an existing (brownfield) project that adopted Claude Code first — that transition is especially interesting.

Extract, with file paths (line numbers where useful) and commit hashes as evidence:
1. Agent instruction surface: CLAUDE.md and agents.md — structure, size, sections, rules; how they relate (duplication? pointer?). Quote key rules verbatim (short).
2. .claude/: settings.json (permissions, hooks), hooks/roadkeep-launch.py, the ~12 domain skills (shio-build-test, shio-database, shio-renderer, shio-console-ui, ...): how are skills partitioned (by domain/layer?), their typical size/structure. Also claude-plugin/, .claude-plugin/, .mcp.json, docs/agents/.
3. docs/: ROADMAP, CHANGELOG (note there's also a root CHANGELOG.md), IMPROVEMENTS, docs/specs, docs/design, docs/recipes — conventions. roadkeep.toml settings. .gates/ directory — what it is.
4. Quality gates: .gates/, tests, CI (.github/workflows), conformance checks. Note the root is littered with ~90 *.log files (sh951.log, shio-test.red.log, ...) — what produces them, are they gitignored? This may be an anti-pattern (agent output pollution) worth documenting.
5. Commit conventions (git log --oneline -60, a few bodies). Task id prefix (SH?).
6. MOST IMPORTANT: learnings, mistakes and reversals. Search commit messages (git log --grep for revert, wrong, mistake, regress, undo, supersede, drift, token, cost, context, flaky, red, gate), CHANGELOG, specs/design docs, and anything describing what did NOT work for an AI agent. Each learning as: claim → evidence (path/commit) → consequence.
7. Metrics: commit count, first/last commit date, date when Claude Code adoption started (first commit touching CLAUDE.md or .claude/), instruction file sizes, number of skills.

Output a structured markdown report up to ~2500 words, sections 1-7, every claim with an evidence pointer. Flag inference as "(inference)".
```
