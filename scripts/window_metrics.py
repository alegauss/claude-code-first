"""Measure one project over a window of days ending at a commit, for before and after (CCF57).

corpus_metrics.py counts a project's whole history to its pin; a realignment is judged by
comparing two windows of the same length, one ending where the audit read the project and
one ending a comparable period after the realignment shipped. This script measures one
window, the same way both times, and writes it as data.

Methods, stated so they can be challenged:

  window               the --days days of committer time ending at --end's committer date
  commits              first-parent commits from --end committed inside the window, so
                       a history merged in from another repository is not counted
  tasks_shipped        ledger entries at --end less those at the last first-parent
                       commit before the window, counted as corpus_metrics.py counts them
  commits_per_task     commits / tasks_shipped
  every_turn_bytes     at --end, as corpus_metrics.py counts it
  stray_files          paths added inside the window and absent at --end: a file that was
                       committed and then had to be taken out again
  red_days             with --ci, the UTC days on which the last completed run of the
                       workflow on the branch concluded failure; the run list comes from
                       the GitHub API, so this one figure is not reproducible from git
  drift_findings       with --report, the failed rules in that audit report

    python scripts/window_metrics.py --repo <path> --end <commit> --days 14 \\
        --ci owner/repo --workflow gate.yml --report validation/<project>.json

Run from the repository root.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus_metrics import every_turn, git, ledger  # noqa: E402


def stray(repo: Path, since: str, end: str) -> list[str]:
    """Paths added inside the window that no longer exist at the end."""
    log = git(repo, "log", f"--since={since}", "--format=", "--name-status", "--diff-filter=A", end)
    added = {line.split("\t", 1)[1] for line in log.splitlines() if line.startswith("A\t")}
    present = set(git(repo, "ls-tree", "-r", "--name-only", end).splitlines())
    return sorted(added - present)


def red_days(runs: list[dict]) -> tuple[int, int]:
    """Days whose last completed run failed, and the days any run completed."""
    last: dict[str, dict] = {}
    for run in runs:
        day = run["created_at"][:10]
        if day not in last or run["created_at"] > last[day]["created_at"]:
            last[day] = run
    return sum(run["conclusion"] == "failure" for run in last.values()), len(last)


def fetch_runs(ci: str, workflow: str, branch: str, start: datetime, end: datetime) -> list[dict]:
    created = f"{start.strftime('%Y-%m-%dT%H:%M:%SZ')}..{end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    out = subprocess.run(
        ["gh", "api", "-X", "GET", f"repos/{ci}/actions/workflows/{workflow}/runs",
         "-f", f"branch={branch}", "-f", f"created={created}", "-f", "status=completed",
         "-f", "per_page=100", "--paginate", "--jq", ".workflow_runs[] | {conclusion, created_at}"],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def measure(repo: Path, end: str, days: int) -> dict:
    stamp = git(repo, "show", "-s", "--format=%cI", end).strip()
    finish = datetime.fromisoformat(stamp)
    start = finish - timedelta(days=days)
    since = start.isoformat()
    before = git(repo, "rev-list", "-1", "--first-parent", f"--before={since}", end).strip()
    commits = int(git(repo, "rev-list", "--count", "--first-parent", f"--since={since}", end).strip())
    shipped = ledger(repo, end).get("ledger_shipped", 0) - (ledger(repo, before).get("ledger_shipped", 0) if before else 0)
    strays = stray(repo, since, end)
    return {
        "end": git(repo, "rev-parse", end).strip(),
        "window_start": since,
        "window_end": finish.isoformat(),
        "days": days,
        "commits": commits,
        "tasks_shipped": shipped,
        "commits_per_task": round(commits / shipped, 2) if shipped else None,
        "every_turn_bytes": every_turn(repo, end),
        "stray_files": len(strays),
        "stray_paths": strays,
    }


def drift(report: Path) -> int:
    rules = json.loads(report.read_text(encoding="utf-8"))["rules"]
    return sum(rule["verdict"] == "fail" for rule in rules)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--end", required=True)
    parser.add_argument("--days", type=int, default=14)
    parser.add_argument("--ci", help="owner/repo whose workflow runs give red_days")
    parser.add_argument("--workflow", default="gate.yml")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--report", type=Path, help="the audit report whose failures are the drift")
    parser.add_argument("--out", type=Path, help="write the window here as JSON")
    args = parser.parse_args(argv)

    record = measure(args.repo, args.end, args.days)
    if args.ci:
        start, finish = (datetime.fromisoformat(record[key]).astimezone(timezone.utc)
                         for key in ("window_start", "window_end"))
        runs = fetch_runs(args.ci, args.workflow, args.branch, start, finish)
        record["ci_runs"] = len(runs)
        record["red_days"], record["ci_days"] = red_days(runs)
    else:
        record["red_days"] = None
    record["drift_findings"] = drift(args.report) if args.report else None

    text = json.dumps(record, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
