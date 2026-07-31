---
type: Bundle Index
title: Key Account Manager / Account Manager
description: Source-aware role bundle for account planning, stakeholder and need review, commercial coordination, renewal and growth planning, and customer-ready account briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- account-management
- key-accounts
- customer-planning
- role
aliases:
- Key Account Manager
- Account Manager
problems_solved:
- Prepare account plans without fabricated customer signals.
- Reconcile commercial and service evidence.
- Separate recommendations from approved commitments.
industries:
- Sales
- Business services
tools: []
frameworks:
- source-evidence matrix
- account-evidence matrix
- qualified-review gate
deliverables:
- Key account plan and decision brief
commands: []
skills: []
evaluations:
- Key Account Manager / Account Manager source-awareness check
okb_bundle_id: key-account-manager-account-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- hubspot-sales-hub
- salesforce-service-cloud
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-3091.00
  soc: []
  isco_08: []
  esco:
  - '2433.1'
limitations:
- Account-specific work requires current customer, contract, service, CRM, and authority evidence.
- This bundle does not establish legal or commercial authority.
- Do not infer satisfaction, intent, risk, renewal, expansion, or stakeholder authority.
safety_notes:
- Minimize customer and personal data.
- Require confirmation before customer messages, CRM edits, pricing, terms, or commitments.
- Route legal, commercial, privacy, and regulated decisions to accountable reviewers.
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
  okb_score: 34
  absolute_lift: 25
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 9/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Key Account Manager / Account Manager

Source-aware role bundle for account planning, stakeholder and need review, commercial coordination, renewal and growth planning, and customer-ready account briefs.

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
- [deliverables/key-account-brief.md](deliverables/key-account-brief.md)
