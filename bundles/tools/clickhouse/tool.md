---
type: "Tool Guide"
title: "ClickHouse"
description: "Source-aware guidance for ClickHouse."
resource: "https://clickhouse.com/docs/"
okb_bundle_id: clickhouse
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Column-oriented analytical database"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "provision or resize resources, create or alter schemas, ingest, query, export or delete data, change grants or networking, run migrations, restore backups, or represent performance or recovery"
---
# ClickHouse Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://clickhouse.com/docs/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable ClickHouse configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before provision or resize resources, create or alter schemas, ingest, query, export or delete data, change grants or networking, run migrations, restore backups, or represent performance or recovery.

## Guardrails

- Do not invent data contents or quality, schema compatibility, query safety, permission, replication state, cost, benchmark result, backup integrity, restore or migration outcome, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
