---
type: Slash Command
command: /diagnose-conversion-drop
title: Diagnose Conversion Drop
description: Create a source-aware GA4 conversion or purchase drop diagnosis memo.
inputs:
  - metric
  - date range
  - comparison range
  - available evidence
outputs:
  - diagnosis memo
  - evidence request
  - source note
requires_confirmation: false
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# /diagnose-conversion-drop

Use when purchases, conversions, revenue, or conversion rate dropped.

## First Sentence Rule

If the user only provides the drop percentage, say that the cause cannot be determined from that claim alone and that the next step is a structured diagnosis.

## Final Answer Must Include

Direct answer, metric frame, available evidence, missing evidence, decomposition, measurement checks, ranked hypothesis table, immediate next actions, and source note.

## Required Checks

GA4 settings, BigQuery query logic if export evidence is used, GTM/release history, consent, purchase event health, backend order check, traffic volume, conversion efficiency, order value, product mix, channel mix, and site/checkout incidents.
