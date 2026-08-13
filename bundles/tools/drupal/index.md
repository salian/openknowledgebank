---
type: "Bundle Index"
title: "Drupal"
description: "Source-aware guidance for content modeling, authoring, publishing, media, taxonomy, workflows, multilingual sites, and web application development. and controlled Drupal use."
category: tools
version: 0.1.0
tags:
- "drupal"
- "tool"
- "source-aware"
aliases:
- "Drupal CMS"
- "Drupal.org"
problems_solved:
- "Review Drupal use from current official sources and inspected local evidence."
- "Prepare a controlled Drupal decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Drupal"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Drupal configuration and use review brief"
commands: []
skills: []
evaluations:
- "Drupal source-awareness check"
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
  - "privacy"
  - "legal"
  - "safety"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, clinical, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for Drupal core version, hosting and PHP stack, site and environment, modules and themes with versions and provenance, content types and workflows, users and permissions, media rights, configuration, custom code, integrations, caching, backups, security advisories, tests, and rollback state."
- "This bundle does not grant authority to install or update code, modules or themes, change schemas, content, workflows or permissions, run database updates, publish or delete content, deploy configuration, or represent security or compatibility."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before install or update code, modules or themes, change schemas, content, workflows or permissions, run database updates, publish or delete content, deploy configuration, or represent security or compatibility."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: drupal
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
# Drupal

Use this bundle to prepare a reviewable **Drupal configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent site state, module trust or compatibility, content ownership, permission, migration result, cache freshness, vulnerability remediation, deployment, rollback viability, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Drupal configuration and use review brief](deliverables/drupal-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
