# Declaring conformance and recording deviations

A project that adopts this specification keeps one file at its root, `ccf.toml`, which
states what it claims and where it departs on purpose. The checker and the audit skill
read it. A deviation recorded here is a *waiver*: a decision with a reason, an owner and
an end. A deviation not recorded here is drift, and an audit reports it as a failure.

The shape follows Shio's ledger of red suites, in which a known failure was allowed to
stand only with a date and the task that would end it (see
[../evidence/findings/F303.md](../evidence/findings/F303.md)).

```toml
# What the project claims.
level = 2                  # 1, 2 or 3 (conformance.md)
spec_version = "0.1.0"     # the version it is judged against
profile = false            # true when it ships a surface for other agents (chapter AP)

# One entry per rule the project departs from on purpose.
[[waiver]]
rule = "EP-2"
reason = "line endings are being renormalised across 400 files"
owner = "the person accountable for the decision"
date = "2026-09-25"        # when the waiver was written
expires = "2026-10-15"     # or, instead of expires: task = "<the task that ends it>"
```

## What the tools do with it

- **The claimed level** is read from `level` unless one is given on the command line.
- **A current waiver** turns its rule's verdict into `waived`, carried into the report
  with the waiver's reason.
- **An expired waiver** turns its rule's verdict into `fail`, naming the date it expired.
  A waiver with neither `expires` nor `task`, or without a reason, owner or date, is
  refused: the checker reports it and exits non-zero.

## Waivers are evidence

A waiver says a project found a rule too costly, or wrong for its case. A rule that most
adopters waive is a rule to re-examine: its grade, its level, or whether it holds at all.
Waivers collected from audits therefore feed the process by which the specification
admits new evidence and revises its rules.
