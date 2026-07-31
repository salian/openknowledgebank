---
type: Workflow
title: "Databricks source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: cloud, region, workspace, and runtime, catalog, schema, table, and volume scope, compute, warehouse, job, notebook, and query state, Unity Catalog grants and policies, lineage and data-quality evidence, and run history, usage, and cost definitions.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable databricks workspace and governance brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification` when no reviewer evidence is provided, and prohibited unapproved actions
- **Source note** with sources and limitations
