# EP Environment portability

## The problem

All five projects ran on Windows, and in each of them text crossing a shell heredoc, a
PowerShell pipe, a locale code page or a tree of mixed line endings changed bytes with no
error, to be found later by a parser, a reader or a count
([F404](../evidence/findings/F404.md)). When text came out corrupted, the first diagnosis
blamed the component that showed the damage, and was withdrawn within hours
([F405](../evidence/findings/F405.md)). Where several copies of a shared tool could answer,
sessions ran a stale or unintended copy and nothing failed
([F403](../evidence/findings/F403.md)). A committed settings file lost entries during a
session and the loss rode into an unrelated commit ([F401](../evidence/findings/F401.md)).
And a guard shipped in a plugin did not reach web sessions, so it was carried by a
launcher committed to the repository ([F400](../evidence/findings/F400.md)), a premise the
harness documentation now contradicts (H10). Every rule below rests on Windows
observations, and none has been seen to hold or fail on another platform
([../evidence/validity.md](../evidence/validity.md), external validity).

### EP-1 One declared copy answers

**Where more than one copy of a shared tool could answer a session, the project MUST declare in committed files which copy answers and at which version.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F403 |
| Harness facts | none |
| Threat | internal: roadkeep is the shared tool in most observations |
| Status | active |

Rationale: sessions in at least three projects ran or read a copy that was stale or not
the intended one, a vendored skill behind its engine, a sibling checkout chosen because an
environment variable arrived unexpanded, a stale plugin registry row, and nothing failed
([F403](../evidence/findings/F403.md), R3/S3). Shio and freewilly vendored the engine to
one path because "which copy answers is not decidable by looking" [shio@821f18d74:agents.md#L277].
A declaration in committed files is what makes the question decidable by reading. It is
not enough alone: Shio's two descriptions of its copy disagree at the pin, which is why
GH-6 asks for a check. The platform facts involved (how an environment variable in a hook
command is expanded on Windows) come from the finding, not from the harness register.

Failing a gate when the copy that answers is stale is rule GH-6 in [GH.md](GH.md).

### EP-2 Line terminators are declared and held

**A repository's line terminators MUST be declared in a committed `.gitattributes` file and held by a *gate* that fails on a file that departs from them.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F404 |
| Harness facts | none |
| Threat | external: one platform, Windows |
| Status | active |

Rationale: roadkeep counted 45 modules ending CRLF and 11 ending LF, so that an edit
anchored on one terminator matched nothing, and answered with a committed `.gitattributes` and a test
that holds one terminator against a mixed file; Shio's line-ending task with a test
reduced the files with incorrect endings from 308 to 11, after a CRLF file had hidden
seven pages from an extractor; winwright normalised endings so real warnings were not
buried ([F404](../evidence/findings/F404.md), R4/S3). The declaration without a test is
what the earlier states lacked: Shio's scripted edit flipped a file to CRLF with nothing
to catch it. This is a Windows finding, where CRLF is the platform's default and tools
disagree about it; on another platform the risk may be smaller, and the corpus cannot say.

### EP-3 A named encoding at a process boundary

**A program in the project that reads text from another process MUST decode it with a named encoding rather than the locale's default.**

| Field | Value |
|---|---|
| Keyword | MUST |
| Level | 2 |
| Checked | by judgement |
| Findings | F404, F405 |
| Harness facts | none |
| Threat | external: one platform, Windows |
| Status | active |

Rationale: on the corpus's machines the locale code page was cp1252. In Shio the agent's
own patching called `subprocess.run(text=True)`, which decoded with it and corrupted
posted content; in polyweave a correct cp1252 byte was read by a pipe that decoded UTF-8;
in freewilly two streams sharing one buffer were decoded as one
([F404](../evidence/findings/F404.md), R4/S3; [F405](../evidence/findings/F405.md)). In
each the writing process saw nothing wrong, and the fix was an explicit encoding, set once
where the stream is opened. The rule depends on a platform fact, that a default decode
follows the locale, which the findings record for Windows only.

### EP-4 A leading byte-order mark is expected

**A tool that reads text piped to it on Windows SHOULD strip or refuse a leading byte-order mark rather than keep it as content.**

| Field | Value |
|---|---|
| Keyword | SHOULD |
| Level | 2 |
| Checked | by judgement |
| Findings | F404 |
| Harness facts | none |
| Threat | external: one platform, Windows PowerShell 5.1 |
| Status | active |

Rationale: Windows PowerShell 5.1 prepends a byte-order mark to text it pipes to a native
command. In roadkeep it broke a stdin path, fixed in RK1023, and on another occasion a mark
reached a governed file through a body file with the lint clean
([F404](../evidence/findings/F404.md)). polyweave's no-clobber hook strips the mark too,
but it was written in another repository and does not count as a second origin. The
support is one project on two occasions, so the keyword is SHOULD. The fact that the mark
is added is a property of PowerShell 5.1, not of Claude Code, and is not in the harness
register; a later PowerShell, or another shell, may not add it.

### EP-5 Encoding is judged on bytes

**An encoding defect MUST NOT be filed or fixed until its bytes have been checked at each boundary the text crossed, the agent's own tools included.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | 2 |
| Checked | by judgement |
| Findings | F405, F404 |
| Harness facts | none |
| Threat | construct: both cases were caught within hours, so the cost recorded is small |
| Status | active |

Rationale: in polyweave and in Shio, a month apart, the first diagnosis of corrupted text
blamed the component that displayed it, and relocating the fault reversed a fix already
shipped in one case and retired a filed defect in the other
([F405](../evidence/findings/F405.md), R3/S2). What moved each diagnosis was checking the
bytes at every hop; Shio's first reading had measured bytes along the product's path and
still missed the agent's own tool in it. Shio wrote the rule down as "judge encoding on bytes with od -c rather than on what a terminal prints" [shio@c17ed995a],
because "A filed defect that does not exist costs whoever picks it up more than the bug would have" [shio@c17ed995a].
A terminal renders both good and damaged bytes through its own decode, which on the
corpus's Windows machines was the locale's ([F404](../evidence/findings/F404.md)).

### EP-6 No source edited through a heredoc

**An agent SHOULD NOT write or edit source files through a shell heredoc.**

| Field | Value |
|---|---|
| Keyword | SHOULD NOT |
| Level | 2 |
| Checked | by judgement |
| Findings | F404 |
| Harness facts | none |
| Threat | external: one platform, Windows shells |
| Status | active |

Rationale: in roadkeep "three heredoc edits corrupted a test file's string literals and only the parser noticed" [roadkeep@91754240:docs/CHANGELOG.md#L655],
and the project's rule became never to edit source that way
([F404](../evidence/findings/F404.md)). A heredoc passes source through the shell's quoting
and newline handling, which the writer does not see. The finding is R4 for text crossing a
boundary in general, but the heredoc is one project's observation, so this rule carries
SHOULD NOT. The harness's own file-editing tools write the bytes given to them, which is
the alternative the rule points to.

Holding the committed settings and the wiring of every guard under a gate is rule GH-5
in [GH.md](GH.md); it is not repeated here.

## Open questions

- **Committed launchers for web sessions.** The corpus carries its guard into web sessions
  through a launcher committed under `.claude/hooks/`, because a web session did not
  install marketplace plugins ([F400](../evidence/findings/F400.md), R1/S2; harness
  observation O3). The documentation read on 2026-09-24 says a plugin enabled for the
  claude.ai account loads in a cloud session as a synced plugin (H10). The finding is one
  origin, and its own grade requires the premise to be re-checked in a cloud session
  before a rule is drawn from it. A cloud session on a current release, with the plugin
  installed from its marketplace and enabled for the account, that records whether its
  hooks run would settle whether nothing the practice relies on may live only in a
  user-level install.
- **Other platforms.** Every finding in this chapter was observed on Windows. Whether line
  endings, locale decoding and byte-order marks cause the same silent damage on Linux or
  macOS, and so whether EP-2 to EP-6 apply there with the same keywords, needs a project
  run this way on another platform.
- **Pinning the harness itself.** roadkeep pins the Claude Code version its CI validator
  runs, after a loader dropped a skill's metadata with no message (harness observation O2).
  Whether the version of the harness a session runs should be pinned or recorded is not
  settled by any finding; it would need a recorded change of behaviour between releases
  that a pin would have caught.
