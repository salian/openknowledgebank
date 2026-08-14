---
type: "Tool Guide"
title: "SAP Business One"
description: "Source-aware guidance for SAP Business One."
resource: "https://www.sap.com/products/erp/business-one.html"
okb_bundle_id: sap-business-one
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Small and midsize business ERP, financial, inventory, production, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create, post or reverse transactions, change master data, inventory, pricing, tax or authorizations, approve purchases or payments, run MRP, deploy add-ons, call APIs, migrate or upgrade systems, or represent financial, inventory, tax, production, or compliance state"
---
# SAP Business One Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.sap.com/products/erp/business-one.html
- https://help.sap.com/docs/SAP_BUSINESS_ONE

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SAP Business One ERP and control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create, post or reverse transactions, change master data, inventory, pricing, tax or authorizations, approve purchases or payments, run MRP, deploy add-ons, call APIs, migrate or upgrade systems, or represent financial, inventory, tax, production, or compliance state.

## Guardrails

- Do not invent version, database or localization applicability, company state, account mapping, posting, balance, tax treatment, inventory, costing, MRP, approval, API result, backup, migration, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
