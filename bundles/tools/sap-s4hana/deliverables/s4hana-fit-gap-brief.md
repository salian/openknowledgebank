---
type: Deliverable
title: SAP S/4HANA Fit-Gap Brief
description: "Source-aware brief for SAP S/4HANA business process, integration, reporting, or migration fit-gap analysis."
okb_bundle_id: sap-s4hana
required_inputs:
  - business requirement and owner
  - S/4HANA edition, release, localization, and activated scope evidence
  - current process, configuration, role, data, integration, or report evidence
outputs:
  - recommendation status
  - evidence matrix
  - fit-gap table
  - risks and confirmation boundaries
quality_criteria:
  - distinguishes official SAP facts, user-provided evidence, assumptions, and missing verification
  - avoids invented tenant configuration, object names, roles, APIs, reports, or data
  - lists risky actions requiring confirmation
timestamp: "2026-07-09T00:00:00Z"
---

# SAP S/4HANA Fit-Gap Brief

## Required Sections

1. **Decision question**: process, report, integration, migration, or configuration decision being supported.
2. **Source note**: official SAP source categories, user-provided local evidence, assumptions, and missing verification.
3. **Recommendation status**: ready to recommend, provisional, blocked, or needs SAP/customer-system inspection.
4. **Evidence matrix**: official SAP documentation checked, local tenant evidence checked, owner, date, and confidence.
5. **Fit-gap table**: requirement, SAP-standard option, customer-specific gap, dependency, risk, validation action, owner, and decision.
6. **Controls and confirmation boundary**: live-system actions, data movement, postings, role changes, transport, integration, or compliance decisions that require explicit confirmation.
7. **Next actions**: source inspection, workshop, prototype, SAP partner review, security review, data migration review, or implementation decision.

## Quality Bar

The brief must not present plausible SAP object names, app IDs, tables, CDS views, APIs, roles, configuration activities, scope items, or report definitions as facts unless they are grounded in official SAP sources or user-provided local evidence.
