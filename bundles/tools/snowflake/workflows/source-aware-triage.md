---
type: Workflow
title: "Snowflake source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: account, region, edition, and version context, database, schema, object, and ownership metadata, warehouse and resource-monitor configuration, roles, grants, policies, and data classification, SQL text, parameters, query profile, and history, freshness, lineage, quality, and source-of-record checks, and cost, change, and approval evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, and owners.
5. Produce the smallest reviewable snowflake analysis and change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations
