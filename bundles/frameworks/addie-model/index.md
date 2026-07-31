---
type: Bundle Index
title: ADDIE Model
description: Source-aware framework bundle for analysis, design, development, implementation, evaluation, learner need, objective, assessment, accessibility, and training review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- addie-model
- framework
- source-aware
aliases:
- ADDIE Model
problems_solved:
- Prepare a addie model application brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- source-evidence matrix
- ADDIE Model application matrix
- qualified-review gate
deliverables:
- ADDIE Model application brief
commands: []
skills: []
evaluations:
- ADDIE Model source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- sales-enablement-manager
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
- Use the listed authoritative or identified source surfaces for general ADDIE Model guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for source interpretation, business and learner needs, audience and context, task analysis, measurable objectives, instructional and assessment strategy, content sources and rights, prototype and review evidence, delivery environment, accessibility, pilot data, evaluation design, owners, and approvals.
- Do not infer learner need, objective alignment, content accuracy, accessibility, assessment validity, transfer, training effect, compliance, or approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that publish or deploy training, enroll or contact learners, collect learner data, change assessments, issue credentials, spend budget, or claim compliance, competence, or causal impact.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: addie-model
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
  okb_score: 33
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
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# ADDIE Model

Source-aware framework bundle for analysis, design, development, implementation, evaluation, learner need, objective, assessment, accessibility, and training review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/addie-model-brief.md](deliverables/addie-model-brief.md)
