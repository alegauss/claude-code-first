"""Tests for build_site.py (CCF60), built from this repository into a temporary folder.

Run from the repository root: python -m unittest discover -s scripts
"""

import json
import tempfile
import tomllib
import unittest
from pathlib import Path

import build_site


class BuildSite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "site"
        cls.counts = build_site.build(cls.out)
        cls.rules = tomllib.loads((build_site.ROOT / "spec" / "rules.toml").read_text(encoding="utf-8"))["rule"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_rule_has_a_page_and_a_markdown_twin(self):
        self.assertEqual(self.counts["rules"], len(self.rules))
        for rule in self.rules:
            self.assertTrue((self.out / "rules" / f"{rule['address']}.html").exists())
            self.assertTrue((self.out / "rules" / f"{rule['address']}.md").exists())

    def test_every_page_names_the_version_and_the_grade(self):
        version = json.loads((build_site.ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
        text = (self.out / "rules" / f"{self.rules[0]['address']}.md").read_text(encoding="utf-8")
        self.assertIn(f"Version {version}.", text)
        self.assertIn("evidence grade R", text)

    def test_llms_txt_lists_every_rule_twin(self):
        llms = (self.out / "llms.txt").read_text(encoding="utf-8")
        for rule in self.rules:
            self.assertIn(f"(rules/{rule['address']}.md)", llms)

    def test_links_leave_no_repository_relative_path_behind(self):
        text = (self.out / "rules" / "PG-1.md").read_text(encoding="utf-8")
        self.assertNotIn("](../evidence/", text)
        self.assertNotIn("](glossary.md", text)

    def test_the_registry_is_published_as_data(self):
        data = json.loads((self.out / "rules.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["rules"]), len(self.rules))


if __name__ == "__main__":
    unittest.main()
