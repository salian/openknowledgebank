---
type: "Tool Guide"
title: "ThoughtSpot"
description: "Source-aware guidance for ThoughtSpot."
resource: "https://docs.thoughtspot.com/"
okb_bundle_id: thoughtspot
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Search and AI analytics, semantic modeling, Liveboard, embedded, action, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or expose data, change models or metrics, publish or embed analytics, enable AI, trigger actions, grant access, call APIs, or represent query, metric, forecast, anomaly, permission, AI output, or business results"
---
# ThoughtSpot Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.thoughtspot.com/
- https://www.thoughtspot.com/product

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable ThoughtSpot analytics, AI, and embedding governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or expose data, change models or metrics, publish or embed analytics, enable AI, trigger actions, grant access, call APIs, or represent query, metric, forecast, anomaly, permission, AI output, or business results.

## Guardrails

- Do not invent edition or release applicability, schema, model, metric definition, query correctness, data freshness, permission, AI output, action or API result, forecast, anomaly, or business conclusion.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
