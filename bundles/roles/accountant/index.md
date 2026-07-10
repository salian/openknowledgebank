---
type: "Bundle Index"
title: "Accountant"
description: "Source-aware role bundle for Accountant scoping, evidence collection, source inspection, and review-ready decision support."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "accountant"
  - "role"
aliases:
  - "Accountant"
  - "Regulated organizations"
  - "General"
problems_solved:
  - "Route Accountant work to the right source category and evidence set."
  - "Separate verified source facts, user-provided facts, assumptions, and missing evidence."
  - "Produce a Accountant source-aware brief suitable for qualified review."
industries:
  - "Regulated organizations"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "inspect-first workflow"
  - "qualified-review gate"
deliverables:
  - "Accountant source-aware brief"
commands:
  []
skills:
  []
evaluations:
  - "Accountant source-awareness check"
okb_bundle_id: accountant
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "frc-uk-gaap-standards"
  - "quickbooks-online"
  - "sap-s4hana"
  - "sox"
  - "us-gaap"
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
  - "Do not infer facts about local systems, records, contracts, people, controls, filings, eligibility, hazards, capabilities, configuration, responsibilities, or outcomes without evidence."
safety_notes:
  - "Minimize sensitive personal, customer, patient, employee, financial, security, and regulated data in prompts and examples."
  - "Require explicit confirmation before live operational, legal, financial, safety, security, employment, reporting, disclosure, filing, contract, system, campaign, or tool actions."
  - "Route final reliance to a qualified role owner, manager, domain expert, or accountable business reviewer."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "measured"
  last_evaluated: "2026-07-10"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 20
  okb_score: 30
  absolute_lift: 10
  task_scores:
    - task: "role-task-with-limited-evidence"
      baseline_score: 8
      okb_score: 10
      max_score: 12
    - task: "role-prioritization-review"
      baseline_score: 6
      okb_score: 11
      max_score: 12
    - task: "role-source-reconciliation"
      baseline_score: 6
      okb_score: 9
      max_score: 12
  comparison_scores:
    []
  display_summary: "Improved measured rubric score from 20/36 to 30/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Accountant

Source-aware role bundle for Accountant scoping, evidence collection, source inspection, and review-ready decision support.

## Required Answer Habit

Include a short **Source note** naming the official or authoritative source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
