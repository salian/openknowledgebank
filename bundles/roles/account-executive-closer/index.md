---
type: Bundle Index
title: Account Executive (Closer)
description: Source-aware role bundle for discovery planning, opportunity evidence review, proposal support, objection preparation, forecast hygiene, and authorized close handoff.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- account-executive
- sales
- deal-management
- role
aliases:
- Account Executive
- Closing Account Executive
problems_solved:
- Prepare deals without fabricated customer signals.
- Draft proposals within approved product and commercial facts.
- Maintain forecast reasoning with explicit uncertainty.
industries:
- Sales
- B2B
tools: []
frameworks:
- source-evidence matrix
- deal-evidence matrix
- qualified-review gate
deliverables:
- Source-aware opportunity and close brief
commands: []
skills: []
evaluations:
- Account Executive (Closer) source-awareness check
okb_bundle_id: account-executive-closer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- docusign
- hubspot-sales-hub
- salesforce-service-cloud
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-4012.00
  soc: []
  isco_08: []
  esco:
  - C3322
limitations:
- Opportunity-specific work requires current customer, product, CRM, pricing, legal, and approval evidence.
- This bundle does not authorize commitments or signatures.
- Do not infer intent, authority, budget, timing, fit, pricing, or contract status.
safety_notes:
- Minimize customer, pricing, contract, and personal data.
- Require confirmation before sending, quoting, discounting, changing CRM, or accepting terms.
- Route legal, commercial, security, and compliance commitments to accountable reviewers.
timestamp: '2026-07-29T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 12
  okb_score: 27
  absolute_lift: 15
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 7
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 12/36 to 27/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Account Executive (Closer)

Source-aware role bundle for discovery planning, opportunity evidence review, proposal support, objection preparation, forecast hygiene, and authorized close handoff.

## Required Answer Habit

Include a short **Source note** naming the source categories and local evidence
used, assumptions made, and missing verification required before reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/opportunity-close-brief.md](deliverables/opportunity-close-brief.md)
