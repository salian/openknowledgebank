---
type: Metric
title: Answer Coverage
description: Measures whether questions receive answers or accepted answers.
tags: [metric, answers, coverage]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Answer Coverage

## Definitions

- Any-answer coverage: share of questions with at least one answer.
- Accepted-answer rate: share of questions with an accepted answer.
- Answer count: count of answer rows associated with a question set.

## Grounded BigQuery Basis

- `posts_questions.answer_count > 0` supports any-answer coverage.
- `posts_questions.accepted_answer_id IS NOT NULL` supports accepted-answer rate.
- `posts_answers.parent_id` links answers to questions when answer-level detail is needed.

## Query-Shape Rule

If the request says "by tag and month", final output must include both tag and month.
