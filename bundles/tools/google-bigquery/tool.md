---
type: Tool Guide
title: Google BigQuery
description: "Defines safe, source-aware use of Google BigQuery in OpenKnowledgeBank bundles."
tool_category: "Data warehouse and analytics platform"
okb_bundle_id: google-bigquery
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan a query from user-provided schema and source definitions.
  - Review a query plan for source scope, grain, filters, joins, validation, and cost preflight.
  - Explain BigQuery concepts using official documentation categories.
confirmation_required:
  - Run live queries.
  - Export data.
  - Create, update, overwrite, or delete datasets, tables, views, routines, connections, reservations, or permissions.
  - Analyze user-level, sensitive, regulated, or confidential data.
timestamp: "2026-07-08T00:00:00Z"
---

# Google BigQuery Tool Guide

BigQuery is a Google Cloud analytics platform. Google describes BigQuery's serverless infrastructure as letting users focus on data rather than resource management and as combining a cloud data warehouse with analytic tools.

## What This Bundle Is For

- Planning BigQuery analyses before writing or running SQL.
- Turning business questions into source-scoped query plans.
- Reviewing query cost, performance, validation, and safety risks.
- Supporting role bundles that use BigQuery, including analytics and marketing roles.

## What This Bundle Is Not

- A full GoogleSQL reference.
- A current pricing, quota, or edition reference.
- An IAM, governance, security, or compliance manual.
- A claim that the agent has access to a user's BigQuery environment.

## Source Discipline

Use exact BigQuery facts only when grounded in official documentation or user-provided local evidence. Treat the following as local evidence requirements:

- project, dataset, table, and column names;
- SQL text and query job metadata;
- partitioning and clustering configuration;
- billing model, reservation, slot, edition, and pricing context;
- permissions and data-sharing rules;
- source-of-record definitions and downstream BI/dashboard logic.

## BigQuery-Specific Guardrails

- Prefer GoogleSQL for new query plans unless the user provides a legacy-SQL constraint.
- Require a dry run or equivalent query estimate before live execution of potentially expensive queries.
- Avoid planning `SELECT *` for production analysis unless the user explicitly needs all columns and accepts the cost/performance tradeoff.
- Consider partition and cluster filters only when the table design and workload pattern support them.
- Require explicit confirmation before running, exporting, writing, deleting, sharing, or changing permissions.

## Source Note Template

```text
Source note: BigQuery guidance is based on official BigQuery documentation categories for SQL, cost/performance, and table design. Local evidence used: [schema/query/job/report provided by user]. Missing before final execution/conclusion: [dry run, table metadata, source-of-record definition, billing/pricing context, permission review].
```
