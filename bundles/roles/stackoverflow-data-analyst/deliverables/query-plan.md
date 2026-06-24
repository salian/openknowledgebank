---
type: Deliverable
title: Query Plan
description: Source-grounded query plan with output-shape self-check.
okb_bundle_id: stackoverflow-data-analyst
required_inputs: [question, source, schema evidence, time period, requested dimensions, requested metrics]
outputs: [source note, SQL/API sketch, query-shape self-check, validation checks]
quality_criteria: [source-grounded, preserves requested output shape, validates grain, includes dry-run/cost note]
timestamp: 2026-06-24T00:00:00Z
---

# Query Plan

## Required Sections

1. Plan status
2. Source note
3. Tables/fields/API parameters
4. Grain and joins
5. Metrics
6. SQL/API sketch
7. Query-shape self-check
8. Validation checks
9. Cost, permission, freshness, and license/privacy caveats

## Query-Shape Rule

Every requested dimension and metric must appear in the final SELECT/GROUP BY/output contract or be explicitly deferred.
