---
type: Bundle Index
title: Mixpanel
description: Tool bundle for source-aware Mixpanel product analytics planning, event taxonomy review, funnel/cohort analysis, and metric reconciliation.
schema_version: 0.1.0
bundle_format: okf-compatible
category: tools
tags:
  - mixpanel
  - product-analytics
  - funnels
  - cohorts
  - event-analytics
aliases:
  - Mixpanel Analytics
  - Mixpanel funnels
  - Mixpanel cohorts
problems_solved:
  - Plan Mixpanel analysis without inventing event names, properties, cohorts, filters, identity logic, or project settings.
  - Review funnels and cohorts with explicit conversion criteria, time windows, segments, and instrumentation caveats.
  - Reconcile Mixpanel findings with source-of-record data before product decisions.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
  - Mixpanel
frameworks:
  - event taxonomy review
  - funnel analysis
  - cohort analysis
  - metric reconciliation
deliverables:
  - Mixpanel analysis brief
commands:
  - /plan-mixpanel-analysis
skills:
evaluations:
  - Mixpanel guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - data-product-manager
adjacent_bundles:
  - amplitude
  - funnel-analysis
  - ga4-analytics-specialist
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc:
  soc:
  isco_08:
  esco:
limitations:
  - Not a complete Mixpanel implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Mixpanel usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before changing instrumentation, cohorts, dashboards, reports, alerts, exports, permissions, integrations, privacy settings, or user-facing product decisions from Mixpanel evidence.
  - Do not claim access to private systems, customer data, workspaces, documents, dashboards, roadmaps, repositories, accounts, or source records unless the user provides evidence or authorized tool access.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 23
  okb_score: 34
  absolute_lift: 11
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 12
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 10
      okb_score: 10
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 23/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: mixpanel
timestamp: "2026-07-09T00:00:00Z"
---

# Mixpanel

This bundle helps an agent work with Mixpanel while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Mixpanel work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [Command](commands/plan-mixpanel-analysis.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/mixpanel-brief.md)
- [Evaluation](evaluations/mixpanel-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Mixpanel Funnels documentation](https://docs.mixpanel.com/docs/reports/funnels) for source behavior and framework grounding. Use user-provided evidence for ['project, event, property, cohort, filter, date range, identity merge, environment, implementation, permission, export, and source-of-record evidence']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
