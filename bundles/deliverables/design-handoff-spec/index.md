---
type: "Bundle Index"
title: "Design Handoff Specification"
description: "Evidence-grounded design-to-engineering handoff covering scope, behavior, states, content, tokens, accessibility, assets, data, tests, and decisions."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "design-handoff"
- "frontend"
aliases:
- "Design Handoff Specification"
problems_solved:
- "Create an implementable handoff without inventing final decisions, component mappings, behavior, assets, accessibility, or engineering feasibility."
- "Prepare a reviewable design handoff specification with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Design"
- "Software"
tools: []
frameworks:
- "design intent, state, token, accessibility, implementation, and acceptance review"
deliverables:
- "design handoff specification"
commands: []
skills: []
evaluations:
- "Design Handoff Specification source-awareness check"
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
  - "legal"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "An accountable designer, frontend engineer, accessibility, content, privacy, and legal reviewer."
limitations:
- "Figma and WCAG sources describe tool capabilities and accessibility guidance; they do not establish local design finality, code mappings, token values, asset rights, behavior, feasibility, conformance, test results, or approval."
- "Task-specific conclusions require current inspected evidence for approved scope and design links, node and component versions, flows and states, design-system mappings, tokens and breakpoints, content and localization, interaction and motion behavior, accessibility requirements and tests, asset provenance, data and error states, analytics, engineering constraints, acceptance criteria, and approvals."
- "This bundle does not grant authority to change source designs or code, export restricted assets, publish content, declare accessibility conformance, commit estimates, merge, deploy, or represent implementation parity."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to change source designs or code, export restricted assets, publish content, declare accessibility conformance, commit estimates, merge, deploy, or represent implementation parity."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: design-handoff-spec
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
# Design Handoff Specification

Use this bundle to prepare a reviewable **design handoff specification** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent design finality, node version, component mapping, token value, interaction behavior, asset right, accessibility conformance, engineering feasibility, estimate, implementation parity, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [design handoff specification](deliverables/design-handoff-spec-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
