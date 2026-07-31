---
type: Tool Guide
title: "Snowflake"
description: "Defines source-aware cloud data platform analysis and administration, evidence handling, and action boundaries."
tool_category: "Data warehouse and business intelligence / analytics platforms"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review cloud data platform analysis and administration from supplied evidence."
  - "Draft a snowflake analysis and change brief with explicit evidence states."
confirmation_required:
  - "running state-changing SQL, changing objects, warehouses, roles, grants, policies, integrations, shares, or production data"
okb_bundle_id: snowflake
timestamp: "2026-07-31T00:00:00Z"
---

# Snowflake

Source-aware tool bundle for Snowflake data, SQL, warehouse, access, performance, cost, governance, and review-ready analysis or change briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- account, region, edition, and version context
- database, schema, object, and ownership metadata
- warehouse and resource-monitor configuration
- roles, grants, policies, and data classification
- SQL text, parameters, query profile, and history
- freshness, lineage, quality, and source-of-record checks
- cost, change, and approval evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before running state-changing SQL, changing objects, warehouses, roles, grants, policies, integrations, shares, or production data.
