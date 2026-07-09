---
type: Bundle Index
title: Kano Model
description: Framework bundle for using the Kano Model to classify feature expectations without inventing survey responses, customer segments, or feature categories.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - kano-model
  - customer-satisfaction
  - feature-prioritization
  - product-research
  - quality
aliases:
  - Kano analysis
  - Kano customer satisfaction model
  - Attractive quality and must-be quality
problems_solved:
  - Classify product features with explicit customer evidence rather than assumed delighters or basics.
  - Design Kano-style research plans that separate functional/dysfunctional questions, segments, and category uncertainty.
  - Explain how feature categories can vary by customer segment and change over time.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
  - cross-industry
tools:
frameworks:
  - Kano Model
  - functional/dysfunctional question pair
  - feature category review
deliverables:
  - Kano feature classification brief
commands:
  - /review-kano-features
skills:
evaluations:
  - Kano Model guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
  - senior-product-manager
  - product-designer
adjacent_bundles:
  - jobs-to-be-done
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
  - Not a complete Kano Model implementation, administration, legal, research, or professional-advice reference.
  - Requires user-provided local evidence before final conclusions about Kano Model usage, readiness, scoring, configuration, or commitments.
  - Does not replace qualified product, design, engineering, data, legal, privacy, security, or administrator review.
safety_notes:
  - Require confirmation before labeling features as must-be, performance, attractive, indifferent, reverse, or questionable without validated customer research.
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
  okb_score: 31
  absolute_lift: 8
  task_scores:
    - task: framework-fit-review
      baseline_score: 6
      okb_score: 10
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 9
      okb_score: 10
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 8
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 23/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: kano-model
timestamp: "2026-07-09T00:00:00Z"
---

# Kano Model

This bundle helps an agent work with Kano Model while keeping source facts, local evidence, assumptions, and risky actions explicit. It is designed for product, design, engineering, data, and operations workflows where plausible generic guidance is not enough.

## Required Answer Habit

For Kano Model work, include a short **Source note** naming the official source category, the user-provided local evidence used, and missing evidence required before treating a conclusion as final.

## Start Here

- [framework.md](framework.md)
- [Command](commands/review-kano-features.md)
- [Primary workflow](workflows/review-evidence.md)
- [Planning workflow](workflows/plan-output.md)
- [Deliverable](deliverables/kano-model-brief.md)
- [Evaluation](evaluations/kano-model-quality-check.md)
- [Source checks](references/source-checks.md)

## Official Source Categories

Use [Noriaki Kano attractive quality article record](https://www.jstage.jst.go.jp/article/quality/14/2/14_KJ00002952366/_article/-char/en) for source behavior and framework grounding. Use user-provided evidence for ['feature list, customer segment, functional/dysfunctional survey wording, response data, sample size, product context, current expectations, and decision criteria']. Do not invent local facts, account state, research findings, estimates, permissions, dates, metrics, or commitments.
