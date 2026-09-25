# Audit reports

An audit of a repository against this specification produces one report: JSON in the
shape of [report.schema.json](report.schema.json), with a Markdown rendering for people.
Two audits of one project can then be compared field by field, which is how realignment
is measured.

## What a report holds

- **The specification version** it was judged against, and the versions of the checker
  and the audit skill that produced it.
- **The audited repository and commit**, and the date.
- **The claimed level** and the **achieved level**: the highest level all of whose rules,
  and those of the levels below, pass, are waived or do not apply. It follows from the
  verdicts; `scripts/report.py validate` refuses a report whose stated level does not.
- **A verdict for each rule examined**, with who reached it (the checker, the verifier
  or a person), the locus and the evidence:

| Verdict | Meaning |
|---|---|
| pass | the repository meets the rule |
| fail | the repository breaks the rule; the locus and evidence show where |
| waived | the project departs from the rule on purpose; the report carries the *waiver*, with its reason and, where temporary, its end |
| not applicable | the rule's condition does not hold, such as an agent-facing rule in a project that ships no agent surface |
| could not run | the check did not execute or could not decide; it counts as neither pass nor fail, and it keeps the level from being achieved until it is resolved |

- **A summary by chapter**, in the rendering.

## Where reports live

A project keeps its reports in its own repository under a path it declares, such as
`docs/audits/<date>-<commit>.json` beside the rendered `.md`, so that its history shows
the trend. Nothing in the audit writes them there without the owner asking.

## Tools

```sh
python scripts/check_conformance.py <repo> --level <N> --report <path.json>   # the checker's verdicts
python scripts/report.py validate <path.json>
python scripts/report.py render <path.json> --out <path.md>
python scripts/report.py diff <older.json> <newer.json>
```

The checker writes a report holding its own verdicts; the audit skill adds the verdicts
its scanners and verifier reach, then validates and renders it.
