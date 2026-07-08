---
type: Slash Command
command: /diagnose-funnel-drop
title: Diagnose Funnel Drop
description: "Create a source-scoped funnel drop-off diagnosis without inventing schemas, settings, or causes."
okb_bundle_id: funnel-analysis
inputs:
  - business question
  - funnel steps and report source
  - date range and comparison period
  - counting unit and denominator basis
  - segment, breakdown, filter, and attribution definitions
outputs:
  - funnel analysis brief
  - required local evidence
  - measurement-health checks
  - hypotheses and next actions
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /diagnose-funnel-drop

Purpose: produce a funnel drop-off diagnosis that is ready for review, not a causal claim made from an under-specified chart.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question and decision to support.
- Tool/report source and whether data comes from UI, export, warehouse, or user-provided table.
- Step names, event/dimension/schema evidence, and step order.
- Date range, timezone, comparison period, filters, and reporting window.
- Counting unit and denominator basis.
- Open/closed entry rule, direct/indirect step rule, and within-timeframe setting if relevant.
- Segment, breakdown, channel, attribution, or experiment definitions.
- Known instrumentation, tagging, consent, release, campaign, or product changes.

## Output Contract

Return:

1. Direct answer: what the funnel evidence does and does not show.
2. Source scope: report/tool/source, date range, filters, denominator, and included/excluded records.
3. Funnel definition: ordered steps, entry rules, sequence rules, and missing evidence.
4. Stage findings: conversion, drop-off, elapsed time, and next actions when provided.
5. Segment or breakdown findings: only when definitions and scope are aligned.
6. Measurement-health checks: tracking, schema, consent, data freshness, reporting, and source-of-record risks.
7. Hypotheses: ranked by evidence, each with required validation.
8. Recommended actions: safe next analysis steps first; live changes only after confirmation.
9. Source note: official source categories, user-provided evidence, and missing verification.

## Confirmation Boundary

Do not modify analytics configuration, tags, dashboards, campaigns, experiments, exports, warehouse tables, or user-level data access without explicit user confirmation and authorized tool access.
