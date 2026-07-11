---
type: "Bundle Index"
title: "HR Business Partner (HRBP)"
description: "Source-aware role bundle for people strategy, workforce planning, performance/talent review, employee-relations triage, and HR advisory documentation."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "human-resources"
  - "hrbp"
  - "people-strategy"
  - "employee-relations"
  - "role"
aliases:
  - "HR Business Partner"
  - "People Business Partner"
  - "Human Resources Business Partner"
problems_solved:
  - "Turn business context, workforce evidence, policy requirements, and manager concerns into a reviewable HR advisory plan."
  - "Separate verified employee/workforce facts, manager-provided claims, assumptions, and missing evidence before recommending HR action."
  - "Prepare workforce plans, talent review notes, employee-relations triage, and performance guidance without inventing policy, legal, or employee facts."
industries:
  - "General"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "employee-relations triage"
  - "qualified HR/legal review gate"
deliverables:
  - "Source-aware HR advisory brief"
commands:
  []
skills:
  []
evaluations:
  - "HRBP source-awareness check"
okb_bundle_id: hr-business-partner-hrbp
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "eeoc"
  - "flsa-minimum-wage-overtime"
  - "fmla"
  - "gdpr"
  - "human-resources-generalist-hr-specialist"
  - "human-resources-manager"
  - "workday-hcm"
adjacent_bundles:
  []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "11-3121.00"
  soc:
    []
  isco_08:
    - "1212"
  esco:
    - "human resources manager"
limitations:
  - "This bundle supports HR advisory planning and documentation; it is not employment-law, benefits, payroll, immigration, medical, tax, or disciplinary approval."
  - "Employee-specific recommendations require current policy, jurisdiction, role, performance, accommodation, leave, investigation, and legal-review evidence."
  - "Do not invent employee facts, manager statements, policy requirements, legal conclusions, medical facts, protected-class status, or disciplinary findings."
safety_notes:
  - "Minimize employee, applicant, compensation, medical, leave, performance, investigation, and sensitive HR data in prompts and examples."
  - "Require explicit confirmation before contacting employees, changing records, sending notices, making employment decisions, or documenting final findings."
  - "Route legal, employee-relations, accommodation, leave, compensation, privacy, and high-risk employment matters to accountable reviewers."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "blocked"
  last_evaluated: "2026-07-11"
  method: "baseline-vs-okb-rubric"
  tasks_count: 0
  display_summary: "Evaluation blocked: measured baseline and OKB-assisted outputs plus reviewer-scored aggregate results are not available for this run."
  evidence_note: "No measured score is claimed; private run records the evaluation blocker."
---

# HR Business Partner (HRBP)

Source-aware role bundle for people strategy, workforce planning, performance/talent review, employee-relations triage, and HR advisory documentation.

## Required Answer Habit

Include a short **Source note** naming the policy/workforce evidence, manager or employee-provided context, jurisdiction assumptions, and missing verification still needed before HR reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-hr-advisory-triage.md](workflows/source-aware-hr-advisory-triage.md)
- [deliverables/source-aware-hr-advisory-brief.md](deliverables/source-aware-hr-advisory-brief.md)
