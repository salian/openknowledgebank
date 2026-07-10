---
type: Bundle Index
title: CAN-SPAM
description: Source-aware compliance hub for U.S. commercial email marketing rules under the CAN-SPAM Act and FTC CAN-SPAM Rule.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - can-spam
  - email-marketing
  - commercial-email
  - ftc
  - united-states
  - compliance
aliases:
  - CAN-SPAM Act
  - FTC CAN-SPAM Rule
  - Commercial Email Marketing Rules
problems_solved:
  - Triage U.S. commercial email compliance questions without inventing legal conclusions.
  - Separate official FTC, statutory, and regulatory sources from user-provided campaign evidence, assumptions, and missing facts.
  - Produce source-aware CAN-SPAM compliance briefs for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - commercial email purpose triage
  - opt-out evidence review
deliverables:
  - source-aware CAN-SPAM compliance brief
commands: []
skills: []
evaluations:
  - CAN-SPAM source-awareness check
okb_bundle_id: can-spam
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
limitations:
  - This bundle is a compliance hub, not legal advice or a full section-by-section CAN-SPAM treatise.
  - Scenario-specific answers require current official source inspection and user-provided campaign, list, sender, and suppression-process evidence.
  - State privacy, TCPA, platform, deliverability, sector-specific, and international email requirements must be inspected separately when relevant.
safety_notes:
  - Require qualified legal or compliance professional review before relying on outputs for campaign, enforcement, contractual, or regulatory decisions.
  - Do not use this bundle for spam, phishing, deceptive sender identity, deceptive subject lines, list harvesting, evasion, or abuse workflows.
  - Require explicit confirmation before sending email, changing campaigns, uploading lists, exporting contacts, changing suppression logic, or sending legal communications.
timestamp: "2026-07-08T22:23:14Z"
---

# CAN-SPAM

This bundle helps an agent answer U.S. commercial email compliance questions with source discipline. It is a hub for triage, evidence collection, and public-safe compliance brief writing, not a replacement for legal advice.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the official FTC, statutory, or regulatory source category checked; the user-provided campaign or suppression evidence used; and any missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/can-spam-obligation-triage.md](workflows/can-spam-obligation-triage.md)
- [deliverables/source-aware-can-spam-compliance-brief.md](deliverables/source-aware-can-spam-compliance-brief.md)
- [evaluations/can-spam-source-awareness-check.md](evaluations/can-spam-source-awareness-check.md)
- [examples/index.md](examples/index.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use FTC business guidance for public compliance guidance, current eCFR 16 CFR Part 316 for the CAN-SPAM Rule, current U.S. Code or GovInfo text for the CAN-SPAM Act, and user-provided campaign evidence for organization-specific facts.
