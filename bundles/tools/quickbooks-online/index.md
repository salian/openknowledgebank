---
type: Bundle Index
title: QuickBooks Online
description: "Tool bundle for source-aware QuickBooks Online accounting, bookkeeping, reporting, reconciliation, and API planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - quickbooks-online
  - quickbooks
  - qbo
  - accounting
  - bookkeeping
  - finance-operations
  - smb-finance
aliases:
  - QuickBooks
  - QBO
  - Intuit QuickBooks Online
problems_solved:
  - Plan QuickBooks Online bookkeeping, reporting, reconciliation, or integration work without inventing company configuration.
  - Separate official Intuit product/API behavior from user-provided QuickBooks company evidence and assumptions.
  - Reconcile QuickBooks Online reports, exports, API data, and external-system totals with explicit source, basis, filter, timing, and entity checks.
  - Produce QuickBooks Online work plans that include source notes, validation checks, confirmation boundaries, and rollback before live accounting changes.
industries:
  - accounting
  - bookkeeping
  - smb-finance
  - ecommerce
  - professional-services
  - nonprofit
tools:
  - QuickBooks Online
  - Intuit Developer
  - QuickBooks Online Accounting API
  - QuickBooks Online API Explorer
frameworks:
  - inspect-first accounting system planning
  - source-of-record reconciliation
  - sandbox-before-production integration review
deliverables:
  - QuickBooks Online work plan
commands:
  - /plan-qbo-accounting-work
skills: []
evaluations:
  - QuickBooks Online plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: []
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete QuickBooks Online implementation, migration, data model, API schema, pricing, packaging, SKU, accounting, payroll, payments, sales-tax, or tax-advice reference."
  - "Requires user-provided QuickBooks company evidence before final conclusions about chart of accounts, classes, locations, products/services, customers, vendors, tax setup, bank feeds, permissions, reports, automations, apps, integrations, or API behavior."
  - "Does not replace a qualified bookkeeper, accountant, controller, tax professional, auditor, QuickBooks administrator, security/privacy reviewer, or Intuit Developer implementation review."
safety_notes:
  - "Require explicit confirmation before sending invoices or customer/vendor communications, exporting accounting data, modifying transactions/accounts/customers/vendors/items/settings, connecting apps, changing bank feeds, running production API calls, or changing tax/payroll/payment-adjacent behavior."
  - "Do not request credentials, client secrets, refresh tokens, bank credentials, or claim QuickBooks company access unless the user provides authorized tool access or evidence."
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric
  tasks_count: 0
  display_summary: "Measured evaluation is blocked until an approved QuickBooks Online task set, model/provider run, and reviewer scoring pass are available."
  evidence_note: "No raw prompts or outputs are included in the public bundle."
okb_bundle_id: quickbooks-online
timestamp: "2026-07-09T00:00:00Z"
---

# QuickBooks Online

This bundle helps an agent use QuickBooks Online as a source-aware accounting, bookkeeping, reporting, reconciliation, and integration platform. It is designed for planning and reviewing QuickBooks Online work, not for silently changing a user's books or substituting for accounting, tax, payroll, audit, or legal review.

It is a companion tool bundle for bookkeeper, accountant, controller, accounts payable/receivable, SMB operator, ecommerce, nonprofit, payroll, tax, and finance operations bundles.

## Required Answer Habit

For source-sensitive QuickBooks Online work, include a short **Source note** naming the official Intuit source category, the user-provided QuickBooks company evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-qbo-accounting-work.md](commands/plan-qbo-accounting-work.md)
- [workflows/reconcile-qbo-report-or-api-data.md](workflows/reconcile-qbo-report-or-api-data.md)
- [workflows/plan-qbo-integration.md](workflows/plan-qbo-integration.md)
- [deliverables/qbo-work-plan.md](deliverables/qbo-work-plan.md)
- [evaluations/qbo-plan-quality-check.md](evaluations/qbo-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Intuit QuickBooks Online product documentation, Intuit Developer QuickBooks Online Accounting API documentation, the QuickBooks Online API Explorer, sandbox/test evidence, and user-provided QuickBooks company evidence. Do not invent chart-of-accounts names, report settings, tax codes, products/services, customers, vendors, API fields, endpoints, supported operations, rate limits, permissions, or integration behavior.
