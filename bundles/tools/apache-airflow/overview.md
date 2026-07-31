---
type: Overview
title: Apache Airflow overview
---
# Apache Airflow Overview

Use this bundle to prepare source-aware Apache Airflow DAG design, scheduling, credentials, testing, deployment, and operations and a review-ready Airflow workflow change brief.

## Operating Principle

Start with the decision and evidence, not a presumed answer. Use current authoritative sources for general behavior and authorized artifacts for local facts. Keep missing evidence visible, reconcile conflicts, and stop before consequential action without accountable approval.

## Scope

- Required evidence: Airflow and provider versions, deployment, executor, scheduler, workers, and environment; DAG code, owners, tasks, dependencies, schedule, timezone, data interval, catchup, retries, pools, concurrency, callbacks, assets, connections, variables, secrets backend, permissions, tests, run history, logs, data contracts, rollback, and approval.
- Unknowns: do not infer DAG parse state, schedule behavior, credential validity, task outcome, data completeness, backfill impact, production state, or incident cause.
- Action boundary: require confirmation before actions that deploy DAG code, create or expose a connection, unpause or trigger a DAG, backfill, clear tasks, alter pools, or move production data.
