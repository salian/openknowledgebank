---
type: Bundle Index
title: Google BigQuery
description: "Tool bundle for source-aware BigQuery query planning, cost checks, performance review, and analytics warehouse work."
schema_version: 0.1.0
bundle_format: okf-compatible
category: tools
tags:
  - bigquery
  - google-cloud
  - data-warehouse
  - analytics
  - sql
aliases:
  - BigQuery
  - Google Cloud BigQuery
problems_solved:
  - Plan BigQuery analysis without inventing schemas or access.
  - Draft query plans with source scope, grain, filters, joins, and validation checks.
  - Add dry-run and cost preflight discipline before live queries.
  - Review partitioning, clustering, and projection choices at a source-aware level.
industries:
  - analytics
  - data
  - marketing
  - product
tools:
  - BigQuery
  - GoogleSQL
  - Google Cloud
frameworks:
  - verify-first query planning
  - cost and performance preflight
  - source-of-record reconciliation
deliverables:
  - BigQuery query plan
commands:
  - /plan-bigquery-query
skills: []
evaluations:
  - BigQuery query plan quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - ga4-analytics-specialist
adjacent_bundles:
  - performance-marketer
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete BigQuery schema, API, IAM, pricing, quota, or SQL syntax reference."
  - "Requires user-provided project, dataset, table, schema, SQL, job, billing, and permission evidence for final conclusions."
  - "Does not replace privacy, security, compliance, or data governance review."
safety_notes:
  - "Require confirmation before running live queries, exporting data, writing tables, changing permissions, or making billing/capacity changes."
  - "Do not claim access to BigQuery projects, datasets, tables, schemas, or jobs unless the user provides evidence or authorized tool access."
okb_bundle_id: google-bigquery
timestamp: "2026-07-08T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 22
  okb_score: 31
  absolute_lift: 9
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 11
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 9
      okb_score: 11
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 6
      okb_score: 9
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 22/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Google BigQuery

This bundle helps an agent use BigQuery as a source-aware analytics and data warehouse tool. It is designed for query planning, cost and performance review, and evidence-first analysis support across data, analytics, BI, marketing, and product roles.

It is a companion tool bundle, not a replacement for role bundles such as [GA4 Analytics Specialist](../../roles/ga4-analytics-specialist/index.md).

## Required Answer Habit

For source-sensitive BigQuery work, include a short **Source note** naming the official BigQuery source category, the user-provided local evidence used, and missing evidence required before running a query or treating a result as a conclusion.

## Start Here

- [tool.md](tool.md)
- [commands/plan-bigquery-query.md](commands/plan-bigquery-query.md)
- [workflows/plan-bigquery-analysis.md](workflows/plan-bigquery-analysis.md)
- [workflows/control-bigquery-cost.md](workflows/control-bigquery-cost.md)
- [deliverables/bigquery-query-plan.md](deliverables/bigquery-query-plan.md)
- [evaluations/bigquery-query-plan-quality-check.md](evaluations/bigquery-query-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use official BigQuery product documentation, SQL documentation, cost and performance best-practice documentation, pricing/quota pages, and user-provided local project evidence. Do not invent project IDs, dataset names, table names, fields, permissions, pricing, quotas, or query results.
