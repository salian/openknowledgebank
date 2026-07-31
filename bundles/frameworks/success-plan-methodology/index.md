---
type: Bundle Index
title: Joint Success Plan Methodology
description: Source-aware framework bundle for customer outcome, baseline, success metric, milestone, action, dependency, owner, cadence, risk, evidence, and mutual commitment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- success-plan-methodology
- framework
- source-aware
aliases:
- Joint Success Plan Methodology
problems_solved:
- Prepare a joint success plan methodology review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- Joint Success Plan Methodology
- source-evidence matrix
- qualified-review gate
deliverables:
- Joint Success Plan Methodology review brief
commands: []
skills: []
evaluations:
- Joint Success Plan Methodology source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- account-manager-client-relationship-manager
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
- Use the listed authoritative or identified source surfaces for general Joint Success Plan Methodology guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for customer-provided outcomes and priorities, baseline and metric definitions, target and date, milestone acceptance criteria, action owners and dependencies, product capability and limitations, adoption or usage source, risks and blockers, meeting notes and consent, plan version, review cadence, commercial terms, customer approval, and change history.
- Do not infer customer outcome, baseline, target, adoption, milestone status, owner commitment, value realization, health, renewal, or approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that contact customers, change success-plan or CRM state, assign commitments, share customer data, promise outcomes or product changes, alter commercial terms, trigger escalation, or claim value realization.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: success-plan-methodology
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
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Joint Success Plan Methodology

Source-aware framework bundle for customer outcome, baseline, success metric, milestone, action, dependency, owner, cadence, risk, evidence, and mutual commitment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/success-plan-methodology-brief.md](deliverables/success-plan-methodology-brief.md)
