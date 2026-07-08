---
type: Bundle Index
title: SOC 2
description: Source-aware compliance hub for SOC 2 readiness triage, evidence framing, and professional-review handoff.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - soc-2
  - compliance
  - security
  - vendor-trust
  - audit-readiness
aliases:
  - System and Organization Controls 2
  - SOC 2 report
  - SOC 2 Type I
  - SOC 2 Type II
problems_solved:
  - Triage SOC 2 questions without inventing audit conclusions or AICPA criteria.
  - Separate official AICPA source categories, user-provided evidence, assumptions, and missing evidence.
  - Produce source-aware SOC 2 readiness briefs for qualified CPA, auditor, legal, security, or compliance review.
industries:
  - saas
  - technology
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - trust services category scoping
  - Type I versus Type II readiness framing
deliverables:
  - source-aware SOC 2 readiness brief
commands: []
skills: []
evaluations:
  - SOC 2 source-awareness check
okb_bundle_id: soc-2
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - auditor-external
  - internal-auditor
  - chief-information-security-officer-ciso
  - security-software-application-security-engineer
  - devops-engineer
  - cloud-engineer
  - saas-contract-lawyer-msa-sla-dpa-drafting
adjacent_bundles:
  - gdpr
  - hipaa
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - This bundle is a compliance hub, not legal, accounting, audit, attestation, or CPA advice.
  - Scenario-specific conclusions require current AICPA materials, the actual SOC 2 report or audit request, user-provided system evidence, and qualified professional review.
  - The bundle does not reproduce AICPA criteria, points of focus, report templates, or opinion language.
  - Measured baseline-vs-OKB evaluation is planned but not complete.
safety_notes:
  - Require qualified CPA, auditor, legal, security, or compliance professional review before relying on outputs for audit, customer, contractual, or control-change decisions.
  - Do not request, expose, or publish sensitive security evidence, customer data, report contents, or credentials beyond what is necessary for user-approved analysis.
  - Require explicit confirmation before contacting auditors, sending customer responses, exporting evidence, changing controls, or modifying production systems.
timestamp: "2026-07-09T00:00:00Z"
---

# SOC 2

This bundle helps an agent answer SOC 2 questions with source discipline. It is a hub for readiness triage, evidence framing, and public-safe handoff notes, not a replacement for AICPA materials or a CPA examination.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the official AICPA source category, user-provided local evidence, and missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/soc-2-readiness-triage.md](workflows/soc-2-readiness-triage.md)
- [deliverables/source-aware-soc-2-readiness-brief.md](deliverables/source-aware-soc-2-readiness-brief.md)
- [evaluations/soc-2-source-awareness-check.md](evaluations/soc-2-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use AICPA/CIMA SOC suite materials for SOC service framing, AICPA/CIMA Trust Services Criteria for the trust services categories, AICPA/CIMA SOC 2 Description Criteria for system description work, auditor request lists for engagement-specific evidence, and user-provided records for organization-specific facts.
