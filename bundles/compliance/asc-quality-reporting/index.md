---
type: "Bundle Index"
title: "Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H)"
description: "Source-aware compliance bundle for Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) applicability, evidence collection, source inspection, and review-ready decision support."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "compliance"
tags:
  - "asc"
  - "quality"
  - "reporting"
  - "ambulatory"
  - "surgical"
  - "center"
  - "ascqr"
  - "cfr"
  - "compliance"
aliases:
  - "Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H)"
  - "US Healthcare"
  - "United States"
problems_solved:
  - "Route Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) work to the right source category and evidence set."
  - "Separate verified source facts, user-provided facts, assumptions, and missing evidence."
  - "Produce a Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) source-aware brief suitable for qualified review."
industries:
  - "Healthcare providers and health plans (HIPAA covered entities and business associates)"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "inspect-first workflow"
  - "qualified-review gate"
deliverables:
  - "Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) source-aware brief"
commands:
  []
skills:
  []
evaluations:
  - "Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) source-awareness check"
okb_bundle_id: asc-quality-reporting
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles: []
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    []
  soc:
    []
  isco_08:
    []
  esco:
    []
limitations:
  - "This bundle is not legal, financial, medical, safety, engineering, tax, audit, or other professional advice."
  - "Scenario-specific answers require current official sources, local evidence, and qualified review."
  - "Do not infer facts about local systems, records, contracts, people, controls, filings, eligibility, hazards, or compliance status without evidence."
safety_notes:
  - "Minimize sensitive personal, customer, patient, employee, financial, security, and regulated data in prompts and examples."
  - "Require explicit confirmation before live operational, legal, financial, safety, security, employment, reporting, disclosure, filing, or contract actions."
  - "Route final reliance to qualified counsel, compliance staff, auditors, clinicians, safety professionals, security leadership, tax professionals, or management as appropriate."
timestamp: "2026-07-10T00:00:00Z"
evaluation_summary:
  status: "measured"
  last_evaluated: "2026-07-10"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 16
  okb_score: 34
  absolute_lift: 18
  task_scores:
    -
      task: "applicability-triage"
      baseline_score: 6
      okb_score: 11
      max_score: 12
    -
      task: "source-aware-checklist"
      baseline_score: 6
      okb_score: 11
      max_score: 12
    -
      task: "conflicting-evidence-review"
      baseline_score: 4
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 16/36 to 34/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H)

Source-aware compliance bundle for Ambulatory Surgical Center Quality Reporting (ASCQR) Program (42 CFR 416 Subpart H) applicability, evidence collection, source inspection, and review-ready decision support.

## Required Answer Habit

Include a short **Source note** naming the official or authoritative source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
