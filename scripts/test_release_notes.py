"""Tests for release_notes.py (CCF58).

Run from the repository root: python -m unittest discover -s scripts
"""

import unittest

import release_notes as rn


def rule(keyword="SHOULD", level="2", statement="A rule.", status="active", chapter="VG"):
    return {"keyword": keyword, "level": level, "statement": statement, "status": status, "chapter": chapter}


class Classify(unittest.TestCase):
    def test_a_new_must_is_major_and_a_new_should_minor(self):
        self.assertEqual(rn.classify({}, {"VG-1": rule("MUST")})[0], "major")
        self.assertEqual(rn.classify({}, {"VG-1": rule("SHOULD")})[0], "minor")

    def test_strengthening_and_moving_down_are_major(self):
        self.assertEqual(rn.classify({"VG-1": rule("SHOULD")}, {"VG-1": rule("MUST")})[0], "major")
        self.assertEqual(rn.classify({"VG-1": rule(level="2")}, {"VG-1": rule(level="1")})[0], "major")

    def test_weakening_withdrawing_and_moving_up_are_minor(self):
        self.assertEqual(rn.classify({"VG-1": rule("MUST")}, {"VG-1": rule("SHOULD")})[0], "minor")
        self.assertEqual(rn.classify({"VG-1": rule()}, {"VG-1": rule(status="withdrawn")})[0], "minor")
        self.assertEqual(rn.classify({"VG-1": rule(level="1")}, {"VG-1": rule(level="3")})[0], "minor")

    def test_rewording_is_a_patch(self):
        self.assertEqual(rn.classify({"VG-1": rule()}, {"VG-1": rule(statement="Reworded.")})[0], "patch")


class Required(unittest.TestCase):
    def test_before_1_0_a_major_change_bumps_the_minor_number(self):
        self.assertEqual(rn.required("0.1.0", "major"), (0, 2, 0))

    def test_after_1_0_each_class_bumps_its_own_number(self):
        self.assertEqual(rn.required("1.2.3", "major"), (2, 0, 0))
        self.assertEqual(rn.required("1.2.3", "minor"), (1, 3, 0))
        self.assertEqual(rn.required("1.2.3", "patch"), (1, 2, 4))


if __name__ == "__main__":
    unittest.main()
