---
type: Bundle Index
title: Amplitude
description: "Tool bundle for source-aware Amplitude product analytics planning, event taxonomy review, funnel analysis, cohorts, experiments, and session replay evidence handling."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - amplitude
  - product-analytics
  - funnel-analysis
  - cohorts
  - experimentation
aliases:
  - Amplitude Analytics
  - Amplitude product analytics
  - Amplitude session replay
problems_solved:
  - Plan Amplitude analysis without inventing event names, properties, chart definitions, cohorts, or account settings.
  - Review product analytics evidence with explicit metric definitions, filters, identity logic, and source-of-record caveats.
  - Use funnels, cohorts, experiments, and session replay as evidence without overstating causality or privacy readiness.
industries:
  - software
  - digital-products
  - b2b-saas
  - ecommerce
  - product-led-growth
tools:
  - Amplitude
frameworks:
  - event taxonomy review
  - funnel analysis
  - cohort analysis
  - experiment evidence review
  - session replay evidence review
deliverables:
  - Amplitude analysis brief
commands:
  - /plan-amplitude-analysis
skills: []
evaluations:
  - Amplitude analysis quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - product-manager
  - data-product-manager
  - senior-product-manager
  - technical-product-manager
adjacent_bundles:
  - funnel-analysis
  - ga4-analytics-specialist
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
  - "Not a complete Amplitude product, API, SDK, pricing, plan, data governance, privacy, or administration reference."
  - "Requires user-provided Amplitude workspace, chart, event, property, cohort, experiment, replay, permission, and policy evidence before final conclusions."
  - "Does not replace data engineering, privacy, security, legal, product analytics, experimentation, or Amplitude administrator review."
safety_notes:
  - "Require confirmation before changing instrumentation, cohorts, experiments, dashboards, alerts, permissions, exports, integrations, privacy settings, or user-facing experiences."
  - "Do not claim access to Amplitude projects, events, properties, users, cohorts, charts, experiments, replays, permissions, or exports unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 24
  okb_score: 34
  absolute_lift: 10
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 12
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 9
      okb_score: 11
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 24/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: amplitude
timestamp: "2026-07-09T00:00:00Z"
---

# Amplitude

This bundle helps an agent plan and review Amplitude product analytics work without inventing local instrumentation, chart definitions, cohorts, experiments, session replay availability, or account settings.

## Required Answer Habit

For Amplitude work, include a short **Source note** naming the official Amplitude source category, the user-provided workspace/chart/event/cohort/experiment/replay evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-amplitude-analysis.md](commands/plan-amplitude-analysis.md)
- [workflows/review-amplitude-event-taxonomy.md](workflows/review-amplitude-event-taxonomy.md)
- [workflows/plan-funnel-analysis.md](workflows/plan-funnel-analysis.md)
- [deliverables/amplitude-analysis-brief.md](deliverables/amplitude-analysis-brief.md)
- [evaluations/amplitude-analysis-quality-check.md](evaluations/amplitude-analysis-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Amplitude documentation for product behavior and user-provided Amplitude evidence for local project configuration, event taxonomy, chart definitions, cohorts, experiments, privacy settings, permissions, exports, and source-of-record reconciliation.
