---
type: Workflow
title: Medallion Architecture Source-Aware Triage
okb_bundle_id: medallion-architecture
---
# Medallion Architecture Source-Aware Triage

1. State the decision and direct answer possible now.
2. Record Verified, Provided, Assumed, and Needs verification separately.
3. Inspect current sources and exact local evidence for platform and runtime version, business use case, source contracts and ingestion mode, layer definitions and ownership, table names and grain, schema and evolution policy, quality rules and quarantine behavior, transformations, keys and deduplication, lineage, refresh and latency, access controls, cost, tests, consumers, approvals, and rollback.
4. Reconcile definitions, identifiers, dates, scope, permissions, processing, and ownership.
5. Record alternatives, stop conditions, and an independent cross-check.
6. Require explicit approval before actions that create or alter tables, schemas, pipelines, quality rules, access controls, retention, or schedules; run workloads; read, write, or delete data; or publish datasets.
7. End with a Source Note naming URLs, user evidence, and missing sources.
