"""Release notes and the version bump a change requires, from the rule registry's diff.

The specification's version lives in one place, `.claude-plugin/plugin.json`, which the
checker and every report already read. This script compares spec/rules.toml and
docs/DECISIONS.md between two git refs and classifies the change (spec/versioning.md):

  major  a new MUST or MUST NOT rule, a keyword made stronger, or a rule moved to a lower
         level, where more projects must meet it
  minor  a new SHOULD, SHOULD NOT or MAY rule, a keyword made weaker, a rule moved to a
         higher level, a rule withdrawn, or a new chapter
  patch  anything else: wording, rationale, evidence

Before 1.0 a major change bumps the minor number, as semantic versioning allows for 0.x.

    python scripts/release_notes.py <older-ref> [<newer-ref>]          print the notes
    python scripts/release_notes.py <older-ref> [<newer-ref>] --check  fail if the version
                                                                       bump is too small

Run from the repository root; <newer-ref> defaults to the working tree.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tomllib
from pathlib import Path

REGISTRY = "spec/rules.toml"
MANIFEST = ".claude-plugin/plugin.json"
DECISIONS = "docs/DECISIONS.md"
STRENGTH = {"MAY": 0, "SHOULD NOT": 1, "SHOULD": 1, "MUST NOT": 2, "MUST": 2}
RANK = {"patch": 0, "minor": 1, "major": 2}


def at(root: Path, ref: str | None, path: str) -> str:
    if ref is None:
        target = root / path
        return target.read_text(encoding="utf-8") if target.exists() else ""
    shown = subprocess.run(["git", "-C", str(root), "show", f"{ref}:{path}"],
                           capture_output=True, text=True, encoding="utf-8")
    return shown.stdout if shown.returncode == 0 else ""


def rules_at(root: Path, ref: str | None) -> dict[str, dict]:
    text = at(root, ref, REGISTRY)
    return {r["address"]: r for r in tomllib.loads(text).get("rule", [])} if text else {}


def level_rank(level: str) -> int:
    return {"1": 1, "2": 2, "3": 3}.get(level, 4)  # the profile sits above every level


def classify(old: dict[str, dict], new: dict[str, dict]) -> tuple[str, list[str]]:
    bump, notes = "patch", []

    def note(kind: str, line: str) -> None:
        nonlocal bump
        notes.append(f"[{kind}] {line}")
        if RANK[kind] > RANK[bump]:
            bump = kind

    for address in sorted(set(new) - set(old)):
        rule = new[address]
        kind = "major" if STRENGTH.get(rule["keyword"], 0) == 2 else "minor"
        note(kind, f"{address} added ({rule['keyword']}, level {rule['level']}): {rule['statement']}")
    for address in sorted(set(old) - set(new)):
        note("minor", f"{address} removed")
    for address in sorted(set(old) & set(new)):
        a, b = old[address], new[address]
        if a.get("status") == "active" and b.get("status") == "withdrawn":
            note("minor", f"{address} withdrawn")
        if STRENGTH.get(b["keyword"], 0) > STRENGTH.get(a["keyword"], 0):
            note("major", f"{address} strengthened: {a['keyword']} -> {b['keyword']}")
        elif STRENGTH.get(b["keyword"], 0) < STRENGTH.get(a["keyword"], 0):
            note("minor", f"{address} weakened: {a['keyword']} -> {b['keyword']}")
        if level_rank(b["level"]) < level_rank(a["level"]):
            note("major", f"{address} moved down: level {a['level']} -> {b['level']}")
        elif level_rank(b["level"]) > level_rank(a["level"]):
            note("minor", f"{address} moved up: level {a['level']} -> {b['level']}")
        elif a["statement"] != b["statement"] and a["keyword"] == b["keyword"]:
            note("patch", f"{address} reworded")
    for chapter in sorted({r["chapter"] for r in new.values()} - {r["chapter"] for r in old.values()}):
        note("minor", f"chapter {chapter} added")
    return bump, notes


def required(version: str, bump: str) -> tuple[int, int, int]:
    major, minor, patch = (int(p) for p in version.split("."))
    if major == 0 and bump == "major":
        bump = "minor"
    if bump == "major":
        return major + 1, 0, 0
    if bump == "minor":
        return major, minor + 1, 0
    return major, minor, patch + 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("older")
    parser.add_argument("newer", nargs="?")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    root = Path(args.root)

    bump, notes = classify(rules_at(root, args.older), rules_at(root, args.newer))
    old_version = json.loads(at(root, args.older, MANIFEST) or '{"version": "0.0.0"}')["version"]
    new_version = json.loads(at(root, args.newer, MANIFEST) or '{"version": "0.0.0"}')["version"]
    old_decisions = {line for line in at(root, args.older, DECISIONS).splitlines() if line.startswith("- ")}
    decided = [line for line in at(root, args.newer, DECISIONS).splitlines()
               if line.startswith("- ") and line not in old_decisions]

    print(f"# {new_version} (from {old_version})")
    print(f"\nChange class: {bump}.\n")
    for line in notes or ["[patch] no rule changed"]:
        print(f"- {line}")
    if decided:
        print("\nDecisions recorded:\n")
        for line in decided:
            print(line)
    if args.check and (notes or decided):
        need = required(old_version, bump)
        have = tuple(int(p) for p in new_version.split("."))
        if have < need:
            print(f"\nversion {new_version} is too small: this change needs at least {'.'.join(map(str, need))}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
