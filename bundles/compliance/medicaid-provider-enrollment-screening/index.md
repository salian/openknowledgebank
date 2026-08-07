---
type: Bundle Index
title: Medicaid Provider Enrollment and Screening
description: Source-aware compliance bundle for separating federal Medicaid provider screening requirements from state implementation, evidence, and enrollment decisions.
schema_version: 0.1.0
bundle_format: okf-compatible
category: compliance
tags: [Medicaid, provider enrollment, provider screening, program integrity, risk-based screening]
aliases: [Medicaid Provider Screening, Medicaid Enrollment Screening, 42 CFR Part 455 Subpart E]
problems_solved:
- Separate federal State-plan screening requirements from state/provider implementation.
- Review risk-based screening, reliance, revalidation, database, fee, moratorium, and decision evidence.
- Prevent invented enrollment status, exclusion matches, adverse actions, fees, deadlines, and appeal outcomes.
industries: [healthcare, Medicaid providers, state Medicaid agencies, healthcare compliance]
tools: []
frameworks: [federal-state-program applicability matrix, screening evidence ledger, enrollment decision boundary]
deliverables: [enrollment applicability review, risk and screening activity record, reliance evidence review, decision and monitoring gap register]
commands: []
skills: []
evaluations: [Medicaid Provider Enrollment and Screening quality check]
okb_bundle_id: medicaid-provider-enrollment-screening
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: [medicaid-claims-billing-requirements, medicare-conditions-of-participation, 340b-drug-pricing-program, corporate-integrity-agreement, anti-kickback-statute]
adjacent_bundles: []
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings: {onet_soc: [], soc: [], isco_08: [], esco: []}
limitations:
- This bundle is a review aid, not legal, enrollment, credentialing, program-integrity, criminal-history, exclusion, adverse-action, or appeal advice and not proof of eligibility or compliance.
- Federal Subpart E requirements are implemented through state-specific law, plans, provider categories, processes, systems, notices, and potentially stricter screening.
- It does not query databases, verify identities/licenses, collect fingerprints/fees, perform site visits, submit applications, contact agencies, or make enrollment decisions.
safety_notes:
- Protect PII, tax, ownership/control, license, criminal-history, fingerprint, credential, enrollment, financial, and investigation information.
- Require current federal and state source inspection before stating risk, screening, reliance, fee, moratorium, decision, deadline, or appeal requirements.
- Require explicit authority and qualified review before access, contact, submission, fingerprint/site activity, disclosure, denial, termination, or appeal action.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or qualified reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve tasks covering missing state/provider context, unsupported reliance on Medicare screening, and a federal-versus-state screening conflict; configure matched runs; obtain qualified reviewer scores; and build a listing scorecard.
---

# Medicaid Provider Enrollment and Screening

Use this bundle to review the federal Medicaid enrollment/screening baseline and the current state implementation applicable to a provider and event.

Start with the [overview](overview.md), apply the [compliance contract](compliance.md), follow the [workflow](workflow.md), and use the [quality check](evaluations/quality-check.md).

This bundle does not establish enrollment eligibility, screening completion, exclusion status, an adverse action, appeal outcome, or compliance.
