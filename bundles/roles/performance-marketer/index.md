---
type: Bundle Index
title: Performance Marketer
description: Entry point for the Performance Marketer OpenKnowledge bundle.
tags: [marketing, paid-acquisition, growth]
okb_bundle_id: performance-marketer
okb_bundle_version: "0.1.0"
status: beta
timestamp: 2026-06-19T00:00:00Z
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 8
  okb_score: 15
  absolute_lift: 7
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 5
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 4
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 6
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 8/36 to 15/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Performance Marketer

This bundle contains role knowledge for an LLM agent operating as a performance marketer.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)

## Sections

- `responsibilities/`
- `frameworks/`
- `workflows/`
- `playbooks/`
- `metrics/`
- `tools/`
- `deliverables/`
- `commands/`
- `evaluations/`
- `examples/`
- `references/`

## Improvement Loop

When users find missing or weak guidance, record private feedback first, then propose reviewed improvements. Public changes should avoid private user context and require approval before contribution.
