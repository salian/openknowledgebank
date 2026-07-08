---
type: Bundle Index
title: GDPR
description: Source-aware compliance hub for the EU General Data Protection Regulation.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - gdpr
  - privacy
  - data-protection
  - compliance
  - eu
aliases:
  - General Data Protection Regulation
  - Regulation EU 2016 679
problems_solved:
  - Triage GDPR applicability and obligation questions without inventing legal conclusions.
  - Separate official law, regulator guidance, user-provided facts, assumptions, and missing evidence.
  - Produce source-aware GDPR compliance briefs for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - controller-processor role triage
deliverables:
  - source-aware GDPR compliance brief
commands: []
skills: []
evaluations:
  - GDPR source-awareness check
okb_bundle_id: gdpr
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - gdpr-art22-automated-decision-making
  - gdpr-art27-eu-representative
  - gdpr-art28-controller-processor-contract
  - gdpr-art30-records-of-processing-activities
  - gdpr-art32-security-of-processing
  - gdpr-art33-breach-notification-supervisory-authority
  - gdpr-art35-dpia
  - gdpr-art37-dpo-designation
  - gdpr-data-subject-rights-access
  - gdpr-international-transfers-tia-supplementary-measures
  - gdpr-transparency-obligations
adjacent_bundles:
  - data-protection-officer-privacy-officer
  - compliance-officer
  - chief-compliance-officer-cco
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
  - This bundle is a compliance hub, not legal advice or a full article-by-article GDPR treatise.
  - Scenario-specific answers require current legal text, regulator guidance, jurisdiction facts, and user-provided processing evidence.
  - National derogations, supervisory authority guidance, enforcement positions, and contract language must be inspected before reliance.
safety_notes:
  - Require qualified legal or privacy professional review before relying on outputs for regulatory, enforcement, contractual, or incident-response decisions.
  - Do not request, expose, or publish personal data beyond what is necessary for the user-approved analysis.
  - Require explicit confirmation before submitting notices, contacting regulators, changing policies, or sending legal communications.
timestamp: "2026-07-09T00:00:00Z"
---

# GDPR

This bundle helps an agent answer GDPR questions with source discipline. It is a hub for triage, source selection, and public-safe compliance brief writing, not a replacement for legal advice.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the official legal text, relevant regulator guidance source category, user-provided evidence, and missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/gdpr-obligation-triage.md](workflows/gdpr-obligation-triage.md)
- [deliverables/source-aware-compliance-brief.md](deliverables/source-aware-compliance-brief.md)
- [evaluations/gdpr-source-awareness-check.md](evaluations/gdpr-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use EUR-Lex for the official GDPR legal text, European Commission pages for EU data protection framework context, EDPB guidance for EU-level regulator interpretation, national supervisory authority sources for local guidance, and user-provided records or documents for organization-specific facts.
