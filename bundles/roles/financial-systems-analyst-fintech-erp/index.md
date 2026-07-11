---
type: "Bundle Index"
title: "Financial Systems Analyst (FinTech/ERP)"
description: "Source-aware role bundle for ERP and finance-system requirements, controls-aware configuration review, reporting specs, and implementation handoff."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "financial-systems"
  - "erp"
  - "fintech"
  - "requirements"
  - "role"
aliases:
  - "Financial Systems Analyst"
  - "ERP Financial Systems Analyst"
  - "Finance Systems Analyst"
problems_solved:
  - "Turn finance process needs, system evidence, controls requirements, and reporting goals into a reviewable functional specification."
  - "Separate verified system behavior, user-provided process claims, assumptions, and missing evidence before recommending ERP or fintech changes."
  - "Prepare requirements, configuration review, reporting, and controls handoff without inventing system fields, permissions, accounting rules, or control evidence."
industries:
  - "General"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "controls-aware requirements triage"
  - "finance system change gate"
deliverables:
  - "Source-aware financial systems specification"
commands:
  []
skills:
  []
evaluations:
  - "Financial systems source-awareness check"
okb_bundle_id: financial-systems-analyst-fintech-erp
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "agile"
  - "microsoft-power-bi"
  - "sap-s4hana"
  - "soc-2"
  - "sox"
  - "us-gaap"
  - "workday-hcm"
adjacent_bundles:
  []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "15-1211.00"
  soc:
    []
  isco_08:
    - "2511"
  esco:
    - "2511"
limitations:
  - "This bundle supports financial systems analysis and planning; it is not accounting, audit, tax, legal, security, or production-change approval."
  - "System-specific recommendations require current configuration, process, control, accounting, access, and reporting evidence from authorized sources."
  - "Do not invent ERP fields, workflows, permissions, accounting treatment, control status, balances, integrations, or report definitions."
safety_notes:
  - "Minimize financial, payroll, employee, customer, vendor, credential, and regulated data in prompts and examples."
  - "Require explicit confirmation before changing configurations, permissions, workflows, integrations, reports, journal logic, exports, or production data."
  - "Route accounting, audit, tax, security, privacy, and production-impacting changes to accountable reviewers."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "blocked"
  last_evaluated: "2026-07-11"
  method: "baseline-vs-okb-rubric"
  tasks_count: 0
  display_summary: "Evaluation blocked: measured baseline and OKB-assisted outputs plus reviewer-scored aggregate results are not available for this run."
  evidence_note: "No measured score is claimed; private run records the evaluation blocker."
---

# Financial Systems Analyst (FinTech/ERP)

Source-aware role bundle for ERP and finance-system requirements, controls-aware configuration review, reporting specs, and implementation handoff.

## Required Answer Habit

Include a short **Source note** naming the finance process evidence, system/configuration source, accounting/control context, user-provided assumptions, and missing verification still needed before implementation or production reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-finance-system-triage.md](workflows/source-aware-finance-system-triage.md)
- [deliverables/source-aware-financial-systems-spec.md](deliverables/source-aware-financial-systems-spec.md)
