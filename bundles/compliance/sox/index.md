---
type: Bundle Index
title: SOX
description: Source-aware compliance hub for Sarbanes-Oxley Act executive certification, disclosure controls, ICFR assessment, and auditor-attestation triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - sox
  - sarbanes-oxley
  - compliance
  - financial-reporting
  - icfr
  - sec
  - pcaob
  - united-states
aliases:
  - Sarbanes-Oxley Act
  - Sarbanes-Oxley Act of 2002
  - SOX compliance
  - SOX 302
  - SOX 404
problems_solved:
  - Triage SOX certification and ICFR questions without inventing legal, accounting, audit, or filing conclusions.
  - Separate official statutory, SEC, PCAOB, user-provided, assumed, and missing evidence.
  - Produce source-aware SOX compliance briefs for qualified professional review.
industries:
  - public-companies
  - financial-reporting
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - disclosure-controls versus ICFR triage
  - management-assessment and auditor-attestation handoff
deliverables:
  - source-aware SOX compliance brief
commands: []
skills: []
evaluations:
  - SOX source-awareness check
okb_bundle_id: sox
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: blocked
license: CC-BY-4.0
related_bundles: []
adjacent_bundles:
  - soc-2
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - This bundle is a compliance hub, not legal, accounting, securities, audit, attestation, or CPA advice.
  - Scenario-specific conclusions require current statutory text, SEC rules and guidance, PCAOB standards where relevant, issuer facts, user-provided evidence, and qualified professional review.
  - Issuer applicability, filer status, exemptions, certification readiness, ICFR effectiveness, deficiency severity, auditor-attestation applicability, filing deadlines, and exact certification text must be verified before reliance.
  - Measured evaluation is planned but not complete.
safety_notes:
  - Require qualified legal, accounting, audit, disclosure-control, securities, or CPA professional review before relying on outputs for filings, certifications, control conclusions, auditor communications, regulator communications, or remediation decisions.
  - Do not request, expose, or publish confidential issuer evidence, nonpublic financial data, audit workpapers, legal advice, board materials, credentials, or control documentation beyond what is necessary for user-approved analysis.
  - Require explicit confirmation before contacting auditors, regulators, executives, the board, or external parties; changing controls; exporting evidence; approving certifications; submitting filings; or modifying live financial-reporting systems.
evaluation_summary:
  status: "measured"
  last_evaluated: "2026-07-09"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 30
  baseline_score: 16
  okb_score: 29
  absolute_lift: 13
  display_summary: "Improved measured rubric score from 16/30 to 29/30 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts, raw outputs, and provider response artifacts. Private artifacts are retained in the evaluation run folder."
timestamp: "2026-07-09T00:00:00Z"
---

# SOX

This bundle helps an agent answer Sarbanes-Oxley Act questions with source discipline. It is a hub for executive certification, disclosure-controls, ICFR assessment, and auditor-attestation triage, not a substitute for current SEC sources, PCAOB standards, issuer evidence, or professional judgment.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the official statutory, SEC, or PCAOB source category; user-provided issuer evidence; assumptions; and missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/sox-obligation-triage.md](workflows/sox-obligation-triage.md)
- [deliverables/source-aware-sox-compliance-brief.md](deliverables/source-aware-sox-compliance-brief.md)
- [evaluations/sox-source-awareness-check.md](evaluations/sox-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use statutory text for SOX section identification, SEC rules and guidance for issuer reporting and certification questions, PCAOB standards for auditor integrated-audit context, issuer filings and company records for organization-specific facts, and qualified professional review for reliance decisions.
