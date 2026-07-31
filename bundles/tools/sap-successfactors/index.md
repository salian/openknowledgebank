---
type: Bundle Index
title: "SAP SuccessFactors"
description: "Source-aware tool bundle for SAP SuccessFactors tenant, module, employee, workflow, integration, permission, reporting, and controlled HR-system briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "sap-successfactors"
  - "hris"
  - "human-capital-management"
  - "tool"
aliases:
  - "SAP SuccessFactors"
problems_solved:
  - "Prepare a successfactors analysis and change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Human resources"
  - "Enterprise software"
tools:
  - "SAP SuccessFactors"
frameworks:
  - "source-evidence matrix"
  - "human-capital-management-system-analysis-and-administration evidence matrix"
  - "qualified-review gate"
deliverables:
  - "SuccessFactors analysis and change brief"
commands: []
skills: []
evaluations:
  - "SAP SuccessFactors source-awareness check"
okb_bundle_id: sap-successfactors
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "hr-business-partner-hrbp"
  - "human-resources-generalist-hr-specialist"
  - "human-resources-manager"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Use official SAP SuccessFactors sources for general context; local human-capital management system analysis and administration, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for tenant, data center, release, and module scope, business configuration and effective dates, OData metadata, entities, fields, and API version, role-based permissions and target populations, workflow, rule, event, and integration configuration, employee, compensation, recruiting, or learning data definitions, and audit, test, privacy, and approval evidence."
  - "Do not infer tenant configuration, module availability, entities, fields, permissions, workflow state, employee data, integration state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before viewing or exporting restricted HR data, changing records, permissions, workflows, rules, integrations, compensation, recruiting, or employee status."
  - "Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-31"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 10
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# SAP SuccessFactors

Source-aware tool bundle for SAP SuccessFactors tenant, module, employee, workflow, integration, permission, reporting, and controlled HR-system briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/sap-successfactors-brief.md](deliverables/sap-successfactors-brief.md)
