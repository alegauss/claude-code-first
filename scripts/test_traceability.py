"""Tests for traceability.py (CCF42): the gate fails on each broken link of the chain.

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import traceability

FINDING = """# F{n} A claim

| Field | Value |
|---|---|
| Status | active |
| Topic | Gates, verification, and hooks against instructions |
| Grade | {grade} |
| Cases | Shio |
| Contrary | none |
| Harness facts | none |
{extra}
## Observations

- Shio: {pointer}
"""

RULE = """# VG Verification gates

### VG-1 A rule

**Work {keyword} be done.**

| Field | Value |
|---|---|
| Keyword | {keyword} |
| Level | 2 |
| Checked | by judgement |
| Findings | {findings} |
| Harness facts | none |
| Threat | internal |
| Status | active |
"""


class Traceability(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "evidence" / "findings").mkdir(parents=True)
        (self.root / "spec" / "catalogue" / "patterns").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def finding(self, n, grade="R3/S3", pointer="[shio@821f18d74]", extra=""):
        (self.root / "evidence" / "findings" / f"F{n}.md").write_text(
            FINDING.format(n=n, grade=grade, pointer=pointer, extra=extra), encoding="utf-8")

    def rule(self, keyword="MUST", findings="F300"):
        (self.root / "spec" / "VG.md").write_text(RULE.format(keyword=keyword, findings=findings), encoding="utf-8")

    def run_trace(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = traceability.main(["--root", str(self.root)])
        return code, out.getvalue()

    def test_a_sound_chain_passes_and_writes_the_matrix(self):
        self.finding(300)
        self.rule()
        code, out = self.run_trace()
        self.assertEqual(code, 0, out)
        self.assertIn("| VG-1 | MUST | 2 |", (self.root / "spec" / "traceability.md").read_text(encoding="utf-8"))

    def test_a_must_on_weak_evidence_fails(self):
        self.finding(300, grade="R1/S2")
        self.rule()
        code, out = self.run_trace()
        self.assertEqual(code, 1)
        self.assertIn("stronger than its findings admit", out)

    def test_a_missing_finding_fails(self):
        self.finding(300)
        self.rule(findings="F300, F999")
        self.assertIn("F999, which does not exist", self.run_trace()[1])

    def test_an_uncited_finding_fails_unless_background(self):
        self.finding(300)
        self.finding(301)
        self.rule()
        self.assertIn("F301: is cited by no rule", self.run_trace()[1])
        self.finding(301, extra="| Use | background |\n")
        self.assertEqual(self.run_trace()[0], 0)

    def test_a_finding_without_a_pointer_fails(self):
        self.finding(300, pointer="no source given")
        self.rule()
        self.assertIn("carries no pointer", self.run_trace()[1])

    def test_a_catalogue_link_to_a_missing_rule_fails(self):
        self.finding(300)
        self.rule()
        (self.root / "spec" / "catalogue" / "patterns" / "x.md").write_text(
            "# X\n\n## Related\n\n[VG-9](../../VG.md)\n", encoding="utf-8")
        self.assertIn("links VG-9, which is not a rule", self.run_trace()[1])


if __name__ == "__main__":
    unittest.main()
