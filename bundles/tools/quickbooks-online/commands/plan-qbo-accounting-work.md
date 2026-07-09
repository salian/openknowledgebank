---
type: Slash Command
command: /plan-qbo-accounting-work
title: Plan QuickBooks Online Accounting Work
description: "Create a source-scoped QuickBooks Online bookkeeping, reporting, reconciliation, or API plan without inventing company configuration."
okb_bundle_id: quickbooks-online
inputs:
  - accounting, bookkeeping, reporting, reconciliation, cleanup, or integration question
  - QuickBooks Online company evidence
  - report, list, transaction, API, sandbox, integration, or external-system context
  - risk and approval constraints
outputs:
  - QuickBooks Online readiness answer
  - required company evidence
  - proposed plan or change
  - reconciliation or query-shape self-check
  - validation and rollback checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-qbo-accounting-work

Purpose: produce a QuickBooks Online plan that is ready for human, accounting, administrator, and security/privacy review, not an unsafely executed production change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, accounting workflow, reporting issue, reconciliation discrepancy, API question, or desired QuickBooks Online change.
- QuickBooks Online company evidence, if available: company settings, screenshots, reports, exports, chart of accounts, products/services, customers, vendors, tax settings, classes, locations, bank-feed evidence, reconciliation reports, app/integration settings, permissions, API docs checked, or sandbox/test evidence.
- External-system context: ecommerce, payments, payroll, CRM, BI, inventory, expense, bank, or custom integration definitions.
- Approval, accounting, tax, payroll, security, privacy, deployment, rollback, and monitoring constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the work now.
2. Source note: official Intuit source categories, user-provided QuickBooks company evidence, and missing verification.
3. Verified facts: what is confirmed by Intuit sources or user-provided company evidence.
4. Missing evidence: company setup, report settings, accounting basis, chart/list/transaction evidence, permission, API, integration, tax, payroll, or policy inputs needed.
5. Plan: proposed bookkeeping/reporting/reconciliation/API work, with assumptions labeled.
6. Reconciliation or query-shape self-check: map requested dimensions, metrics, filters, source systems, entity identifiers, grain, date range, accounting basis, currency, and output rows to the proposed report/export/API query or explicitly defer unsupported pieces.
7. Risk and confirmation boundary: accounting impact, customer/vendor impact, tax/payroll/payment-adjacent impact, data export impact, integration impact, and actions requiring explicit approval.
8. Validation and rollback: sandbox/test plan, sample records, report comparison, owner, monitoring, rollback trigger, and rollback action.

## Confirmation Boundary

Do not send invoices or customer/vendor communications, export data, modify accounting records or settings, connect apps, change bank feeds, alter tax/payroll/payment-adjacent behavior, run production API calls, or change integrations without explicit user confirmation and authorized access.
