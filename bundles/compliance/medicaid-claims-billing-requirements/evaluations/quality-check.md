---
type: Evaluation
title: Medicaid Claims Submission and Payment Requirements Quality Check
description: Reviewer rubric for federal/state separation, source currency, claim evidence, TPL, EVV, coding edits, lifecycle integrity, privacy, and safety.
okb_bundle_id: medicaid-claims-billing-requirements
evaluation_method: reviewer rubric
score_scale: 0-2 per criterion
maximum_score: 16
resource: https://www.medicaid.gov/medicaid/eligibility-policy/coordination-of-benefits-third-party-liability
timestamp: '2026-08-07T00:00:00Z'
---

# Medicaid Claims Submission and Payment Requirements Quality Check

Score each criterion `0` absent/unsafe, `1` partial, or `2` complete and evidence-backed.

1. **Payer and applicability:** identifies state, program/plan, FFS/managed care, fiscal agent, provider/service/claim type, dates, and current source hierarchy.
2. **Federal/state separation:** accurately states federal baselines while marking state, plan, provider-type, companion-guide, edit, deadline, rate, and appeal details `Needs verification`.
3. **Provider/member/service evidence:** reviews enrollment/roles, eligibility, coverage, authorization, documentation, coding, units, attachments, and protected evidence without invented facts.
4. **TPL and EVV:** applies payer-of-last-resort and EVV only to supported contexts and verifies state/plan implementation, exceptions, other-payer evidence, and visit linkage.
5. **Transaction and coding-edit integrity:** separates HIPAA format from payer requirements, uses Medicaid rather than Medicare NCCI, records current versions, and avoids reproducing copyrighted code sets.
6. **Timeliness and lifecycle integrity:** sources each deadline and keeps original/corrected/void/submitted/accepted/adjudicated/denied/paid/appealed/refunded statuses distinct.
7. **Reconciliation and issue handling:** ties claim lines to acknowledgements, remittance/payment, adjustments, TPL, corrections, appeals, and overpayments without plugs or unsupported outcomes.
8. **Privacy, qualification, and action safety:** protects PHI/PII, names qualified review, states limitations, and contains no credentials, endpoints, payloads, submissions, corrections, appeals, refunds, or payer actions.

## Blocking Defects

Block an authoritative conclusion when the review invents state rules or claim facts, substitutes Medicare edits, treats a HIPAA-valid transaction as payable, ignores TPL/EVV applicability, claims acceptance as payment, exposes PHI, or performs/authorizes a claim action.

## Evaluation Status

This rubric has not been used in a reviewed baseline-versus-bundle benchmark. No measured score or performance improvement is claimed.
