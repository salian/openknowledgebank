---
type: Bundle Index
title: AI / ML Product Manager
description: Source-aware role bundle for AI and ML product discovery, requirements, evaluation, risk, and rollout planning, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- ai-ml-product-manager
- ai
- role
aliases:
- AI / ML Product Manager
problems_solved:
- Prepare a AI product decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Digital products
- Technology
tools: []
frameworks:
- source-evidence matrix
- AI and ML product discovery, requirements, evaluation, risk, and rollout planning review matrix
- qualified-review gate
deliverables:
- AI product decision brief
commands: []
skills: []
evaluations:
- AI / ML Product Manager source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- amplitude
- databricks
- eu-ai-act
- figma
- gdpr
- jira
- jobs-to-be-done
- mlflow
- okrs
- product-roadmap
- scrum
- soc-2
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
  - http://data.europa.eu/esco/occupation/a79170ad-0b7b-4697-864f-1748359aa10a
limitations:
- Use the listed authoritative sources for general role or tool behavior; local configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for users, use case, problem, decision, and success criteria; product requirements, model and provider versions, data provenance, rights, and consent; evaluation datasets, metrics, thresholds, subgroup results, failure modes, and human oversight; privacy, security, safety, legal, accessibility, cost, latency, rollout, monitoring, incident, and approval evidence.
- Do not infer user value, model capability, accuracy, fairness, safety, compliance, cost, launch readiness, or business impact.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that select or deploy a model, change thresholds or safeguards, process sensitive data, commit spend, launch a feature, or make performance or safety claims.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: ai-ml-product-manager
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
  okb_score: 34
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-task-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# AI / ML Product Manager

Source-aware role bundle for AI and ML product discovery, requirements, evaluation, risk, and rollout planning, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/ai-ml-product-manager-brief.md](deliverables/ai-ml-product-manager-brief.md)
