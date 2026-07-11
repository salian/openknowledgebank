---
type: "Bundle Index"
title: "Customer Success Manager (CSM)"
description: "Source-aware role bundle for onboarding plans, account health review, QBR preparation, renewal risk triage, and customer value realization."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "customer-success"
  - "account-management"
  - "renewals"
  - "qbr"
  - "role"
aliases:
  - "Customer Success Manager"
  - "CSM"
  - "Customer Success Lead"
problems_solved:
  - "Turn customer context, product usage evidence, support signals, and commercial goals into a reviewable success plan."
  - "Separate verified account facts, user-provided claims, assumptions, and missing evidence before making renewal or expansion recommendations."
  - "Prepare QBR, health-score, onboarding, and risk-triage outputs without overstating access to systems or account data."
industries:
  - "General"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "customer-health triage"
  - "value-realization review gate"
deliverables:
  - "Source-aware customer success plan"
commands:
  []
skills:
  []
evaluations:
  - "Customer success source-awareness check"
okb_bundle_id: customer-success-manager-csm
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "gdpr"
  - "salesforce-service-cloud"
  - "soc-2"
  - "zendesk"
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
  - "This bundle supports customer success planning and analysis; it is not legal, financial, privacy, security, or professional advice."
  - "Account-specific recommendations require current CRM, support, product usage, contract, billing, and customer-communication evidence."
  - "Do not invent account health, renewal risk, usage, entitlement, support, commercial, or stakeholder facts."
safety_notes:
  - "Minimize customer, contract, account, personal, support, and usage data in prompts and examples."
  - "Require explicit confirmation before contacting customers, changing account records, exporting data, altering commercial terms, or committing renewal/expansion actions."
  - "Route legal, security, privacy, commercial, and contractual issues to the accountable reviewer."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "blocked"
  last_evaluated: "2026-07-11"
  method: "baseline-vs-okb-rubric"
  tasks_count: 0
  display_summary: "Evaluation blocked: measured baseline and OKB-assisted outputs plus reviewer-scored aggregate results are not available for this run."
  evidence_note: "No measured score is claimed; private run records the evaluation blocker."
---

# Customer Success Manager (CSM)

Source-aware role bundle for onboarding plans, account health review, QBR preparation, renewal risk triage, and customer value realization.

## Required Answer Habit

Include a short **Source note** naming the account evidence, system source, user-provided context, assumptions, and missing facts still needed before customer-facing or commercial reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-account-triage.md](workflows/source-aware-account-triage.md)
- [deliverables/source-aware-customer-success-plan.md](deliverables/source-aware-customer-success-plan.md)
