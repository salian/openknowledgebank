---
type: "Tool Guide"
title: "Wave"
description: "Source-aware guidance for Wave."
resource: "https://support.waveapps.com/hc/en-us"
okb_bundle_id: wave
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Small-business accounting, invoicing, payments, banking, receipts, payroll, and reporting platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "post or alter transactions, invoices, payroll or tax data, connect banks, reconcile accounts, initiate or refund payments, expose API credentials, or represent balances, tax, payroll, payment, profit, compliance, or audit conclusions"
---
# Wave Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.waveapps.com/hc/en-us
- https://developer.waveapps.com/hc/en-us

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Wave accounting, invoicing, and payment control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before post or alter transactions, invoices, payroll or tax data, connect banks, reconcile accounts, initiate or refund payments, expose API credentials, or represent balances, tax, payroll, payment, profit, compliance, or audit conclusions.

## Guardrails

- Do not invent country or feature availability, account or ledger state, transaction classification, balance, tax treatment, payroll, invoice delivery, payment or refund, reconciliation, profit, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
