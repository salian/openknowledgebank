---
type: Workflow
title: Medicaid Claim Requirements Review Workflow
description: An inspect-first workflow for mapping federal and state requirements, reviewing claim evidence, and reconciling lifecycle outcomes without submitting claims.
okb_bundle_id: medicaid-claims-billing-requirements
inputs:
- state/program/plan and provider/service/claim context
- current federal and state/program sources
- protected claim, clinical, authorization, TPL, EVV, submission, remittance, and payment evidence
outputs:
- applicability and readiness decision
- claim gap and lifecycle register
- qualified-review and next-evidence plan
resource: https://www.cms.gov/medicare/coding-billing/ncci-medicaid
timestamp: '2026-08-07T00:00:00Z'
---

# Medicaid Claim Requirements Review Workflow

1. **Identify the payer context.** Confirm state, program/waiver, plan/MCO, fiscal agent, FFS versus encounter, provider/service/claim type, service location, and dates. Stop if the responsible payer is unknown.
2. **Freeze current sources.** Capture federal regulation/guidance plus current state plan/waiver, provider manual, fee schedule, bulletin, NCCI material, companion guide, plan manual, payer edits, and provider agreement with effective dates.
3. **Map applicability.** Separate federal baseline, state agency requirements, MCO/plan contract, provider-type/service policy, clearinghouse/transport rules, and organization controls. Mark conflicts and superseded sources.
4. **Verify provider and beneficiary prerequisites.** Review enrollment, NPI/taxonomy and provider roles, location, eligibility, plan assignment, coverage, benefit limits, authorization/referral, and dates from approved systems.
5. **Verify service evidence.** Confirm documentation supports the service, code, modifier, units, date, place, rendering/order/referral, medical-necessity source, signature/attestation, and retention without making an independent clinical or coding determination.
6. **Review TPL and EVV.** Establish other coverage and payer order, other-payer response and amounts, exceptions, and cost sharing. For applicable in-home PCS/HHCS, verify state EVV and claim-linkage evidence.
7. **Review transaction and edits.** Confirm form/transaction/version, companion guide, payer ID, situational fields, attachments, code-set date, Medicaid NCCI applicability/version, state edits, and batch/clearinghouse rules from current sources.
8. **Review timeliness and claim history.** Calculate deadlines only from the applicable source and event; preserve original, corrected, replacement, void, crossover, retroactive, exception, resubmission, and appeal history.
9. **Issue readiness status.** State `Ready for qualified review`, `Partially ready`, or `Not ready`; list verified/provided/assumed/needs-verification evidence, blocking gaps, owner, and exact source/evidence needed. Do not submit or authorize a claim.
10. **Reconcile outcomes.** When protected evidence is supplied, match submission/control identifiers to acknowledgements, payer status, remittance lines, allowed/adjusted/paid amounts, TPL/cost sharing, withholds/recoupments, bank/ledger evidence, corrections, and appeals.
11. **Handle denials and overpayments safely.** Preserve denial reason and source, distinguish correction/resubmission/appeal routes, and route suspected overpayment, fraud, or disclosure duties to qualified owners without changing, refunding, or reporting anything.
12. **Monitor change.** Track state/plan bulletins, companion guides, fee schedules, code/NCCI updates, EVV changes, contracts, enrollment, and source effective dates; re-review affected claims and controls through approved processes.

## Confirmation Boundary

No submission, eligibility query, authorization request, record retrieval, code change, claim correction/void, appeal, refund, disclosure, payer contact, or portal action is authorized by this workflow. Each requires protected-system access, qualified review, and explicit accountable confirmation.
