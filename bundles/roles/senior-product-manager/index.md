---
type: Bundle Index
title: Senior Product Manager
description: Entry point for the Senior Product Manager OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [product-management, product-strategy, roadmap, requirements, product-metrics, stakeholder-alignment]
aliases: [Senior PM, Sr PM, senior software product manager, senior digital product manager, product lead]
problems_solved:
  - frame ambiguous product strategy and discovery decisions
  - review roadmap tradeoffs for executive and cross-functional alignment
  - improve PRDs and requirements before delivery work starts
  - reconcile product metric conflicts without inventing definitions
  - turn stakeholder disagreement into explicit options, risks, and decisions
industries: [software, saas, digital-products, platforms, internal-tools]
tools: [Jira, Linear, Confluence, Notion, Figma, Amplitude, Mixpanel, Productboard, Aha!, spreadsheets, BI dashboards]
frameworks: [Jobs-to-be-Done, RICE prioritization, Kano model, opportunity solution tree, OKRs, North Star metric, evidence-to-decision matrix, product risk review]
deliverables: [strategy brief, roadmap decision memo, PRD review, metric interpretation memo, stakeholder alignment memo]
commands: [/draft-strategy-brief, /review-roadmap-tradeoffs, /review-prd]
skills: []
evaluations: [senior-product-management-quality-check]
okb_bundle_id: senior-product-manager
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: [agile, figma, gdpr, jira, okrs]
adjacent_bundles: [product-manager, technical-product-manager, data-product-manager, product-designer, performance-marketer]
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: ["11-2021.00"]
  soc: ["11-2021"]
  isco_08: ["1330"]
  esco: ["1330.6"]
limitations:
  - Product-management scope and seniority vary by organization; verify local ownership, decision rights, and escalation paths.
  - This bundle does not replace legal, privacy, security, accessibility, medical, financial, procurement, or regulated-domain review.
  - This bundle does not include authoritative tool-specific schemas, APIs, workspace fields, analytics definitions, or live system permissions.
  - Taxonomy mappings are broad role adjacencies and should not be treated as a precise seniority-specific occupation code.
safety_notes:
  - Confirm before changing live product docs, tickets, roadmap systems, analytics definitions, feature flags, pricing, release notes, customer communications, or external commitments.
  - Treat customer data, roadmap plans, product strategy, sales feedback, support tickets, and research notes as confidential unless the user confirms they are safe to use.
  - Require qualified review for regulated-domain, legal, privacy, security, accessibility, medical, financial, employment, or contractual conclusions.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 20
  absolute_lift: 3
  task_scores:
    - task: strategy-brief-ambiguous-bet
      baseline_score: 5
      okb_score: 5
      max_score: 12
    - task: prd-review-missing-evidence
      baseline_score: 7
      okb_score: 8
      max_score: 12
    - task: metric-discrepancy-review
      baseline_score: 5
      okb_score: 7
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 17/36 to 20/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
timestamp: 2026-07-09T00:00:00Z
---

# Senior Product Manager

This bundle helps an agent support senior product-management work: turning ambiguous product problems into evidence-aware decisions, strategy briefs, roadmap tradeoffs, PRD reviews, metric interpretations, and stakeholder alignment memos.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)
- [Responsibilities](responsibilities/index.md)

## Workflows

- [Senior Product Strategy](workflows/senior-product-strategy.md)
- [Executive Roadmap Alignment](workflows/executive-roadmap-alignment.md)
- [PRD and Requirements Review](workflows/prd-and-requirements-review.md)
- [Product Metric Review](workflows/product-metric-review.md)
- [Stakeholder Escalation](workflows/stakeholder-escalation.md)

## Deliverables and Commands

- [Strategy Brief](deliverables/strategy-brief.md)
- [Roadmap Decision Memo](deliverables/roadmap-decision-memo.md)
- [PRD Review](deliverables/prd-review.md)
- [Metric Interpretation Memo](deliverables/metric-interpretation-memo.md)
- [Stakeholder Alignment Memo](deliverables/stakeholder-alignment-memo.md)
- [/draft-strategy-brief](commands/draft-strategy-brief.md)
- [/review-roadmap-tradeoffs](commands/review-roadmap-tradeoffs.md)
- [/review-prd](commands/review-prd.md)

Use this bundle as decision support. It does not authorize the agent to make commitments, modify live systems, or treat unverified product evidence as fact.
