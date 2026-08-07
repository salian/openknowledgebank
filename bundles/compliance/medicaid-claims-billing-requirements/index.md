---
type: Bundle Index
title: Medicaid Claims Submission and Payment Requirements
description: Source-aware compliance bundle for reviewing Medicaid claim readiness, submission requirements, adjudication evidence, payment reconciliation, and state/program-specific gaps.
schema_version: 0.1.0
bundle_format: okf-compatible
category: compliance
tags:
- Medicaid claims
- medical billing
- claims submission
- claims payment
- program integrity
aliases:
- Medicaid Billing Requirements
- Medicaid Claim Submission Compliance
- Medicaid Claims Payment Rules
problems_solved:
- Separate federal Medicaid claims baselines from state, program, plan, provider-type, and payer implementation rules.
- Review claim evidence across enrollment, eligibility, coverage, authorization, TPL, EVV, coding, submission, adjudication, and payment.
- Prevent invented billing fields, deadlines, codes, claim status, payment, appeal, and compliance claims.
industries:
- healthcare
- Medicaid providers
- health plans
- medical billing
tools: []
frameworks:
- federal-state-program applicability matrix
- claim evidence-status ledger
- claim lifecycle reconciliation
deliverables:
- Medicaid claim readiness review
- billing requirement and source matrix
- claim status and payment reconciliation
- denial, correction, appeal, and overpayment issue register
commands: []
skills: []
evaluations:
- Medicaid Claims Submission and Payment Requirements quality check
okb_bundle_id: medicaid-claims-billing-requirements
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- hipaa
- hipaa-claims-attachments-standards
- hipaa-eligibility-claim-status-operating-rules
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
- This bundle is a compliance-review aid, not legal, coding, clinical, reimbursement, or fraud advice and not proof that a service or claim is covered, correct, payable, medically necessary, or compliant.
- Medicaid billing is state- and program-administered; exact forms, fields, edits, deadlines, rates, units, modifiers, attachments, EVV, submission routes, denial handling, and appeals require current state/plan sources.
- It does not submit, change, correct, void, appeal, refund, disclose, or check any real claim, eligibility record, authorization, or payment.
safety_notes:
- Protect PHI, PII, credentials, claim identifiers, clinical documentation, financial information, and payer communications using minimum-necessary access.
- Route coding, clinical, legal, payer-contract, program-integrity, overpayment, and fraud questions to qualified accountable reviewers.
- Require explicit authorization before any submission, correction, appeal, refund, disclosure, payer contact, or record change.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Create and approve three public-safe tasks covering empty evidence, Medicare-versus-Medicaid NCCI confusion, and a federal-versus-state timely-filing conflict; configure matched runs; obtain qualified reviewer-scored aggregate results; and build a listing scorecard.
---

# Medicaid Claims Submission and Payment Requirements

Use this bundle to review Medicaid claims requirements from current federal sources and the responsible state, program, plan, fiscal agent, and payer materials.

Start with the [overview](overview.md) and [compliance contract](compliance.md), follow the [review workflow](workflow.md), and apply the [quality check](evaluations/quality-check.md).

This bundle does not contain state billing instructions or establish that a claim was submitted, accepted, adjudicated, paid, appealed, refunded, or compliant.
