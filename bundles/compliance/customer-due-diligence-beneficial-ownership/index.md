---
type: "Bundle Index"
title: "Customer Due Diligence / Beneficial Ownership Rule"
description: "Source-aware compliance bundle for Customer Due Diligence / Beneficial Ownership Rule applicability, evidence collection, source inspection, and review-ready decision support."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "compliance"
tags:
  - "customer"
  - "due"
  - "diligence"
  - "beneficial"
  - "ownership"
  - "rule"
  - "us"
  - "banking"
  - "financial"
  - "institutions"
aliases:
  - "Customer Due Diligence / Beneficial Ownership Rule"
  - "US Banking & Financial Institutions"
  - "United States"
problems_solved:
  - "Route Customer Due Diligence / Beneficial Ownership Rule work to the right source category and evidence set."
  - "Separate verified source facts, user-provided facts, assumptions, and missing evidence."
  - "Produce a Customer Due Diligence / Beneficial Ownership Rule source-aware brief suitable for qualified review."
industries:
  - "Banks, depository institutions, and bank holding companies"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "inspect-first workflow"
  - "qualified-review gate"
deliverables:
  - "Customer Due Diligence / Beneficial Ownership Rule source-aware brief"
commands:
  []
skills:
  []
evaluations:
  - "Customer Due Diligence / Beneficial Ownership Rule source-awareness check"
okb_bundle_id: customer-due-diligence-beneficial-ownership
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "draft"
license: "CC-BY-4.0"
related_bundles:
  []
adjacent_bundles:
  []
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
  baseline_score: 20
  okb_score: 32
  absolute_lift: 12
  task_scores:
    -
      task: "applicability-triage"
      baseline_score: 7
      okb_score: 11
      max_score: 12
    -
      task: "source-aware-checklist"
      baseline_score: 9
      okb_score: 11
      max_score: 12
    -
      task: "conflicting-evidence-review"
      baseline_score: 4
      okb_score: 10
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 20/36 to 32/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Customer Due Diligence / Beneficial Ownership Rule

Source-aware compliance bundle for Customer Due Diligence / Beneficial Ownership Rule applicability, evidence collection, source inspection, and review-ready decision support.

## Required Answer Habit

Include a short **Source note** naming the official or authoritative source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
