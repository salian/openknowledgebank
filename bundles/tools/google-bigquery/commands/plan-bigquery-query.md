---
type: Slash Command
command: /plan-bigquery-query
title: Plan BigQuery Query
description: "Create a source-scoped BigQuery query plan without inventing schema, access, or costs."
okb_bundle_id: google-bigquery
inputs:
  - business question
  - source tables or schema evidence
  - time range and grain
  - filters, joins, and metric definitions
  - validation source
outputs:
  - BigQuery query plan
  - required local evidence
  - cost and performance preflight
  - validation checklist
requires_confirmation: true
timestamp: "2026-07-08T00:00:00Z"
---

# /plan-bigquery-query

Purpose: produce a BigQuery query plan that is ready for review, not an unsafely executed query.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question and decision to support.
- Project, dataset, table, and schema evidence, if available.
- Time range, timezone, grain, filters, joins, and entity identifiers.
- Metric definitions and source-of-record expectations.
- Existing SQL, dashboard/report definition, or job metadata, if reconciling.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to draft a query now.
2. Required local evidence: missing schema, source, permissions, cost, or business-definition inputs.
3. Query shape: source tables, selected columns, joins, filters, grouping grain, output rows, and assumptions.
4. Cost/performance preflight: dry-run requirement, projection check, partition/cluster filter check, and expensive-operation confirmation.
5. Validation plan: row-count, reconciliation, source-of-record, freshness, and edge-case checks.
6. Source note: official BigQuery source categories, user-provided evidence, and missing verification.

## Confirmation Boundary

Do not run a query, export data, write tables, change permissions, or modify capacity/billing settings without explicit user confirmation and authorized tool access.
