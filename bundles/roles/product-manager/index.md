---
type: Bundle Index
title: Product Manager
description: Entry point for the Product Manager OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [product-management, product-strategy, requirements, roadmap, discovery]
aliases: [PM, product owner, software product manager, digital product manager, technical product manager]
problems_solved:
  - frame product opportunities
  - draft product requirements
  - prioritize roadmap options
  - review product metrics
  - align stakeholders on product decisions
industries: [software, saas, digital-products, internal-tools]
tools: [Jira, Linear, Confluence, Notion, Figma, Amplitude, Mixpanel, Productboard, Aha!]
frameworks: [Jobs-to-be-Done, RICE prioritization, Kano model, opportunity solution tree, North Star metric, Scrum]
deliverables: [product brief, product requirements document, roadmap narrative, opportunity assessment, metric review]
commands: [/draft-product-brief, /review-prd, /prioritize-roadmap]
skills: []
evaluations: [product-management-quality-check]
okb_bundle_id: product-manager
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: [agile, amplitude, confluence, figma, jira, jobs-to-be-done, kano-model, linear, mixpanel, okrs, product-requirements-document, product-roadmap, rice-prioritization, scrum]
adjacent_bundles: [performance-marketer]
contributors: []
maintainers: []
standard_mappings:
  onet_soc: ["11-2021.00"]
  soc: ["11-2021"]
  isco_08: ["1221"]
  esco: ["1221"]
limitations:
  - Product management scope varies by organization; verify local ownership, process, and decision rights.
  - Does not replace legal, privacy, security, accessibility, finance, medical, or regulated-domain review.
  - Does not include tool-specific API or workspace configuration details.
safety_notes:
  - Confirm before modifying live product docs, tickets, roadmap systems, analytics definitions, feature flags, pricing, release notes, or customer communications.
  - Treat customer data, roadmap plans, product strategy, sales feedback, and research notes as confidential unless the user confirms they are safe to use.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 19
  okb_score: 25
  absolute_lift: 6
  task_scores:
    - task: prd-from-support-tickets
      baseline_score: 8
      okb_score: 11
      max_score: 12
    - task: roadmap-prioritization
      baseline_score: 5
      okb_score: 6
      max_score: 12
    - task: metric-discrepancy-review
      baseline_score: 6
      okb_score: 8
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 19/36 to 25/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
timestamp: 2026-07-09T00:00:00Z
---

# Product Manager

This bundle helps an agent support product-management work: framing customer problems, drafting requirements, prioritizing roadmap options, reviewing metrics, and preparing decision-ready product artifacts.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)
- [Responsibilities](responsibilities/index.md)

## Workflows

- [Define Product Opportunity](workflows/define-product-opportunity.md)
- [Write PRD](workflows/write-prd.md)
- [Prioritize Roadmap](workflows/prioritize-roadmap.md)
- [Review Product Metrics](workflows/review-product-metrics.md)

## Deliverables and Commands

- [Product Brief](deliverables/product-brief.md)
- [Product Requirements Document](deliverables/prd.md)
- [Roadmap Narrative](deliverables/roadmap-narrative.md)
- [/draft-product-brief](commands/draft-product-brief.md)
- [/review-prd](commands/review-prd.md)
- [/prioritize-roadmap](commands/prioritize-roadmap.md)

Use this bundle as decision support, not as authority to make commitments or change live systems without confirmation.
