---
type: "Tool Guide"
title: "Sigma Computing"
description: "Source-aware guidance for Sigma Computing."
resource: "https://help.sigmacomputing.com/"
okb_bundle_id: sigma-computing
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Cloud warehouse analytics, spreadsheet, writeback, data-app, embedding, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect warehouses, query, export or embed data, change models or metrics, write data through input tables, trigger actions, grant permissions, enable AI or agents, send data to model providers, or represent query, metric, forecast, writeback, security, or business results"
---
# Sigma Computing Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.sigmacomputing.com/
- https://www.sigmacomputing.com/product

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Sigma analytics, writeback, and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect warehouses, query, export or embed data, change models or metrics, write data through input tables, trigger actions, grant permissions, enable AI or agents, send data to model providers, or represent query, metric, forecast, writeback, security, or business results.

## Guardrails

- Do not invent connection or feature applicability, schema, model relationship, metric definition, query correctness, data freshness, writeback or action result, permission, AI output, model-provider data flow, forecast, business conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
