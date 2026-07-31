---
type: Bundle Index
title: Data Architect
description: Source-aware role bundle for data-domain architecture, modeling and contracts, integration and lineage review, governance, and implementation-ready architecture briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- data-architecture
- data-modeling
- data-governance
- role
aliases:
- Data Architect
- Enterprise Data Architect
problems_solved:
- Prepare data architecture and governance decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Data and analytics
- Software
tools: []
frameworks:
- source-evidence matrix
- data-architecture evidence matrix
- qualified-review gate
deliverables:
- Data architecture and governance decision brief
commands: []
skills: []
evaluations:
- Data Architect source-awareness check
okb_bundle_id: data-architect
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- google-bigquery
- hipaa
- soc-2
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1243.00
  soc: []
  isco_08: []
  esco:
  - '2521.1'
limitations:
- Use as occupational context; domains, schemas, contracts, lineage, classification, retention, access, workloads, and platform state require inspected evidence.
- Task-specific work requires current evidence for business domains and ownership, current logical and physical models, source and consumer contracts, lineage and quality evidence, data classification and retention policy, identity and access controls, workload, SLO, and cost constraints.
- Do not infer domains, schemas, fields, relationships, lineage, classification, retention, access, cost.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before data classification, access, retention, schema migrations, production data, privacy, or security.
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
  baseline_score: 11
  okb_score: 33
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Data Architect

Source-aware role bundle for data-domain architecture, modeling and contracts, integration and lineage review, governance, and implementation-ready architecture briefs.

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
- [deliverables/data-architecture-brief.md](deliverables/data-architecture-brief.md)
