---
type: Bundle Index
title: Supply Chain Analyst
description: Source-aware role bundle for demand, supply, inventory, supplier, transport, and service analysis with decision-ready scenario and exception briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- supply-chain
- logistics-analysis
- inventory
- role
aliases:
- Supply Chain Analyst
- Logistics Analyst
problems_solved:
- Prepare supply-chain scenario and exception brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Supply chain
- Logistics
tools: []
frameworks:
- source-evidence matrix
- supply-chain evidence matrix
- qualified-review gate
deliverables:
- Supply-chain scenario and exception brief
commands: []
skills: []
evaluations:
- Supply Chain Analyst source-awareness check
okb_bundle_id: supply-chain-analyst
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- c-tpat
- fda-qmsr-13485
- microsoft-power-bi
- sap-s4hana
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1081.02
  soc: []
  isco_08: []
  esco:
  - '2421'
limitations:
- Use as occupational context; item, location, period, demand, inventory, lead time, supplier, transport, cost, and service data require current evidence.
- Task-specific work requires current evidence for item, location, and time grain, demand and order definitions, inventory and capacity state, lead-time and supplier evidence, transport and service constraints, cost and currency definitions, policy and approval limits.
- Do not infer demand, inventory, lead times, supplier status, capacity, cost, service level, order state.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before orders, suppliers, production, inventory, transport, regulated goods, or financial commitments.
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
  baseline_score: 9
  okb_score: 33
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 9/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Supply Chain Analyst

Source-aware role bundle for demand, supply, inventory, supplier, transport, and service analysis with decision-ready scenario and exception briefs.

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
- [deliverables/supply-chain-brief.md](deliverables/supply-chain-brief.md)
