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

### §CCF77 The site on the shared design system

`scripts/build_site.py` builds `site/` from `guide/` and the specification: the guide,
then one page per rule and finding under `spec/`. Every page links `guide/style.css`,
copied into `site/` as is: 892 lines that declare their own `--bg`, `--text` and
`--accent` tokens in both colour modes and draw the nav, hero, cards and footer by hand.
The hub and the other alegauss sites are moving onto `@viglet/viglet-design-system`, and
VDS216 ships the plain CSS a page with no build can link.

The move:

- Link `tokens.css` and `site.css` at a pinned version, and drop the rules they cover. The
  reading styles for rules, findings and tables stay local.
- `data-tone="cool"`, since the ground is a blue-tinted white and near-black, not clay.
- The accent is settled first. The page is blue (`#17699c`, `#2e9bd6` in dark), which is
  FreeWilly's accent on the hub, so the hub gave this project rose instead. One value goes
  into the hub's `projects.json` and the page takes it.
- The `{{gtag}}` that `build_site.py` writes loads only after consent, as on the hub.

Done when no rule in `style.css` duplicates one `site.css` provides, every built page
holds the same text as before, light and dark screenshots of the guide and of one rule
page are compared before and after, and the site is listed in the design system's
`consumers.json`.
