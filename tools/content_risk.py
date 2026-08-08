#!/usr/bin/env python3
"""Infer conservative professional-review boundaries from bundle metadata."""

from __future__ import annotations

import re
from typing import Any


DOMAIN_ORDER = [
    "medical",
    "tax",
    "accounting",
    "financial",
    "insurance",
    "legal",
    "employment",
    "privacy",
    "security",
    "safety",
    "regulatory",
]

YMYL_DOMAINS = {
    "medical",
    "tax",
    "accounting",
    "financial",
    "insurance",
    "legal",
    "employment",
}

DOMAIN_PATTERNS = {
    "medical": re.compile(
        r"\b(medical|clinical|physician|doctor|surgeon|nurse|dentist|dental|"
        r"healthcare|health care|pharmacy|pharmacist|pharmacology|therapist|"
        r"psychologist|psychiatrist|mental health|dietitian|nutritionist|medicaid|"
        r"medicare|hipaa|patient)\b"
    ),
    "tax": re.compile(r"\b(tax|taxation)\b"),
    "accounting": re.compile(
        r"\b(accountant|accounting|auditor|bookkeeping|bookkeeper|controller|"
        r"payroll|accounts payable|accounts receivable|ifrs)\b"
    ),
    "financial": re.compile(
        r"\b(financial|finance|investment|wealth|banking|credit analyst|loan|"
        r"mortgage|securities|financial adviser|financial advisor|stockbroker|"
        r"actuary|revenue officer|cash flow|treasurer)\b"
    ),
    "insurance": re.compile(r"\binsurance\b"),
    "legal": re.compile(
        r"\b(legal|lawyer|attorney|counsel|paralegal|litigation|contract manager|"
        r"notary|compliance officer|regulatory affairs)\b"
    ),
    "employment": re.compile(
        r"\b(human resources|recruiter|recruiting|talent acquisition|compensation|"
        r"employee|employment|workplace|labor relations|benefits|diversity officer|"
        r"chro|job description)\b"
    ),
    "privacy": re.compile(r"\b(privacy|data protection|gdpr|ccpa)\b"),
    "security": re.compile(
        r"\b(cybersecurity|cyber security|information security|security officer|"
        r"security policy|incident response|ciso)\b"
    ),
    "safety": re.compile(r"\b(safety|emergency|hazard|occupational health)\b"),
}

QUALIFICATION_LABELS = {
    "medical": "healthcare",
    "tax": "tax",
    "accounting": "accounting",
    "financial": "financial",
    "insurance": "insurance",
    "legal": "legal",
    "employment": "employment or human-resources",
    "privacy": "data-protection",
    "security": "information-security",
    "safety": "safety",
    "regulatory": "compliance",
}


def _string_values(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def searchable_text(bundle: dict[str, Any]) -> str:
    """Return stable public metadata used for conservative risk inference."""
    values = [
        str(bundle.get("id", "")),
        str(bundle.get("title", "")),
        *_string_values(bundle.get("aliases", [])),
        *_string_values(bundle.get("tags", [])),
    ]
    return re.sub(r"[-_/]+", " ", " ".join(values).lower())


def infer_domains(bundle: dict[str, Any]) -> list[str]:
    text = searchable_text(bundle)
    matched = {
        domain
        for domain, pattern in DOMAIN_PATTERNS.items()
        if pattern.search(text)
    }
    if bundle.get("category") == "compliance":
        matched.add("regulatory")
    return [domain for domain in DOMAIN_ORDER if domain in matched]


def _join_labels(labels: list[str]) -> str:
    if len(labels) == 1:
        return labels[0]
    if len(labels) == 2:
        return f"{labels[0]} or {labels[1]}"
    return ", ".join(labels[:-1]) + f", or {labels[-1]}"


def required_qualification(domains: list[str]) -> str:
    labels: list[str] = []
    for domain in domains:
        label = QUALIFICATION_LABELS[domain]
        if label not in labels:
            labels.append(label)
    return (
        f"A qualified {_join_labels(labels)} professional appropriate to the "
        "question, decision, organization, and jurisdiction."
    )


def infer_content_risk(bundle: dict[str, Any]) -> dict[str, Any] | None:
    """Return required conservative metadata, or None for no detected signal."""
    domains = infer_domains(bundle)
    if not domains:
        return None
    classification = "ymyl" if YMYL_DOMAINS.intersection(domains) else "regulated"
    return {
        "classification": classification,
        "domains": domains,
        "professional_review": {
            "status": "not_reviewed",
            "required_qualification": required_qualification(domains),
        },
    }
