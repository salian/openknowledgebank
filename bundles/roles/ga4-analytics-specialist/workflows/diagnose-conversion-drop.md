---
type: Workflow
title: Diagnose Conversion Drop
description: "Workflow for diagnosing GA4 ecommerce purchase, revenue, or conversion movement."
tags:
  - workflow
  - diagnosis
  - ecommerce
inputs:
  - metric
  - date range
  - comparison range
  - evidence
outputs:
  - diagnosis memo
  - evidence request
  - next action plan
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Diagnose Conversion Drop

## First Move

If the user only reports a drop percentage, say the cause cannot be determined yet. Then structure the diagnosis.

## Steps

1. Frame the metric: purchases, purchase revenue, ecommerce conversion rate, sessions, active users, or revenue per session.
2. Confirm source: GA4 UI/API, BigQuery export, backend orders, ad platform, or spreadsheet.
3. Confirm date range, comparison range, timezone, filters, segments, and data quality notices.
4. Decompose movement into traffic volume, conversion efficiency, order value, product mix, channel mix, and measurement integrity.
5. Check implementation changes: GTM/container changes, purchase event health, consent mode, release log, checkout incidents, and backend order reconciliation.
6. Produce a ranked hypothesis table with evidence, expected signal, confidence, and next action.
7. End with a source note.

## Required Output Sections

Direct answer, metric frame, available evidence, missing evidence, decomposition, measurement checks, hypothesis table, next actions, source note.
