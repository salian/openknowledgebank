---
type: Bundle Index
title: Quotation and Pricing Estimate
description: Source-aware deliverable bundle for scope, line item, quantity, unit price, currency, tax, discount, assumption, exclusion, validity, term, approval, and customer-ready quotation review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: deliverables
version: 0.1.0
tags:
- quotation-pricing-estimate
- deliverable
- source-aware
aliases:
- Quotation and Pricing Estimate
problems_solved:
- Prepare a quotation and pricing estimate review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- source-evidence matrix
- qualified-review gate
deliverables:
- Quotation and Pricing Estimate review brief
commands: []
skills: []
evaluations:
- Quotation and Pricing Estimate source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- purchasing-agent-buyer
- sales-representative-of-services
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
- Use the listed authoritative or identified source surfaces for general Quotation and Pricing Estimate guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for seller and buyer legal identities, request and scope, product or service specification, quantities and units, approved price list and currency, cost basis where relevant, discount authority, tax and fee treatment, delivery and payment terms, assumptions and exclusions, validity period, dependencies, legal text, version, owner, and approvals.
- Do not infer scope, quantity, price, discount, tax, fee, availability, delivery date, margin, contractual effect, or approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that issue or send a quotation, commit price, discount, tax, fee, scope, availability, delivery, payment, or legal terms; change pricing records; expose confidential costs; or accept an order.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: quotation-pricing-estimate
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
  - task: deliverable-quality-review
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
# Quotation and Pricing Estimate

Source-aware deliverable bundle for scope, line item, quantity, unit price, currency, tax, discount, assumption, exclusion, validity, term, approval, and customer-ready quotation review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/quotation-pricing-estimate-brief.md](deliverables/quotation-pricing-estimate-brief.md)
