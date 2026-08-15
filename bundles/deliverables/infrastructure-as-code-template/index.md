---
type: "Bundle Index"
title: "Infrastructure as Code Template"
description: "Evidence-grounded infrastructure-as-code template specification with version, state, security, validation, change, rollback, and operational boundaries."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "infrastructure-as-code"
- "cloud"
aliases:
- "Infrastructure as Code Template"
problems_solved:
- "Prepare a reviewable IaC template without inventing provider schemas, environment state, credentials, security, cost, or deployment success."
- "Prepare a reviewable infrastructure-as-code template and release brief with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Cloud infrastructure"
- "Software"
tools: []
frameworks:
- "IaC version, schema, state, security, validation, plan, and rollback review"
deliverables:
- "infrastructure-as-code template and release brief"
commands: []
skills: []
evaluations:
- "Infrastructure as Code Template source-awareness check"
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
  - "security"
  - "privacy"
  - "financial"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "An accountable cloud-platform, security, privacy, finance, compliance, and production-operations reviewer for the target environment."
limitations:
- "AWS and HashiCorp documentation is product-specific and versioned; examples do not establish local provider schemas, account state, permissions, quotas, security, compliance, cost, plan effects, rollback, or production readiness."
- "Task-specific conclusions require current inspected evidence for tool and provider versions, target accounts and regions, current state and imports, approved architecture, resource schemas and quotas, module provenance, inputs and outputs, identity and access design, secrets handling, network and data controls, policy checks, formatting and validation, tests and plan output, cost estimate, drift and rollback plan, observability, and approvals."
- "This bundle does not grant authority to request or embed credentials, initialize remote state, access accounts, create plans against production, apply or destroy resources, change IAM or networks, expose data, deploy, or claim security or compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to request or embed credentials, initialize remote state, access accounts, create plans against production, apply or destroy resources, change IAM or networks, expose data, deploy, or claim security or compliance."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: infrastructure-as-code-template
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
# Infrastructure as Code Template

Use this bundle to prepare a reviewable **infrastructure-as-code template and release brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent tool or provider version, schema, account state, permission, quota, resource value, secret, plan effect, cost, policy result, security, compliance, rollback success, production readiness, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [infrastructure-as-code template and release brief](deliverables/infrastructure-as-code-template-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
