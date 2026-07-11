---
type: Bundle Index
title: Technical Sales Representative (Technical and Scientific Products)
description: Source-aware role bundle for technical sales scoping, customer evidence
  review, product-fit reasoning, proposal support, and qualified-review-ready decision
  support.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- technical-sales
- sales
- scientific-products
- technical-products
- role
aliases:
- Technical Sales Representative
- Sales Representatives, Wholesale and Manufacturing, Technical and Scientific Products
- O*NET 41-4011.00
problems_solved:
- Route technical sales requests to the right product, customer, commercial, and source-evidence
  checks.
- Separate source-confirmed role facts, user-provided account facts, assumptions,
  and missing evidence.
- Produce a technical-sales source-aware brief suitable for qualified review.
industries:
- Wholesale and manufacturing
- Technical products
- Scientific products
tools: []
frameworks:
- source-evidence matrix
- inspect-first workflow
- qualified-review gate
deliverables:
- Technical sales source-aware brief
commands: []
skills: []
evaluations:
- Technical sales source-awareness check
okb_bundle_id: technical-sales-representative-technical-and-scientific-products
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- hubspot-sales-hub
- sales-development-representative-sdr
- sales-representative-of-services
- salesforce-service-cloud
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-4011.00
  soc: []
  isco_08:
  - '3322'
  esco:
  - '3322'
limitations:
- This bundle is not legal, financial, medical, safety, engineering, tax, export-control,
  procurement, contracting, or scientific advice.
- Scenario-specific answers require current product documentation, approved claims,
  customer evidence, commercial authority, local records, and qualified review.
- Do not infer product capabilities, technical fit, pricing, discounts, delivery commitments,
  contractual terms, customer status, compliance claims, or CRM facts without evidence.
safety_notes:
- Minimize sensitive customer, pricing, contract, security, personal, scientific,
  regulated, and proprietary product data in prompts and examples.
- Require explicit confirmation before sending customer messages, changing CRM records,
  committing pricing or delivery terms, sharing proposals, exporting customer data,
  or making public claims.
- Route final reliance to a qualified sales owner, product specialist, solution engineer,
  legal/commercial reviewer, or accountable business reviewer.
timestamp: '2026-07-11T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-11'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 16
  okb_score: 31
  absolute_lift: 15
  task_scores:
  - task: role-task-with-limited-evidence
    baseline_score: 7
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 9
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 16/36 to 31/36 across 3 benchmark
    tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Technical Sales Representative (Technical and Scientific Products)

Source-aware role bundle for technical sales scoping, customer evidence review, product-fit reasoning, proposal support, and qualified-review-ready decision support.

## Required Answer Habit

Include a short **Source note** naming the authoritative role, product, customer, commercial, or technical source category; local evidence used; and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
