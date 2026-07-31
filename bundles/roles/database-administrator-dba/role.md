---
type: Role
title: Database Administrator (DBA) Source-Aware Guide
description: Defines source-aware database administration and reliability, evidence handling, and action boundaries.
tags:
- database-administrator-dba
- database
- role
resource: https://www.onetonline.org/link/summary/15-1242.00
okb_bundle_id: database-administrator-dba
timestamp: '2026-07-31T00:00:00Z'
---
# Database Administrator (DBA) Source-Aware Guide

Source-aware role bundle for database administration and reliability, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- database purpose, owners, environments, engine, version, topology, and dependencies
- schemas, data classification, volume, workload, queries, indexes, and statistics
- identities, roles, privileges, encryption, keys, audit, and network controls
- backups, retention, restore tests, replication, recovery objectives, and incidents
- change plan, migration, capacity, monitoring, maintenance, rollback, and approvals

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Do not infer schema meaning, privilege, backup validity, recoverability, performance cause, replication state, capacity, or production health.
- Do not invent an artifact owner, author, date, or version.
- Require accountable confirmation before querying or exporting sensitive data, changing schemas or privileges, restoring backups, failing over, or modifying production.
