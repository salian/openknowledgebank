---
type: Deliverable
title: Cybersecurity Incident Response Plan Package
description: Defines the governance, evidence, authority, lifecycle, communications, notification, recovery, and improvement contract for a reviewable incident response plan.
okb_bundle_id: incident-response-plan
required_inputs:
- organization, jurisdiction, sector, service, asset, data, architecture, dependency, and risk context
- current incident-response, legal, regulatory, contractual, insurance, evidence, privacy, continuity, and recovery sources
- roles, alternates, decision authority, approved channels, suppliers, and contact-validation evidence
- detection, response, recovery, exercise, incident, and improvement evidence when available
outputs:
- versioned incident response plan
- activation, severity, escalation, role, authority, and communication matrices
- evidence, decision, obligation, stakeholder, recovery, and closure registers
- exercise, metric, improvement, and maintenance plan
quality_criteria:
- exact obligations, thresholds, contacts, actions, and decisions trace to current sources and organization evidence
- observed facts, hypotheses, decisions, actions, approvals, and outcomes remain distinct
- consequential action requires named authority, safety and business-impact review, evidence preservation, rollback, and confirmation
resource: https://csrc.nist.gov/pubs/sp/800/61/r3/final
timestamp: '2026-08-07T00:00:00Z'
---

# Cybersecurity Incident Response Plan Package

## Output Contract

1. **Document control:** identify organization and plan scope, jurisdictions and sector, covered services/assets/data, version, effective date, owner, reviewers, approval authority, distribution classification, exercise date, and superseded material only when evidenced.
2. **Source note:** distinguish external guidance from local authority and evidence: law/regulation, contracts, insurer terms, policies, risk/assets/data, architecture/dependencies, identities, telemetry, backups, continuity/recovery, suppliers, contacts, procedures, exercises, and incident records.
3. **Evidence status:** list `Verified`, `Provided`, `Assumed`, and `Needs verification`. For incident records additionally separate `Observed`, `Hypothesis`, `Decision`, `Authorized action`, and `Outcome`. With no local evidence, set verified/assumed incident facts to `None`.
4. **Governance and scope:** define plan purpose, covered incident types and environments, relationship to enterprise risk, security operations, privacy, safety, business continuity, disaster recovery, crisis management, legal/privilege, insurance, communications, HR, suppliers, and law enforcement.
5. **Activation and classification:** define locally approved event/incident criteria, declaration authority, severity/impact dimensions, confidence, escalation, reassessment, downgrade, and closure. Do not import a severity scale or deadline without source and approval.
6. **Roles and decision authority:** identify primary and alternate incident leadership, technical, service/business, legal/privacy, evidence/forensics, continuity/recovery, communications, HR, physical safety, insurance, supplier, regulator, and executive roles. For each consequential decision state who recommends, authorizes, executes, validates, is informed, and records it.
7. **Detection and analysis:** define intake sources, record creation, chronology, triage, asset/data/service scope, evidence provenance, hypothesis and confidence, impact, related cases, escalation, and handoff. Preserve unknowns and contradictory telemetry rather than forcing certainty or attribution.
8. **Response and containment contract:** describe approved decision criteria for isolation, blocking, access or credential changes, service degradation, supplier coordination, data protection, or other containment. Require authorization, safety and business impact, evidence risk, dependencies, rollback/fallback, communication, timestamp, executor evidence, and validation before recording an action as complete.
9. **Eradication and recovery contract:** require cause and persistence hypotheses, remediation scope, integrity checks, trusted recovery source, dependency order, restoration criteria, heightened monitoring, fallback, business-owner acceptance, and residual risk. Recovery of service does not by itself prove eradication, data integrity, notification completion, or incident closure.
10. **Evidence and records:** define approved evidence identifiers, provenance, collection authority, timestamps/time source, access, integrity, transfer, storage, retention/legal hold, disclosure, and disposition. Detailed forensic procedures and chain-of-custody forms must come from qualified organization-specific sources.
11. **Communications and notification:** separate internal coordination, executive updates, workforce communication, supplier/customer obligations, insurer notice, regulator/government reporting, law enforcement, affected-person notice, information sharing, and public statements. For each, record trigger, authority, deadline source, content owner, facts approved for release, channel, evidence, and status; never infer that notification is required or completed.
12. **Closure and improvement:** define technical stabilization, recovery acceptance, evidence/record completeness, obligation tracking, residual risk, ongoing monitoring, ownership, closure authority, after-action/postmortem, corrective actions, metrics, exercise lessons, plan/source updates, and verification. Keep closure distinct from resolution of every legal, customer, insurance, or improvement item.

## Reconciliation Rule

When telemetry, reports, timestamps, asset identities, data scope, impact, or obligations disagree, no source is automatically right. Align source/provenance, clock and timezone, asset/account identity, environment, collection window, retention, query/filter, detection rule version, scope, duplication, confidence, and chain of custody. Record the reconciled conclusion and remaining uncertainty; do not alter evidence or manufacture a single narrative.

## Source Note

NIST SP 800-61 Rev. 3 is the current core source and supersedes Rev. 2. NIST CSF 2.0 supplies risk-management outcomes; NIST SP 800-184 adds recovery planning; CISA provides useful but partly federal-specific playbooks; FTC provides general U.S. breach-response guidance. Exact obligations and response decisions require current organization-, sector-, jurisdiction-, contract-, and incident-specific review.

## Safety Boundary

This package contains no commands, scripts, indicators, malware, credentials, live contacts, reporting endpoints, forensic acquisition steps, isolation instructions, restoration actions, notification text, or ransom guidance. A consuming agent must treat the document as planning guidance, not trusted executable behavior. Consequential action requires explicit human authorization and approved procedures.
