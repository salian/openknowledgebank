---
type: Metric
title: Tag Trend
description: Question activity over time for one or more tags.
tags: [metric, tags, trends]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Tag Trend

## Definition

Question count, share, or related metric by tag and time bucket.

## Required Output Shape

If the user asks for trend by tag and month, output one row per tag per month.

## Caveats

- Validate tag names and synonyms.
- Do not assume a tag bridge table.
- Do not treat question volume as adoption.
