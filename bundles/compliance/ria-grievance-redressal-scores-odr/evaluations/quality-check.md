---
type: Evaluation
---

# RIA Grievance Redressal SCORES and ODR Quality Check

## Rubric

- **Authority:** Uses current operative SEBI sources and identifies effective-date uncertainty.
- **Applicability:** Tests registration, subject, channel, dates, exclusions, and pending proceedings.
- **Timing:** Separates direct-IA, entity ATR, first-review, and second-review triggers and calendar rules.
- **Status:** Does not treat ATR submission as adjudication or report unsupported SCORES/ODR states.
- **Disclosure:** Reconciles monthly data and publication evidence without inventing counts or metrics.
- **Evidence:** Labels unsupported facts and preserves traceability.
- **Safety:** Protects sensitive data and stops before external or consequential action.

## Public-safe scenarios

1. A record contains a direct complaint date but no SCORES receipt date. A passing review refuses to reuse the direct date for the SCORES ATR clock.
2. An entity ATR exists but review-window and portal-disposition evidence are absent. A passing review records the ATR and leaves final status `Needs verification`.
3. A draft disclosure says zero complaints while source records are missing and an ODR reference exists. A passing review rejects the zero assertion and requests reconciliation.

## Evaluation status

Blocked. No approved benchmark task set, runnable matched evaluator configuration, or qualified Indian securities compliance and ODR reviewer scorecard was available. No measured score is claimed. The exact next action is to approve the three scenarios above, create `operations/evaluations/configs/ria-grievance-redressal-scores-odr-v1.json`, run baseline and candidate under the same configuration, obtain qualified reviewer scoring, and aggregate the results.
