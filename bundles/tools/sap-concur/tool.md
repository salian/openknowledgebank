---
type: "Tool Guide"
title: "SAP Concur"
description: "Source-aware guidance for SAP Concur."
resource: "https://developer.concur.com/api-reference/"
okb_bundle_id: sap-concur
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Travel, expense, invoice, request, payment, and developer platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change traveler, card, expense, receipt, invoice or itinerary data, approve expenses or payments, book travel, change policies, connect systems, expose OAuth credentials, or represent expense, tax, travel, payment, audit, or compliance state"
---
# SAP Concur Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.concur.com/api-reference/
- https://www.concur.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SAP Concur travel, expense, and API control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change traveler, card, expense, receipt, invoice or itinerary data, approve expenses or payments, book travel, change policies, connect systems, expose OAuth credentials, or represent expense, tax, travel, payment, audit, or compliance state.

## Guardrails

- Do not invent person identity, card ownership, receipt or expense validity, policy applicability, travel booking, invoice, approval, tax treatment, payment, reimbursement, audit conclusion, API result, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
