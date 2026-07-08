---
type: Reference
title: BigQuery Source Checks
description: "Official and local source categories to inspect before BigQuery claims or execution."
okb_bundle_id: google-bigquery
timestamp: "2026-07-08T00:00:00Z"
---

# BigQuery Source Checks

## Official Source Categories

- BigQuery overview and product documentation for platform scope.
- BigQuery SQL documentation for dialect and syntax.
- BigQuery performance best practices for projection and query computation.
- BigQuery cost best practices and pricing pages for dry runs, bytes processed, and current billing context.
- BigQuery partitioning and clustering docs for table design behavior.
- BigQuery API, IAM, quota, and client-library docs when those exact facts are needed.

## Local Evidence Categories

- Project, dataset, table, view, routine, and connection metadata.
- Schema excerpts or `INFORMATION_SCHEMA` output.
- Existing SQL and job metadata.
- BI/dashboard definitions and source-of-record documentation.
- Billing, reservation, slot, and edition context.
- Privacy, security, and governance requirements.

## Rule

If an exact BigQuery fact is not in official docs or local evidence, do not present it as authoritative. Ask for inspection or mark the item as an assumption.
