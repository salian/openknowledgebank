---
type: Tool Guide
title: QuickBooks Online
description: "Defines safe, source-aware use of QuickBooks Online in OpenKnowledgeBank bundles."
tool_category: "Accounting, bookkeeping, and finance operations software"
okb_bundle_id: quickbooks-online
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan QuickBooks Online bookkeeping, reporting, reconciliation, or API work from user-provided evidence.
  - Review proposed QuickBooks Online changes for source scope, accounting impact, validation, approval, and rollback.
  - Explain QuickBooks Online concepts using official Intuit documentation categories.
confirmation_required:
  - Send invoices, estimates, reminders, receipts, or customer/vendor communications.
  - Export, create, update, delete, void, merge, or bulk-modify QuickBooks Online accounting data.
  - Change accounts, products/services, customers, vendors, classes, locations, tax settings, payroll/payment-adjacent settings, bank feeds, permissions, apps, integrations, webhooks, or API behavior.
  - Run production API calls or access sensitive financial, customer, vendor, employee, payroll, tax, or bank-feed data.
timestamp: "2026-07-09T00:00:00Z"
---

# QuickBooks Online Tool Guide

QuickBooks Online is a cloud accounting platform for bookkeeping, invoicing, bills, customers, vendors, accounts, reporting, and integrations. Official source categories include Intuit QuickBooks Online documentation for product behavior and Intuit Developer documentation for Accounting API behavior.

## What This Bundle Is For

- Planning QuickBooks Online bookkeeping, reporting, reconciliation, data cleanup, integration, API, or administrator-review work.
- Turning accounting-system questions into source-scoped evidence requests.
- Reviewing planned changes before they affect books, reports, taxes, customers, vendors, payments-adjacent flows, integrations, or production data.
- Supporting role bundles that work with accounting, finance operations, AP/AR, bookkeeping, tax preparation, nonprofit administration, ecommerce operations, payroll coordination, or SMB operations.

## What This Bundle Is Not

- A complete QuickBooks Online implementation, migration, data model, API schema, pricing, packaging, SKU, tax, payroll, payments, or marketplace reference.
- A substitute for a qualified bookkeeper, accountant, controller, tax professional, auditor, QuickBooks administrator, security/privacy reviewer, or Intuit Developer implementation review.
- A claim that the agent has access to the user's QuickBooks Online company, bank feed, Intuit Developer app, API credentials, or reports.

## Source Discipline

Use exact QuickBooks Online facts only when grounded in official Intuit documentation or user-provided company evidence. Treat the following as local evidence requirements:

- company, region, plan/SKU, enabled features, accounting basis, fiscal year, closing date, currency, and permissions;
- chart of accounts, classes, locations, products/services, customers, vendors, employees, tax agencies/codes, custom fields, attachments, and list state;
- report type, date range, accounting basis, filters, grouping, comparison periods, timezone, refresh timing, and export method;
- bank-feed, reconciliation, payment, payroll, sales-tax, app, automation, webhook, and integration configuration;
- API app, OAuth scope, realm/company ID context, sandbox/production environment, entity, operation, endpoint, field, payload, pagination, rate-limit, minor-version, and test evidence.

## QuickBooks Online Guardrails

- Treat official Intuit docs as source categories, not proof of a user's company configuration.
- Verify the user's company evidence before recommending account names, tax treatment, report filters, API payloads, permissions, sync behavior, or accounting entries.
- Separate sandbox or test evidence from production company evidence.
- Explain when a recommendation is a design hypothesis rather than a source-confirmed implementation step.
- Require explicit confirmation before live accounting changes, customer/vendor communications, data exports, app connections, bank-feed changes, API calls, tax/payroll/payment-adjacent changes, or production integrations.

## Source Note Template

```text
Source note: QuickBooks Online guidance is based on official Intuit source categories for [QuickBooks Online product docs / Intuit Developer QBO Accounting API docs / API Explorer / sandbox docs / webhook docs / query docs]. Local evidence used: [company settings, reports, exports, screenshots, chart of accounts, lists, app settings, sandbox test, or authorized read-only access provided by user]. Missing before action or conclusion: [current doc/API Explorer check, company evidence, report settings, sandbox test, approval, rollback, accounting/tax/security/privacy review].
```
