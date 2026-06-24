---
type: Workflow
title: Plan Answer Coverage
description: Plans accepted-answer rate and answer coverage by requested dimensions such as tag and month.
tags: [workflow, answer-coverage, query-shape]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Plan Answer Coverage

Use this workflow for accepted-answer rate, any-answer coverage, and answer volume analysis.

## Required Inputs

- Tags or comparison set
- Time period and bucket
- Source
- Requested dimensions, such as tag and month
- Metrics: accepted-answer rate, any-answer coverage, answer count, or answer coverage ratio

## Steps

1. Use question grain as the base.
2. Confirm tag representation and source schema.
3. Define output row before SQL. Example: "one row per tag per month."
4. Define metrics:
   - question count: distinct question IDs
   - any-answer coverage: questions with `answer_count > 0`
   - accepted-answer rate: questions with `accepted_answer_id IS NOT NULL`
   - answer count: aggregated answer rows by parent question
5. Join answers only when answer-level detail is needed.
6. Run the query-shape self-check before finalizing.

## BigQuery Sketch For Tag And Month

This is a sketch, not executed SQL. Verify active schema before running.

```sql
WITH tag_list AS (
  SELECT tag FROM UNNEST(['python', 'rust']) AS tag
),
questions AS (
  SELECT
    tag_list.tag,
    DATE_TRUNC(DATE(q.creation_date), MONTH) AS month,
    q.id AS question_id,
    q.answer_count,
    q.accepted_answer_id
  FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
  JOIN tag_list
    ON q.tags LIKE CONCAT('%<', tag_list.tag, '>%')
  WHERE q.creation_date >= TIMESTAMP('2021-01-01')
    AND q.creation_date < TIMESTAMP('2022-01-01')
)
SELECT
  tag,
  month,
  COUNT(DISTINCT question_id) AS question_count,
  COUNTIF(answer_count > 0) AS questions_with_answers,
  SAFE_DIVIDE(COUNTIF(answer_count > 0), COUNT(DISTINCT question_id)) AS any_answer_coverage,
  COUNTIF(accepted_answer_id IS NOT NULL) AS questions_with_accepted_answer,
  SAFE_DIVIDE(COUNTIF(accepted_answer_id IS NOT NULL), COUNT(DISTINCT question_id)) AS accepted_answer_rate
FROM questions
GROUP BY tag, month
ORDER BY tag, month;
```

## Query-Shape Self-Check

| Requested Element | Covered? | Where |
| --- | --- | --- |
| Tag | Yes | `SELECT tag`, `GROUP BY tag` |
| Month | Yes | `SELECT month`, `GROUP BY month` |
| Accepted-answer rate | Yes | `accepted_answer_rate` |
| Any-answer coverage | Yes | `any_answer_coverage` |
| Question grain | Yes | base CTE uses `question_id` |

## Caveats

- Accepted answer is not a guarantee of answer quality.
- Deleted/private content handling can vary by source.
- Historical public data may not match live counts.
