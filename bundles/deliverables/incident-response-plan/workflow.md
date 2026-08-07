---
type: Workflow
title: Incident Response Plan Development and Review Workflow
description: An inspect-first sequence for grounding, drafting, exercising, and maintaining a cybersecurity incident response plan.
okb_bundle_id: incident-response-plan
inputs:
- organization risk, service, asset, data, architecture, obligation, and dependency sources
- response, evidence, communication, continuity, recovery, supplier, and contact evidence
- incident, exercise, metric, and improvement records when available
outputs:
- reviewable incident response plan
- authority, evidence, obligation, recovery, and communication registers
- exercise and maintenance decision record
resource: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
timestamp: '2026-08-07T00:00:00Z'
---

# Incident Response Plan Development and Review Workflow

1. **Set scope and authority.** Identify organization, jurisdictions, sector, covered services/assets/data, plan owner, executive authority, distribution, interfaces with other plans, and explicit exclusions.
2. **Inventory sources and capabilities.** Collect current obligations, policies, insurer/contracts, risk/assets/data, architecture/dependencies, identities, telemetry, backups, continuity/recovery, suppliers, channels, procedures, roles, alternates, and exercise/incident evidence.
3. **Map applicability and obligations.** Record each legal, regulatory, contractual, insurer, customer, government, information-sharing, evidence, retention, and notification surface with trigger, deadline source, owner, reviewer, and unresolved question.
4. **Design governance.** Define activation, declaration, severity/impact dimensions, escalation, incident leadership, alternates, handoffs, decision authority, recordkeeping, privilege decisions, communication cadence, and closure authority.
5. **Design evidence and analysis.** Specify intake, chronology, scope, provenance, confidence, hypothesis, impact, contradiction, handoff, preservation, access, retention, and disclosure requirements without embedding forensic commands.
6. **Design authorized response decisions.** For each response category define recommendation and approval roles, safety/business/evidence considerations, dependencies, rollback, communication, execution evidence, and validation. Keep the plan declarative and link only to approved controlled procedures.
7. **Integrate recovery and continuity.** Align restoration priority, trusted sources, integrity validation, dependencies, recovery objectives, fallback, monitoring, business acceptance, residual risk, and continuity/crisis interfaces.
8. **Design communications and notification.** Separate audiences and obligations; define fact approval, legal/privacy/security review, channels, alternates, records, and source-backed timing. Avoid pre-deciding notification from hypothetical facts.
9. **Review operational fit.** Validate that roles, alternates, contacts, channels, tools, telemetry, suppliers, evidence handling, backups, authority, procedures, and staffing exist and are accessible under expected failure conditions.
10. **Exercise and improve.** Use approved, non-production scenarios to test decisions, handoffs, out-of-band communication, evidence, obligations, recovery, and fallback. Record observations, owners, due dates, retest evidence, and plan changes without claiming readiness from attendance alone.
11. **Approve and maintain.** Obtain qualified security, legal/privacy, business, continuity, communications, HR, insurance, supplier, and executive review as applicable; control version/distribution; validate contacts and dependencies; monitor source changes; and update after incidents, exercises, major changes, or review dates.

## Review Questions

- Is Rev. 3 used instead of superseded NIST SP 800-61 Rev. 2?
- Do local definitions, severity, activation, authority, contacts, channels, and obligations have evidence?
- Can responders distinguish observations, hypotheses, decisions, actions, approvals, and outcomes?
- Are disruptive actions gated by authority, safety/business impact, evidence preservation, rollback, and validation?
- Are notification audiences, triggers, deadlines, content approval, and completion states separated?
- Does recovery require integrity validation, business acceptance, monitoring, fallback, and residual-risk ownership?
- Have contacts, dependencies, suppliers, exercises, improvements, and source updates been maintained?

## Confirmation Boundary

The plan may identify decision categories but does not authorize system isolation, traffic blocking, account or credential changes, evidence acquisition, eradication, restoration, reporting, notification, disclosure, law-enforcement contact, attacker contact, or ransom decisions. Each requires current incident evidence, approved procedures, and explicit accountable confirmation.
