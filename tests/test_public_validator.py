import unittest

from src.public_validator import (
    route_card,
    select_active_standards,
    validate_repertoire_card,
)


def valid_repertoire_card():
    return {
        "title": "Bach – Goldberg-Variationen, BWV 988 – Variation 2",
        "card_type": "Repertoire",
        "composer": "Johann Sebastian Bach",
        "parent_work": "Bach – Goldberg-Variationen, BWV 988",
        "work_type": "Einzelstück",
        "standard_status": "active",
        "sections": [
            "Überblick",
            "Werkhintergrund",
            "Musikalische Merkmale",
            "Interpretation und Übung",
            "Quellen",
        ],
    }


class RoutingTests(unittest.TestCase):
    def test_routes_repertoire_card(self):
        self.assertEqual(route_card("Repertoire"), "repertoire")

    def test_rejects_unsupported_card_type(self):
        with self.assertRaises(ValueError):
            route_card("Unknown")


class StandardSelectionTests(unittest.TestCase):
    def test_excludes_legacy_and_inactive_standards(self):
        standards = [
            {"name": "Core 2.0", "status": "active", "active": True},
            {"name": "Core 1.0", "status": "legacy", "active": False},
            {"name": "Draft", "status": "active", "active": False},
        ]
        self.assertEqual(
            select_active_standards(standards),
            [{"name": "Core 2.0", "status": "active", "active": True}],
        )


class RepertoireValidationTests(unittest.TestCase):
    def test_accepts_conforming_card(self):
        self.assertEqual(validate_repertoire_card(valid_repertoire_card()), [])

    def test_rejects_unsupported_work_type(self):
        card = valid_repertoire_card()
        card["work_type"] = "Variation"
        errors = validate_repertoire_card(card)
        self.assertIn("unsupported work_type: Variation", errors)

    def test_reports_missing_required_section(self):
        card = valid_repertoire_card()
        card["sections"].remove("Quellen")
        errors = validate_repertoire_card(card)
        self.assertIn("missing sections: Quellen", errors)

    def test_requires_composer_relation(self):
        card = valid_repertoire_card()
        card["composer"] = ""
        errors = validate_repertoire_card(card)
        self.assertIn("composer relation is required", errors)


if __name__ == "__main__":
    unittest.main()
