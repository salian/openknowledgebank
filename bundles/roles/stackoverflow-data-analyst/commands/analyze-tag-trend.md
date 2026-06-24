---
type: Slash Command
command: /analyze-tag-trend
title: Analyze Tag Trend
description: Plan Stack Overflow tag trend analysis.
okb_bundle_id: stackoverflow-data-analyst
inputs: [tags, source, time period, comparison set]
outputs: [tag trend memo]
requires_confirmation: false
timestamp: 2026-06-24T00:00:00Z
---

# /analyze-tag-trend

Use [plan tag trend analysis](../workflows/plan-tag-trend-analysis.md) and output a [tag trend memo](../deliverables/tag-trend-memo.md).

## Required Behavior

- Confirm tags and time period.
- Ground source and tag representation.
- Preserve requested dimensions in final output.
- Ask for confirmation before execution.
