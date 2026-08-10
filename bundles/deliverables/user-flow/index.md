---
type: Bundle Index
title: User Flow
description: Diagram mapping the sequence of steps a user takes through a product.
category: deliverables
version: 0.1.0
tags:
- user
- flow
aliases:
- User Flow
- user flows
problems_solved:
- Prepare a source-grounded User Flow.
- Separate verified evidence, prompt-provided facts, assumptions, and missing evidence.
- Expose applicability, validation, risk, and authority boundaries before consequential use.
industries:
- Cross-industry
tools:
[]
frameworks:
- source-evidence matrix
deliverables:
- User Flow
commands: []
skills: []
evaluations:
- User Flow source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- interaction-designer
- product-designer
- ux-designer
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: ymyl
  domains:
  - privacy
  professional_review:
    status: not_reviewed
    required_qualification: A qualified UX, accessibility, privacy, research, or domain professional appropriate to the users and service.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for the governing source and version, objective, audience, scope, local records, definitions, inputs, calculations or mappings, permissions, conflicts, validation results, approvals, and reviewer authority.
- This bundle does not grant authority to approve, sign, publish, distribute, file, implement, or use the artifact for consequential decisions.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before approve, sign, publish, distribute, file, implement, or use the artifact for consequential decisions.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: user-flow
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# User Flow

Use this bundle to prepare a reviewable **User Flow** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent source versions, applicability, local records, measurements, calculations, findings, owners, approvals, dates, permissions, compliance status, or outcomes.

## Start Here

- [Overview](overview.md)
- [User Flow Source-Aware Guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [User Flow](deliverables/user-flow-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

