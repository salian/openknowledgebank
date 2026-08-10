---
type: Bundle Index
title: Data Contracts
description: Source-aware guidance for schema, semantics, ownership, compatibility, quality, policy, enforcement, versioning, and governed change.
category: frameworks
version: 0.1.0
tags:
- data-contracts
- data-governance
- data-quality
aliases:
- Data Contract
problems_solved:
- Apply Data Contracts using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- Data Contracts
deliverables:
- Data contract design and enforcement brief
commands: []
skills: []
evaluations:
- Data Contracts source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
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
  classification: regulated
  domains:
  - privacy
  - security
  - legal
  professional_review:
    status: not_reviewed
    required_qualification: A qualified data engineering, governance, architecture, security, privacy, legal, or domain professional appropriate to the asset and consumers.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for data asset, producer, consumers, owners, schema, field semantics, identifiers, classifications, quality rules, SLAs, compatibility policy, versions, lineage, access rules, enforcement points, exception process, tests, monitoring, and approvals.
- This bundle does not grant authority to publish or enforce contracts, block changes, expose data, alter schemas or semantics, change access, notify consumers, or deploy controls.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before publish or enforce contracts, block changes, expose data, alter schemas or semantics, change access, notify consumers, or deploy controls.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: data-contracts
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
# Data Contracts

Use this bundle to prepare a reviewable **Data contract design and enforcement brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Asset contents, producer and consumer ownership, schema and semantic meaning, quality thresholds, compatibility, effective access, enforcement behavior, lineage, SLA, exception effect, and authority.

## Start Here

- [Overview](overview.md)
- [Data Contracts Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Data contract design and enforcement brief](deliverables/data-contracts-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

