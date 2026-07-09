---
type: Bundle Index
title: ADA
description: Source-aware compliance hub for Americans with Disabilities Act Title III public accommodation and digital accessibility questions.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - ada
  - accessibility
  - digital-accessibility
  - title-iii
  - public-accommodations
  - compliance
aliases:
  - Americans with Disabilities Act
  - ADA Title III
  - ADA web accessibility
problems_solved:
  - Triage ADA Title III and digital accessibility questions without inventing legal conclusions.
  - Separate DOJ source facts, W3C/WAI technical-standard facts, user-provided accessibility evidence, assumptions, and missing verification.
  - Produce source-aware ADA accessibility compliance briefs for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - Title III public accommodation triage
  - WCAG technical-reference framing
deliverables:
  - source-aware ADA compliance brief
commands: []
skills: []
evaluations:
  - ADA source-awareness check
okb_bundle_id: ada
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - wcag
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
limitations:
  - This bundle is a compliance hub, not legal advice, accessibility certification, litigation strategy, or a complete ADA treatise.
  - Scenario-specific answers require current DOJ, ADA, W3C/WAI, case-law, state-law, and user-provided product evidence as relevant.
  - Private-sector Title III web accessibility questions require careful distinction from the DOJ Title II web/mobile rule for state and local governments.
  - WCAG conformance, accessibility statements, VPAT/ACR claims, remediation sufficiency, and legal-risk conclusions require qualified review.
safety_notes:
  - Require qualified accessibility, legal, compliance, procurement, or professional review before relying on outputs for regulatory, contractual, litigation, public conformance, or remediation decisions.
  - Do not claim ADA compliance or WCAG conformance from incomplete scanner output, overlays, unsupported assumptions, or unreviewed product evidence.
  - Require explicit confirmation before publishing accessibility statements, sending legal or regulator communications, committing remediation timelines, changing live products, or exporting user data.
evaluation_summary:
  status: blocked
  last_evaluated:
  method: baseline-vs-okb-rubric planned
  tasks_count: 3
  display_summary: "Measured evaluation is blocked until a benchmark task set, evaluator config, model/provider credentials, and reviewer scoring are selected."
  evidence_note: "No measured score is claimed. The public bundle includes a rubric or evaluation plan, but no completed baseline-vs-OKB model run exists."
evaluation_detail: {}
timestamp: "2026-07-09T00:00:00Z"
---

# ADA

This bundle helps an agent answer Americans with Disabilities Act questions with source discipline, focused on Title III public accommodations and digital accessibility triage. It is a hub for source selection, issue framing, and public-safe brief writing, not a replacement for legal advice, accessibility audit, or certification.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the DOJ or ADA source category, the W3C/WAI or WCAG technical source category when digital accessibility is involved, user-provided product or business evidence, and any missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/ada-digital-accessibility-triage.md](workflows/ada-digital-accessibility-triage.md)
- [deliverables/source-aware-ada-compliance-brief.md](deliverables/source-aware-ada-compliance-brief.md)
- [evaluations/ada-source-awareness-check.md](evaluations/ada-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use ADA.gov and DOJ Civil Rights Division materials for ADA source framing, current ADA legal/regulatory sources for exact legal text, W3C/WAI materials for WCAG technical-standard facts, and user-provided business, website, app, audit, remediation, vendor, policy, and communication evidence for scenario-specific conclusions.
