---
type: Framework
title: Grain and Join Discipline
description: Prevents inflated counts and wrong joins in Stack Overflow public data plans.
tags: [grain, joins, aggregation]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Grain and Join Discipline

## Common Grains

- `posts_questions`: question grain.
- `posts_answers`: answer grain.
- `votes`: vote-event grain.
- `comments`: comment grain.
- `post_history`: post-history-event grain.
- `post_links`: post-link grain.
- `tags`: tag dictionary grain.

## Rules

- Start question-level metrics from question rows.
- Aggregate child tables before joining to question grain.
- Use distinct identifiers when joins can duplicate rows.
- State what one output row represents.
- Do not assume a tag bridge table unless the active schema confirms one.
