---
type: Bundle Index
title: Jira
description: "Tool bundle for source-aware Jira work tracking, board, backlog, workflow, JQL, report, automation, and REST API planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - jira
  - jira-software
  - work-tracking
  - agile
  - jql
  - project-management
aliases:
  - Jira Software
  - Jira Cloud
  - Atlassian Jira
problems_solved:
  - Plan Jira board, backlog, workflow, and report work without inventing local fields, statuses, filters, permissions, or issue data.
  - Separate official Atlassian product behavior from user-provided Jira site evidence.
  - Create source-scoped JQL, reporting, automation, and REST API plans with verification and confirmation boundaries.
  - Reconcile board, report, JQL, and API differences by aligning scope, filters, permissions, time windows, and status logic.
industries:
  - software
  - digital-products
  - technology
  - support
  - professional-services
tools:
  - Jira
  - Jira Software
  - Jira Cloud
  - JQL
  - Jira Automation
  - Jira Cloud REST API
frameworks:
  - verify-first Jira evidence review
  - board-report-query reconciliation
  - workflow change confirmation boundary
deliverables:
  - Jira board cleanup plan
commands:
  - /plan-jira-board-cleanup
skills: []
evaluations:
  - Jira planning quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
adjacent_bundles:
  - agile
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
  - "Not a complete Jira administration, Data Center, pricing, plan, Marketplace app, Rovo, REST API, automation, or release-feature reference."
  - "Requires user-provided Jira site, space/project, board, workflow, field, permission, report, automation, and API evidence before final conclusions."
  - "Does not replace security, privacy, procurement, legal, compliance, administrator, scrum master, project manager, product owner, or engineering-lead review."
safety_notes:
  - "Require explicit confirmation before creating, editing, transitioning, deleting, commenting on, exporting, bulk changing, or moving Jira work items; changing workflows, statuses, boards, filters, dashboards, permissions, automations, notifications, or API-connected actions."
  - "Do not claim access to Jira sites, projects/spaces, boards, workflows, work items/issues, reports, automations, users, groups, permissions, or API results unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric
  tasks_count: 0
  display_summary: "Measured evaluation is blocked until a Jira task set and model/provider configuration are selected."
  evidence_note: "No raw prompts or outputs are included in the public bundle."
evaluation_detail: {}
okb_bundle_id: jira
timestamp: "2026-07-09T00:00:00Z"
---

# Jira

This bundle helps an agent use Jira as a source-aware work-tracking, planning, reporting, workflow, JQL, automation, and integration tool. It is designed for Jira board cleanup, backlog and sprint planning, workflow review, report/JQL reconciliation, automation planning, and REST API evidence requests.

It is a companion tool bundle, not a replacement for role bundles such as product manager, scrum master, software engineer, QA analyst, project manager, product operations manager, or engineering leader.

## Required Answer Habit

For source-sensitive Jira work, include a short **Source note** naming the official Atlassian source category, the user-provided Jira site/project/space/board/workflow/report/API evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-jira-board-cleanup.md](commands/plan-jira-board-cleanup.md)
- [workflows/review-jira-board-and-backlog.md](workflows/review-jira-board-and-backlog.md)
- [workflows/plan-jira-jql-and-report.md](workflows/plan-jira-jql-and-report.md)
- [deliverables/jira-board-cleanup-plan.md](deliverables/jira-board-cleanup-plan.md)
- [evaluations/jira-planning-quality-check.md](evaluations/jira-planning-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Atlassian Jira product pages, Jira Software Cloud Support, Jira Cloud Administration Support, Jira Automation Support, and Atlassian Developer Jira Cloud REST API documentation for product behavior, plus user-provided Jira instance evidence. Do not invent site names, project/space keys, board filters, statuses, transitions, work item types, custom fields, reports, automations, permissions, users, groups, API scopes, endpoints, payloads, or issue/work-item data.
