---
type: Workflow
title: Control BigQuery Cost
description: "Review a BigQuery query plan for avoidable scan, cost, and execution risk before live use."
okb_bundle_id: google-bigquery
timestamp: "2026-07-08T00:00:00Z"
---

# Control BigQuery Cost

## Checks

- Projection: does the query select only needed columns?
- Scope: does the query restrict time, entity, and source records intentionally?
- Partition pruning: if a partitioned table is involved, does the filter qualify on the partitioning column?
- Cluster pruning: if a clustered table is involved, do filters align with clustering columns?
- Dry run: has the query been validated and estimated before execution?
- Pricing context: are current pricing, edition, reservation, slot, and billing assumptions verified from official docs and local account context?
- Confirmation: has the user explicitly approved live execution, exports, writes, or capacity/billing changes?

## Do Not Claim

- Do not quote exact cost, quota, or pricing values unless official current docs and account context are inspected.
- Do not guarantee cost savings from partitioning or clustering without the table design and workload pattern.
- Do not treat bytes processed as the whole business risk; privacy, permissions, and data movement also matter.
