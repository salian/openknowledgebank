---
type: Bundle Index
title: Onboarding Plan
description: Source-aware deliverable bundle for employee, customer, or partner onboarding with explicit audience, outcomes, milestones, access, learning, support, measurement, privacy, and handoff.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- onboarding-plan
- adoption
- enablement
- deliverable
aliases:
- Onboarding Plan
problems_solved:
- Prepare a onboarding plan without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Human resources
- Customer success
- Business services
tools: []
frameworks:
- source-evidence matrix
- structured onboarding and adoption review matrix
- qualified-review gate
deliverables:
- onboarding plan
commands: []
skills: []
evaluations:
- Onboarding Plan source-awareness check
okb_bundle_id: onboarding-plan
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
- Use the cited official, originator, standards, or professional sources for general structured onboarding and adoption context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for onboarding type, audience, owner, start, scope, and desired outcomes, prerequisites, contracts, policies, profile, and consent, milestones, tasks, sequence, dependencies, and acceptance criteria, accounts, access, equipment, data, security, and privacy requirements, learning, communications, support, escalation, accessibility, and localization, and progress measures, feedback, risks, completion, handoff, and approvals.
- Do not infer participant need, prerequisite, access status, milestone completion, adoption, and handoff readiness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before creating access, sharing sensitive data, sending communications, changing contracts or employment status, or marking onboarding complete without accountable confirmation.
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
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
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
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Onboarding Plan

Source-aware deliverable bundle for employee, customer, or partner onboarding with explicit audience, outcomes, milestones, access, learning, support, measurement, privacy, and handoff.

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
- [deliverables/onboarding-plan-brief.md](deliverables/onboarding-plan-brief.md)
