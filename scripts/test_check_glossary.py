"""Tests for check_glossary.py (CCF25).

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import check_glossary


class CheckGlossary(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "spec").mkdir()
        (self.root / "spec" / "glossary.md").write_text("# Glossary\n\n## every-turn file\n\nText.\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, chapter):
        (self.root / "spec" / "IS.md").write_text(chapter, encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check_glossary.main([str(self.root)])
        return code, out.getvalue()

    def test_a_defined_term_passes_whatever_its_case(self):
        code, out = self.run_on("### IS-1 A budget\n\n**The *Every-turn file* MUST carry a budget.**\n")
        self.assertEqual(code, 0, out)

    def test_an_undefined_term_fails(self):
        code, out = self.run_on("### IS-2 A cap\n\n**A *skill body* MUST stay small.**\n")
        self.assertEqual(code, 1)
        self.assertIn("'skill body'", out)

    def test_italics_outside_a_rule_sentence_are_ignored(self):
        code, out = self.run_on("## The problem\n\nThe *undefined thing* grows.\n\n### IS-3 X\n\n**Plain MUST.**\n")
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
