---
type: Bundle Index
title: Linear
description: Tool bundle for source-aware Linear planning, issue triage, project/cycle review, GraphQL API evidence handling, and safe workflow recommendations.
schema_version: 0.1.0
bundle_format: okf-compatible
category: tools
tags:
  - linear
  - issue-tracking
  - product-delivery
  - engineering-planning
  - project-management
aliases:
  - Linear issue tracking
  - Linear projects
  - Linear cycles
problems_solved:
  - Plan Linear issue and project workflows without inventing teams, cycles, statuses, labels, fields, automations, or API results.
  - Separate Linear product/API behavior from local workspace configuration and user-provided issue evidence.
  - Review product-delivery work with explicit scope, ownership, priority, dependency, and permission caveats.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
  - Linear
frameworks:
  - issue triage review
  - project planning review
  - GraphQL evidence review
deliverables:
  - Linear work planning brief
commands:
  - /plan-linear-workflow
skills:
evaluations:
  - Linear guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - technical-product-manager
adjacent_bundles:
  - jira
  - agile
  - scrum
  - product-roadmap
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
  - Not a complete Linear implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Linear usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before creating, editing, assigning, closing, deleting, importing, exporting, or automating Linear issues, projects, cycles, teams, comments, integrations, webhooks, or API actions.
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
  okb_score: 30
  absolute_lift: 7
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 8
      okb_score: 10
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 7
      okb_score: 9
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 23/36 to 30/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: linear
timestamp: "2026-07-09T00:00:00Z"
---

# Linear

This bundle helps an agent work with Linear while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Linear work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [Command](commands/plan-linear-workflow.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/linear-brief.md)
- [Evaluation](evaluations/linear-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Linear Developers](https://linear.app/developers) for source behavior and framework grounding. Use user-provided evidence for ['workspace, team, issue, project, cycle, label, status, priority, assignee, estimate, dependency, automation, Git integration, and API permission evidence']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
