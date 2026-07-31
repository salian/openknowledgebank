---
type: Tool Guide
title: SAP Ariba
description: Defines source-aware SAP Ariba procurement configuration, approval, integration, and transaction review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a SAP Ariba change and approval brief with explicit evidence states.
confirmation_required:
- change configuration or master data, approve or deny, submit a requisition or invoice, create an order, onboard a supplier, export data, or commit spend
okb_bundle_id: sap-ariba
timestamp: '2026-07-31T00:00:00Z'
---
# SAP Ariba

Source-aware tool bundle for SAP Ariba procurement configuration, approval, integration, and transaction review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.sap.com/products/spend-management/ariba-procurement-solutions.html
- https://help.sap.com/docs/ARIBA_PROCUREMENT
- https://help.sap.com/docs/ARIBA_PROCUREMENT/095db213a1b34a17b7acc7d625c6e337/6b6f7934c1da1014a19da56f90b9aa77.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- tenant, enabled SAP Ariba products, release, realm, and environment
- user, group, role, permission, supplier, catalog, accounting, and master-data scope
- approvable type, document, lines, amounts, rules, approval flow, delegation, contracts, integration mappings, ERP source, audit history, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer approval path, document status, supplier state, budget availability, accounting validity, integration result, compliance, or transaction outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that change configuration or master data, approve or deny, submit a requisition or invoice, create an order, onboard a supplier, export data, or commit spend.
