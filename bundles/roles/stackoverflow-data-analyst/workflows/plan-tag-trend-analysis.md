---
type: Workflow
title: Plan Tag Trend Analysis
description: Plans Stack Overflow tag trend analysis with source and query-shape checks.
tags: [workflow, tags, trends]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Plan Tag Trend Analysis

## Steps

1. Confirm exact tags and comparison set.
2. Choose source.
3. Ground tag representation.
4. Define metrics: question count, share of all questions, answer coverage, or engagement.
5. Define output row, such as one row per tag per month.
6. Draft query/API plan.
7. Run query-shape self-check.

## BigQuery Sketch For Tag And Month

```sql
WITH tag_list AS (
  SELECT tag FROM UNNEST(['rust', 'go', 'python']) AS tag
),
question_tags AS (
  SELECT
    tag_list.tag,
    DATE_TRUNC(DATE(q.creation_date), MONTH) AS month,
    q.id AS question_id
  FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
  JOIN tag_list
    ON q.tags LIKE CONCAT('%<', tag_list.tag, '>%')
  WHERE q.creation_date >= TIMESTAMP('2020-01-01')
    AND q.creation_date < TIMESTAMP('2023-01-01')
)
SELECT
  tag,
  month,
  COUNT(DISTINCT question_id) AS question_count
FROM question_tags
GROUP BY tag, month
ORDER BY tag, month;
```

## Caveats

- This is historical question activity, not technology adoption.
- Verify tag string encoding before execution.
- BigQuery execution requires confirmation and preferably a dry run.
