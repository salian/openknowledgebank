---
type: Bundle Index
title: AARRR Pirate Metrics
description: Source-aware framework bundle for acquisition, activation, retention, referral, revenue, event definition, cohort, attribution, funnel, experiment, and growth review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- aarrr-pirate-metrics
- framework
- source-aware
aliases:
- AARRR Pirate Metrics
problems_solved:
- Prepare a aarrr pirate metrics review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- AARRR Pirate Metrics
- source-evidence matrix
- qualified-review gate
deliverables:
- AARRR Pirate Metrics review brief
commands: []
skills: []
evaluations:
- AARRR Pirate Metrics source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- growth-marketing-manager
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
- Use the listed authoritative or identified source surfaces for general AARRR Pirate Metrics guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for source interpretation and local framework variant, product and user scope, event taxonomy and instrumentation, identity and deduplication, acquisition source and attribution, activation definition, cohort and retention window, referral event, revenue definition and refunds, filters and exclusions, source queries, baselines, experiments, privacy, owner, and approvals.
- Do not infer stage definition, event accuracy, identity, cohort retention, attribution, referral, revenue, causal growth, or product outcome.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that change tracking or metric definitions, launch experiments or campaigns, contact users, collect or export personal data, spend budget, publish metrics, or claim causal growth.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: aarrr-pirate-metrics
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 13
  okb_score: 35
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: framework-application-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# AARRR Pirate Metrics

Source-aware framework bundle for acquisition, activation, retention, referral, revenue, event definition, cohort, attribution, funnel, experiment, and growth review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. For an empty-evidence task, write `None` under Verified, Provided, and Assumed. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role. Facts explicitly stated in a non-empty request belong under `Provided` as `Prompt-provided request`; do not invent owner, author, date, version, or provenance.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/aarrr-pirate-metrics-brief.md](deliverables/aarrr-pirate-metrics-brief.md)
