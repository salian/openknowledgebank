---
type: "Bundle Index"
title: "RFP and RFQ Response"
description: "Requirement-traceable solicitation response with controlled claims, solution, pricing, exceptions, approvals, and submission boundaries."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "proposal"
- "procurement-response"
aliases:
- "RFP and RFQ Response"
problems_solved:
- "Prepare a solicitation response without inventing requirements, capabilities, credentials, references, pricing, legal acceptance, or authority to submit."
- "Prepare a reviewable RFP or RFQ response and compliance matrix with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Sales"
- "Procurement"
tools: []
frameworks:
- "solicitation, compliance, claim, solution, price, exception, and submission review"
deliverables:
- "RFP or RFQ response and compliance matrix"
commands: []
skills: []
evaluations:
- "RFP and RFQ Response source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "legal"
  - "financial"
  - "privacy"
  - "security"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Authorized proposal, technical, delivery, finance, tax, contracts, legal, security, privacy, and executive reviewers."
limitations:
- "FAR Part 15 governs negotiated United States federal acquisitions and does not establish another solicitation's rules, bidder eligibility, capability, past performance, pricing, legal terms, evaluation outcome, or submission authority."
- "Task-specific conclusions require current inspected evidence for complete solicitation and amendments, authorized bidder identity, instructions and deadlines, compliance matrix, approved solution and architecture, verified personnel and references with consent, certifications and evidence, schedule and capacity, pricing model and approvals, legal terms and exceptions, security and privacy review, redactions, sign-off, and submission record."
- "This bundle does not grant authority to contact the buyer, commit capability or personnel, use references without consent, certify facts, accept terms, set prices, sign, submit, or predict award."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to contact the buyer, commit capability or personnel, use references without consent, certify facts, accept terms, set prices, sign, submit, or predict award."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: rfp-rfq-response
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# RFP and RFQ Response

Use this bundle to prepare a reviewable **RFP or RFQ response and compliance matrix** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent solicitation requirement, amendment, eligibility, capability, credential, reference consent, certification, schedule, price, tax, term acceptance, evaluation result, award, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [RFP or RFQ response and compliance matrix](deliverables/rfp-rfq-response-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
