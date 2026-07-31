---
type: Bundle Index
title: Purchasing Agent / Buyer
description: Source-aware role bundle for purchasing and sourcing, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- purchasing-agent-buyer
- purchasing
- role
aliases:
- Purchasing Agent / Buyer
problems_solved:
- Prepare a procurement decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Procurement
- Supply chain
tools: []
frameworks:
- source-evidence matrix
- purchasing and sourcing review matrix
- qualified-review gate
deliverables:
- procurement decision brief
commands: []
skills: []
evaluations:
- Purchasing Agent / Buyer source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- sox
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1023.00
  soc: []
  isco_08: []
  esco:
  - '3323'
limitations:
- Use the cited official, originator, standards, or professional sources for general purchasing and sourcing context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for business need, specifications, quantities, budget, timeline, and authority; supplier identities, qualifications, sanctions, conflicts, ownership, and due diligence; RFQ or RFP, bids, currencies, taxes, freight, terms, and validity dates; evaluation criteria, scoring, total cost, risk, service levels, and negotiation history; contract, policy, competition, approvals, purchase order, receipt, and performance evidence.
- Do not infer supplier qualification, bid comparability, total cost, conflict status, authority, contract term, delivery, or best-value conclusion.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and other sensitive data.
- Require explicit confirmation before contacting suppliers, awarding business, negotiating or signing terms, issuing purchase orders, or committing spend.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 19
  okb_score: 36
  absolute_lift: 17
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 19/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: purchasing-agent-buyer
okb_bundle_version: 0.1.0
---
# Purchasing Agent / Buyer

Source-aware role bundle for purchasing and sourcing, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

Do not assign an owner, author, date, or version to a provided artifact unless the request states it. Mark each absent field `Needs verification`.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/purchasing-agent-buyer-brief.md](deliverables/purchasing-agent-buyer-brief.md)
