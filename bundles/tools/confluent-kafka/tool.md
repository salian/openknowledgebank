---
type: "Tool Guide"
title: "Confluent"
description: "Source-aware guidance for Confluent."
resource: "https://docs.confluent.io/"
okb_bundle_id: confluent-kafka
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Data streaming platform based on Apache Kafka"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "provision clusters, create or alter topics or schemas, ingest, consume or export data, deploy connectors or Flink jobs, change ACLs, networking or retention, delete data, or represent delivery or recovery"
---
# Confluent Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.confluent.io/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Confluent configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before provision clusters, create or alter topics or schemas, ingest, consume or export data, deploy connectors or Flink jobs, change ACLs, networking or retention, delete data, or represent delivery or recovery.

## Guardrails

- Do not invent deployment applicability, message contents or ordering, schema compatibility, producer or consumer state, connector safety, permission, delivery semantics, lineage, cost, recovery, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
