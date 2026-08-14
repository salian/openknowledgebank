---
type: "Tool Guide"
title: "Oracle Sales"
description: "Source-aware guidance for Oracle Sales."
resource: "https://docs.oracle.com/en/cloud/saas/sales/"
okb_bundle_id: oracle-sales-cx
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise sales automation, CRM, forecasting, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or identify contacts, change leads, opportunities, stages, values, territories, quotas or forecasts, enable AI, send communications, call APIs, change access, or represent pipeline, forecast, incentive, or revenue"
---
# Oracle Sales Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.oracle.com/en/cloud/saas/sales/
- https://www.oracle.com/cx/sales/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Oracle Sales CRM and forecast review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or identify contacts, change leads, opportunities, stages, values, territories, quotas or forecasts, enable AI, send communications, call APIs, change access, or represent pipeline, forecast, incentive, or revenue.

## Guardrails

- Do not invent product naming or availability, contact identity, consent, lead qualification, opportunity stage or amount, forecast, territory, quota, AI recommendation, incentive, API result, revenue, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
