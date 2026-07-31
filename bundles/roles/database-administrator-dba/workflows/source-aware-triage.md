---
type: Workflow
title: Database Administrator (DBA) source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: database purpose, owners, environments, engine, version, topology, and dependencies; schemas, data classification, volume, workload, queries, indexes, and statistics; identities, roles, privileges, encryption, keys, audit, and network controls; backups, retention, restore tests, replication, recovery objectives, and incidents; change plan, migration, capacity, monitoring, maintenance, rollback, and approvals.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable database change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification`, and prohibited actions
- **Source note** with sources and limitations
