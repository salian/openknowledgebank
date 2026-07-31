---
type: Bundle Index
title: Monitoring and Performance Dashboard
description: Source-aware deliverable bundle for specifying a monitoring dashboard with evidenced users, decisions, signals, definitions, sources, thresholds, freshness, ownership, and response links.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- monitoring-dashboard
- observability
- performance
- deliverable
aliases:
- Monitoring and Performance Dashboard
problems_solved:
- Prepare a monitoring dashboard specification without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Information technology
- Software
- Operations
tools: []
frameworks:
- source-evidence matrix
- operational monitoring and performance visualization review matrix
- qualified-review gate
deliverables:
- monitoring dashboard specification
commands: []
skills: []
evaluations:
- Monitoring and Performance Dashboard source-awareness check
okb_bundle_id: monitoring-dashboard
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
- Use the cited official, originator, standards, or professional sources for general operational monitoring and performance visualization context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for audience, decisions, services, models, or processes in scope, metric, event, log, and trace definitions, source systems, queries, filters, aggregation, and dimensions, time range, timezone, latency, freshness, and missing-data behavior, baseline, objective, threshold, alert, and uncertainty, and owner, access, privacy, runbook, escalation, and validation evidence.
- Do not infer metric meaning, query correctness, data freshness, threshold validity, system health, and response ownership.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before changing alerts, production monitoring, access, retention, or incident status, or publishing performance claims without validated data.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Monitoring and Performance Dashboard

Source-aware deliverable bundle for specifying a monitoring dashboard with evidenced users, decisions, signals, definitions, sources, thresholds, freshness, ownership, and response links.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/monitoring-dashboard-brief.md](deliverables/monitoring-dashboard-brief.md)
