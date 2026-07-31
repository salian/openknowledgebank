---
type: Tool Guide
title: Apache Airflow
description: Defines source-aware Apache Airflow DAG design, scheduling, credentials, testing, deployment, and operations, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Airflow workflow change brief with explicit evidence states.
confirmation_required:
- deploy DAG code, create or expose a connection, unpause or trigger a DAG, backfill, clear tasks, alter pools, or move production data
okb_bundle_id: apache-airflow
timestamp: '2026-07-31T00:00:00Z'
---
# Apache Airflow

Source-aware tool bundle for Apache Airflow DAG design, scheduling, credentials, testing, deployment, and operations, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://airflow.apache.org/
- https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
- https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Airflow and provider versions, deployment, executor, scheduler, workers, and environment
- DAG code, owners, tasks, dependencies, schedule, timezone, data interval, catchup, retries, pools, concurrency, callbacks, assets, connections, variables, secrets backend, permissions, tests, run history, logs, data contracts, rollback, and approval

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer DAG parse state, schedule behavior, credential validity, task outcome, data completeness, backfill impact, production state, or incident cause.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that deploy DAG code, create or expose a connection, unpause or trigger a DAG, backfill, clear tasks, alter pools, or move production data.
