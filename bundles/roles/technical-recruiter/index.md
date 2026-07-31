---
type: Bundle Index
title: Technical Recruiter
description: Source-aware role bundle for technical hiring intake, sourcing and screening plans, structured interview evidence, candidate communication, and approval-ready hiring briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- technical-recruiting
- structured-hiring
- candidate-evidence
- role
aliases:
- Technical Recruiter
- Technology Recruiter
problems_solved:
- Prepare technical hiring and candidate review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Human resources
- Technology
tools: []
frameworks:
- source-evidence matrix
- hiring-evidence matrix
- qualified-review gate
deliverables:
- Technical hiring and candidate review brief
commands: []
skills: []
evaluations:
- Technical Recruiter source-awareness check
okb_bundle_id: technical-recruiter
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ada
- eeoc
- federal-contractor-affirmative-action
- gdpr
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1071.00
  soc: []
  isco_08: []
  esco:
  - '2423'
limitations:
- Use as occupational context; requisitions, competencies, candidate facts, consent, assessments, accommodations, compensation, and decisions require current authorized evidence.
- Task-specific work requires current evidence for approved requisition and competencies, job-related screening criteria, candidate-provided materials and consent, structured interview scorecards, accommodation and communications policy, compensation authority, decision owners and audit trail.
- Do not infer candidate qualifications, identity traits, employment history, consent, assessment results, compensation, hiring decision.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before candidate data, screening, employment decisions, accommodations, compensation, or communications.
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
  okb_score: 31
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 3
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 9/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Technical Recruiter

Source-aware role bundle for technical hiring intake, sourcing and screening plans, structured interview evidence, candidate communication, and approval-ready hiring briefs.

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
- [deliverables/technical-recruiting-brief.md](deliverables/technical-recruiting-brief.md)
