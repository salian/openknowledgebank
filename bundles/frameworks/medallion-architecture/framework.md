---
type: Framework
title: Medallion Architecture Source-Aware Guide
description: Defines source-aware bronze, silver, and gold layer purpose, grain, schema, quality, lineage, batch or streaming, access, and consumption review, evidence handling, and action boundaries.
resource: https://docs.databricks.com/aws/en/lakehouse/medallion
okb_bundle_id: medallion-architecture
timestamp: '2026-08-01T00:00:00Z'
---
# Medallion Architecture Source-Aware Guide

Source-aware framework bundle for bronze, silver, and gold layer purpose, grain, schema, quality, lineage, batch or streaming, access, and consumption review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://docs.databricks.com/aws/en/lakehouse/medallion
- https://www.databricks.com/glossary/medallion-architecture

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- platform and runtime version, business use case, source contracts and ingestion mode, layer definitions and ownership, table names and grain, schema and evolution policy, quality rules and quarantine behavior, transformations, keys and deduplication, lineage, refresh and latency, access controls, cost, tests, consumers, approvals, and rollback

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer layer assignment, table or schema state, data quality, lineage, freshness, duplication, access, cost, or analytical readiness.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that create or alter tables, schemas, pipelines, quality rules, access controls, retention, or schedules; run workloads; read, write, or delete data; or publish datasets.
