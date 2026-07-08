---
type: Workflow
title: SOC 2 Readiness Triage
description: Source-aware workflow for triaging SOC 2 readiness and customer-trust questions without inventing audit conclusions.
tags:
  - soc-2
  - readiness
  - evidence
okb_bundle_id: soc-2
outputs:
  - source-aware SOC 2 readiness brief
  - evidence gap list
  - professional-review handoff
timestamp: "2026-07-09T00:00:00Z"
---

# SOC 2 Readiness Triage

Use this workflow when a user asks whether SOC 2 applies, what evidence is needed, how to answer a customer, or whether they are ready for an audit.

## 1. Classify the Question

Identify whether the question is about:

- SOC service framing;
- trust services category scoping;
- Type I versus Type II readiness;
- system description;
- control inventory or evidence collection;
- customer questionnaire response;
- report sharing or bridge-period explanation;
- auditor handoff.

## 2. Establish Source Scope

Name the source categories used for the answer:

- AICPA/CIMA SOC suite materials for SOC service framing.
- AICPA/CIMA Trust Services Criteria for security, availability, processing integrity, confidentiality, and privacy category framing.
- AICPA/CIMA SOC 2 Description Criteria for system description questions.
- Auditor request lists, engagement letters, and report materials for engagement-specific facts.
- User-provided system descriptions, control inventories, policies, tickets, logs, and evidence exports for organization-specific facts.

If the necessary source is not available, keep the answer at triage level.

## 3. Separate Evidence Classes

Create four buckets:

- **Verified from source:** facts found in official source categories, auditor requests, or provided report materials.
- **Provided by user:** facts the user states or uploads.
- **Assumed for draft:** temporary assumptions needed to outline next steps.
- **Needs verification:** missing source material, evidence, scope, period, control owner, or reviewer input.

## 4. Scope the Trust Services Category Question

If the user asks which categories apply, do not infer from company type alone. Ask for customer requirements, contract commitments, security claims, system boundaries, auditor scoping notes, and current business commitments.

Use the category names only as high-level framing unless the user provides current AICPA criteria or an auditor request that supports deeper mapping.

## 5. Handle Type I and Type II Carefully

For readiness work, distinguish design/readiness questions from operating-period evidence questions. Do not claim that a report type, period, opinion, or scope exists unless the user provides the actual report or auditor evidence.

## 6. Produce the Handoff

The output should include:

- direct triage answer;
- source note;
- scope, category, and report-type framing;
- evidence available and evidence missing;
- professional-review boundary;
- next evidence requests or reviewer handoff.

Use the [source-aware SOC 2 readiness brief](../deliverables/source-aware-soc-2-readiness-brief.md) when the user needs a formal deliverable.
