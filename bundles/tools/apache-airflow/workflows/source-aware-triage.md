---
type: Workflow
title: Apache Airflow source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: Airflow and provider versions, deployment, executor, scheduler, workers, and environment; DAG code, owners, tasks, dependencies, schedule, timezone, data interval, catchup, retries, pools, concurrency, callbacks, assets, connections, variables, secrets backend, permissions, tests, run history, logs, data contracts, rollback, and approval.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Airflow workflow change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
