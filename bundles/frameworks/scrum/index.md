---
type: Bundle Index
title: Scrum
description: "Framework hub bundle for applying Scrum using the official Scrum Guide structure without inventing local team practice, tool settings, or delivery metrics."
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - scrum
  - agile
  - software-delivery
  - product-development
  - sprint-planning
aliases:
  - Scrum framework
  - Scrum Guide
  - Scrum process
  - sprint operating model
problems_solved:
  - Review Scrum practice against source-grounded accountabilities, events, artifacts, commitments, and values.
  - Separate official Scrum framework terms from local team workflow, tooling, and governance choices.
  - Draft Scrum operating briefs without inventing sprint metrics, board fields, Definition of Done, or team policy.
industries:
  - software
  - digital-products
  - technology
  - b2b-saas
tools: []
frameworks:
  - Scrum
  - Scrum Guide
  - Sprint
  - Product Goal
  - Sprint Goal
  - Definition of Done
deliverables:
  - Scrum operating brief
commands:
  - /review-scrum-practice
skills: []
evaluations:
  - Scrum guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - agile
  - product-manager
  - senior-product-manager
  - data-product-manager
  - technical-product-manager
adjacent_bundles:
  - jira
  - okrs
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
  - "Not a substitute for Scrum training, organizational coaching, HR policy, contract advice, or delivery governance."
  - "Requires user-provided local evidence before judging actual team practice, sprint cadence, Definition of Done, metrics, tooling, or stakeholder process."
  - "Does not prescribe a universal sprint length, velocity target, estimation method, board setup, or reporting cadence."
safety_notes:
  - "Require confirmation before changing live boards, sprint commitments, Definition of Done, release plans, staffing responsibilities, stakeholder communications, or customer-facing delivery promises."
  - "Do not claim access to private backlogs, sprint metrics, team policies, source repositories, product plans, or delivery tools unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 20
  okb_score: 34
  absolute_lift: 14
  task_scores:
    - task: framework-fit-review
      baseline_score: 4
      okb_score: 12
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 7
      okb_score: 11
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 9
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 20/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: scrum
timestamp: "2026-07-09T00:00:00Z"
---

# Scrum

This bundle helps an agent use Scrum as a lightweight framework for complex product work. It keeps the official Scrum Guide structure visible while requiring local evidence before judging a team's actual practice or recommending process changes.

## Required Answer Habit

For Scrum work, include a short **Source note** naming the Scrum source category, the user-provided team or delivery evidence used, and missing local evidence required before treating a recommendation as specific to the user's organization.

## Start Here

- [framework.md](framework.md)
- [frameworks/scrum-guide-lens.md](frameworks/scrum-guide-lens.md)
- [commands/review-scrum-practice.md](commands/review-scrum-practice.md)
- [workflows/scrum-adoption-review.md](workflows/scrum-adoption-review.md)
- [workflows/sprint-operating-review.md](workflows/sprint-operating-review.md)
- [deliverables/scrum-operating-brief.md](deliverables/scrum-operating-brief.md)
- [evaluations/scrum-guidance-quality-check.md](evaluations/scrum-guidance-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use the official Scrum Guide for Scrum accountabilities, events, artifacts, commitments, and values. Use user-provided local evidence for a team's actual workflow, sprint cadence, backlog quality, Definition of Done, release constraints, metrics, tool configuration, governance, and stakeholder process.
