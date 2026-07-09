---
type: Bundle Index
title: Confluence
description: Tool bundle for source-aware Confluence documentation, page review, knowledge-base planning, REST API evidence handling, and permission-safe collaboration workflows.
schema_version: 0.1.0
bundle_format: okf-compatible
category: tools
tags:
  - confluence
  - atlassian
  - knowledge-management
  - product-documentation
  - collaboration
aliases:
  - Atlassian Confluence
  - Confluence Cloud
  - Confluence knowledge base
problems_solved:
  - Plan Confluence documentation without inventing spaces, pages, owners, permissions, labels, page trees, or API fields.
  - Review knowledge-base and product documentation evidence with source, version, permission, and stakeholder caveats.
  - Draft documentation briefs that connect Confluence content to product, support, engineering, and release workflows.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
  - Confluence
frameworks:
  - source-aware documentation review
  - page and space evidence review
  - permission confirmation boundary
deliverables:
  - Confluence documentation brief
commands:
  - /plan-confluence-documentation
skills:
evaluations:
  - Confluence guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - data-product-manager
  - technical-product-manager
adjacent_bundles:
  - jira
  - product-requirements-document
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
  - Not a complete Confluence implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Confluence usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before editing, deleting, moving, publishing, restricting, exporting, archiving, or sharing Confluence pages, spaces, comments, attachments, templates, or API-connected content.
  - Do not claim access to private systems, customer data, workspaces, documents, dashboards, roadmaps, repositories, accounts, or source records unless the user provides evidence or authorized tool access.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 24
  okb_score: 31
  absolute_lift: 7
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 9
      okb_score: 11
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 9
      okb_score: 9
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 6
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 24/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: confluence
timestamp: "2026-07-09T00:00:00Z"
---

# Confluence

This bundle helps an agent work with Confluence while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Confluence work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [Command](commands/plan-confluence-documentation.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/confluence-brief.md)
- [Evaluation](evaluations/confluence-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Confluence Cloud REST API v2](https://developer.atlassian.com/cloud/confluence/rest/) for source behavior and framework grounding. Use user-provided evidence for ['site URL, space key, page IDs, owners, labels, restrictions, app configuration, API scopes, permissions, templates, and current content exports']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
