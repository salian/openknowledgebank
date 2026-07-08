---
type: Workflow
title: Plan BigQuery Analysis
description: "Translate a business question into a source-aware BigQuery analysis plan."
okb_bundle_id: google-bigquery
timestamp: "2026-07-08T00:00:00Z"
---

# Plan BigQuery Analysis

## Steps

1. State the decision the analysis should support.
2. Identify source tables and require schema evidence before naming fields as real.
3. Define grain, time range, timezone, filters, joins, entity identifiers, and metric logic.
4. Prefer GoogleSQL for new work unless the user provides a legacy-SQL constraint.
5. Check projection: name required columns instead of defaulting to broad scans.
6. Check partitioning and clustering evidence when scan reduction matters.
7. Require a dry run or job estimate before live execution.
8. Define validation against a trusted source of record or independent cross-check.
9. Separate verified facts, user-provided evidence, assumptions, and missing verification.

## Output

Use [BigQuery query plan](../deliverables/bigquery-query-plan.md).

## Source Note

Name official BigQuery documentation categories used for SQL, table design, cost/performance, and the user-provided local evidence used for actual table or field claims.
