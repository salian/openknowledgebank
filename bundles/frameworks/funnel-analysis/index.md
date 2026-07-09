---
type: Bundle Index
title: Funnel Analysis
description: "Framework bundle for defining funnels, measuring stage-by-stage conversion and drop-off, comparing segments, and turning friction into verified hypotheses."
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - funnel-analysis
  - conversion
  - analytics
  - ecommerce
  - product-analytics
aliases:
  - conversion funnel analysis
  - funnel exploration
  - stage-by-stage drop-off analysis
  - conversion path analysis
problems_solved:
  - Define funnel steps without inventing analytics events or schemas.
  - Interpret stage conversion and drop-off with explicit denominator logic.
  - Compare funnel performance across segments and breakdowns.
  - Separate measurement findings, hypotheses, and actions.
industries:
  - ecommerce
  - b2b-saas
  - digital-products
  - marketing
tools:
  - Google Analytics
  - Adobe Customer Journey Analytics
  - BigQuery
frameworks:
  - funnel step definition
  - denominator reconciliation
  - stage drop-off diagnosis
deliverables:
  - funnel analysis brief
commands:
  - /diagnose-funnel-drop
skills: []
evaluations:
  - Funnel analysis quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - ga4-analytics-specialist
  - google-bigquery
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
  - "Not a complete GA4, Adobe Analytics, BigQuery, experimentation, or SQL implementation guide."
  - "Requires user-provided event, schema, report, date-range, segment, and denominator evidence for final conclusions."
  - "Does not prove causality from funnel drop-off alone."
safety_notes:
  - "Require confirmation before modifying live analytics configuration, tags, dashboards, campaigns, experiments, exports, or warehouse tables."
  - "Do not claim access to analytics tools, event schemas, user-level records, or reports unless the user provides evidence or authorized tool access."
okb_bundle_id: funnel-analysis
timestamp: "2026-07-09T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 21
  okb_score: 24
  absolute_lift: 3
  task_scores:
    - task: framework-fit-review
      baseline_score: 6
      okb_score: 6
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 6
      okb_score: 6
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 9
      okb_score: 12
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 21/36 to 24/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Funnel Analysis

This bundle helps an agent use funnel analysis as a source-aware framework. It is designed for defining ordered journey steps, measuring conversion and drop-off, comparing segments, and producing decision-ready analysis without pretending unknown tool settings or event schemas are known.

It is a companion framework bundle for role and tool bundles such as [GA4 Analytics Specialist](../../roles/ga4-analytics-specialist/index.md) and [Google BigQuery](../../tools/google-bigquery/index.md).

## Required Answer Habit

For funnel work, include a short **Source note** naming the analytics/reporting source, the user-provided local evidence used, and missing evidence required before treating the funnel as a final measurement or causal diagnosis.

## Start Here

- [framework.md](framework.md)
- [commands/diagnose-funnel-drop.md](commands/diagnose-funnel-drop.md)
- [workflows/define-funnel.md](workflows/define-funnel.md)
- [workflows/diagnose-stage-dropoff.md](workflows/diagnose-stage-dropoff.md)
- [workflows/compare-funnel-segments.md](workflows/compare-funnel-segments.md)
- [deliverables/funnel-analysis-brief.md](deliverables/funnel-analysis-brief.md)
- [evaluations/funnel-analysis-quality-check.md](evaluations/funnel-analysis-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use official analytics-tool documentation, report configuration, event/schema evidence, warehouse exports, source-of-record definitions, and user-provided business context. Do not invent event names, parameters, dimensions, segment rules, attribution settings, denominators, date ranges, or causes.
