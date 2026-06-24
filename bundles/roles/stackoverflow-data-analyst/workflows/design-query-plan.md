---
type: Workflow
title: Design Query Plan
description: Designs a source-grounded query plan with explicit output-shape validation.
tags: [workflow, query-planning, sql]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Design Query Plan

## Steps

1. State whether the output is a plan, sketch, dry-run candidate, or executed result.
2. Select the active source.
3. Ground tables, fields, API parameters, and enum values.
4. Define requested dimensions, metrics, filters, source, grain, and output row.
5. Draft source-specific SQL or API steps.
6. Run [query-shape self-check](../frameworks/query-shape-self-check.md).
7. Add validation, dry-run/cost, permission, freshness, and license/privacy caveats.

## Output Contract

- Source note
- Schema evidence
- Metric definitions
- Grain and joins
- Query/API sketch
- Query-shape self-check table
- Validation checks
- Limitations
