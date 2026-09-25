"""Tests for rules.py (CCF41).

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import rules

CHAPTER = """# VG Verification gates

```markdown
### VG-99 An example inside a fence is not a rule
```

### VG-1 Gates before done

**Work MUST NOT be called done before its *gate* passes.**

| Field | Value |
|---|---|
| Keyword | MUST NOT |
| Level | 2 |
| Checked | by judgement |
| Findings | F305, F303 |
| Harness facts | none |
| Threat | internal |
| Status | active |
"""


class Rules(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "spec").mkdir()
        (self.root / "spec" / "VG.md").write_text(CHAPTER, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def run_main(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = rules.main(["--root", str(self.root), *args])
        return code, out.getvalue()

    def test_a_rule_is_parsed_and_a_fenced_example_is_not(self):
        parsed = rules.parse(self.root)
        self.assertEqual([r["address"] for r in parsed], ["VG-1"])
        self.assertEqual(parsed[0]["findings"], ["F305", "F303"])
        self.assertEqual(parsed[0]["statement"], "Work MUST NOT be called done before its gate passes.")

    def test_build_then_check_then_a_stale_registry_fails(self):
        self.assertEqual(self.run_main("build")[0], 0)
        self.assertEqual(self.run_main("build", "--check")[0], 0)
        path = self.root / "spec" / "VG.md"
        path.write_text(CHAPTER.replace("| Level | 2 |", "| Level | 3 |"), encoding="utf-8")
        code, out = self.run_main("build", "--check")
        self.assertEqual(code, 1)
        self.assertIn("out of date", out)

    def test_query_filters(self):
        self.run_main("build")
        self.assertIn("1 of 1", self.run_main("query", "--level", "2", "--finding", "F303")[1])
        self.assertIn("0 of 1", self.run_main("query", "--checked", "automatically")[1])

    def test_a_rule_without_findings_is_a_problem(self):
        path = self.root / "spec" / "VG.md"
        path.write_text(CHAPTER.replace("F305, F303", "none"), encoding="utf-8")
        code, out = self.run_main("build")
        self.assertEqual(code, 1)
        self.assertIn("cites no finding", out)


if __name__ == "__main__":
    unittest.main()
