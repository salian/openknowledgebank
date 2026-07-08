---
type: Workflow
title: Reconcile GAAP and Non-GAAP Measures
description: "Workflow for comparing GAAP and non-GAAP financial measures without assuming either number is automatically correct."
tags:
  - non-gaap
  - sec-reporting
  - reconciliation
okb_bundle_id: us-gaap
resource: https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-8
timestamp: "2026-07-09T00:00:00Z"
---

# Reconcile GAAP and Non-GAAP Measures

Use this workflow when the user asks which number is right, why adjusted EBITDA differs from net income, whether a metric is non-GAAP, or how to review a reconciliation.

## Inputs

- Exact GAAP measure and source statement or filing location.
- Exact non-GAAP measure label, calculation, period, and presentation context.
- Most directly comparable GAAP measure, if applicable.
- Reconciliation schedule and adjustment definitions.
- Whether the entity is an SEC registrant and where the measure appears.

## Reconciliation Pattern

Neither number is automatically right until definitions, source, period, scope, and calculation method are aligned. The answer should:

- Define what each measure actually includes and excludes.
- Identify the source of each value.
- Align reporting period, entity scope, currency, segment, continuing/discontinued operations, and per-share or total presentation.
- Identify each adjustment, its direction, and whether it is recurring, cash/noncash, or management-defined.
- Separate expected differences from unresolved discrepancies.

## SEC Registrant Source Check

For SEC registrant contexts, use SEC non-GAAP source categories and ask for the exact disclosure, comparable GAAP measure, and reconciliation. Do not declare compliance without qualified review.

## Output Contract

Include:

- **Source note:** FASB/SEC source categories used, user-provided disclosure evidence, and missing sources.
- **Direct answer:** whether the difference is explained, partially explained, or unresolved.
- **Measure definitions:** GAAP and non-GAAP labels, periods, and source locations.
- **Reconciliation table:** adjustment label, direction, amount, source, and verification status.
- **Expected differences:** adjustments that explain the variance.
- **Unresolved discrepancies:** missing or inconsistent items.
- **Review trigger:** filing, investor, lender, board, or regulator-facing uses require qualified review.
