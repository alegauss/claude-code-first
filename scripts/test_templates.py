"""Tests for the templates (CCF47): a repository assembled from them conforms at level 2.

Run from the repository root: python -m unittest discover -s scripts
"""

import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

import assemble_templates
import check_conformance


class Templates(unittest.TestCase):
    def test_an_assembled_repository_passes_the_checker_at_level_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            written = {p.as_posix() for p in assemble_templates.assemble(repo)}
            self.assertIn(".claude/CLAUDE.md", written)
            self.assertIn(".gitattributes", written)
            subprocess.run(["git", "-C", tmp, "init", "-q"], check=True)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = check_conformance.main([tmp, "--json"])
            self.assertEqual(code, 0, out.getvalue())
            self.assertNotIn('"verdict": "failed"', out.getvalue())
            self.assertNotIn('"verdict": "could not decide"', out.getvalue())

    def test_assembly_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "agents.md").write_text("mine\n", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                assemble_templates.assemble(Path(tmp))


if __name__ == "__main__":
    unittest.main()
