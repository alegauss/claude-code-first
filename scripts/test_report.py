"""Tests for report.py (CCF45).

Run from the repository root: python -m unittest discover -s scripts
"""

import unittest

import report


def make(rules, achieved=None):
    return {
        "spec_version": "0.1.0", "repository": "demo", "commit": "abcdef1", "date": "2026-09-25",
        "claimed_level": 2, "achieved_level": report.achieved(rules, 2) if achieved is None else achieved,
        "tools": {"checker": "0.1.0", "skill": "0.1.0"}, "rules": rules,
    }


def rule(address, level, verdict, **extra):
    return {"rule": address, "level": level, "verdict": verdict, "by": "checker", **extra}


class Report(unittest.TestCase):
    def test_could_not_run_blocks_the_level_it_belongs_to(self):
        rules = [rule("IS-1", "1", "pass"), rule("VG-5", "2", "could not run")]
        self.assertEqual(report.achieved(rules, 2), 1)
        rules[1]["verdict"] = "pass"
        self.assertEqual(report.achieved(rules, 2), 2)

    def test_the_achieved_level_never_exceeds_the_claim(self):
        self.assertEqual(report.achieved([rule("IS-1", "1", "pass")], 1), 1)

    def test_waived_and_not_applicable_do_not_block(self):
        rules = [rule("IS-1", "1", "waived", waiver="until 2026-12-01: budget being cut"),
                 rule("AP-1", "profile", "fail"), rule("CD-1", "1", "not applicable")]
        self.assertEqual(report.achieved(rules, 2), 2)

    def test_a_stated_level_that_does_not_follow_is_refused(self):
        found = report.problems(make([rule("IS-1", "1", "fail")], achieved=1))
        self.assertTrue(any("does not follow" in p for p in found))

    def test_a_waiver_needs_its_reason(self):
        found = report.problems(make([rule("IS-1", "1", "waived")]))
        self.assertIn("IS-1: a waived rule needs its waiver", found)

    def test_diff_names_each_changed_rule(self):
        older = make([rule("IS-1", "1", "fail"), rule("VG-5", "2", "pass")])
        newer = make([rule("IS-1", "1", "pass"), rule("VG-5", "2", "pass")])
        newer["commit"] = "1234567"
        lines = report.diff(older, newer)
        self.assertIn("IS-1: fail -> pass", lines)
        self.assertEqual(len(lines), 2)

    def test_render_has_a_row_per_rule(self):
        text = report.render(make([rule("IS-1", "1", "pass", evidence="2 files under budget")]))
        self.assertIn("| IS-1 | 1 | pass | checker |", text)


if __name__ == "__main__":
    unittest.main()
