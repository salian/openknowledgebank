---
type: "Bundle Index"
title: "Voice-of-Customer and Feedback Summary"
description: "Traceable synthesis of customer feedback with collection context, consent, sampling, coding, uncertainty, minority views, and decision limits."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "voice-of-customer"
- "customer-research"
aliases:
- "Voice-of-Customer and Feedback Summary"
problems_solved:
- "Summarize feedback without inventing participant identity, consent, representativeness, sentiment, themes, causes, priorities, or customer agreement."
- "Prepare a reviewable voice-of-customer summary and evidence map with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Customer research"
- "Product management"
tools: []
frameworks:
- "question, collection, consent, sample, coding, synthesis, and use review"
deliverables:
- "voice-of-customer summary and evidence map"
commands: []
skills: []
evaluations:
- "Voice-of-Customer and Feedback Summary source-awareness check"
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
  - "privacy"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified customer researcher, statistician or qualitative-methods reviewer, data owner, privacy, legal, accessibility, and product decision reviewers."
limitations:
- "OMB and NIST sources provide government customer-experience and privacy guidance; they do not establish local consent, participant identity, sample representativeness, coding validity, sentiment, themes, customer priorities, causal explanations, or approval."
- "Task-specific conclusions require current inspected evidence for approved research question and use, channel and collection records, participant notices and consent basis, population and sample frame, response and nonresponse data, raw feedback and provenance, redaction rules, coding guide and versions, coder calibration and agreement, theme evidence and counterexamples, subgroup and channel coverage, uncertainty, privacy controls, validation, and approvals."
- "This bundle does not grant authority to contact customers, identify or profile participants, disclose quotes without consent, infer sensitive traits, automate decisions, claim representativeness or causality, publish findings, or commit product changes."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to contact customers, identify or profile participants, disclose quotes without consent, infer sensitive traits, automate decisions, claim representativeness or causality, publish findings, or commit product changes."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: voice-of-customer-summary
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
# Voice-of-Customer and Feedback Summary

Use this bundle to prepare a reviewable **voice-of-customer summary and evidence map** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent participant identity, consent, population, sample representativeness, sentiment, code, theme prevalence, causal explanation, customer priority, agreement, product outcome, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [voice-of-customer summary and evidence map](deliverables/voice-of-customer-summary-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
