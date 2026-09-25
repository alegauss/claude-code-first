"""Audit reports: validate one, render it as Markdown, or compare two.

A report is JSON in the shape of spec/report.schema.json. Could not run is a verdict of
its own and is never folded into pass, so a rule that could not run keeps a level from
being achieved.

    python scripts/report.py validate <report.json>
    python scripts/report.py render <report.json> [--out <report.md>]
    python scripts/report.py diff <older.json> <newer.json>

Standard library only: the validation checks the schema's required fields and
enumerations by hand, so it runs wherever the checker runs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VERDICTS = ("pass", "fail", "waived", "not applicable", "could not run")
LEVELS = ("1", "2", "3", "profile")
BY = ("checker", "verifier", "person")
REQUIRED = ("spec_version", "repository", "commit", "date", "claimed_level", "achieved_level", "tools", "rules")


def problems(report: dict) -> list[str]:
    found = [f"missing {key}" for key in REQUIRED if key not in report]
    if found:
        return found
    if not re.fullmatch(r"[0-9a-f]{7,40}", str(report["commit"])):
        found.append("commit is not a hash")
    if report["claimed_level"] not in (1, 2, 3):
        found.append("claimed_level must be 1, 2 or 3")
    for key in ("checker", "skill"):
        if key not in report["tools"]:
            found.append(f"tools.{key} is missing")
    for i, rule in enumerate(report["rules"]):
        where = rule.get("rule", f"rules[{i}]")
        if not re.fullmatch(r"[A-Z]{2}-\d+", str(rule.get("rule", ""))):
            found.append(f"{where}: bad rule address")
        if rule.get("level") not in LEVELS:
            found.append(f"{where}: level must be one of {', '.join(LEVELS)}")
        if rule.get("verdict") not in VERDICTS:
            found.append(f"{where}: verdict must be one of {', '.join(VERDICTS)}")
        if rule.get("by") not in BY:
            found.append(f"{where}: by must be one of {', '.join(BY)}")
        if rule.get("verdict") == "waived" and not rule.get("waiver"):
            found.append(f"{where}: a waived rule needs its waiver")
    expected = achieved(report["rules"], report["claimed_level"])
    if report["achieved_level"] != expected:
        found.append(f"achieved_level {report['achieved_level']} does not follow from the verdicts "
                     f"(they give {expected})")
    return found


def achieved(rules: list[dict], claimed: int = 3) -> int:
    """The highest level all of whose rules, and those below, pass, are waived or do not apply.

    Never above the claimed level: the rules of a higher level were not examined.
    """
    level = 0
    for n in range(1, claimed + 1):
        at_or_below = [r for r in rules if r.get("level") in {str(k) for k in range(1, n + 1)}]
        if any(r.get("verdict") in ("fail", "could not run") for r in at_or_below):
            break
        level = n
    return level


def render(report: dict) -> str:
    out = [
        f"# Conformance audit: {report['repository']}",
        "",
        f"- Commit: `{report['commit']}`, audited {report['date']}",
        f"- Specification version: {report['spec_version']}",
        f"- Claimed level: {report['claimed_level']}; achieved level: {report['achieved_level']}"
        + ("; agent-facing profile audited" if report.get("profile") else ""),
        f"- Checker: {report['tools']['checker']}; audit skill: {report['tools']['skill']}",
        "",
        "## Summary by chapter",
        "",
        "| Chapter | " + " | ".join(VERDICTS) + " |",
        "|---|" + "---|" * len(VERDICTS),
    ]
    chapters = sorted({r["rule"][:2] for r in report["rules"]})
    for chapter in chapters:
        counts = [sum(1 for r in report["rules"] if r["rule"][:2] == chapter and r["verdict"] == v) for v in VERDICTS]
        out.append(f"| {chapter} | " + " | ".join(str(c) for c in counts) + " |")
    out += ["", "## Rules", "", "| Rule | Level | Verdict | By | Locus | Evidence |", "|---|---|---|---|---|---|"]
    for r in sorted(report["rules"], key=lambda r: (r["rule"][:2], int(r["rule"].split("-")[1]))):
        detail = r.get("waiver") if r["verdict"] == "waived" else r.get("evidence", "")
        out.append(
            f"| {r['rule']} | {r['level']} | {r['verdict']} | {r['by']} "
            f"| {r.get('locus', '').replace('|', '/')} | {(detail or '').replace('|', '/')} |"
        )
    return "\n".join(out) + "\n"


def diff(older: dict, newer: dict) -> list[str]:
    before = {r["rule"]: r["verdict"] for r in older["rules"]}
    after = {r["rule"]: r["verdict"] for r in newer["rules"]}
    lines = [f"{older['commit'][:9]} -> {newer['commit'][:9]}: achieved level "
             f"{older['achieved_level']} -> {newer['achieved_level']}"]
    for rule in sorted(set(before) | set(after)):
        a, b = before.get(rule, "absent"), after.get(rule, "absent")
        if a != b:
            lines.append(f"{rule}: {a} -> {b}")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate")
    v.add_argument("report")
    r = sub.add_parser("render")
    r.add_argument("report")
    r.add_argument("--out")
    d = sub.add_parser("diff")
    d.add_argument("older")
    d.add_argument("newer")
    args = parser.parse_args(argv)

    def load(path: str) -> dict:
        return json.loads(Path(path).read_text(encoding="utf-8"))

    if args.command == "validate":
        found = problems(load(args.report))
        for problem in found:
            print(problem)
        print(f"{len(found)} problem(s)")
        return 1 if found else 0
    if args.command == "render":
        text = render(load(args.report))
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8", newline="\n")
        else:
            print(text, end="")
        return 0
    for line in diff(load(args.older), load(args.newer)):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
