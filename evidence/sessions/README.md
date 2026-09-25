# Session cost per task

One JSON file per corpus project, each holding what the Claude Code sessions that built
that project cost per backlog task, as far as the local transcripts still reach. The
files are aggregates: task ids, commit hashes and token counts. No prompt, commit subject
or path inside a project is in them, which is what lets them be committed where the
transcripts they come from could not be.

## How they were produced

By `tools/task-cost.mjs` in the claude-code-usage repository at commit `069d1e7`, which
charges every request a session made in a project's directory to the first commit that
landed after it in that repository, and sums per task id. A commit that names two ids
gives each half; a filing range stays one key and is never judged as a task. The
transcripts were read on 2026-09-25, against Claude Code 2.1.282, on the machine that
wrote this, with `--until
2026-09-24`, the date of the pins in [../corpus.md](../corpus.md):

```sh
node tools/task-cost.mjs --repo <roadkeep>  --name roadkeep  --prefix RK,RG --until 2026-09-24 --json roadkeep.json
node tools/task-cost.mjs --repo <polyweave> --name polyweave --until 2026-09-24 --json polyweave.json
node tools/task-cost.mjs --repo <freewilly> --name freewilly --until 2026-09-24 --json freewilly.json
node tools/task-cost.mjs --repo <winwright> --name winwright --until 2026-09-24 --json winwright.json
node tools/task-cost.mjs --repo <shio>      --name shio      --until 2026-09-24 --json shio.json \
  --project '^(D--Git-viglet-shio|D--Git-viglet-shio-latest|D--Git-viglet-shio-2026-3(-.*)?)$'
```

Each file names the tool's commit, the repository's head when it was read, the date range
the transcripts covered, and the attribution rule, so a reader can see what the figures
are without this page.

## What they can and cannot say

- **Cost is priced at list rates**, per million tokens by model, with cache writes and
  reads weighted as the API bills them. Under a subscription nobody paid these sums; the
  figures compare tasks with each other, not with an invoice.
- **The window is thirty days at most.** Claude Code deletes a transcript after the
  `cleanupPeriodDays` retention, thirty days by default (H18), so each series starts
  where the oldest surviving transcript does, which the file's `range.first` records.
  Shio's starts later than the others: its earlier sessions ran from a directory whose
  transcripts no longer exist.
- **The transcript format is internal** and changes between versions (H17); the usage
  fields the tool reads are observed, not documented (O4).
- **The attribution is approximate.** Two sessions working in one checkout at once both
  charge the next commit, and exploration that led to no commit is charged to whatever
  commit came next; each commit's `gapHours` shows how far back its charge reaches. Spend
  on commits that name no task is kept in the totals and reported as
  `summary.costOnIdsPct`, which is low where a project's commit tool wrote subjects
  without an id.
- **No one else can rerun it.** The transcripts are on one machine and expire. The
  aggregate is pinned by this repository's history, its source is not, so an observation
  resting on it grades at S3 at best and carries that threat
  ([../method.md](../method.md), section 3).
