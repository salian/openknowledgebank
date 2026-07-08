---
type: Evaluation
title: BigQuery Query Plan Quality Check
description: "Rubric for reviewing whether a BigQuery query plan is source-aware and execution-safe."
okb_bundle_id: google-bigquery
task_type: query-planning
criteria:
  - source scope
  - schema discipline
  - query shape
  - cost preflight
  - validation plan
  - safety boundary
timestamp: "2026-07-08T00:00:00Z"
---

# BigQuery Query Plan Quality Check

Score each criterion 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Source scope | Invents or omits sources | Names some sources | Defines included/excluded records, freshness, and source of record |
| Schema discipline | Invents fields/tables | Notes some missing evidence | Requires schema/user evidence before exact SQL |
| Query shape | Vague query idea | Partial dimensions/filters | Maps fields, joins, grain, filters, and output rows |
| Cost preflight | No cost check | Mentions cost generally | Requires dry run, projection, and partition/cluster checks |
| Validation plan | No validation | Generic QA | Includes totals, samples, reconciliation, and edge cases |
| Safety boundary | Suggests live action without confirmation | Some caution | Requires confirmation for live queries, exports, writes, permissions, and sensitive data |
