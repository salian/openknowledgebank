---
type: Framework
title: Query-Shape Self-Check
description: Checklist for ensuring a query plan output matches the user's requested dimensions, metrics, filters, source, and grain.
tags: [query-planning, output-shape, validation]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Query-Shape Self-Check

Run this before finalizing any SQL, API, report, or dashboard plan.

## Check

| Requested Element | Must Appear In | If Missing |
| --- | --- | --- |
| Dimension, such as tag, month, source, segment, cohort, geography, or status | Final SELECT and GROUP BY, or API/report output fields | Add it or explicitly defer it. |
| Metric, such as count, rate, share, average, ratio, coverage, or score | Metric definition and final SELECT/output | Define numerator, denominator, aggregation, and null handling. |
| Filter | WHERE/API parameters/report filters | State filter logic and exclusions. |
| Source | Source note and source object list | Ask for source selection or schema inspection. |
| Grain | Grain section and join plan | Change joins/aggregation to preserve grain. |
| Output row | Final result description | State what one output row represents. |

## Final Review Prompt

Ask: "If the user requested results by X and Y, do X and Y both appear in the final output shape?"

## Common Failures

- SQL groups by month but omits the requested tag.
- SQL joins child rows and reports question-level metrics without deduplication.
- Metric appears in prose but not in final SELECT.
- API plan has filters but no output fields.
- Query plan gives a source but omits freshness and validation.
