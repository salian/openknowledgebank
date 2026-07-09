---
type: Bundle Index
title: Jobs to be Done / Outcome-Driven Innovation
description: Framework bundle for applying Jobs to be Done and Outcome-Driven Innovation without inventing customer research, job maps, outcomes, or opportunity scores.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - jobs-to-be-done
  - jtbd
  - outcome-driven-innovation
  - customer-research
  - product-strategy
aliases:
  - JTBD
  - Jobs to be Done
  - Outcome-Driven Innovation
  - ODI
problems_solved:
  - Frame customer research around jobs and desired outcomes without inventing interviews or evidence.
  - Separate JTBD/ODI source concepts from local market, segment, and customer evidence.
  - Draft opportunity briefs that expose assumptions, missing research, outcome statements, and prioritization risks.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
frameworks:
  - Jobs to be Done
  - Outcome-Driven Innovation
  - job map
  - outcome statement review
deliverables:
  - JTBD opportunity brief
commands:
  - /review-jtbd-opportunity
skills:
evaluations:
  - Jobs to be Done / Outcome-Driven Innovation guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - data-product-manager
  - technical-product-manager
  - product-designer
adjacent_bundles:
  - kano-model
  - rice-prioritization
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
  - Not a complete Jobs to be Done / Outcome-Driven Innovation implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Jobs to be Done / Outcome-Driven Innovation usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before claiming customer needs, market opportunity, prioritization scores, or roadmap recommendations without verified research evidence.
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
  okb_score: 28
  absolute_lift: 7
  task_scores:
    - task: framework-fit-review
      baseline_score: 4
      okb_score: 9
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 8
      okb_score: 10
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 9
      okb_score: 9
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 21/36 to 28/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: jobs-to-be-done
timestamp: "2026-07-09T00:00:00Z"
---

# Jobs to be Done / Outcome-Driven Innovation

This bundle helps an agent work with Jobs to be Done / Outcome-Driven Innovation while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Jobs to be Done / Outcome-Driven Innovation work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [framework.md](framework.md)
- [Command](commands/review-jtbd-opportunity.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/jobs-to-be-done-brief.md)
- [Evaluation](evaluations/jobs-to-be-done-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Strategyn Jobs to be Done](https://strategyn.com/jobs-to-be-done/) for source behavior and framework grounding. Use user-provided evidence for ['target market, customer segment, job performer, interviews, survey evidence, job steps, desired outcomes, importance/satisfaction data, opportunity scores, and product constraints']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
