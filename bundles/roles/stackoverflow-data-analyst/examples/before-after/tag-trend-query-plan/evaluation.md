---
type: Evaluation
title: Tag Trend Query Plan Evaluation
description: Evaluation notes for the tag trend query task.
okb_bundle_id: stackoverflow-data-analyst
task_type: data-analysis
criteria: [source_scope, schema_grounding, query_shape, caveats]
timestamp: 2026-06-24T00:00:00Z
---

# Tag Trend Query Plan Evaluation

Use [Stack Overflow analysis quality check](../../../evaluations/stackoverflow-analysis-quality-check.md).

Specific pass expectations:

- Uses `posts_questions` as question base.
- Does not invent a tag bridge table.
- Does not use array tag operations unless schema proves array type.
- Final output includes tag and time bucket.
- Includes dry-run/cost/freshness caveats.
