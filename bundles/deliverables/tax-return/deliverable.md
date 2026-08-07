---
type: Deliverable
title: Tax Return Preparation and Review Package
description: Defines the evidence, reconciliation, review, and status contract for a federal individual income tax return package.
okb_bundle_id: tax-return
required_inputs:
- applicable tax year and filing population
- current official form and instructions
- taxpayer-authorized source documents and prior context
- named reviewer and authorization evidence when available
outputs:
- evidence and missing-information register
- form and schedule applicability map
- reconciled draft return package
- exception, review, authorization, and filing-status record
quality_criteria:
- every material amount and filing decision traces to current instructions and supplied evidence
- preparation, review, authorization, transmission, payment, and acceptance states remain distinct
- unsupported facts and positions are marked Needs verification
resource: https://www.irs.gov/forms-pubs/about-form-1040
timestamp: '2026-08-07T00:00:00Z'
---

# Tax Return Preparation and Review Package

## Output Contract

1. **Document control:** taxpayer-approved identifier, tax year, return type, jurisdiction, form revision, preparation date, confidentiality handling, and scope limitations.
2. **Evidence status:** list `Verified`, `Provided`, `Assumed`, and `Needs verification`. With no local evidence, set the first three to `None` except facts explicitly supplied in the request.
3. **Form applicability map:** identify each proposed return, schedule, attachment, and election; cite the current official instruction supporting applicability; keep unresolved items open.
4. **Reconciliation register:** map each material amount to source evidence, tax treatment, return destination, calculation support, and unresolved difference.
5. **Draft return package:** present the prepared forms and schedules as a draft until the taxpayer and accountable reviewer complete review.
6. **Exception and review register:** record missing documents, conflicting amounts, uncertain treatment, reviewer questions, decisions, and evidence for resolution.
7. **Authorization and filing status:** separately record taxpayer review, signature authorization, transmission, payment, authority acknowledgement, rejection, and correction evidence. Never collapse these into a single `filed` status.
8. **Retention and follow-up:** identify the records supporting reported items, the authority used to determine retention, and unresolved post-filing actions.

## Reconciliation Rule

When two records disagree, neither is automatically right. Define what each value represents; align taxpayer, tax year, period, source scope, gross/net treatment, timing, entity, identifiers, adjustments, aggregation, and duplication; then classify the difference as explained or unresolved. Do not force the draft to balance by inventing an adjustment.

## Quality Bar

- Every material fact is traceable to current official instructions or taxpayer-authorized evidence.
- Exact form lines, schedules, rates, thresholds, dates, and elections are verified for the applicable tax year rather than recalled.
- An unevidenced preparer, reviewer, signer, owner, or approver remains `Needs verification`.
- Sensitive data is minimized in summaries and excluded from reusable examples.
- The package states what remains unverified before taxpayer authorization or filing.

## Source Note

Official source categories: current IRS form, instructions, post-release changes, filing/payment guidance, and recordkeeping guidance for the applicable tax year. Local evidence: taxpayer-authorized identity, source documents, elections, prior context, reconciliations, review decisions, authorization, and filing acknowledgements. Missing sources must remain under `Needs verification`; the bundle supplies no taxpayer-specific evidence.

## Safety Boundary

This is a drafting and review aid, not tax or legal advice. It contains no filing, payment, account-access, credential, or transmission instructions. Signing, filing, transmitting, paying, or disclosing return information requires explicit taxpayer authorization and an approved system.
