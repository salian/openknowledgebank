---
type: Bundle Index
title: Product Roadmap
description: Deliverable bundle for creating and reviewing product roadmaps without inventing strategy, dates, priorities, capacity, dependencies, or stakeholder commitments.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
  - product-roadmap
  - roadmapping
  - product-strategy
  - prioritization
  - planning
aliases:
  - roadmap
  - product roadmap
  - agile roadmap
  - now next later roadmap
problems_solved:
  - Connect roadmap items to strategy, goals, evidence, priorities, and progress.
  - Separate roadmap intent from delivery plans, release commitments, and task backlogs.
  - Review roadmap communication for audience, confidence, dependencies, and update cadence.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
frameworks:
  - roadmap evidence review
  - strategy-to-execution alignment
  - stakeholder communication
deliverables:
  - Product Roadmap
commands:
  - /review-product-roadmap
skills:
evaluations:
  - Product Roadmap guidance quality check
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
  - rice-prioritization
  - product-requirements-document
  - jira
  - okrs
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
  - Not a complete Product Roadmap implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Product Roadmap usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before publishing dates, commitments, customer promises, staffing implications, or release plans without authority, evidence, and stakeholder approval.
  - Do not claim access to private systems, customer data, workspaces, documents, dashboards, roadmaps, repositories, accounts, or source records unless the user provides evidence or authorized tool access.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 25
  okb_score: 31
  absolute_lift: 6
  task_scores:
    - task: deliverable-draft-with-missing-evidence
      baseline_score: 10
      okb_score: 10
      max_score: 12
    - task: deliverable-quality-review
      baseline_score: 7
      okb_score: 10
      max_score: 12
    - task: deliverable-reconciliation
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 25/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: product-roadmap
timestamp: "2026-07-09T00:00:00Z"
---

# Product Roadmap

This bundle helps an agent work with Product Roadmap while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Product Roadmap work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [deliverable.md](deliverable.md)
- [Command](commands/review-product-roadmap.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/product-roadmap-brief.md)
- [Evaluation](evaluations/product-roadmap-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Atlassian product roadmap guide](https://www.atlassian.com/agile/product-management/product-roadmaps) for source behavior and framework grounding. Use user-provided evidence for ['strategy, goals, themes, initiatives, evidence, priority rationale, dependencies, capacity, confidence, audience, time horizon, commitments, and update process']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
