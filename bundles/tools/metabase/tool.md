---
type: "Tool Guide"
title: "Metabase"
description: "Source-aware guidance for Metabase."
resource: "https://www.metabase.com/docs/latest/"
okb_bundle_id: metabase
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source business intelligence, semantic, dashboard, and embedding platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect production databases, run queries, expose or export data, publish embeds, change metadata, models, metrics or permissions, deploy upgrades, restore backups, or represent metric, query, security, or availability state"
---
# Metabase Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.metabase.com/docs/latest/
- https://www.metabase.com/product/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Metabase analytics, governance, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect production databases, run queries, expose or export data, publish embeds, change metadata, models, metrics or permissions, deploy upgrades, restore backups, or represent metric, query, security, or availability state.

## Guardrails

- Do not invent schema, field semantics, query correctness, metric definition, row or column security, data freshness, dashboard result, export completeness, embed access, backup validity, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
