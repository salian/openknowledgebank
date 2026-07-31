---
type: Bundle Index
title: AIDA Model
description: Source-aware framework bundle for attention, interest, desire, action, audience, message, channel, evidence, measurement, and ethical marketing review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- aida-model
- framework
- source-aware
aliases:
- AIDA Model
problems_solved:
- Prepare a aida model application brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- source-evidence matrix
- AIDA Model application matrix
- qualified-review gate
deliverables:
- AIDA Model application brief
commands: []
skills: []
evaluations:
- AIDA Model source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- advertising-promotions-manager
- performance-marketing-manager
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
- Use the listed authoritative or identified source surfaces for general AIDA Model guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for source interpretation and model variant, audience and need evidence, offer and substantiation, message and creative, channel and placement, stage definitions, conversion event, attribution window, baseline, experiment design, consent and policy constraints, approvals, and results.
- Do not infer audience intent, stage, causal effect, claim validity, conversion attribution, performance, consent, or approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that publish content, launch or change campaigns, spend budget, contact audiences, collect or export personal data, make unsupported claims, or alter live conversion tracking.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: aida-model
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 34
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: framework-application-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# AIDA Model

Source-aware framework bundle for attention, interest, desire, action, audience, message, channel, evidence, measurement, and ethical marketing review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/aida-model-brief.md](deliverables/aida-model-brief.md)
