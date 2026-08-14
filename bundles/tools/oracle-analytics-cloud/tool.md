---
type: "Tool Guide"
title: "Oracle Analytics Cloud"
description: "Source-aware guidance for Oracle Analytics Cloud."
resource: "https://docs.oracle.com/en/cloud/paas/analytics-cloud/"
okb_bundle_id: oracle-analytics-cloud
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Cloud analytics, semantic modeling, visualization, reporting, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect production data, run queries, change models or metrics, train models, enable AI, share or embed content, grant access, schedule exports, migrate catalogs, or represent query, forecast, security, or business results"
---
# Oracle Analytics Cloud Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.oracle.com/en/cloud/paas/analytics-cloud/
- https://www.oracle.com/business-analytics/analytics-cloud.html

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Oracle Analytics Cloud model, insight, and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect production data, run queries, change models or metrics, train models, enable AI, share or embed content, grant access, schedule exports, migrate catalogs, or represent query, forecast, security, or business results.

## Guardrails

- Do not invent service version, schema, metric definition, query correctness, data freshness, model accuracy, AI output, permission, row-level security, report result, forecast, migration completeness, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
