---
type: "Tool Guide"
title: "Hex"
description: "Source-aware guidance for Hex."
resource: "https://hex.tech/product/"
okb_bundle_id: hex
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Collaborative analytics notebook, data app, semantic, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or expose data, run code or queries, install packages, use secrets, change metrics, publish apps, schedule jobs, enable AI or MCP, make consequential decisions, or represent analytical results"
---
# Hex Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://hex.tech/product/
- https://learn.hex.tech/docs

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Hex documentation for the workspace, plan, connection, runtime, and AI feature.
- Project, version, connection, schema, query, code, package, secret, semantic model, parameter, schedule, app, permission, output, and log state.
- Data lineage, privacy and security review, reproducibility, reconciliation, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Hex analytical project and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or expose data, run code or queries, install packages, use secrets, change metrics, publish apps, schedule jobs, enable AI or MCP, make consequential decisions, or represent analytical results.

## Guardrails

- Do not invent source availability, schema, query or code execution, package safety, secret handling, metric definition, data freshness, AI accuracy, reproducibility, causal conclusion, business result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
