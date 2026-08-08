#!/usr/bin/env python3
"""Regression checks for automatic bundle content-risk inference."""

from __future__ import annotations

import unittest

from content_risk import infer_content_risk


class ContentRiskInferenceTest(unittest.TestCase):
    def test_general_role_has_no_inferred_professional_boundary(self) -> None:
        self.assertIsNone(
            infer_content_risk(
                {
                    "id": "seo-specialist-consultant",
                    "title": "SEO Specialist / Consultant",
                    "category": "roles",
                    "tags": ["search", "content strategy"],
                }
            )
        )

    def test_compliance_is_always_regulated(self) -> None:
        risk = infer_content_risk(
            {
                "id": "eu-ai-act",
                "title": "EU AI Act",
                "category": "compliance",
                "tags": ["artificial intelligence"],
            }
        )
        self.assertEqual("regulated", risk["classification"])
        self.assertEqual(["regulatory"], risk["domains"])

    def test_tax_role_is_ymyl(self) -> None:
        risk = infer_content_risk(
            {
                "id": "tax-accountant-tax-specialist",
                "title": "Tax Accountant / Tax Specialist",
                "category": "roles",
                "tags": ["accounting"],
            }
        )
        self.assertEqual("ymyl", risk["classification"])
        self.assertIn("tax", risk["domains"])
        self.assertIn("accounting", risk["domains"])

    def test_security_deliverable_is_regulated(self) -> None:
        risk = infer_content_risk(
            {
                "id": "incident-response-plan",
                "title": "Incident Response Plan",
                "category": "deliverables",
                "tags": ["security"],
            }
        )
        self.assertEqual("regulated", risk["classification"])
        self.assertEqual(["security"], risk["domains"])


if __name__ == "__main__":
    unittest.main()
