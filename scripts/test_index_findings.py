"""Tests for index_findings.py (CCF20).

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import index_findings

GOOD = """# F{n} {claim}

| Field | Value |
|---|---|
| Status | {status} |
| Topic | {topic} |
| Grade | {grade} |
| Cases | roadkeep, Shio |
| Contrary | none |
| Harness facts | none |

## Claim

Text.
"""


class IndexFindings(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "evidence" / "findings").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, n, claim="A claim", status="active", topic="Context economy and agent prose", grade="R3/S2"):
        path = self.root / "evidence" / "findings" / f"F{n}.md"
        path.write_text(GOOD.format(n=n, claim=claim, status=status, topic=topic, grade=grade), encoding="utf-8")

    def run_script(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = index_findings.main(["--root", str(self.root), *args])
        return code, out.getvalue()

    def index(self):
        return (self.root / "evidence" / "findings" / "index.md").read_text(encoding="utf-8")

    def test_the_index_orders_by_grade_and_the_check_then_passes(self):
        self.write(1, "Weaker", grade="R2/S2")
        self.write(2, "Stronger", grade="R4/S3")
        code, out = self.run_script()
        self.assertEqual(code, 0, out)
        text = self.index()
        self.assertLess(text.index("Stronger"), text.index("Weaker"))
        self.assertEqual(self.run_script("--check")[0], 0)

    def test_a_stale_index_fails_the_check(self):
        self.write(1)
        self.run_script()
        self.write(2, "Added later")
        code, out = self.run_script("--check")
        self.assertEqual(code, 1)
        self.assertIn("out of date", out)

    def test_a_number_outside_its_topic_block_is_refused(self):
        self.write(150, topic="Context economy and agent prose")
        code, out = self.run_script()
        self.assertEqual(code, 1)
        self.assertIn("outside the block", out)

    def test_a_malformed_grade_is_refused(self):
        self.write(3, grade="R5/S1")
        code, out = self.run_script()
        self.assertEqual(code, 1)
        self.assertIn("is not R1-R4/S1-S4", out)

    def test_withdrawn_findings_are_listed_apart(self):
        self.write(4, "Still holds")
        self.write(5, "Fell", status="withdrawn")
        self.run_script()
        text = self.index()
        self.assertIn("1 active, 1 withdrawn", text)
        self.assertGreater(text.index("Fell"), text.index("## Withdrawn"))


if __name__ == "__main__":
    unittest.main()
