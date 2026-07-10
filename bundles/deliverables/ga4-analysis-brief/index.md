---
type: Bundle Index
title: GA4 Analysis Brief
description: "Deliverable bundle for producing source-scoped, decision-ready GA4 analysis briefs."
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
  - ga4
  - google-analytics
  - analytics
  - reporting
  - analysis-brief
aliases:
  - GA4 analysis memo
  - GA4 diagnostic brief
  - GA4 conversion analysis brief
  - Google Analytics analysis brief
problems_solved:
  - Turn GA4 reports, explorations, and exports into decision-ready analysis.
  - Define source scope, metrics, dimensions, filters, and caveats before conclusions.
  - Separate verified observations from hypotheses and next actions.
  - Avoid inventing GA4 access, schemas, metrics, or causes.
industries:
  - ecommerce
  - b2b-saas
  - digital-products
  - marketing
tools:
  - Google Analytics
  - GA4
  - BigQuery
frameworks:
  - source-scoped analytics brief
  - funnel analysis
  - measurement-health review
deliverables:
  - GA4 analysis brief
commands:
  - /draft-ga4-analysis-brief
skills: []
evaluations:
  - GA4 analysis brief quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - ga4-analytics-specialist
  - google-bigquery
  - funnel-analysis
adjacent_bundles:
  - performance-marketer
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a full GA4 implementation, admin, tagging, reporting, or SQL guide."
  - "Requires user-provided report, exploration, export, schema, date-range, metric, dimension, filter, and segment evidence for final conclusions."
  - "Does not prove causality from GA4 metric changes alone."
safety_notes:
  - "Require confirmation before modifying live GA4, GTM, dashboards, campaigns, experiments, exports, or warehouse tables."
  - "Do not claim access to GA4 properties, reports, events, or exports unless the user provides evidence or authorized tool access."
okb_bundle_id: ga4-analysis-brief
timestamp: "2026-07-09T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 22
  okb_score: 34
  absolute_lift: 12
  task_scores:
    - task: deliverable-draft-with-missing-evidence
      baseline_score: 8
      okb_score: 12
      max_score: 12
    - task: deliverable-quality-review
      baseline_score: 6
      okb_score: 11
      max_score: 12
    - task: deliverable-reconciliation
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 22/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# GA4 Analysis Brief

This bundle defines a concise, source-scoped deliverable for GA4 analysis. It helps an agent answer the user’s question while making the data source, metric definitions, caveats, and next actions visible.

It is a companion deliverable for [GA4 Analytics Specialist](../../roles/ga4-analytics-specialist/index.md), [Google BigQuery](../../tools/google-bigquery/index.md), and [Funnel Analysis](../../frameworks/funnel-analysis/index.md).

## Required Answer Habit

Every GA4 analysis brief must include a **Source note** naming the GA4 report, exploration, export, or user-provided evidence used; the metric/dimension definitions available; and missing evidence required before treating the brief as final.

## Start Here

- [deliverable.md](deliverable.md)
- [commands/draft-ga4-analysis-brief.md](commands/draft-ga4-analysis-brief.md)
- [workflows/prepare-ga4-analysis-brief.md](workflows/prepare-ga4-analysis-brief.md)
- [evaluations/ga4-analysis-brief-quality-check.md](evaluations/ga4-analysis-brief-quality-check.md)
- [references/source-checks.md](references/source-checks.md)
