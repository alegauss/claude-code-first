"""Tests for build_site.py (CCF60), built from this repository into a temporary folder.

Run from the repository root: python -m unittest discover -s scripts
"""

import json
import re
import struct
import tempfile
import tomllib
import unittest
from pathlib import Path

import build_site
import og_card


class BuildSite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "site"
        cls.spec = cls.out / build_site.SPEC
        cls.counts = build_site.build(cls.out)
        cls.rules = tomllib.loads((build_site.ROOT / "spec" / "rules.toml").read_text(encoding="utf-8"))["rule"]
        cls.guide = (cls.out / "index.html").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_rule_has_a_page_and_a_markdown_twin(self):
        self.assertEqual(self.counts["rules"], len(self.rules))
        for rule in self.rules:
            self.assertTrue((self.spec / "rules" / f"{rule['address']}.html").exists())
            self.assertTrue((self.spec / "rules" / f"{rule['address']}.md").exists())

    def test_every_page_names_the_version_and_the_grade(self):
        version = json.loads((build_site.ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
        text = (self.spec / "rules" / f"{self.rules[0]['address']}.md").read_text(encoding="utf-8")
        self.assertIn(f"Version {version}.", text)
        self.assertIn("evidence grade R", text)

    def test_llms_txt_lists_every_rule_twin(self):
        llms = (self.out / "llms.txt").read_text(encoding="utf-8")
        for rule in self.rules:
            self.assertIn(f"({build_site.SPEC}/rules/{rule['address']}.md)", llms)

    def test_links_leave_no_repository_relative_path_behind(self):
        text = (self.spec / "rules" / "PG-1.md").read_text(encoding="utf-8")
        self.assertNotIn("](../evidence/", text)
        self.assertNotIn("](glossary.md", text)

    def test_the_registry_is_published_as_data(self):
        data = json.loads((self.spec / "rules.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["rules"]), len(self.rules))

    def test_the_guide_is_the_root_and_the_first_site_is_under_spec(self):
        self.assertIn('href="spec/index.html"', self.guide)
        self.assertTrue((self.out / "style.css").exists())
        index = (self.spec / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="../index.html"', index)

    def test_the_guide_leaves_no_placeholder_and_types_no_count(self):
        self.assertNotRegex(self.guide, build_site.PLACEHOLDER)
        self.assertIn(f"<b>{len(self.rules)}</b> rules", self.guide)
        template = (build_site.ROOT / "guide" / "index.html").read_text(encoding="utf-8")
        self.assertNotIn(f">{len(self.rules)}<", template)

    def test_the_lesson_count_is_the_number_of_cards(self):
        template = (build_site.ROOT / "guide" / "index.html").read_text(encoding="utf-8")
        cards = build_site.LESSONS.search(template).group(1).count('<article class="card">')
        word = build_site.NUMBER_WORDS[cards]
        self.assertIn(f"{word} things the projects learned the hard way", self.guide)
        self.assertNotIn(f"{word} things", template)

    def test_every_finding_and_rule_the_guide_cites_exists(self):
        cited = re.findall(r'href="spec/(rules|findings)/([A-Z0-9-]+)\.html"', self.guide)
        self.assertTrue(cited)
        for kind, name in cited:
            self.assertTrue((self.spec / kind / f"{name}.html").exists(), f"{kind}/{name}")

    def test_the_grade_chart_counts_every_finding(self):
        cells = re.findall(r'class="cell[^"]*"[^>]*>(\d+)<', self.guide)
        self.assertEqual(len(cells), 16)
        self.assertEqual(sum(int(n) for n in cells), self.counts["findings"])

    def test_an_unknown_placeholder_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("evidence/corpus.md", "evidence/metrics/metrics.json", "spec/README.md", "guide/style.css"):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_bytes((build_site.ROOT / rel).read_bytes())
            (root / "guide" / "index.html").write_text("{{nothing_fills_this}}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "nothing_fills_this"):
                build_site.guide(root, root, "0", self.rules, {})

    def test_analytics_loads_only_from_the_consent_script(self):
        pages = sorted(self.out.rglob("*.html"))
        self.assertGreater(len(pages), 1)
        for page in pages:
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("googletagmanager", text, page.name)
            self.assertIn('class="consent-settings"', text, page.name)
        script = (self.out / "site.js").read_text(encoding="utf-8")
        self.assertIn('localStorage.getItem(KEY)', script)
        self.assertIn('"G-6HG45Q9BHP"', script)

    def test_every_page_takes_the_design_system_at_one_pinned_version(self):
        template = (build_site.ROOT / "guide" / "index.html").read_text(encoding="utf-8")
        links = build_site.design_links(template)
        self.assertRegex(links, r"@\d+\.\d+\.\d+/dist/site\.css")
        for page in sorted(self.out.rglob("*.html")):
            text = page.read_text(encoding="utf-8")
            head = text[:text.index("</head>")]
            depth = len(page.relative_to(self.out).parts) - 1
            self.assertIn(links, head + "\n", page.name)
            self.assertIn(f'href="{"../" * depth}style.css"', head, page.name)
            self.assertIn(f'src="{"../" * depth}site.js"', head, page.name)
            self.assertIn(build_site.THEME_SCRIPT, head, page.name)
            self.assertIn('<body class="vg-site">', text, page.name)
            self.assertIn('data-tone="cool"', text, page.name)

    def test_a_bold_sentence_holding_an_italic_term_renders_as_markup(self):
        page = (self.spec / "rules" / "PG-1.html").read_text(encoding="utf-8")
        self.assertIn("<strong>Each planning file an agent writes SHOULD be a <em>governed file</em>.</strong>", page)
        for path in sorted((self.spec / "rules").glob("*.html")):
            self.assertNotIn("**", path.read_text(encoding="utf-8"), path.name)

    def test_every_header_links_the_family_and_the_repository(self):
        repo = build_site.SOURCE.removesuffix("blob/main/")
        for page in sorted(self.out.rglob("*.html")):
            text = page.read_text(encoding="utf-8")
            nav = text[text.index('<nav class="vg-site-nav">'):text.index("</nav>")]
            self.assertIn('class="vg-site-parent" href="https://alegauss.github.io/"', nav, page.name)
            self.assertIn(f'class="vg-site-btn vg-site-btn-ghost" href="{repo}"', nav, page.name)

    def test_design_links_at_two_versions_are_refused(self):
        mixed = ('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@viglet/viglet-design-system@1.0.0/dist/a.css">'
                 '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@viglet/viglet-design-system@1.0.0/dist/b.css">'
                 '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@viglet/viglet-design-system@2.0.0/dist/c.css">')
        with self.assertRaisesRegex(ValueError, "one pinned version"):
            build_site.design_links(mixed)

    def test_style_css_restates_no_rule_site_css_draws(self):
        style = (build_site.ROOT / "guide" / "style.css").read_text(encoding="utf-8")
        for old in ("nav {", ".hero {", ".btn {", ".eyebrow {", "footer {", ".pill {", "--azure"):
            self.assertNotIn(old, style)

    def test_every_page_links_the_icon_and_the_social_card_in_its_head(self):
        pages = sorted(self.out.rglob("*.html"))
        for page in pages:
            text = page.read_text(encoding="utf-8")
            head = text[:text.index("</head>")]
            depth = len(page.relative_to(self.out).parts) - 1
            self.assertIn(f'<link rel="icon" href="{"../" * depth}icon.svg"', head, page.name)
            self.assertIn(f'<meta property="og:image" content="{build_site.SITE}og.png">', head, page.name)
            self.assertIn('<meta name="twitter:card" content="summary_large_image">', head, page.name)
            self.assertEqual(text.count('property="og:image"'), 1, page.name)
        self.assertTrue((self.out / "icon.svg").exists())
        self.assertIn('src="icon.svg"', self.guide)

    def test_the_social_card_is_a_1200_by_630_png_showing_the_mark_and_title(self):
        data = (self.out / "og.png").read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", data[16:24]), (1200, 630))
        pixels = og_card.render()
        colours = {bytes(pixels[i:i + 3]) for i in range(0, len(pixels), 3)}
        for colour in (og_card.ROSE, og_card.SEAL, og_card.INK):
            self.assertIn(bytes(colour), colours)

    def test_the_card_refuses_a_letter_its_alphabet_lacks(self):
        with self.assertRaisesRegex(ValueError, "no glyph"):
            og_card.text_shapes("Claude Code Zero", 0, 0, 10)


if __name__ == "__main__":
    unittest.main()
