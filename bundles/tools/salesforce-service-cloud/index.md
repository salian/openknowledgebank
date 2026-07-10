---
type: Bundle Index
title: Salesforce Service Cloud
description: "Tool bundle for source-aware Salesforce Service Cloud and Agentforce Service planning, case routing review, automation checks, and support operations work."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - salesforce
  - service-cloud
  - agentforce-service
  - customer-support
  - contact-center
  - crm
aliases:
  - Service Cloud
  - Salesforce Agentforce Service
  - Agentforce Service
problems_solved:
  - Plan Service Cloud case, routing, and automation work without inventing org configuration.
  - Separate official Salesforce source facts from user-provided org evidence and assumptions.
  - Review case lifecycle, Omni-Channel, queues, knowledge, reports, and automation with explicit confirmation boundaries.
  - Produce change plans that include validation, rollback, and source notes before production changes.
industries:
  - customer-service
  - customer-support
  - contact-center
  - customer-success
tools:
  - Salesforce Service Cloud
  - Agentforce Service
  - Salesforce Help
  - Salesforce Developers
  - Omni-Channel
  - Salesforce Knowledge
frameworks:
  - verify-first Salesforce planning
  - source-of-record reconciliation
  - production-change confirmation boundary
deliverables:
  - Service Cloud change plan
commands:
  - /plan-service-cloud-case-work
skills: []
evaluations:
  - Service Cloud plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: []
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
  - "Not a complete Salesforce implementation, object model, API, pricing, edition, license, release, or limits reference."
  - "Requires user-provided Salesforce org evidence before final conclusions about objects, fields, queues, routing, flows, entitlements, reports, permissions, or AI behavior."
  - "Does not replace Salesforce administrator, architect, security, privacy, compliance, legal, or change-management review."
safety_notes:
  - "Require explicit confirmation before changing Salesforce records, metadata, routing, queues, permissions, automations, integrations, exports, AI/customer-facing behavior, or customer communications."
  - "Do not request credentials or claim Salesforce org access unless the user provides authorized tool access or evidence."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 23
  okb_score: 31
  absolute_lift: 8
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 10
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 10
      okb_score: 11
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 6
      okb_score: 10
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 23/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: salesforce-service-cloud
timestamp: "2026-07-09T00:00:00Z"
---

# Salesforce Service Cloud

This bundle helps an agent use Salesforce Service Cloud, also referenced in current Salesforce materials as Agentforce Service, as a source-aware customer service platform. It is designed for case lifecycle planning, routing review, knowledge and service workspace work, support analytics, automation checks, and implementation planning.

It is a companion tool bundle, not a replacement for customer service, contact center, customer success operations, Salesforce administrator, or support analytics role bundles.

## Required Answer Habit

For source-sensitive Salesforce Service Cloud work, include a short **Source note** naming the official Salesforce source category, the user-provided org evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-service-cloud-case-work.md](commands/plan-service-cloud-case-work.md)
- [workflows/plan-case-triage-routing.md](workflows/plan-case-triage-routing.md)
- [workflows/review-service-cloud-automation.md](workflows/review-service-cloud-automation.md)
- [deliverables/service-cloud-change-plan.md](deliverables/service-cloud-change-plan.md)
- [evaluations/service-cloud-plan-quality-check.md](evaluations/service-cloud-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Salesforce Help, Salesforce Developers documentation, Salesforce release notes, Salesforce pricing/packaging pages when commercial claims matter, and user-provided Salesforce org evidence. Do not invent org names, objects, fields, record types, queue names, routing rules, flow behavior, entitlements, milestones, report filters, permissions, licenses, API calls, or AI behavior.
