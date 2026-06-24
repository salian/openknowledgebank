---
type: Reference
title: Role-Critical Schema
description: Compact schema reference for common Stack Overflow public data planning.
tags: [schema, bigquery, source-grounding]
okb_bundle_id: stackoverflow-data-analyst
source_quality: grounded-summary
timestamp: 2026-06-24T00:00:00Z
---

# Role-Critical Schema

Use this as compact guidance, not a full catalog. Verify active source schema before execution.

## Grounded BigQuery Sample

Dataset: `bigquery-public-data.stackoverflow`

Common tables:

| Table | Grain | Use |
| --- | --- | --- |
| `posts_questions` | question | question volume, tags, answer coverage |
| `posts_answers` | answer | answer attributes and answer counts |
| `tags` | tag dictionary | tag metadata, not per-question assignment |
| `votes` | vote event | engagement with vote type interpretation |
| `comments` | comment | comment activity |
| `users` | user profile | aggregate user analysis only |
| `post_history` | history event | edits, closes, migration events |
| `post_links` | post link | linked/duplicate relationships |

## Role-Critical Fields

`posts_questions`: `id`, `creation_date`, `tags`, `answer_count`, `accepted_answer_id`, `score`, `view_count`, `comment_count`, `owner_user_id`, `content_license`.

`posts_answers`: `id`, `parent_id`, `creation_date`, `score`, `comment_count`, `owner_user_id`, `content_license`.

`tags`: `id`, `tag_name`, `count`, `excerpt_post_id`, `wiki_post_id`.

`votes`: `id`, `post_id`, `vote_type_id`, `user_id`, `creation_date`.

## Tag Handling

In the grounded BigQuery sample, `posts_questions.tags` is a `STRING`. Do not use `UNNEST(tags)` unless the active source schema proves `tags` is an array. Use delimiter-aware matching such as `<tag>` patterns after verifying encoding.

## Joins And Metrics

- Answer-to-question join: `posts_answers.parent_id = posts_questions.id`.
- Accepted-answer rate can be calculated from `posts_questions.accepted_answer_id IS NOT NULL`.
- Any-answer coverage can be calculated from `posts_questions.answer_count > 0`.
- Aggregate child rows before joining to question grain.

## Vote Types

Use a vote type reference before interpreting `votes.vote_type_id`. Common grounded values include `2` for upvote and `3` for downvote.
