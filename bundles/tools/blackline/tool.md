---
type: "Tool Guide"
title: "BlackLine"
description: "Source-aware guidance for BlackLine."
resource: "https://www.blackline.com/products/financial-close/account-reconciliations/"
okb_bundle_id: blackline
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Financial close and accounting operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import balances, configure rules, prepare or certify reconciliations, post or approve journals, close tasks or periods, change roles, resolve exceptions, or represent financial assurance"
---
# BlackLine Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.blackline.com/products/financial-close/account-reconciliations/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable BlackLine configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import balances, configure rules, prepare or certify reconciliations, post or approve journals, close tasks or periods, change roles, resolve exceptions, or represent financial assurance.

## Guardrails

- Do not invent balance or transaction accuracy, account ownership, rule validity, reconciliation completeness, exception resolution, journal support, close status, audit assurance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
