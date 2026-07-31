---
type: Bundle Index
title: Business Continuity and Disaster Recovery Plan
description: Source-aware deliverable bundle for continuity and disaster-recovery planning with evidenced critical activities, impacts, dependencies, recovery objectives, strategies, roles, communications, tests, and maintenance.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- business-continuity
- disaster-recovery
- resilience
- deliverable
aliases:
- Business Continuity and Disaster Recovery Plan
problems_solved:
- Prepare a business continuity and disaster recovery plan without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Business services
- Information technology
- Government
tools: []
frameworks:
- source-evidence matrix
- organizational continuity and technology recovery review matrix
- qualified-review gate
deliverables:
- business continuity and disaster recovery plan
commands: []
skills: []
evaluations:
- Business Continuity and Disaster Recovery Plan source-awareness check
okb_bundle_id: business-continuity-plan
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
- Use the cited official, originator, standards, or professional sources for general organizational continuity and technology recovery context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for organization, sites, services, processes, systems, people, and scenario scope, business impact analysis, criticality, dependencies, and maximum tolerable disruption, recovery time, recovery point, service level, and data assumptions, continuity, workaround, alternate-site, supplier, backup, restoration, and return strategies, activation, command, roles, succession, contact, communication, safety, and regulatory requirements, and exercise, test evidence, gaps, remediation, maintenance, distribution, access, and approval.
- Do not infer critical activity, dependency, recovery objective, backup recoverability, role assignment, and plan effectiveness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before activating plans, declaring emergencies, contacting authorities or stakeholders, changing production recovery controls, or claiming readiness without tested and approved evidence.
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
  baseline_score: 20
  okb_score: 36
  absolute_lift: 16
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 7
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 20/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Business Continuity and Disaster Recovery Plan

Source-aware deliverable bundle for continuity and disaster-recovery planning with evidenced critical activities, impacts, dependencies, recovery objectives, strategies, roles, communications, tests, and maintenance.

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
- [deliverables/business-continuity-plan-brief.md](deliverables/business-continuity-plan-brief.md)
