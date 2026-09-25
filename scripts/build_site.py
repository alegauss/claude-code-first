"""Build the published site: a plain-language guide, and the specification under spec/.

Everything is generated from the repository; nothing in the output is edited by hand.

    python scripts/build_site.py [--out site]

The root is the guide, rendered from guide/index.html: its copy is written there, and every
figure and chart on it is computed here from the registry, the findings, the corpus and
the metrics, so none can go stale in the template (F7). Under spec/ is the site as first
published: for every rule and every finding, an HTML page and its Markdown twin
(spec/rules/IS-1.html and spec/rules/IS-1.md), an index page, and the rule registry as
data (rules.toml and rules.json) so a tool can fetch one version's rules without the
prose. `llms.txt` stays at the root, where agents look for it, and lists the twins. Every
specification page names the version and the evidence grade, and links back to the
guide. Standard library only: the HTML conversion covers the Markdown this repository
writes (headings, paragraphs, lists, tables, emphasis, code and links).
"""

from __future__ import annotations

import argparse
import html
import json
import math
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


def to_html(markdown: str, title: str, version: str, home: str) -> str:
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
        f"<p><small>Claude Code First, specification version {html.escape(version)}. "
        f"<a href=\"{home}\">The plain-language guide</a></small></p>"
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
SPEC = "spec"  # the folder of the site as first published, under the guide
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
    spec = out / SPEC
    (spec / "rules").mkdir(parents=True)
    (spec / "findings").mkdir()
    sections = rule_sections(root)

    def grade_of(rule: dict) -> str:
        grades = [findings[f][0]["Grade"] for f in rule["findings"] if f in findings]
        return max(grades) if grades else "none"

    for rule in registry:
        header = (f"Version {version}. Level {rule['level']}. Best evidence grade {grade_of(rule)}.\n\n")
        text = header + relink(sections.get(rule["address"], f"# {rule['address']}\n\n{rule['statement']}\n"), "spec")
        (spec / "rules" / f"{rule['address']}.md").write_text(text, encoding="utf-8", newline="\n")
        title = f"{rule['address']} {rule['title']}"
        (spec / "rules" / f"{rule['address']}.html").write_text(
            to_html(text.replace(".md)", ".html)"), title, version, "../../index.html"),
            encoding="utf-8", newline="\n")
    for fid, (finding, text) in sorted(findings.items(), key=lambda kv: int(kv[0][1:])):
        body = f"Version {version}. Grade {finding['Grade']}.\n\n" + relink(text, "evidence/findings")
        (spec / "findings" / f"{fid}.md").write_text(body, encoding="utf-8", newline="\n")
        (spec / "findings" / f"{fid}.html").write_text(
            to_html(body, f"{fid} {finding['claim']}", version, "../../index.html"), encoding="utf-8", newline="\n")

    shutil.copyfile(root / "spec" / "rules.toml", spec / "rules.toml")
    (spec / "rules.json").write_text(json.dumps({"version": version, "rules": registry}, indent=2) + "\n",
                                     encoding="utf-8", newline="\n")
    llms = [
        "# Claude Code First",
        "",
        "> An evidence-based specification of how to run a software project with Claude Code as",
        "> its primary author. Each rule cites graded findings from five projects.",
        "",
        f"Version {version}. The rule registry as data: [rules.toml]({SPEC}/rules.toml), "
        f"[rules.json]({SPEC}/rules.json). A plain-language guide for people: [index.html](index.html).",
        "",
        "## Rules",
        "",
    ]
    llms += [f"- [{r['address']} {r['title']}]({SPEC}/rules/{r['address']}.md): {r['keyword']}, level {r['level']}"
             for r in registry]
    llms += ["", "## Findings", ""]
    llms += [f"- [{fid} {f[0]['claim']}]({SPEC}/findings/{fid}.md): {f[0]['Grade']}"
             for fid, f in sorted(findings.items(), key=lambda kv: int(kv[0][1:]))]
    (out / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8", newline="\n")
    index = ["# Claude Code First", "", f"Specification version {version}.", "", "## Rules", "",
             "| Rule | Keyword | Level | Statement |", "|---|---|---|---|"]
    index += [f"| [{r['address']}](rules/{r['address']}.html) | {r['keyword']} | {r['level']} | {r['statement']} |"
              for r in registry]
    (spec / "index.html").write_text(to_html("\n".join(index), "Claude Code First", version, "../index.html"),
                                     encoding="utf-8", newline="\n")
    guide(out, root, version, registry, {fid: f for fid, (f, _) in findings.items()})
    return {"rules": len(registry), "findings": len(findings)}


# ---------- the guide ----------

PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")
LEVELS = [("1", "Level 1", "--lv-1"), ("2", "Level 2", "--lv-2"), ("3", "Level 3", "--lv-3"),
          ("profile", "Agent-facing profile", "--lv-p")]
LEVEL_KEYS = [lv for lv, _, _ in LEVELS]
GRADE = re.compile(r"R(\d)/S(\d)")


def corpus_rows(root: Path) -> list[dict]:
    """The projects, in the order and words of the descriptive table in evidence/corpus.md."""
    rows = []
    for line in (root / "evidence" / "corpus.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) == 8 and cells[7] in ("greenfield", "brownfield"):
            rows.append({"name": cells[0], "language": cells[1], "what": cells[2], "kind": cells[7]})
    return rows


def chapter_names(root: Path) -> list[tuple[str, str]]:
    """The chapters, in the order of the table in spec/README.md."""
    text = (root / "spec" / "README.md").read_text(encoding="utf-8")
    return re.findall(r"^\| ([A-Z]{2}) \| \[([^\]]+)\]\([A-Z]{2}\.md\)", text, re.MULTILINE)


def bar_row(label: str, segments: list[tuple[int, str]], share: float, value: str, tip: str) -> str:
    """One row of a bar chart: the fill's width is `share` of the track, split into segments."""
    fills = "".join(f'<i style="flex:{n};--sw:var({sw})"></i>' for n, sw in segments if n)
    return (f'<div class="bar-row" title="{html.escape(tip)}"><span class="bar-label">{html.escape(label)}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{share * 82:.1f}%">{fills}</span>'
            f'<span class="bar-value">{html.escape(value)}</span></span></div>')


def table_view(head: list[str], rows: list[list[str]]) -> str:
    """The chart's figures as a table, for a reader who cannot or would rather not read the marks."""
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    heads = "".join(f"<th>{html.escape(h)}</th>" for h in head)
    return (f'<details><summary>Show the figures as a table</summary><div class="table-scroll">'
            f"<table><thead><tr>{heads}</tr></thead><tbody>{body}</tbody></table></div></details>")


def chart_every_turn(metrics: list[dict], names: dict[str, str]) -> str:
    ordered = sorted(metrics, key=lambda m: -m["every_turn_tokens"])
    top = max(m["every_turn_tokens"] for m in ordered) or 1
    rows = [bar_row(names.get(m["project"], m["project"]), [(1, "--lv-2")], m["every_turn_tokens"] / top,
                    f"about {m['every_turn_tokens']:,} tokens",
                    f"{names.get(m['project'], m['project'])}: {m['every_turn_bytes']:,} bytes, "
                    f"about {m['every_turn_tokens']:,} tokens")
            for m in ordered]
    table = table_view(["Project", "Bytes", "Tokens (estimate)"],
                       [[html.escape(names.get(m["project"], m["project"])), f"{m['every_turn_bytes']:,}",
                         f"{m['every_turn_tokens']:,}"] for m in ordered])
    return f'<div class="bars">{"".join(rows)}</div>{table}'


def chart_levels(registry: list[dict], chapters: list[tuple[str, str]]) -> str:
    counts = {code: dict.fromkeys(LEVEL_KEYS, 0) for code, _ in chapters}
    for rule in registry:
        counts.setdefault(rule["chapter"], dict.fromkeys(LEVEL_KEYS, 0))[rule["level"]] += 1
    top = max(sum(c.values()) for c in counts.values()) or 1
    legend = "".join(f'<span><i style="--sw:var({sw})"></i>{name}</span>' for _, name, sw in LEVELS)
    rows, table = [], []
    for code, name in chapters:
        c = counts[code]
        total = sum(c.values())
        split = ", ".join(f"{c[lv]} at {label.lower()}" for lv, label, _ in LEVELS if c[lv])
        rows.append(bar_row(name, [(c[lv], sw) for lv, _, sw in LEVELS], total / top,
                            f"{total} rule{'s' if total != 1 else ''}", f"{code}, {name}: {split}"))
        table.append([f'<a href="{SPEC}/index.html">{code}</a> {html.escape(name)}'] + [str(c[lv]) for lv, _, _ in LEVELS]
                     + [str(total)])
    head = ["Chapter"] + [label for _, label, _ in LEVELS] + ["Total"]
    return (f'<div class="legend">{legend}</div><div class="bars wide">{"".join(rows)}</div>'
            + table_view(head, table))


def chart_grades(findings: dict[str, dict]) -> str:
    cells: dict[tuple[int, int], list[str]] = {}
    for fid, finding in findings.items():
        grade = GRADE.search(finding["Grade"])
        if grade:
            cells.setdefault((int(grade.group(1)), int(grade.group(2))), []).append(fid)
    top = max((len(v) for v in cells.values()), default=1)
    grid = ['<span class="corner">R \\ S</span>'] + [f'<span class="axis">S{s}</span>' for s in range(1, 5)]
    table = []
    for r in range(4, 0, -1):
        grid.append(f'<span class="axis">R{r}</span>')
        for s in range(1, 5):
            ids = sorted(cells.get((r, s), []), key=lambda f: int(f[1:]))
            n = len(ids)
            # a square root, so the few findings in most cells stay tellable from none
            pct = 0 if not n else max(18, round(100 * math.sqrt(n / top)))
            klass = "cell zero" if not n else ("cell hi" if pct >= 55 else "cell")
            tip = f"R{r}/S{s}: {n} finding{'s' if n != 1 else ''}" + (f" ({', '.join(ids)})" if ids else "")
            grid.append(f'<span class="{klass}" style="--pct:{pct}%" title="{tip}">{n}</span>')
            if ids:
                links = " ".join(f'<a href="{SPEC}/findings/{f}.html">{f}</a>' for f in ids)
                table.append([f"R{r}/S{s}", str(n), links])
    foot = ('<p class="heat-foot">Rows: recurrence, R4 seen in all five projects. '
            "Columns: strength, S4 held by a test that fails.</p>")
    return (f'<div class="heat" role="img" aria-label="Findings counted by recurrence and strength grade">'
            f'{"".join(grid)}</div>{foot}' + table_view(["Grade", "Findings", "Which"], table))


def project_cards(root: Path, metrics: list[dict]) -> str:
    by_name = {m["project"].lower(): m for m in metrics}
    kinds = {"greenfield": "run this way from its first days",
             "brownfield": "adopted the practice after years of history"}
    cards = []
    for row in corpus_rows(root):
        m = by_name[row["name"].lower()]
        what = row["what"][0].upper() + row["what"][1:]
        cards.append(
            f'      <article class="card"><h3>{html.escape(row["name"])}</h3>'
            f"<p>{html.escape(what)}, {kinds[row['kind']]}.</p>"
            f'<p class="stat"><b>{m["commits"]:,}</b> commits over <b>{m["active_days"]:,}</b> active days '
            f"&middot; {html.escape(row['language'])}</p></article>")
    if len(cards) != len(metrics):
        raise ValueError(f"evidence/corpus.md describes {len(cards)} project(s), the metrics {len(metrics)}")
    return "\n".join(cards)


LESSONS = re.compile(r'<section id="lessons">(.*?)</section>', re.DOTALL)
NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve"]


def lesson_count(template: str) -> str:
    """The number of lesson cards, as the word the headings read, so adding a card cannot leave them stale."""
    section = LESSONS.search(template)
    count = section.group(1).count('<article class="card">') if section else 0
    return NUMBER_WORDS[count] if count < len(NUMBER_WORDS) else str(count)


def guide(out: Path, root: Path, version: str, registry: list[dict], findings: dict[str, dict]) -> None:
    """Render guide/index.html at the root, refusing a placeholder the build does not fill."""
    metrics = json.loads((root / "evidence" / "metrics" / "metrics.json").read_text(encoding="utf-8"))
    chapters = chapter_names(root)
    names = {row["name"].lower(): row["name"] for row in corpus_rows(root)}
    template = (root / "guide" / "index.html").read_text(encoding="utf-8")
    values = {
        "version": html.escape(version),
        "rules": str(len(registry)),
        "findings": str(len(findings)),
        "chapters": str(len(chapters)),
        "projects": str(len(metrics)),
        "commits": f"{sum(m['commits'] for m in metrics):,}",
        "repo": SOURCE,
        "repo_home": SOURCE.removesuffix("blob/main/"),
        "project_cards": project_cards(root, metrics),
        "chart_every_turn": chart_every_turn(metrics, names),
        "chart_levels": chart_levels(registry, chapters),
        "chart_grades": chart_grades(findings),
        "lessons": lesson_count(template),
    }
    missing = sorted({name for name in PLACEHOLDER.findall(template) if name not in values})
    if missing:
        raise ValueError(f"guide/index.html names placeholders the build does not fill: {', '.join(missing)}")
    page = PLACEHOLDER.sub(lambda m: values[m.group(1)], template)
    (out / "index.html").write_text(page, encoding="utf-8", newline="\n")
    shutil.copyfile(root / "guide" / "style.css", out / "style.css")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", default="site")
    args = parser.parse_args(argv)
    counts = build(Path(args.out))
    print(f"{counts['rules']} rule page(s), {counts['findings']} finding page(s) in {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
