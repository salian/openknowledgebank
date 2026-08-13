---
type: "Tool Guide"
title: "GoodData"
description: "Source-aware guidance for GoodData."
resource: "https://www.gooddata.com/docs/cloud/"
okb_bundle_id: gooddata
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Governed semantic analytics and embedded business intelligence platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or expose data, change models or metrics, publish dashboards, embed analytics, schedule exports, change access, or represent analytical or business results"
---
# GoodData Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.gooddata.com/docs/cloud/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current GoodData documentation for the deployment, API, SDK, and edition.
- Workspace, data source, model, metric definition, filter, permission, embedding, schedule, and log state.
- Data lineage, reconciliation, privacy review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable GoodData semantic analytics review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or expose data, change models or metrics, publish dashboards, embed analytics, schedule exports, change access, or represent analytical or business results.

## Guardrails

- Do not invent schema, lineage, metric definition, filter context, data freshness, access, dashboard state, calculation accuracy, forecast, business conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
