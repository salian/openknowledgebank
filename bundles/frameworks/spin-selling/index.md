---
type: Bundle Index
title: SPIN Selling
description: Source-aware framework bundle for situation, problem, implication, need-payoff, buyer evidence, questioning, value, ethics, and sales progression review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- spin-selling
- framework
- source-aware
aliases:
- SPIN Selling
problems_solved:
- Prepare a spin selling application brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- source-evidence matrix
- SPIN Selling application matrix
- qualified-review gate
deliverables:
- SPIN Selling application brief
commands: []
skills: []
evaluations:
- SPIN Selling source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- account-executive-closer
- sales-manager
adjacent_bundles: []
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
- Use the listed authoritative or identified source surfaces for general SPIN Selling guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for source version and local sales policy, account and contact context, buyer-provided situation, problems and consequences, need-payoff language, question plan, call notes or recording with consent, opportunity criteria, product evidence, pricing authority, owner, and approvals.
- Do not infer buyer situation, problem, implication, need, value, intent, opportunity stage, consent, forecast, or commitment.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that contact or record a prospect, store sensitive buyer data, change CRM or forecast state, advance or disqualify an opportunity, commit pricing or terms, or make unsupported product or outcome claims.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: spin-selling
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 14
  okb_score: 34
  absolute_lift: 20
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: framework-application-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# SPIN Selling

Source-aware framework bundle for situation, problem, implication, need-payoff, buyer evidence, questioning, value, ethics, and sales progression review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/spin-selling-brief.md](deliverables/spin-selling-brief.md)
