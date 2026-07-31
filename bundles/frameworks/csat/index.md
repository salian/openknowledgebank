---
type: Bundle Index
title: Customer Satisfaction Score
description: Source-aware framework bundle for survey question, response scale, satisfied threshold, sampling, timing, response rate, score, segmentation, and interpretation review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- csat
- framework
- source-aware
aliases:
- Customer Satisfaction Score
problems_solved:
- Prepare a customer satisfaction score review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- Customer Satisfaction Score
- source-evidence matrix
- qualified-review gate
deliverables:
- Customer Satisfaction Score review brief
commands: []
skills: []
evaluations:
- Customer Satisfaction Score source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- customer-support-cx-analyst
- customer-service-support-manager
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
- Use the listed authoritative or identified source surfaces for general Customer Satisfaction Score guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for survey purpose and exact question, scale and satisfied threshold, invitation population and sampling, channel and timing, response counts and exclusions, score formula, weighting, segments, period, confidence or uncertainty treatment, consent and privacy, benchmarks and comparability, source extract, owner, and approvals.
- Do not infer customer sentiment, representativeness, score formula, benchmark comparability, causal driver, trend significance, or business outcome.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that send surveys, contact customers, collect or export personal data, change scoring or dashboards, publish scores or benchmarks, trigger outreach, or claim causal improvement.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: csat
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
  okb_score: 35
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
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
  display_summary: Improved measured rubric score from 14/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Customer Satisfaction Score

Source-aware framework bundle for survey question, response scale, satisfied threshold, sampling, timing, response rate, score, segmentation, and interpretation review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/csat-brief.md](deliverables/csat-brief.md)
