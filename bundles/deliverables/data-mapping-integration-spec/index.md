---
type: "Bundle Index"
title: "Data Mapping and Integration Specification"
description: "Evidence-grounded source-to-target mapping specification with schemas, transformations, quality, security, reconciliation, and operational controls."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "data-integration"
- "data-mapping"
aliases:
- "Data Mapping and Integration Specification"
problems_solved:
- "Specify an integration without inventing schemas, semantics, transformations, access, data quality, or runtime behavior."
- "Prepare a reviewable data mapping and integration specification with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Data engineering"
tools: []
frameworks:
- "source-to-target schema, transformation, quality, security, and operations review"
deliverables:
- "data mapping and integration specification"
commands: []
skills: []
evaluations:
- "Data Mapping and Integration Specification source-awareness check"
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
  - "security"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "An accountable data architect, source and target owner, security, privacy, and legal reviewer."
limitations:
- "Informatica documentation describes a product-specific mapping specification template; it does not establish local schemas, field semantics, data quality, compatibility, permissions, transformations, performance, or production readiness."
- "Task-specific conclusions require current inspected evidence for source and target systems and versions, inspected schemas and samples, field definitions and owners, keys and grain, types and constraints, mapping and transformation rules, code sets, timing and volumes, lineage, quality and reconciliation rules, privacy and security controls, failure handling, tests, and approvals."
- "This bundle does not grant authority to access systems, extract or move data, expose credentials or personal data, create mappings, alter schemas, run jobs, overwrite records, deploy, or represent reconciliation success."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access systems, extract or move data, expose credentials or personal data, create mappings, alter schemas, run jobs, overwrite records, deploy, or represent reconciliation success."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: data-mapping-integration-spec
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
# Data Mapping and Integration Specification

Use this bundle to prepare a reviewable **data mapping and integration specification** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent system access, schema, field meaning, key, grain, type, transformation, data quality, permission, compatibility, runtime result, reconciliation, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [data mapping and integration specification](deliverables/data-mapping-integration-spec-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
