---
type: Evaluation
title: QuickBooks Online Plan Quality Check
description: "Rubric for source-aware QuickBooks Online planning outputs."
okb_bundle_id: quickbooks-online
task_type: "planning-rubric"
criteria:
  - source discipline
  - company evidence handling
  - reconciliation/query-shape completeness
  - safety and confirmation boundary
  - validation and rollback
timestamp: "2026-07-09T00:00:00Z"
---

# QuickBooks Online Plan Quality Check

Score an output against these criteria:

| Criterion | Pass Standard |
| --- | --- |
| Source discipline | Includes a source note naming Intuit source categories, user-provided company evidence, and missing verification. |
| Company evidence handling | Does not invent company settings, accounts, lists, report filters, tax codes, permissions, integrations, or API schema. |
| Reconciliation/query shape | Aligns source scope, accounting basis, date range, filters, entity identifiers, grain, aggregation, currency, timing, and output rows. |
| Safety boundary | Requires explicit confirmation for live accounting, communications, exports, API, app, bank-feed, tax/payroll/payment-adjacent, or integration actions. |
| Validation and rollback | Provides sandbox/test/sample-record checks, report comparison, monitoring, rollback trigger, rollback action, and owner. |
| Professional review | Flags accounting, tax, payroll, audit, legal, privacy, security, or administrator review when reliance or risk requires it. |

Fail the output if it claims account access without evidence, gives production API payloads or accounting entries as final without source/company verification, or recommends live changes without explicit confirmation.
