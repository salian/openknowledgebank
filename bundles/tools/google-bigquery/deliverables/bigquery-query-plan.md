---
type: Deliverable
title: BigQuery Query Plan
description: "A source-scoped plan for writing or reviewing a BigQuery query."
okb_bundle_id: google-bigquery
required_inputs:
  - business question
  - source/schema evidence
  - time range and grain
  - validation source
outputs:
  - query shape
  - evidence gaps
  - cost/performance preflight
  - validation checklist
quality_criteria:
  - Does not invent schema or access.
  - Names missing verification before execution.
  - Includes dry-run and projection checks.
  - Includes a visible source note.
timestamp: "2026-07-08T00:00:00Z"
---

# BigQuery Query Plan

## Required Sections

1. **Decision and direct answer**: what the analysis can and cannot answer with current evidence.
2. **Source scope**: project/dataset/table evidence, included and excluded records, freshness, and source-of-record assumptions.
3. **Metric and entity logic**: definitions, identifiers, joins, deduplication, grain, time range, and timezone.
4. **Query shape**: selected columns, filters, grouping, output rows, and unsupported pieces.
5. **Cost/performance preflight**: dry run, projection check, partition/cluster check, and confirmation boundary.
6. **Validation plan**: totals, samples, edge cases, reconciliation target, and expected differences.
7. **Source note**: official BigQuery source categories, user evidence, and missing source checks.

## Quality Bar

A good plan lets a human or authorized agent write SQL without pretending that unknown schemas, permissions, costs, or results are known.
