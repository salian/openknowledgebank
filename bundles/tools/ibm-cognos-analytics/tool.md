---
type: "Tool Guide"
title: "IBM Cognos Analytics"
description: "Source-aware guidance for IBM Cognos Analytics."
resource: "https://www.ibm.com/products/cognos-analytics"
okb_bundle_id: ibm-cognos-analytics
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Governed business intelligence, reporting, dashboard, forecasting, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or expose data, change models or metrics, generate or distribute reports, publish dashboards, run forecasts or agents, change access, make consequential decisions, or represent compliance or business results"
---
# IBM Cognos Analytics Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.ibm.com/products/cognos-analytics

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current IBM Cognos documentation for the deployed offering, version, capabilities, and data sources.
- Deployment, namespace, connection, package or module, certified model, field, metric, filter, forecast, report, dashboard, agent, schedule, permission, and audit state.
- Data lineage, governance, financial or regulatory review, reconciliation, validation, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable IBM Cognos Analytics governed reporting review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or expose data, change models or metrics, generate or distribute reports, publish dashboards, run forecasts or agents, change access, make consequential decisions, or represent compliance or business results.

## Guardrails

- Do not invent source availability, lineage, certification, model or metric definition, filter context, data freshness, forecast accuracy, AI or agent result, report distribution, governance, compliance, business conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
