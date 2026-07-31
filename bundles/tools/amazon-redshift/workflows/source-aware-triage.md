---
type: Workflow
title: Amazon Redshift source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: AWS account, region, cluster or serverless namespace, engine and client versions; database, schema, table, view, owner, data contracts, lineage, load and transformation logic; IAM, database roles, network, encryption, secrets, workload management, SQL, query plans, statistics, monitoring, audit logs, snapshots, recovery tests, costs, and approvals.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Amazon Redshift change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
