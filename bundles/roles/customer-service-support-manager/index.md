---
type: Bundle Index
title: Customer Service / Support Manager
description: Source-aware role bundle for customer-service policy, staffing, quality, escalation, and performance planning, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- customer-service-support-manager
- customer
- role
aliases:
- Customer Service / Support Manager
problems_solved:
- Prepare a customer support operating brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Customer service
- Business operations
tools: []
frameworks:
- source-evidence matrix
- customer-service policy, staffing, quality, escalation, and performance planning review matrix
- qualified-review gate
deliverables:
- customer support operating brief
commands: []
skills: []
evaluations:
- Customer Service / Support Manager source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- intercom
- itil
- salesforce-service-cloud
- soc-2
- tableau
- tcpa
- zendesk
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-1021.00
  soc: []
  isco_08: []
  esco:
  - http://data.europa.eu/esco/occupation/customer-service-manager (ISCO 1439)
limitations:
- Use the listed authoritative sources for general role or tool behavior; local configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for service scope, channels, products, jurisdictions, hours, and policies; demand history, contact reasons, forecasts, staffing, skills, schedules, vendors, and budgets; SLA and KPI definitions, queues, routing, QA samples, calibration, escalations, customer commitments, consent, recording, privacy, and approvals.
- Do not infer demand, staffing requirement, service performance, QA result, customer entitlement, compliance, or policy effectiveness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that change staffing, routing, policy, SLA, or schedule; contact or record customers; issue credits; share data; or commit vendor spend.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: customer-service-support-manager
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
    okb_score: 11
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Customer Service / Support Manager

Source-aware role bundle for customer-service policy, staffing, quality, escalation, and performance planning, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/customer-service-support-manager-brief.md](deliverables/customer-service-support-manager-brief.md)
