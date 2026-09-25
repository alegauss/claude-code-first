# Harness facts

Some rules in the specification depend on how Claude Code behaves, not on anything the
corpus shows about practice. This register lists each such behaviour with the official
page that states it, so that when a release changes one, the rules that name it can be
found and revisited. The specification cites these facts; it does not restate the manual,
as the non-goal "A manual of Claude Code features" requires.

**Read on:** 2026-09-24, against Claude Code 2.1.280 (`claude --version` on the machine
that wrote this register). A fact is re-read, with a new date and version, whenever a
rule that depends on it is written or changed.

Each fact has an identifier (**H1**, **H2**, …). A rule that depends on one names it.

## Documented behaviour

Every quotation below is copied from the page named, as retrieved on the date above.

| Id | Behaviour | Source | What the page says |
|---|---|---|---|
| H1 | A `CLAUDE.md` file can pull in other files with `@path` imports | [memory](https://code.claude.com/docs/en/memory.md) | "CLAUDE.md files can import additional files using `@path/to/import` syntax." |
| H2 | `CLAUDE.md` is read from several locations, each with its own scope, and loads every session | [memory](https://code.claude.com/docs/en/memory.md) | "CLAUDE.md files can live in several locations, each with a different scope." |
| H3 | A skill's body loads only when the skill is used; until then only its name and description cost context | [skills](https://code.claude.com/docs/en/skills.md) | "Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it." |
| H4 | Hooks run on lifecycle events such as `SessionStart`, `PreToolUse` and `Stop`, matched by tool name | [hooks guide](https://code.claude.com/docs/en/hooks-guide.md#what-you-can-automate) | "Claude Code fires hook events at specific points in its lifecycle." |
| H5 | A hook's exit code is its verdict: 0 raises no objection, 2 blocks the action and sends stderr as the reason | [hooks guide](https://code.claude.com/docs/en/hooks-guide.md#read-input-and-return-output) | "Exit 2: Claude Code blocks the action. Write a reason to stderr." |
| H6 | A `PreToolUse` hook can deny a call with JSON carrying `permissionDecision: "deny"` and a reason | [hooks guide](https://code.claude.com/docs/en/hooks-guide.md#structured-json-output) | shown in the page's example output |
| H7 | Settings are layered: managed, command line, local project, shared project, user, from highest to lowest | [settings](https://code.claude.com/docs/en/settings.md) | shown as the page's precedence diagram |
| H8 | Project MCP servers are declared in a committed `.mcp.json` | [MCP](https://code.claude.com/docs/en/mcp.md) | "Project-scoped servers are configured with the `--scope project` flag and stored in `.mcp.json`" |
| H9 | MCP tool definitions are not all sent up front when tool search is on, which is the default | [MCP](https://code.claude.com/docs/en/mcp.md) | "With tool search enabled (the default), Claude Code uses efficient matching rather than sending all tool definitions to Claude" |
| H10 | In a cloud session, a plugin loads when it is enabled for the claude.ai account as a synced plugin | [discover plugins](https://code.claude.com/docs/en/discover-plugins.md) | "Cloud sessions: enable the plugin for your claude.ai account so Claude Code loads it as a synced plugin." |
| H11 | A cloud session reads settings committed in the repository's `.claude/settings.json` | [on the web](https://code.claude.com/docs/en/claude-code-on-the-web.md) | "commit the key to that repository's `.claude/settings.json`" |
| H12 | `/loop` runs a prompt repeatedly while the session stays open | [scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks.md) | "The `/loop` bundled skill is the quickest way to run a prompt on repeat while the session stays open." |
| H13 | `claude plugin validate` checks a plugin before it is published | [plugins](https://code.claude.com/docs/en/plugins.md) | "Run `claude plugin validate ./your-plugin` locally before you submit" |
| H15 | `${CLAUDE_PLUGIN_ROOT}` written in a plugin's skill or agent body is replaced with the plugin's installed path when the content loads, though it is not in the environment of Bash commands | [plugins reference](https://code.claude.com/docs/en/plugins-reference.md#where-each-variable-resolves) | "In skill, command, and agent content, write the `${...}` reference in the Markdown body instead, and Claude Code substitutes the path inline when it loads the content." |
| H14 | `${CLAUDE_PROJECT_DIR}` in a hook command resolves to the project root | [hooks reference](https://code.claude.com/docs/en/hooks.md) | "`${CLAUDE_PROJECT_DIR}` is a path placeholder that resolves to the project root where the session started." |

H1 to H14 were located by a documentation-lookup agent. H5 and H10 were then re-read by
hand from the pages and match word for word. The others are quoted as that agent
returned them.

## Observed behaviour

Behaviour the corpus recorded that no documentation page states, or that the
documentation now contradicts. Each is an observation with its evidence, graded like any
other ([grading.md](grading.md)), and it is not a documented fact.

**O1. The harness rewrote `.claude/settings.json` during a session.** In freewilly,
fifteen permission entries disappeared mid-session and were swept into an unrelated
commit by a stage-everything commit tool:
"The harness rewrote .claude/settings.json mid-session" [freewilly@ac7e7ec].
The same message calls it the second time in that session. No page documents a session
removing entries from a committed settings file, so a rule resting on this cites the
incident and names the version it was seen on, which the commit does not record.

**O2. Invalid YAML frontmatter made the loader drop a skill's metadata silently.**
"invalid YAML frontmatter caused the loader to drop essential metadata" [roadkeep@f79ca3b4].
The failure left no message, which is why roadkeep then pinned the validator its CI runs:
"CLAUDE_VERSION:" [roadkeep@91754240:.github/workflows/gate.yml#L71] is set to 2.1.220
(RK335).

**O3. Plugins did not load in Claude Code on the web.** On 2026-08-08 a Claude session on
the web committed a self-locating launcher to Shio so that the guard would load there
[shio@c215718bb]. Four days later roadkeep generalised it into `install --committed`,
"which do not support plugin installations" [roadkeep@7243dc05],
and its ledger records the origin: a project "hand-writes the launcher that finds one" [roadkeep@91754240:docs/CHANGELOG.md#L1067].
From roadkeep the launcher reached freewilly and polyweave. **H10 now contradicts this**:
the documentation read on 2026-09-24 says a plugin enabled for the claude.ai account loads
in cloud sessions as a synced plugin. The practice may have outlived its cause, or synced
plugins may not cover a plugin installed from a marketplace. Any rule about committed
launchers names both O3 and H10, and must be re-checked in a cloud session before it is
written.
