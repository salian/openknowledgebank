---
type: Compliance
title: Medicaid Claims Submission and Payment Compliance Contract
description: Defines the federal baseline, state/program evidence, claim-readiness, lifecycle, reconciliation, and safety contract for Medicaid billing review.
okb_bundle_id: medicaid-claims-billing-requirements
jurisdiction: United States
authorities:
- Centers for Medicare & Medicaid Services
- State Medicaid agency or delegated plan, as applicable
required_inputs:
- state, program or plan, fiscal agent, provider type, service, claim type, dates, and FFS or managed-care context
- current state/plan manuals, bulletins, fee schedules, companion guides, payer edits, and provider agreement
- enrollment, eligibility, coverage, authorization, documentation, EVV, TPL, coding, submission, adjudication, and payment evidence
outputs:
- federal-state-program applicability matrix
- claim evidence and readiness review
- lifecycle, denial, correction, appeal, payment, and overpayment register
resource: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.45
timestamp: '2026-08-07T00:00:00Z'
---

# Medicaid Claims Submission and Payment Compliance Contract

## Direct Answer Contract

Begin with one of: `Ready for qualified review`, `Not ready`, or `Partially ready`. Name the state/program/plan, provider/service/claim type, dates, source versions, and decisive gaps. Do not issue a payment or compliance conclusion from federal sources alone.

## Federal Baseline

- **Timely claims processing:** 42 CFR 447.45 requires a state plan to address claims processing and review. It requires agencies to require provider claims no later than 12 months from date of service and establishes federal clean-claim and other payment timeframes with stated exceptions. These are state-plan requirements, not a universal promise of provider payment or a substitute for a shorter applicable state/plan filing rule, adjustment deadline, exception, or managed-care contract.
- **Claims review:** the same regulation addresses eligibility/provider authorization checks, logical consistency, duplicate/conflict checks, state-plan rate/limit checks, TPL checks, and postpayment review. Exact payer edits and documentation remain state/program specific.
- **Electronic standards:** CMS lists adopted HIPAA transaction standards, including ASC X12N 837 Version 5010 for institutional, professional, and dental health claims and NCPDP standards for applicable pharmacy transactions. A standard transaction does not prove coverage, completeness, companion-guide compliance, acceptance, or payment.
- **Provider identifier:** covered providers and plans use the NPI in adopted HIPAA transactions. The correct billing, rendering, attending, ordering, referring, prescribing, servicing, pay-to, group, taxonomy, and enrollment relationships require payer-specific verification.
- **TPL/COB:** Medicaid is generally payer of last resort, with third parties meeting legal obligations before Medicaid payment, subject to federal exceptions and state/MCO implementation. Verify coverage, payer order, denial/payment evidence, cost avoidance or recovery rules, and beneficiary cost sharing from current sources.
- **Medicaid NCCI:** Medicaid NCCI applies to specified Medicaid fee-for-service claims reimbursed using HCPCS/CPT and differs from Medicare NCCI. Current Medicaid methodologies and state adjudication apply; claim-specific denial/resubmission questions go to the responsible state agency.
- **EVV:** federal EVV requirements concern Medicaid-funded personal care and home health services requiring an in-home visit within specified authorities. Whether a claim needs EVV, the captured elements, exceptions, aggregator/interface, match rules, and correction process are state/program specific.
- **Program integrity:** provider screening/enrollment, pre/postpayment review, payment suspension, improper-payment, recordkeeping, and overpayment requirements may affect claims. OIG compliance guidance is voluntary and nonbinding unless another authority makes a control required.

## Needs Verification: State and Program

Record `Needs verification` unless current authoritative evidence establishes:

1. State, program, waiver, plan/MCO, fiscal agent, payer, claim administrator, FFS/encounter status, provider type, service, place, and dates of service.
2. Provider agreement, enrollment/revalidation, licensure, NPI/taxonomy, service location, affiliations, and billing/rendering/ordering/referring/prescribing roles.
3. Beneficiary eligibility, program enrollment, managed-care assignment, coverage, benefit limits, medical-necessity source, authorization/referral, and coordination with other coverage.
4. Current form/transaction, version, companion guide, payer ID, situational fields, code sets, revenue/procedure/diagnosis codes, modifiers, units, place of service, taxonomy, attachments, signatures/attestations, and batch rules.
5. State/plan timely filing for originals, Medicare/TPL crossover, retroactive eligibility, corrected/replacement/void claims, appeals, disasters, and other exceptions.
6. TPL/COB order, other-payer amounts and adjustment reasons, denial evidence, exceptions, postpayment recovery, and cost-sharing treatment.
7. Medicaid NCCI edit version, claim applicability, modifiers, documentation, state-specific edits, denial explanation, resubmission, and review path.
8. EVV service applicability, state model/vendor, visit elements, exception/correction, linkage, authorization, units, and claim/encounter consequences.
9. Fee schedule, rate cell, limits, units, bundled payment, withhold, incentive, recoupment, cost sharing, and payment methodology.
10. Acknowledgement, acceptance, suspension, rejection, denial, remittance, correction, appeal, payment, recoupment, refund, and retention procedures and deadlines.

## Claim Evidence Contract

For each claim or synthetic review, record source and version, beneficiary/provider identifiers only in approved protected systems, service facts, eligibility/coverage, authorization, provider enrollment/roles, documentation, coding and units, TPL, EVV, attachments, transaction/companion guide, filing deadline and exception, submission identifier/time, acknowledgements, payer status, remittance/payment, corrections/appeals, owner, reviewer, and unresolved issue. Never place PHI or credentials in reusable output.

## Status Separation

Keep `Draft`, `Ready for review`, `Authorized to submit`, `Submitted`, `Transport acknowledged`, `Payer accepted`, `Suspended`, `Rejected`, `Adjudicated`, `Denied`, `Paid`, `Reconciled`, `Corrected`, `Voided`, `Appealed`, `Recouped`, `Refunded`, and `Closed` distinct. One status does not establish another.

## Reconciliation Rule

When claim, eligibility, authorization, clinical, EVV, TPL, acknowledgement, remittance, or payment sources disagree, align member/provider/service identity, state/plan, dates, claim/line/control identifiers, original/replacement/void frequency, code/modifier/unit, authorization, EVV visit, other-payer sequence, billed/allowed/paid/adjusted amounts, reason codes, remittance cycle, and source timestamp. Record explained and unresolved differences; do not alter source facts or create balancing adjustments.

## Safety Boundary

This bundle contains no claims, code-set content, transaction payloads, forms, payer endpoints, credentials, portal instructions, or submission actions. It does not replace qualified coding, clinical, legal, state Medicaid, plan, clearinghouse, privacy, or compliance review.
