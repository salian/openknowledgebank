---
type: "Bundle Index"
title: "Argo CD"
description: "Source-aware guidance for declarative gitops delivery and synchronization for kubernetes applications. and controlled Argo CD use."
category: tools
version: 0.1.0
tags:
- "argo-cd"
- "tool"
- "source-aware"
aliases:
- "ArgoCD"
- "Argo Continuous Delivery"
problems_solved:
- "Review Argo CD use from current official sources and inspected local evidence."
- "Prepare a controlled Argo CD decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Argo CD"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Argo CD configuration and use review brief"
commands: []
skills: []
evaluations:
- "Argo CD source-awareness check"
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
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "security"
  - "safety"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for Argo CD and Kubernetes versions, repositories and revisions, application specs, clusters, namespaces, projects, RBAC, SSO, secrets references, health, sync policy, hooks, diffs, events, and audit logs."
- "This bundle does not grant authority to connect repositories or clusters, change manifests or projects, sync or prune applications, rotate credentials, alter RBAC, or represent deployment health."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before connect repositories or clusters, change manifests or projects, sync or prune applications, rotate credentials, alter RBAC, or represent deployment health."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: argo-cd
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
# Argo CD

Use this bundle to prepare a reviewable **Argo CD configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent repository contents, desired or live state, cluster access, diff safety, hook behavior, sync result, health, rollback viability, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Argo CD configuration and use review brief](deliverables/argo-cd-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
