---
type: "Tool Guide"
title: "Omni Analytics"
description: "Source-aware guidance for Omni Analytics."
resource: "https://docs.omni.co/"
okb_bundle_id: omni
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Governed semantic analytics, workbook, embedding, and AI-agent platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect warehouses, run or schedule queries, expose or embed data, change semantic models or metrics, merge branches, grant permissions, enable agents or MCP, send data to model providers, or represent query, metric, AI, security, or business results"
---
# Omni Analytics Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.omni.co/
- https://omni.co/platform

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Omni semantic model, analytics, and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect warehouses, run or schedule queries, expose or embed data, change semantic models or metrics, merge branches, grant permissions, enable agents or MCP, send data to model providers, or represent query, metric, AI, security, or business results.

## Guardrails

- Do not invent schema, model relationship, metric definition, permission, query correctness, data freshness, AI answer or summary, external-model data flow, branch or merge state, dashboard result, embed security, business conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
