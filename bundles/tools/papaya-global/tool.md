---
type: "Tool Guide"
title: "Papaya Global"
description: "Source-aware guidance for Papaya Global."
resource: "https://www.papayaglobal.com/platform/"
okb_bundle_id: papaya-global
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Global payroll, employer-of-record, workforce payment, and compliance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "onboard or classify workers, change employment or payroll data, calculate or fund payroll, initiate payments, manage benefits, upload identity or bank data, approve invoices, or make employment, tax, eligibility, payment, or compliance decisions"
---
# Papaya Global Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.papayaglobal.com/platform/
- https://support.papayaglobal.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Papaya Global payroll and workforce-payment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before onboard or classify workers, change employment or payroll data, calculate or fund payroll, initiate payments, manage benefits, upload identity or bank data, approve invoices, or make employment, tax, eligibility, payment, or compliance decisions.

## Guardrails

- Do not invent worker identity or classification, employment status, compensation, benefit eligibility, payroll calculation, tax treatment, invoice, funding, payment, exchange rate, country compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
