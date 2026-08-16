---
type: "Bundle Index"
title: "National Correct Coding Initiative Edits"
description: "Source-aware NCCI compliance guidance with program, payer, setting, edit type, quarterly version, effective date, code pair, units, modifier indicator, documentation, and claim boundaries."
category: compliance
version: 0.1.0
tags:
- "compliance"
- "ncci"
- "medical-coding"
- "cms"
aliases:
- "National Correct Coding Initiative Edits"
problems_solved:
- "Apply NCCI without inventing program applicability, edit version, service facts, code pair, units, modifier support, medical necessity, claim payment, or compliance."
- "Prepare a reviewable NCCI edit analysis and claim-support record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Healthcare coding"
- "Medicare and Medicaid"
tools: []
frameworks:
- "program, payer, setting, date, version, edit, service, documentation, modifier, and claim review"
deliverables:
- "NCCI edit analysis and claim-support record"
commands: []
skills: []
evaluations:
- "National Correct Coding Initiative Edits source-awareness check"
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
  - "medical"
  - "insurance"
  - "privacy"
  - "financial"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified certified coding, relevant clinician, Medicare or Medicaid and payer policy, patient privacy, revenue-cycle, compliance, and audit reviewers."
limitations:
- "CMS NCCI sources do not establish local payer adoption, service facts, code assignment, units, clinically appropriate modifier, medical necessity, coverage, claim payment, or compliance."
- "Task-specific conclusions require current inspected evidence for payer program beneficiary provider setting service date and claim authority, authenticated encounter and procedure documentation, licensed current CPT HCPCS sources, correct Medicare or Medicaid edit type file version effective date and checksum, exact code pair unit or add-on lookup, modifier indicator and clinical support, payer policy and adoption evidence, coder clinician and compliance review, claim edit denial appeal and adjustment records, PHI controls and approvals."
- "This bundle does not grant authority to create clinical facts, copy protected code descriptors improperly, select codes or modifiers without support, override edits, expose PHI, submit or alter claims, appeal without authority, or promise payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to create clinical facts, copy protected code descriptors improperly, select codes or modifiers without support, override edits, expose PHI, submit or alter claims, appeal without authority, or promise payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: national-correct-coding-initiative
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
# National Correct Coding Initiative Edits

Use this bundle to prepare a reviewable **NCCI edit analysis and claim-support record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent program applicability, payer adoption, edit type or version, service, code, unit, modifier support, necessity, coverage, claim payment, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Compliance guide](compliance.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [NCCI edit analysis and claim-support record](deliverables/national-correct-coding-initiative-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
