---
type: Bundle Index
title: Zendesk
description: "Tool bundle for source-aware Zendesk Support, Suite, ticketing, business-rule, Help Center, AI agent, reporting, and API planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - zendesk
  - zendesk-support
  - zendesk-suite
  - customer-support
  - helpdesk
  - ticketing
  - cx-operations
aliases:
  - Zendesk Support
  - Zendesk Suite
  - Zendesk AI agents
problems_solved:
  - Plan Zendesk ticketing, routing, automation, Help Center, AI agent, reporting, or API work without inventing account configuration.
  - Separate official Zendesk product/API behavior from user-provided account evidence and assumptions.
  - Review triggers, automations, macros, views, routing, AI agents, reports, permissions, and integrations with explicit confirmation boundaries.
  - Produce Zendesk change plans that include source notes, validation checks, and rollback before live support-system changes.
industries:
  - customer-service
  - customer-support
  - contact-center
  - customer-success
  - ecommerce
  - b2b-saas
tools:
  - Zendesk
  - Zendesk Support
  - Zendesk Suite
  - Zendesk Help Center
  - Zendesk AI agents
  - Zendesk Developer API Reference
frameworks:
  - verify-first support operations planning
  - source-of-record reconciliation
  - live support-system confirmation boundary
deliverables:
  - Zendesk change plan
commands:
  - /plan-zendesk-support-work
skills: []
evaluations:
  - Zendesk plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: []
adjacent_bundles:
  - salesforce-service-cloud
  - hubspot-sales-hub
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
  - "Not a complete Zendesk implementation, migration, object schema, API, pricing, packaging, plan, add-on, limit, release, Explore, AI agent, or app marketplace reference."
  - "Requires user-provided Zendesk account evidence before final conclusions about ticket fields, forms, statuses, brands, channels, groups, organizations, views, macros, triggers, automations, routing, SLAs, reports, permissions, AI agents, integrations, or API behavior."
  - "Does not replace Zendesk administrator, support operations, CX leadership, security, privacy, legal, procurement, deliverability, accessibility, AI governance, or change-management review."
safety_notes:
  - "Require explicit confirmation before sending customer communications, exporting or modifying customer data, changing tickets/users/organizations, activating triggers or automations, changing routing or permissions, publishing Help Center content, enabling AI/customer-facing behavior, or running integrations/API actions."
  - "Do not request credentials or claim Zendesk account access unless the user provides authorized tool access or evidence."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 26
  okb_score: 33
  absolute_lift: 7
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 9
      okb_score: 10
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 26/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: zendesk
timestamp: "2026-07-09T00:00:00Z"
---

# Zendesk

This bundle helps an agent use Zendesk as a source-aware customer support, helpdesk, ticketing, knowledge, AI agent, reporting, and API platform. It is designed for support operations planning, ticket workflow review, business-rule checks, Help Center and AI agent planning, reporting reconciliation, permission review, and integration planning.

It is a companion tool bundle, not a replacement for customer support, contact center, customer success, support engineering, support operations, Zendesk administration, or CX analytics role bundles.

## Required Answer Habit

For source-sensitive Zendesk work, include a short **Source note** naming the official Zendesk source category, the user-provided account evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-zendesk-support-work.md](commands/plan-zendesk-support-work.md)
- [workflows/plan-ticket-triage-and-routing.md](workflows/plan-ticket-triage-and-routing.md)
- [workflows/review-zendesk-automation-and-ai.md](workflows/review-zendesk-automation-and-ai.md)
- [deliverables/zendesk-change-plan.md](deliverables/zendesk-change-plan.md)
- [evaluations/zendesk-plan-quality-check.md](evaluations/zendesk-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Zendesk Help, Zendesk Developer documentation, Zendesk release/product/commercial pages when current packaging or limits matter, and user-provided Zendesk account evidence. Do not invent subdomains, brands, channels, ticket fields, forms, statuses, groups, organizations, views, macros, triggers, automations, routing rules, SLA policies, report filters, permissions, AI agent settings, knowledge-source behavior, API syntax, or integration behavior.
