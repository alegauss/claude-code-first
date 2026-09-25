"""Tests for check_conformance.py (CCF43): each detector on a passing and a failing fixture.

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

import check_conformance as cc


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, text):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")


class Detectors(Fixture):
    def test_is_1(self):
        self.assertEqual(cc.is_1(self.repo)[0], cc.PASSED)  # no every-turn file, allowed by D2
        self.write(".claude/CLAUDE.md", "@../agents.md\n")
        self.write("agents.md", "x\n" * 20)
        self.assertEqual(cc.is_1(self.repo)[0], cc.UNDECIDED)
        self.write("roadkeep.toml", '[budgets]\n"agents.md" = { lines = 10 }\n".claude/CLAUDE.md" = { lines = 5 }\n')
        verdict, detail = cc.is_1(self.repo)
        self.assertEqual(verdict, cc.FAILED)
        self.assertIn("agents.md over 10 lines", detail)
        self.write("roadkeep.toml", '[budgets]\n"agents.md" = { lines = 30 }\n".claude/CLAUDE.md" = { lines = 5 }\n')
        self.assertEqual(cc.is_1(self.repo)[0], cc.PASSED)

    def test_pg_1(self):
        self.assertEqual(cc.pg_1(self.repo)[0], cc.UNDECIDED)
        self.write("roadkeep.toml", 'prefix = "X"\n')
        self.assertEqual(cc.pg_1(self.repo)[0], cc.FAILED)
        self.write(".claude/settings.json", '{"hooks": {"PreToolUse": []}}')
        self.assertEqual(cc.pg_1(self.repo)[0], cc.PASSED)

    def test_vg_2(self):
        self.write("CLAUDE.md", "Run `./mvnw test`.\n")
        self.assertEqual(cc.vg_2(self.repo)[0], cc.PASSED)
        self.write(".claude/skills/build/SKILL.md", "./mvnw test 2>&1 | grep Tests\n")
        self.assertEqual(cc.vg_2(self.repo)[0], cc.FAILED)

    def test_vg_5(self):
        self.assertEqual(cc.vg_5(self.repo)[0], cc.FAILED)
        self.write(".github/workflows/ci.yml", "on:\n  workflow_dispatch:\n")
        self.assertEqual(cc.vg_5(self.repo)[0], cc.FAILED)
        self.write(".github/workflows/ci.yml", "on: [push, pull_request]\n")
        self.assertEqual(cc.vg_5(self.repo)[0], cc.PASSED)

    def test_ep_2(self):
        self.write(".gitattributes", "docs/ROADMAP.md merge=roadkeep\n")
        self.assertEqual(cc.ep_2(self.repo)[0], cc.FAILED)
        self.write(".gitattributes", "* text=auto eol=lf\n")
        self.assertEqual(cc.ep_2(self.repo)[0], cc.PASSED)

    def test_cd_1(self):
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        self.write("roadkeep.toml", 'prefix = "X"\n')
        self.write("docs/CHANGELOG.md", "- s **X1** one\n")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-q", "-m", "one")
        self.assertEqual(cc.cd_1(self.repo)[0], cc.PASSED)
        self.write("docs/CHANGELOG.md", "- s **X1** one\n- s **X2** two\n- s **X3** three\n")
        git(self.repo, "commit", "-q", "-am", "two at once")
        self.assertEqual(cc.cd_1(self.repo)[0], cc.FAILED)


class Levels(Fixture):
    def test_a_failure_above_the_claimed_level_does_not_fail_the_claim(self):
        self.write(".github/workflows/ci.yml", "on: workflow_dispatch\n")  # VG-5, level 2, fails
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cc.main([str(self.repo), "--level", "1", "--json"]), 0)
            self.assertEqual(cc.main([str(self.repo), "--level", "2", "--json"]), 1)


if __name__ == "__main__":
    unittest.main()
