---
type: Bundle Index
title: Design Operations (DesignOps) Manager
description: Source-aware role bundle for design-team workflow, tooling, governance, research operations, capacity, and approval-ready DesignOps improvements.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- designops
- design-operations
- design-governance
- role
aliases:
- Design Operations Manager
- DesignOps Manager
problems_solved:
- Prepare design operations improvement brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Design
- Digital products
tools: []
frameworks:
- source-evidence matrix
- design-operations evidence matrix
- qualified-review gate
deliverables:
- Design operations improvement brief
commands: []
skills: []
evaluations:
- Design Operations (DesignOps) Manager source-awareness check
okb_bundle_id: design-operations-designops-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- confluence
- figma
- jira
- okrs
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1082.00
  soc: []
  isco_08: []
  esco:
  - '2421'
limitations:
- Use as practitioner context; team structure, workflow, tools, repositories, research operations, governance, capacity, budgets, and maturity require local evidence.
- Task-specific work requires current evidence for design-team goals and service scope, workflow and handoff evidence, tool and repository configuration, design-system and research-operations state, governance and decision rights, capacity and demand evidence, budget, privacy, and approval policy.
- Do not infer team maturity, capacity, workflow state, tool configuration, adoption, research repository state, budget.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before participant data, research repositories, tool access, staffing, procurement, budgets, or organizational changes.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Design Operations (DesignOps) Manager

Source-aware role bundle for design-team workflow, tooling, governance, research operations, capacity, and approval-ready DesignOps improvements.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/designops-brief.md](deliverables/designops-brief.md)
