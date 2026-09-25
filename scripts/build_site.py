"""Build the published site: a page per rule and per finding, Markdown twins, llms.txt.

Everything is generated from the repository; nothing in the output is edited by hand.

    python scripts/build_site.py [--out site]

The output holds, for every rule and every finding, an HTML page and its Markdown twin
(rules/IS-1.html and rules/IS-1.md), an index page, `llms.txt` listing the Markdown
twins for agents, and the rule registry as data (rules.toml and rules.json) so a tool can
fetch one version's rules without the prose. Every page names the specification version
and the evidence grade. Standard library only: the HTML conversion covers the Markdown
this repository writes (headings, paragraphs, lists, tables, emphasis, code and links).
"""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from index_findings import parse as parse_finding  # noqa: E402

RULE_HEADING = re.compile(r"^### ([A-Z]{2}-\d+) ")


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", text)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


def to_html(markdown: str, title: str, version: str) -> str:
    out, paragraph, in_list, in_code, table = [], [], False, False, []

    def flush():
        nonlocal paragraph, in_list, table
        if paragraph:
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph = []
        if in_list:
            out.append("</ul>")
            in_list = False
        if table:
            rows = [r for r in table if not re.fullmatch(r"\|[\s|:-]+\|", r)]
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            body = "".join(
                "<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{inline(c)}</{'th' if i == 0 else 'td'}>"
                                 for c in row) + "</tr>" for i, row in enumerate(cells))
            out.append(f"<table>{body}</table>")
            table = []

    for line in markdown.splitlines():
        if line.startswith("```"):
            flush()
            out.append("</code></pre>" if in_code else "<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        heading = re.match(r"^(#{1,6}) (.*)$", line)
        if heading:
            flush()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif line.startswith("|"):
            if paragraph or in_list:
                flush()
            table.append(line)
        elif re.match(r"^\s*[-*] ", line):
            if paragraph or table:
                flush()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(re.sub(r'^\s*[-*] ', '', line))}</li>")
        elif not line.strip():
            flush()
        else:
            paragraph.append(line.strip())
    flush()
    return (
        "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>{html.escape(title)}</title>"
        "<style>body{max-width:46rem;margin:2rem auto;padding:0 1rem;font:16px/1.55 system-ui,sans-serif}"
        "table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:.25rem .5rem;text-align:left}"
        "code{font-size:.9em}pre{overflow-x:auto}</style></head><body>"
        f"<p><small>Claude Code First, specification version {html.escape(version)}</small></p>"
        + "\n".join(out) + "</body></html>\n"
    )


def rule_sections(root: Path) -> dict[str, str]:
    """Each rule's Markdown, from its heading to the next rule or section."""
    sections = {}
    for chapter in sorted((root / "spec").glob("[A-Z][A-Z].md")):
        current, lines = None, []
        for line in chapter.read_text(encoding="utf-8").splitlines() + ["## end"]:
            match = RULE_HEADING.match(line)
            if match or line.startswith("## "):
                if current:
                    sections[current] = "\n".join(lines).strip() + "\n"
                current, lines = (match.group(1), [line.replace("### ", "# ", 1)]) if match else (None, [])
            elif current:
                lines.append(line)
    return sections


SOURCE = "https://github.com/alegauss/claude-code-first/blob/main/"
LINK = re.compile(r"\]\((?!https?://|#)([^)\s]+)\)")


def relink(markdown: str, source_dir: str) -> str:
    """Resolve each relative link from the file it came from: a finding becomes the site's
    own finding page, and anything else the site does not carry becomes the file on GitHub."""

    def target(match: re.Match) -> str:
        path, _, anchor = match.group(1).partition("#")
        resolved = posixpath.normpath(posixpath.join(source_dir, path))
        finding = re.fullmatch(r"evidence/findings/(F\d+)\.md", resolved)
        if finding:
            return f"](../findings/{finding.group(1)}.md)"
        return f"]({SOURCE}{resolved}{'#' + anchor if anchor else ''})"

    return LINK.sub(target, markdown)


def build(out: Path, root: Path = ROOT) -> dict:
    version = json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    registry = tomllib.loads((root / "spec" / "rules.toml").read_text(encoding="utf-8"))["rule"]
    findings = {}
    for path in (root / "evidence" / "findings").glob("F*.md"):
        finding, _ = parse_finding(path)
        if finding:
            findings[f"F{finding['number']}"] = (finding, path.read_text(encoding="utf-8"))
    if out.exists():
        shutil.rmtree(out)
    (out / "rules").mkdir(parents=True)
    (out / "findings").mkdir()
    sections = rule_sections(root)

    def grade_of(rule: dict) -> str:
        grades = [findings[f][0]["Grade"] for f in rule["findings"] if f in findings]
        return max(grades) if grades else "none"

    for rule in registry:
        header = (f"Version {version}. Level {rule['level']}. Best evidence grade {grade_of(rule)}.\n\n")
        text = header + relink(sections.get(rule["address"], f"# {rule['address']}\n\n{rule['statement']}\n"), "spec")
        (out / "rules" / f"{rule['address']}.md").write_text(text, encoding="utf-8", newline="\n")
        title = f"{rule['address']} {rule['title']}"
        (out / "rules" / f"{rule['address']}.html").write_text(
            to_html(text.replace(".md)", ".html)"), title, version), encoding="utf-8", newline="\n")
    for fid, (finding, text) in sorted(findings.items(), key=lambda kv: int(kv[0][1:])):
        body = f"Version {version}. Grade {finding['Grade']}.\n\n" + relink(text, "evidence/findings")
        (out / "findings" / f"{fid}.md").write_text(body, encoding="utf-8", newline="\n")
        (out / "findings" / f"{fid}.html").write_text(
            to_html(body, f"{fid} {finding['claim']}", version), encoding="utf-8", newline="\n")

    shutil.copyfile(root / "spec" / "rules.toml", out / "rules.toml")
    (out / "rules.json").write_text(json.dumps({"version": version, "rules": registry}, indent=2) + "\n",
                                    encoding="utf-8", newline="\n")
    llms = [
        "# Claude Code First",
        "",
        "> An evidence-based specification of how to run a software project with Claude Code as",
        "> its primary author. Each rule cites graded findings from five projects.",
        "",
        f"Version {version}. The rule registry as data: [rules.toml](rules.toml), [rules.json](rules.json).",
        "",
        "## Rules",
        "",
    ]
    llms += [f"- [{r['address']} {r['title']}](rules/{r['address']}.md): {r['keyword']}, level {r['level']}"
             for r in registry]
    llms += ["", "## Findings", ""]
    llms += [f"- [{fid} {f[0]['claim']}](findings/{fid}.md): {f[0]['Grade']}"
             for fid, f in sorted(findings.items(), key=lambda kv: int(kv[0][1:]))]
    (out / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8", newline="\n")
    index = ["# Claude Code First", "", f"Specification version {version}.", "", "## Rules", "",
             "| Rule | Keyword | Level | Statement |", "|---|---|---|---|"]
    index += [f"| [{r['address']}](rules/{r['address']}.html) | {r['keyword']} | {r['level']} | {r['statement']} |"
              for r in registry]
    (out / "index.html").write_text(to_html("\n".join(index), "Claude Code First", version),
                                    encoding="utf-8", newline="\n")
    return {"rules": len(registry), "findings": len(findings)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", default="site")
    args = parser.parse_args(argv)
    counts = build(Path(args.out))
    print(f"{counts['rules']} rule page(s), {counts['findings']} finding page(s) in {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
