---
type: Bundle Index
title: HubSpot Sales Hub
description: "Tool bundle for source-aware HubSpot Sales Hub CRM, pipeline, prospecting, automation, reporting, and integration planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - hubspot
  - sales-hub
  - crm
  - sales-engagement
  - revops
aliases:
  - HubSpot Sales
  - Sales Hub
  - HubSpot Smart CRM
problems_solved:
  - Plan HubSpot Sales Hub work without inventing portal configuration, properties, pipelines, sequences, workflows, reports, or permissions.
  - Separate official HubSpot product/API behavior from user-provided account evidence and assumptions.
  - Review sales process, pipeline, sequence, workflow, reporting, permission, and integration changes with explicit confirmation boundaries.
  - Produce HubSpot Sales Hub plans that include source notes, validation checks, and rollback before live CRM or outreach changes.
industries:
  - sales
  - revenue-operations
  - b2b-saas
  - professional-services
  - ecommerce
tools:
  - HubSpot Sales Hub
  - HubSpot Smart CRM
  - HubSpot Knowledge Base
  - HubSpot Developers
frameworks:
  - verify-first CRM planning
  - source-of-record reconciliation
  - sales communication confirmation boundary
deliverables:
  - HubSpot Sales Hub change plan
commands:
  - /plan-hubspot-sales-work
skills: []
evaluations:
  - HubSpot Sales Hub plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - sales-development-representative-sdr
  - account-executive-closer
  - revenue-operations-revops-manager
  - sales-operations-analyst
adjacent_bundles:
  - salesforce-service-cloud
  - google-bigquery
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
  - "Not a complete HubSpot implementation, CRM schema, API, pricing, edition, seat, limit, workflow, deliverability, or release reference."
  - "Requires user-provided HubSpot portal evidence before final conclusions about objects, properties, pipelines, stages, records, sequences, workflows, reports, permissions, seats, quotes, products, integrations, or API behavior."
  - "Does not replace HubSpot administrator, RevOps, sales leadership, security, privacy, legal, procurement, deliverability, or change-management review."
safety_notes:
  - "Require explicit confirmation before sending outreach, enrolling contacts in sequences, modifying records, activating workflows, changing pipeline or permission settings, exporting CRM data, changing quote/payment behavior, or running integrations/API actions."
  - "Do not request credentials or claim HubSpot portal access unless the user provides authorized tool access or evidence."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 20
  okb_score: 35
  absolute_lift: 15
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 12
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 7
      okb_score: 11
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 20/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: hubspot-sales-hub
timestamp: "2026-07-09T00:00:00Z"
---

# HubSpot Sales Hub

This bundle helps an agent use HubSpot Sales Hub as a source-aware CRM and sales engagement tool. It is designed for sales process planning, pipeline and deal review, prospecting and sequence planning, workflow and automation checks, reporting reconciliation, permission review, and integration planning.

It is a companion tool bundle, not a replacement for sales, RevOps, sales operations, sales management, HubSpot administrator, marketing operations, or customer success role bundles.

## Required Answer Habit

For source-sensitive HubSpot work, include a short **Source note** naming the official HubSpot source category, the user-provided portal evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-hubspot-sales-work.md](commands/plan-hubspot-sales-work.md)
- [workflows/plan-sales-process-and-pipeline.md](workflows/plan-sales-process-and-pipeline.md)
- [workflows/review-sales-automation-and-outreach.md](workflows/review-sales-automation-and-outreach.md)
- [deliverables/hubspot-sales-change-plan.md](deliverables/hubspot-sales-change-plan.md)
- [evaluations/hubspot-sales-plan-quality-check.md](evaluations/hubspot-sales-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current HubSpot product pages, HubSpot Knowledge Base, HubSpot Developers documentation, HubSpot legal/commercial pages when commercial claims matter, and user-provided HubSpot portal evidence. Do not invent portal IDs, object schemas, property names, pipeline stages, deal values, sequences, workflow branches, reports, dashboards, permissions, seats, quote/payment settings, API syntax, or integration behavior.
