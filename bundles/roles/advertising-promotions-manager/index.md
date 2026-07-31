---
type: Bundle Index
title: Advertising / Promotions Manager
description: Source-aware role bundle for advertising and promotions strategy, creative and media review, budget governance, campaign measurement, and approval-ready decision briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- advertising-management
- promotions
- media-planning
- role
aliases:
- Advertising Manager
- Promotions Manager
problems_solved:
- Plan advertising without fabricated commercial facts.
- Reconcile creative, media, budget, and measurement evidence.
- Separate recommendations from authorized spend and launch.
industries:
- Advertising
- Marketing
tools: []
frameworks:
- source-evidence matrix
- campaign-governance matrix
- qualified-review gate
deliverables:
- Advertising and promotions decision brief
commands: []
skills: []
evaluations:
- Advertising / Promotions Manager source-awareness check
okb_bundle_id: advertising-promotions-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- gdpr
- hubspot-sales-hub
- meta-ads-manager
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-2011.00
  soc: []
  isco_08: []
  esco:
  - '2431.1'
limitations:
- Campaign-specific work requires current audience, claim, creative, rights, media, budget, contract, and result evidence.
- This bundle does not establish legal compliance.
- Do not infer rights, rates, budget, approval, delivery, or performance.
safety_notes:
- Minimize audience and customer data.
- Require confirmation before contracting, spending, publishing, targeting, or tracking changes.
- Route legal, privacy, regulated-category, discrimination, and claim decisions to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 9
  okb_score: 32
  absolute_lift: 23
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 9/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Advertising / Promotions Manager

Source-aware role bundle for advertising and promotions strategy, creative and media review, budget governance, campaign measurement, and approval-ready decision briefs.

## Required Answer Habit

Include a short **Source note** naming authoritative source categories and local
evidence used, assumptions made, and missing verification required before reliance.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name the source category, scope, date or version, and conflict checks required.
4. **Confirmation boundary** - identify the accountable reviewer and actions that must not occur without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not collapse missing evidence into a general disclaimer. Ask for the exact artifacts needed and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/advertising-promotions-brief.md](deliverables/advertising-promotions-brief.md)
