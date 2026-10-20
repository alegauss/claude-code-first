# Improvements

## Block A — The repository follows its own rule

## Block B — Research method and the evidence corpus

## Block C — Case studies and the findings register

## Block D — The normative specification

## Block E — Patterns and anti-patterns

## Block F — Conformance and the audit

## Block G — Adoption and realignment

## Block H — Validation against the corpus

### §CCF56 Measuring audit accuracy

For a sample of rules across all five projects, the person records a verdict
independently of the audit. Compute agreement per rule and overall, with Cohen's kappa
where the sample allows, and list every disagreement with its cause: an ambiguous rule,
a checker defect, a missing fixture, or the person's own error. Run the audit twice on
the same commit to measure its repeatability, since the verifier is a model. Ambiguous
rules are rewritten and defects become tasks. `validation/accuracy.md` reports the
numbers with the sample size and its limits.

### §CCF57 Measuring the effect of realignment

Pick one project whose owner accepted realignment tasks; Shio is the likely case because
of its size. Before realignment, record with the corpus metrics script: bytes loaded on
every turn, drift findings, days with a red suite, stray files committed, and commits
per task. After the realignment ships and a comparable period passes, record the same.
Report the differences with the confounders stated: the project changes for other
reasons, the models change, and the person learns. This is an observational measurement,
not an experiment, and the report says so.

## Block I — Governance and publication of the specification

## Block J — The site's mark and look

### §CCF79 The family chip and the repository button in the header

The other alegauss sites draw one header: the brand, a chip that says the product is
part of alegauss and links `https://alegauss.github.io/`, the section links, and the
actions, which hold a ghost button to the repository on GitHub beside the theme toggle
(`claude-tray/site/src/components/Chrome.tsx`, `Nav`: `parent` and the `★ GitHub`
`SiteButton`). This site's guide header has the brand, the anchors, a "Full
specification" button and the toggle: nothing leads to the family it belongs to, and the
repository is reached only from a banner near the end of the page and the footer.

The change, in the `SiteNav` markup class for class, once CCF77 has put the page on
`site.css`:

- `vg-site-nav-left` holds the brand and the `vg-site-parent` chip, "part of
  **alegauss**" with the arrow icon, titled "alegauss: small developer tools", as
  claude-tray words it.
- The actions gain `★ GitHub` as a `vg-site-btn-ghost` to the repository, beside "Full
  specification".
- The specification pages, which carry a one-line header, gain the same two links.

Done when every built page links `https://alegauss.github.io/` and the repository from
its header, and `test_build_site.py` fails when either is missing.

### §CCF80 Bold around an italic term on the rule pages

Every rule's normative sentence is bold, and most hold an italic glossary term: `**Each
planning file an agent writes SHOULD be a *governed file*.**` (spec/PG.md, PG-1).
`inline()` in `scripts/build_site.py` matches bold as `\*\*([^*]+)\*\*`, which cannot
span the inner asterisks, so the bold never matches; the italic then does, and the page
prints `**Each planning file ... <em>governed file</em>.**` with the four asterisks as
text. The rule page is the one place a reader goes for the sentence the rule is, and it
renders wrong on every rule that cites a term. The guide is not affected.

The change: match bold as `\*\*(.+?)\*\*` before italic, so the inner pair is left to
the italic pass. Done when PG-1's page holds `<strong>Each planning file` and no `**`,
and a test in `test_build_site.py` fails on any rule page that still prints two
asterisks.
