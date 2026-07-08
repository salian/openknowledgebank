---
type: Deliverable
title: Funnel Analysis Brief
description: "A source-scoped brief for defining, interpreting, and acting on funnel performance."
okb_bundle_id: funnel-analysis
required_inputs:
  - business question
  - source/report evidence
  - funnel step definitions
  - denominator and counting unit
  - date range and comparison period
  - segment and filter definitions
outputs:
  - direct answer
  - funnel definition
  - stage findings
  - hypotheses
  - recommended next actions
quality_criteria:
  - Does not invent event schemas, segment rules, or causes.
  - Names denominator and source scope.
  - Separates findings from hypotheses.
  - Includes a visible source note.
timestamp: "2026-07-09T00:00:00Z"
---

# Funnel Analysis Brief

## Required Sections

1. **Direct answer**: what the current funnel evidence shows and what remains unknown.
2. **Source scope**: analytics tool or warehouse source, report/export name, date range, timezone, filters, attribution, data freshness, and included/excluded records.
3. **Funnel definition**: ordered steps, event/schema evidence, open/closed rule, sequence rule, time window, denominator, and counting unit.
4. **Stage findings**: conversion, drop-off, elapsed time, next actions, and comparison-period changes when provided.
5. **Segment and breakdown findings**: differences by segment, cohort, channel, device, geography, experiment, or other verified breakdown.
6. **Measurement-health checks**: tracking, tagging, schema, consent, thresholds, data freshness, source-of-record, and reporting-surface risks.
7. **Hypotheses**: likely explanations ranked by evidence, with validation required for each.
8. **Recommended next actions**: analysis and verification steps first; live product, campaign, tag, or experiment changes only after confirmation.
9. **Source note**: official source categories, user evidence, and missing verification.

## Quality Bar

A good brief makes the funnel actionable without hiding uncertainty. It should be clear enough for a human analyst to reproduce the metric definition and challenge every hypothesis.
