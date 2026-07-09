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
status: draft
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
  status: blocked
  last_evaluated: null
  method: baseline-vs-okb-rubric
  tasks_count: 3
  display_summary: "Measured evaluation is blocked until a reviewed Amplitude task set, evaluator config, model outputs, and reviewer scoring are completed."
  evidence_note: "No measured score is claimed. The public bundle includes a rubric, but no completed baseline-vs-OKB model run exists."
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
