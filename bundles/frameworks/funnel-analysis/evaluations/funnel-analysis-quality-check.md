---
type: Evaluation
title: Funnel Analysis Quality Check
description: "Rubric for reviewing whether a funnel analysis is source-aware, denominator-safe, and action-ready."
okb_bundle_id: funnel-analysis
task_type: analysis
criteria:
  - source scope
  - funnel definition
  - denominator logic
  - segment discipline
  - measurement health
  - action safety
timestamp: "2026-07-09T00:00:00Z"
---

# Funnel Analysis Quality Check

Score each criterion 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Source scope | Omits source and period | Names partial source | Defines tool/report, date range, filters, freshness, and source of record |
| Funnel definition | Invents or omits steps | Lists steps with weak evidence | Requires verified step evidence, order, entry rule, sequence rule, and time window |
| Denominator logic | Mixes denominators | Mentions denominator generally | States counting unit, first/previous-step basis, open/closed behavior, and comparability limits |
| Segment discipline | Infers segments from labels | Compares partial segments | Requires exact segment/breakdown definitions and aligned scope |
| Measurement health | Ignores tracking risk | Mentions QA generally | Checks instrumentation, consent, schema, data freshness, filters, thresholds, and reporting surface |
| Action safety | Recommends live changes without confirmation | Some caution | Separates findings/hypotheses/actions and requires confirmation for live changes or exports |
