---
type: Tool Guide
title: "Xero"
description: "Defines source-aware cloud accounting records and reporting, evidence handling, and action boundaries."
tool_category: "cloud accounting records and reporting"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review cloud accounting records and reporting from supplied evidence."
  - "Draft a xero accounting and reconciliation brief with explicit evidence states."
confirmation_required:
  - "posting or updating transactions, recording payments, reconciling bank items, changing tax or lock dates, changing scopes, or exporting financial data"
okb_bundle_id: xero
timestamp: "2026-07-31T00:00:00Z"
---

# Xero

Source-aware tool bundle for Xero organizations, ledgers, invoices, bills, payments, bank reconciliation, reports, tax settings, integrations, and controlled accounting actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- organization, tenant, region, and accounting period
- chart of accounts and tax rates
- contacts, invoices, bills, payments, bank transactions, and journals
- report definition, filters, and as-of date
- lock dates and approval workflow
- API connection and granted scopes

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer ledger accuracy, payment status, bank match, tax treatment, report completeness, and scope authorization.
- Require accountable confirmation before posting or updating transactions, recording payments, reconciling bank items, changing tax or lock dates, changing scopes, or exporting financial data.
