---
type: "Tool Guide"
title: "Odoo Accounting"
description: "Source-aware guidance for Odoo Accounting."
resource: "https://www.odoo.com/documentation/latest/applications/finance/accounting.html"
okb_bundle_id: odoo-accounting
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Accounting, invoicing, banking, tax, reconciliation, and reporting application"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create, post, reverse or reconcile accounting entries, connect banks, configure taxes or localizations, register payments, close periods, import data, change access, file or represent tax, financial, payment, or compliance state"
---
# Odoo Accounting Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.odoo.com/documentation/latest/applications/finance/accounting.html
- https://www.odoo.com/app/accounting

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Odoo Accounting configuration and close review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create, post, reverse or reconcile accounting entries, connect banks, configure taxes or localizations, register payments, close periods, import data, change access, file or represent tax, financial, payment, or compliance state.

## Guardrails

- Do not invent company or edition state, account mapping, invoice or bill validity, posting, reconciliation, bank balance, exchange rate, tax rule, localization applicability, asset schedule, close, report balance, filing, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
