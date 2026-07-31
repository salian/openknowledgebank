---
type: Tool Guide
title: "Databricks"
description: "Defines source-aware lakehouse data and analytics operations, evidence handling, and action boundaries."
tool_category: "lakehouse data and analytics operations"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review lakehouse data and analytics operations from supplied evidence."
  - "Draft a databricks workspace and governance brief with explicit evidence states."
confirmation_required:
  - "running jobs or SQL, creating or changing data or compute, changing grants or policies, handling secrets, or deleting resources"
okb_bundle_id: databricks
timestamp: "2026-07-31T00:00:00Z"
---

# Databricks

Source-aware tool bundle for Databricks workspaces, compute, notebooks, jobs, SQL, Unity Catalog, lineage, quality, and controlled data-platform changes.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- cloud, region, workspace, and runtime
- catalog, schema, table, and volume scope
- compute, warehouse, job, notebook, and query state
- Unity Catalog grants and policies
- lineage and data-quality evidence
- run history, usage, and cost definitions

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer data contents, lineage completeness, grant effectiveness, compute state, job outcome, and cost attribution.
- Require accountable confirmation before running jobs or SQL, creating or changing data or compute, changing grants or policies, handling secrets, or deleting resources.
