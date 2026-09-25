"""Tests for window_metrics.py (CCF57), against a throwaway repository.

Run from the repository root: python -m unittest discover -s scripts
"""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import window_metrics


def git(repo, *args, date=None):
    env = dict(os.environ)
    if date:
        env["GIT_COMMITTER_DATE"] = env["GIT_AUTHOR_DATE"] = date
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True,
                          env=env).stdout.strip()


class WindowMetrics(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        self.write("roadkeep.toml", 'prefix = "DM"\n[markers]\nshipped = "s"\n')
        self.write("docs/CHANGELOG.md", "- s **DM1** old\n")
        self.write("CLAUDE.md", "x" * 10)
        self.commit("feat: before the window (DM1)", "2026-01-01T12:00:00+00:00")
        self.write("docs/CHANGELOG.md", "- s **DM1** old\n- s **DM2** new\n")
        self.write("stray.txt", "oops")
        self.commit("feat: inside (DM2)", "2026-01-10T12:00:00+00:00")
        (self.repo / "stray.txt").unlink()
        self.commit("fix: take the stray file out", "2026-01-11T12:00:00+00:00")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, text):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def commit(self, message, date):
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", message, date=date)

    def test_counts_only_inside_the_window(self):
        record = window_metrics.measure(self.repo, "HEAD", 5)
        self.assertEqual(record["commits"], 2)
        self.assertEqual(record["tasks_shipped"], 1)
        self.assertEqual(record["commits_per_task"], 2.0)
        self.assertEqual(record["every_turn_bytes"], 10)

    def test_a_file_added_and_removed_is_stray(self):
        record = window_metrics.measure(self.repo, "HEAD", 5)
        self.assertEqual(record["stray_paths"], ["stray.txt"])

    def test_the_last_run_of_a_day_decides_it(self):
        runs = [
            {"conclusion": "failure", "created_at": "2026-01-10T08:00:00Z"},
            {"conclusion": "success", "created_at": "2026-01-10T09:00:00Z"},
            {"conclusion": "success", "created_at": "2026-01-11T08:00:00Z"},
            {"conclusion": "failure", "created_at": "2026-01-11T09:00:00Z"},
        ]
        self.assertEqual(window_metrics.red_days(runs), (1, 2))


if __name__ == "__main__":
    unittest.main()
