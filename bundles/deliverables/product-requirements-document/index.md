---
type: Bundle Index
title: Product Requirements Document (PRD)
description: Deliverable bundle for drafting and reviewing Product Requirements Documents without inventing customer evidence, scope, requirements, metrics, or approvals.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
  - prd
  - product-requirements
  - product-management
  - requirements
  - documentation
aliases:
  - PRD
  - Product Requirements Document
  - product requirements
problems_solved:
  - Draft PRDs that separate goals, evidence, requirements, open questions, risks, and decision status.
  - Review PRDs for missing customer, business, technical, design, analytics, and rollout evidence.
  - Prevent PRDs from becoming unsupported commitments or over-detailed pseudo-specs.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
frameworks:
  - requirements evidence review
  - scope and success criteria review
  - stakeholder alignment
deliverables:
  - Product Requirements Document
commands:
  - /draft-prd
skills:
evaluations:
  - Product Requirements Document (PRD) guidance quality check
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
  - product-roadmap
  - confluence
  - jira
  - figma
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
  - Not a complete Product Requirements Document (PRD) implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Product Requirements Document (PRD) usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before turning draft requirements into engineering, customer, legal, launch, or roadmap commitments without stakeholder review and evidence.
  - Do not claim access to private systems, customer data, workspaces, documents, dashboards, roadmaps, repositories, accounts, or source records unless the user provides evidence or authorized tool access.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 19
  okb_score: 31
  absolute_lift: 12
  task_scores:
    - task: deliverable-draft-with-missing-evidence
      baseline_score: 7
      okb_score: 11
      max_score: 12
    - task: deliverable-quality-review
      baseline_score: 6
      okb_score: 10
      max_score: 12
    - task: deliverable-reconciliation
      baseline_score: 6
      okb_score: 10
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 19/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: product-requirements-document
timestamp: "2026-07-09T00:00:00Z"
---

# Product Requirements Document (PRD)

This bundle helps an agent work with Product Requirements Document (PRD) while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Product Requirements Document (PRD) work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [deliverable.md](deliverable.md)
- [Command](commands/draft-prd.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/product-requirements-document-brief.md)
- [Evaluation](evaluations/product-requirements-document-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Atlassian PRD guide](https://www.atlassian.com/agile/product-management/requirements) for source behavior and framework grounding. Use user-provided evidence for ['problem statement, customer evidence, goals, non-goals, users, requirements, constraints, designs, dependencies, metrics, rollout plan, approvals, and open questions']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
