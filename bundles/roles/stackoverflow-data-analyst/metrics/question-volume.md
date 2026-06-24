---
type: Metric
title: Question Volume
description: Count of questions over a source, time period, and filter set.
tags: [metric, questions]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Question Volume

## Definition

Distinct question count for a source and time period.

## Grounded BigQuery Basis

- Table: `posts_questions`
- Identifier: `id`
- Time field: `creation_date`

## Caveats

- Historical public data may not match live counts.
- Tag matching must be delimiter-aware.
- Question volume is not technology adoption.
