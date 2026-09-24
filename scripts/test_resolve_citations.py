"""Tests for resolve_citations.py (CCF9), against a throwaway corpus repository.

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

import resolve_citations


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


class ResolveCitations(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.source = base / "demo"
        self.source.mkdir()
        git(self.source, "init", "-q")
        git(self.source, "config", "user.email", "t@example.com")
        git(self.source, "config", "user.name", "t")
        (self.source / "rules.md").write_text("one\nthe single most\nviolated rule\nfour\n", encoding="utf-8")
        git(self.source, "add", "rules.md")
        git(self.source, "commit", "-q", "-m", "add the rules file")
        self.pin = git(self.source, "rev-parse", "HEAD")
        (self.source / "later.md").write_text("after the pin\n", encoding="utf-8")
        git(self.source, "add", "later.md")
        git(self.source, "commit", "-q", "-m", "a commit after the pin")
        self.later = git(self.source, "rev-parse", "HEAD")

        self.root = base / "repo"
        (self.root / "evidence").mkdir(parents=True)
        (self.root / "evidence" / "corpus.md").write_text(
            "| Project | Remote | Branch | Pin | Date |\n|---|---|---|---|---|\n"
            f"| demo | `example.invalid/demo` | `main` | `{self.pin}` | today |\n"
            f"| gone | `example.invalid/gone` | `main` | `{self.pin}` | today |\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, text, *extra):
        (self.root / "evidence" / "note.md").write_text(text, encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = resolve_citations.main(
                ["--root", str(self.root), "--source", f"demo={self.source}", *extra]
            )
        return code, out.getvalue()

    def test_a_commit_a_file_and_a_line_range_resolve(self):
        short = self.pin[:9]
        code, out = self.run_on(
            f"[demo@{short}] and [demo@{short}:rules.md] and [demo@{short}:rules.md#L2-L3]\n"
        )
        self.assertEqual(code, 0, out)
        self.assertIn("3 pointer(s): 3 resolved", out)

    def test_a_quote_is_found_across_lines_whitespace_aside(self):
        code, out = self.run_on(f'"the single most violated rule" [demo@{self.pin[:9]}:rules.md#L2-L3]\n')
        self.assertEqual(code, 0, out)

    def test_a_quote_outside_its_range_fails(self):
        code, out = self.run_on(f'"violated rule" [demo@{self.pin[:9]}:rules.md#L1]\n')
        self.assertEqual(code, 1)
        self.assertIn("not found there", out)

    def test_a_quote_on_a_bare_commit_is_read_from_its_message(self):
        code, out = self.run_on(f'"add the rules file" [demo@{self.pin[:9]}]\n')
        self.assertEqual(code, 0, out)

    def test_a_line_past_the_end_fails(self):
        code, out = self.run_on(f"[demo@{self.pin[:9]}:rules.md#L9]\n")
        self.assertEqual(code, 1)
        self.assertIn("has 4 lines", out)

    def test_a_missing_path_fails(self):
        code, out = self.run_on(f"[demo@{self.pin[:9]}:nowhere.md]\n")
        self.assertEqual(code, 1)
        self.assertIn("no file nowhere.md", out)

    def test_a_commit_after_the_pin_fails(self):
        code, out = self.run_on(f"[demo@{self.later[:9]}]\n")
        self.assertEqual(code, 1)
        self.assertIn("not in the history", out)

    def test_an_unknown_commit_fails(self):
        code, out = self.run_on("[demo@deadbeef1]\n")
        self.assertEqual(code, 1)
        self.assertIn("no commit deadbeef1", out)

    def test_a_project_not_in_the_corpus_fails(self):
        code, out = self.run_on(f"[other@{self.pin[:9]}]\n")
        self.assertEqual(code, 1)
        self.assertIn("not a project", out)

    def test_pointers_in_code_are_examples_and_are_skipped(self):
        code, out = self.run_on("```text\n[demo@deadbeef1]\n```\nand `[demo@deadbeef1]` inline\n")
        self.assertEqual(code, 0, out)
        self.assertIn("0 pointer(s)", out)

    def test_an_unreachable_project_fails_unless_allowed(self):
        text = f"[gone@{self.pin[:9]}]\n"
        missing = str(Path(self.tmp.name) / "missing")
        code, out = self.run_on(text, "--source", f"gone={missing}")
        self.assertEqual(code, 1)
        self.assertIn("gone: unreachable, 1 pointer(s) unchecked (a failure)", out)
        code, out = self.run_on(text, "--source", f"gone={missing}", "--allow-unreachable", "gone")
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
