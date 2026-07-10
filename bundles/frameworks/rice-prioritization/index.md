---
type: Bundle Index
title: RICE Prioritization
description: Framework bundle for using RICE prioritization without inventing reach estimates, impact scores, confidence levels, effort sizing, or roadmap commitments.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - rice
  - prioritization
  - product-management
  - roadmapping
  - decision-making
aliases:
  - RICE scoring
  - Reach Impact Confidence Effort
  - RICE prioritization framework
problems_solved:
  - Score product ideas using explicit reach, impact, confidence, and effort evidence.
  - Expose weak estimates, gaming risks, and missing assumptions before ranking roadmap options.
  - Turn a RICE table into a decision brief with caveats and review steps.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
frameworks:
  - RICE Prioritization
  - reach impact confidence effort scoring
  - confidence discounting
deliverables:
  - RICE prioritization brief
commands:
  - /score-rice-priorities
skills:
evaluations:
  - RICE Prioritization guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - data-product-manager
  - technical-product-manager
adjacent_bundles:
  - product-roadmap
  - product-requirements-document
  - jobs-to-be-done
  - kano-model
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
  - Not a complete RICE Prioritization implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about RICE Prioritization usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before ranking roadmap items or committing delivery order from unsupported estimates, hidden assumptions, or unreviewed stakeholder pressure.
  - Do not claim access to private systems, customer data, workspaces, documents, dashboards, roadmaps, repositories, accounts, or source records unless the user provides evidence or authorized tool access.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 21
  okb_score: 31
  absolute_lift: 10
  task_scores:
    - task: framework-fit-review
      baseline_score: 5
      okb_score: 9
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 8
      okb_score: 11
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 21/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: rice-prioritization
timestamp: "2026-07-09T00:00:00Z"
---

# RICE Prioritization

This bundle helps an agent work with RICE Prioritization while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For RICE Prioritization work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [framework.md](framework.md)
- [Command](commands/score-rice-priorities.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/rice-prioritization-brief.md)
- [Evaluation](evaluations/rice-prioritization-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Intercom RICE prioritization article](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) for source behavior and framework grounding. Use user-provided evidence for ['candidate initiatives, target population, reach window, impact scale, confidence rationale, effort estimate, dependencies, constraints, strategy, and decision owner']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
