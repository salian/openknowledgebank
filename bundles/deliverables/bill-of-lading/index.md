---
type: Bundle Index
title: Bill of Lading and Shipping Documentation
description: Source-aware deliverable bundle for reviewing bill-of-lading and shipping-document data with explicit mode, jurisdiction, parties, cargo, route, terms, identifiers, dangerous-goods, filing, and authorization checks.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- bill-of-lading
- shipping
- logistics
- deliverable
aliases:
- Bill of Lading and Shipping Documentation
problems_solved:
- Prepare a bill-of-lading review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Logistics
- Manufacturing
- International trade
tools: []
frameworks:
- source-evidence matrix
- shipping documentation and cargo records review matrix
- qualified-review gate
deliverables:
- bill-of-lading review brief
commands: []
skills: []
evaluations:
- Bill of Lading and Shipping Documentation source-awareness check
okb_bundle_id: bill-of-lading
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
- Use the cited official, originator, standards, or professional sources for general shipping documentation and cargo records context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for transport mode, route, ports, dates, jurisdiction, and applicable form, shipper, consignee, notify party, carrier, forwarder, and authority, booking, bill, container, seal, vessel, voyage, and reference identifiers, cargo description, classification, packages, marks, quantity, weight, measure, and value evidence, freight terms, carriage terms, Incoterm if applicable, originals, negotiability, and endorsements, and dangerous goods, customs, sanctions, filing, release, signatures, corrections, and approvals.
- Do not infer party identity, cargo description, quantity, route, document status, and customs acceptance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before issuing, signing, endorsing, filing, amending, releasing cargo, or making customs, sanctions, legal, title, or dangerous-goods determinations without qualified authorization.
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
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 9
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

# Bill of Lading and Shipping Documentation

Source-aware deliverable bundle for reviewing bill-of-lading and shipping-document data with explicit mode, jurisdiction, parties, cargo, route, terms, identifiers, dangerous-goods, filing, and authorization checks.

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
- [deliverables/bill-of-lading-brief.md](deliverables/bill-of-lading-brief.md)
