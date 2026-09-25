"""Tests for check_catalogue.py (CCF37).

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import check_catalogue

ENTRY = """# Deny with a door

| Field | Value |
|---|---|
| Kind | {kind} |
| Grade | R3/S3 |

## Intent

Refuse, and name the way through.

## Context

## Problem

## Forces

## {solution}

{body}

## Consequences

## Known uses

## Related

{related}
"""


class CheckCatalogue(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for folder in ("patterns", "anti-patterns"):
            (self.root / "spec" / "catalogue" / folder).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, folder, **fields):
        values = {"kind": "pattern", "solution": "Solution", "body": "Text.", "related": "[GH-1](../../GH.md)"}
        values.update(fields)
        (self.root / "spec" / "catalogue" / folder / "entry.md").write_text(ENTRY.format(**values), encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check_catalogue.main([str(self.root)])
        return code, out.getvalue()

    def test_a_well_formed_pattern_passes(self):
        code, out = self.run_on("patterns")
        self.assertEqual(code, 0, out)

    def test_an_anti_pattern_needs_a_refactored_solution(self):
        code, out = self.run_on("anti-patterns", kind="anti-pattern")
        self.assertEqual(code, 1)
        self.assertIn("sections must be", out)
        code, out = self.run_on("anti-patterns", kind="anti-pattern", solution="Refactored solution")
        self.assertEqual(code, 0, out)

    def test_a_keyword_in_prose_fails_but_not_in_code(self):
        code, out = self.run_on("patterns", body="The guard MUST refuse.")
        self.assertEqual(code, 1)
        self.assertIn("keyword MUST", out)
        code, out = self.run_on("patterns", body="A rule reads `MUST refuse` in its chapter.")
        self.assertEqual(code, 0, out)

    def test_related_must_link_a_rule(self):
        code, out = self.run_on("patterns", related="[F300](../../../evidence/findings/F300.md)")
        self.assertEqual(code, 1)
        self.assertIn("links no rule", out)


if __name__ == "__main__":
    unittest.main()
