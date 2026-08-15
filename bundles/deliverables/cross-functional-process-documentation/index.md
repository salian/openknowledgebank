---
type: "Bundle Index"
title: "Cross-Functional Process Documentation"
description: "Evidence-grounded process documentation spanning roles, handoffs, controls, systems, exceptions, measures, and governance."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "process-documentation"
- "bpmn"
aliases:
- "Cross-Functional Process Documentation"
problems_solved:
- "Document an end-to-end process without inventing steps, ownership, system behavior, controls, or performance."
- "Prepare a reviewable cross-functional process specification with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Operations"
tools: []
frameworks:
- "BPMN-aware process evidence, handoff, control, and validation review"
deliverables:
- "cross-functional process specification"
commands: []
skills: []
evaluations:
- "Cross-Functional Process Documentation source-awareness check"
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
  classification: "ymyl"
  domains:
  - "privacy"
  - "security"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "An accountable process owner, system owner, security, privacy, control, and legal reviewer as applicable."
limitations:
- "The OMG BPMN specification defines a modeling notation; it does not establish a local process, role, sequence, system behavior, control, performance, compliance, or approval, and not every audience needs formal BPMN."
- "Task-specific conclusions require current inspected evidence for process objective and boundaries, observed work and interviews, roles and decision rights, inputs and outputs, systems and data, handoffs, business rules, controls, exceptions, timing and measures, variants, accessibility, validation walkthroughs, owners, and approvals."
- "This bundle does not grant authority to change workflow, assign roles, alter systems or controls, expose data, automate decisions, commit service levels, publish procedures, or represent process performance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to change workflow, assign roles, alter systems or controls, expose data, automate decisions, commit service levels, publish procedures, or represent process performance."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: cross-functional-process-documentation
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
# Cross-Functional Process Documentation

Use this bundle to prepare a reviewable **cross-functional process specification** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent process step, sequence, role, handoff, rule, system state, control operation, exception, timing, performance, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [cross-functional process specification](deliverables/cross-functional-process-documentation-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
