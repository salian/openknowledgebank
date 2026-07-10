---
type: Bundle Index
title: WCAG
description: Source-aware compliance hub for Web Content Accessibility Guidelines questions, conformance-target framing, and accessibility brief drafting.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - wcag
  - accessibility
  - web-accessibility
  - digital-accessibility
  - compliance
aliases:
  - Web Content Accessibility Guidelines
  - WCAG 2.2
  - WCAG 2.1
problems_solved:
  - Triage WCAG questions without inventing conformance or legal conclusions.
  - Separate W3C/WAI source facts, user-provided product evidence, assumptions, and missing verification.
  - Produce source-aware WCAG accessibility briefs for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - POUR source-evidence matrix
  - conformance target triage
  - accessibility evidence separation
deliverables:
  - source-aware WCAG brief
commands: []
skills: []
evaluations:
  - WCAG source-awareness check
okb_bundle_id: wcag
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
  - This bundle is a compliance hub, not legal advice or a WCAG certification.
  - Scenario-specific answers require current W3C/WAI source inspection, a defined conformance target, product scope, test method, and user-provided evidence.
  - Jurisdiction-specific legal obligations, procurement requirements, VPAT/ACR claims, and tool-specific scanner findings must be inspected separately before reliance.
safety_notes:
  - Require qualified accessibility, legal, compliance, or procurement review before relying on outputs for regulatory, contractual, litigation, public conformance, or procurement decisions.
  - Do not claim that a product conforms to WCAG from incomplete scanner output or unsupported assumptions.
  - Require explicit confirmation before publishing accessibility statements, submitting VPAT/ACR materials, changing live products, or sending legal/compliance communications.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 14
  okb_score: 33
  absolute_lift: 19
  task_scores:
    - task: applicability-triage
      baseline_score: 5
      okb_score: 11
      max_score: 12
    - task: source-aware-checklist
      baseline_score: 4
      okb_score: 11
      max_score: 12
    - task: conflicting-evidence-review
      baseline_score: 5
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 14/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
evaluation_detail: {}
timestamp: "2026-07-09T00:00:00Z"
---

# WCAG

This bundle helps an agent answer Web Content Accessibility Guidelines (WCAG) questions with source discipline. It is a standards and evidence hub for accessibility triage, conformance-target framing, and public-safe brief writing, not a replacement for accessibility audit, legal advice, or certification.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the W3C/WAI source category, the requested WCAG version and conformance level, user-provided product evidence, jurisdictional or contractual source categories if relevant, and missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/wcag-accessibility-triage.md](workflows/wcag-accessibility-triage.md)
- [deliverables/source-aware-wcag-brief.md](deliverables/source-aware-wcag-brief.md)
- [evaluations/wcag-source-awareness-check.md](evaluations/wcag-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use W3C/WAI WCAG pages for standard content, the WCAG 2.2 Recommendation for exact conformance wording, the Quick Reference for success-criteria navigation and support materials, and user-provided audits, code, designs, test results, VPAT/ACR materials, contracts, or legal sources for product-specific or jurisdiction-specific facts.
