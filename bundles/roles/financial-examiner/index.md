---
type: Bundle Index
title: Financial Examiner
description: Source-aware guidance for planning and documenting financial examinations without inventing institution facts, supervisory authority, findings, ratings, or corrective actions.
category: roles
version: 0.1.0
tags:
- financial-examiner
- financial-supervision
- examination
aliases:
- Financial Institution Examiner
- Bank Examiner
problems_solved:
- Prepare a risk-focused examination scoping memorandum from inspected evidence.
- Reconcile institution records, regulatory sources, and examination evidence without unsupported findings.
- Separate analysis and draft observations from authorized supervisory conclusions and actions.
industries:
- Financial services
- Banking
- Regulatory supervision
tools: []
frameworks:
- risk-focused examination evidence matrix
- source-evidence reconciliation
- qualified-review gate
deliverables:
- examination scoping memorandum
commands: []
skills: []
evaluations:
- Financial Examiner source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- annual-audited-financial-reports
- anti-money-laundering-program
- basel-iii
- compliance-officer
- auditor-external
adjacent_bundles:
- financial-risk-specialist-risk-analyst
- sox
- us-gaap
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-2061.00
  soc:
  - 13-2061
  isco_08:
  - '2411'
  esco: []
content_risk:
  classification: ymyl
  domains:
  - financial
  - legal
  - privacy
  professional_review:
    status: not_reviewed
    required_qualification: A qualified financial-supervision, examination, legal, privacy, or subject-matter professional appropriate to the institution, product, authority, and jurisdiction.
limitations:
- Occupational and agency manuals provide general role and examination context; they do not establish the user's authority, institution scope, applicable law, evidence, ratings, findings, or required action.
- Local conclusions require current, authorized examination evidence with provenance, scope, period, definitions, sampling method, exceptions, and supervisory review.
- This bundle does not grant authority to access supervisory information, direct an institution, assign a rating, issue a finding, require remediation, refer a matter, or initiate enforcement.
safety_notes:
- Minimize and compartmentalize confidential supervisory, customer, employee, account, transaction, credential, and legally protected information.
- Record every material claim as Verified, Provided, Assumed, or Needs verification and preserve contradictory evidence.
- Require explicit confirmation from an evidenced authorized reviewer before communicating findings or taking consequential supervisory action.
timestamp: '2026-08-09T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: financial-examiner
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Financial Examiner

Use this bundle to prepare a reviewable examination scoping memorandum while preserving evidence, jurisdiction, confidentiality, and supervisory authority boundaries.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Examination plan** - authority, scope, period, risk hypothesis, evidence, sampling, testing, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent an institution condition, control result, violation, rating, finding, reviewer, or authority.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware examination workflow](workflows/source-aware-examination.md)
- [Examination scoping memorandum](deliverables/examination-scoping-memorandum.md)
- [Quality check](evaluations/source-awareness-check.md)
