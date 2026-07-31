---
type: Bundle Index
title: E-commerce Marketing Manager
description: Source-aware role bundle for e-commerce growth planning, merchandising and offer review, channel and lifecycle coordination, performance analysis, and approval-ready commerce briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- ecommerce-marketing
- merchandising
- commerce-growth
- role
aliases:
- E-commerce Marketing Manager
- Ecommerce Marketing Manager
problems_solved:
- Prepare e-commerce marketing and merchandising brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- E-commerce
- Retail
tools: []
frameworks:
- source-evidence matrix
- commerce-evidence matrix
- qualified-review gate
deliverables:
- E-commerce marketing and merchandising brief
commands: []
skills: []
evaluations:
- E-commerce Marketing Manager source-awareness check
okb_bundle_id: e-commerce-marketing-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- ccpa
- gdpr
- meta-ads-manager
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-2021.00
  soc: []
  isco_08: []
  esco:
  - 6fcf4638-e7c7-4978-9302-9a7b63a3d57c
limitations:
- Use as broad marketing-management context; catalog, pricing, inventory, claims, promotions, channels, customer consent, orders, returns, budgets, and outcomes require current evidence.
- Task-specific work requires current evidence for business objective and customer segment, catalog, price, inventory, and margin evidence, approved offer and claims, channel and lifecycle configuration, consent and suppression state, orders, returns, and analytics definitions, budget and promotional authority.
- Do not infer inventory, prices, margin, offer terms, orders, returns, consent, campaign performance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before pricing, promotions, inventory, customer data, consent, communications, spend, or public claims.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 6
  okb_score: 32
  absolute_lift: 26
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 2
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 6/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# E-commerce Marketing Manager

Source-aware role bundle for e-commerce growth planning, merchandising and offer review, channel and lifecycle coordination, performance analysis, and approval-ready commerce briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/ecommerce-marketing-brief.md](deliverables/ecommerce-marketing-brief.md)
