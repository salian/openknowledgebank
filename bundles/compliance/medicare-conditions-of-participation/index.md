---
type: Bundle Index
title: Medicare Conditions of Participation and Conditions for Coverage
description: Source-aware compliance bundle for resolving provider-specific Medicare participation and coverage requirements, point-in-time rule boundaries, evidence, and survey-readiness gaps.
schema_version: 0.1.0
bundle_format: okf-compatible
category: compliance
tags:
- Medicare
- conditions of participation
- conditions for coverage
- survey readiness
- provider certification
aliases:
- Medicare CoPs and CfCs
- CMS Conditions of Participation
- Medicare Provider Health and Safety Standards
problems_solved:
- Resolve the provider or supplier type and governing requirement before applying Medicare participation guidance.
- Separate current, historical, proposed, delayed, and future-effective rule text.
- Organize requirement-to-evidence traceability without inventing a deficiency or compliance conclusion.
industries:
- healthcare
- Medicare providers
- Medicare suppliers
- healthcare compliance
tools: []
frameworks:
- provider-type applicability matrix
- point-in-time authority record
- requirement-to-evidence ledger
deliverables:
- provider and certification-scope record
- current-rule and effective-date matrix
- survey-readiness evidence and gap register
- change-monitoring and accountable-review log
commands: []
skills: []
evaluations:
- Medicare Conditions of Participation and Conditions for Coverage quality check
okb_bundle_id: medicare-conditions-of-participation
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- medicaid-claims-billing-requirements
- 340b-drug-pricing-program
- cahps-patient-experience-surveys
- corporate-integrity-agreement
- deficit-reduction-act-fca-policies
- anti-kickback-statute
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
- This bundle is a research and review aid, not legal, clinical, accreditation, survey, certification, enforcement, or reimbursement advice and not proof of compliance.
- CoPs, CfCs, certification requirements, survey rules, and guidance vary by provider or supplier type, program, component, location, event date, and survey pathway.
- It does not inspect protected records, conduct a survey, assign a deficiency, prepare or submit a plan of correction, contact an authority, or make an operational change.
safety_notes:
- Protect PHI, PII, personnel, credentialing, peer-review, quality, complaint, survey, accreditation, legal, and security information using minimum-necessary access.
- Require exact current and point-in-time source inspection before stating an applicable requirement, effective date, survey consequence, or compliance status.
- Require explicit authorization and qualified accountable review before external communication, certification, corrective action, submission, disclosure, or operational change.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or qualified reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve three public-safe tasks covering an unspecified provider type, a superseded-versus-current rule conflict, and a hospital rule incorrectly applied to a separately certified component; configure matched runs; obtain qualified reviewer-scored aggregate results; and build a listing scorecard.
---

# Medicare Conditions of Participation and Conditions for Coverage

Use this bundle to resolve the applicable Medicare provider or supplier health-and-safety requirement, its point-in-time status, and the evidence needed for accountable review.

Start with the [overview](overview.md) and [compliance contract](compliance.md), follow the [review workflow](workflow.md), and apply the [quality check](evaluations/quality-check.md).

This bundle does not provide a universal CoP checklist or establish a deficiency, compliance status, certification result, corrective action, or enforcement outcome.
