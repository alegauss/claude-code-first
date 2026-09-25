"""Tests for corpus_metrics.py (CCF23), against a throwaway repository.

Run from the repository root: python -m unittest discover -s scripts
"""

import subprocess
import tempfile
import unittest
from pathlib import Path

import corpus_metrics


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout.strip()


class CorpusMetrics(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        files = {
            ".claude/CLAUDE.md": "@../agents.md\n",
            "agents.md": "x" * 100 + "\n",
            ".claude/skills/demo/SKILL.md": "---\nname: demo\ndescription: twelve chars\n---\nbody not counted\n",
            "roadkeep.toml": 'prefix = "DM"\n[markers]\nopen = ["o"]\nshipped = "s"\nretired = "r"\n',
            "docs/CHANGELOG.md": "- **DM1** unmarked\n- s **DM2** marked\n- r **DM3** gone\n",
            "docs/ROADMAP.md": "- o **DM4** open\n",
            "tests/test_a.py": "def test_one():\n    pass\n\ndef test_two():\n    pass\n",
        }
        for path, text in files.items():
            target = self.repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-q", "-m", "feat: add everything (DM1)\n\nCo-Authored-By: Claude <x>")
        git(self.repo, "commit", "-q", "--allow-empty", "-m", "untyped subject")
        self.pin = git(self.repo, "rev-parse", "HEAD")

    def tearDown(self):
        self.tmp.cleanup()

    def test_an_import_relative_to_the_importing_file_is_followed(self):
        # The pointer file imports ../agents.md; before the fix it was not counted.
        total = corpus_metrics.every_turn(self.repo, self.pin)
        self.assertEqual(total, len("@../agents.md\n") + 101 + len("name: demo\ndescription: twelve chars"))

    def test_a_ledger_without_shipped_markers_still_counts_its_entries(self):
        counts = corpus_metrics.ledger(self.repo, self.pin)
        self.assertEqual((counts["ledger_shipped"], counts["ledger_retired"], counts["ledger_open"]), (2, 1, 1))

    def test_shares_and_tests(self):
        record = corpus_metrics.measure("demo", self.repo, self.pin)
        self.assertEqual(record["commits"], 2)
        self.assertEqual(record["conventional_share"], 0.5)
        self.assertEqual(record["task_id_share"], 0.5)
        self.assertEqual(record["coauthored_share"], 0.5)
        self.assertEqual(record["test_declarations"], 2)


if __name__ == "__main__":
    unittest.main()
