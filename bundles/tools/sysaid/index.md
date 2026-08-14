---
type: "Bundle Index"
title: "SysAid"
description: "Source-aware guidance for SysAid ITSM incidents, requests, assets, service catalog, workflows, self-service, Copilot and agentic AI, integrations, APIs, and administration."
category: tools
version: 0.1.0
tags:
- "tool"
- "source-aware"
aliases:
- "SysAid ITSM"
- "SysAid Copilot"
problems_solved:
- "Review product use from current official sources and inspected local evidence."
- "Prepare a controlled decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "SysAid"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "SysAid ITSM, automation, and AI governance review brief"
commands: []
skills: []
evaluations:
- "SysAid source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "ymyl"
  domains:
  - "financial"
  - "legal"
  - "privacy"
  - "regulatory"
  - "safety"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and domain, privacy, security, legal, financial, safety, employment, healthcare, tax, education, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for current product identity and lifecycle, account or deployment, plan and region, users and roles, configuration, source data, permissions, integrations, logs, controls, validation, rollback, and approval evidence."
- "This bundle does not grant authority to access user or asset data, create or alter tickets, changes or approvals, run discovery or automation, enable AI agents, connect systems, expose credentials, or represent identity, priority, SLA, resolution, change success, security, or compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before access user or asset data, create or alter tickets, changes or approvals, run discovery or automation, enable AI agents, connect systems, expose credentials, or represent identity, priority, SLA, resolution, change success, security, or compliance."
timestamp: "2026-08-14T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: sysaid
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# SysAid

Use this bundle to prepare a reviewable **SysAid ITSM, automation, and AI governance review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent record or asset identity, urgency or priority, SLA state, AI output, automation or API result, change approval, resolution, security finding, compliance, or authorization.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [SysAid ITSM, automation, and AI governance review brief](deliverables/sysaid-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
