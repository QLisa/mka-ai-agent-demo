"""Reduced, privacy-safe validator used by the public MKA portfolio demo."""

SUPPORTED_CARD_TYPES = {
    "Repertoire": "repertoire",
    "Musiker": "musician",
    "Musikgeschichte": "music_history",
    "Practice Log": "practice_log",
}

REQUIRED_REPERTOIRE_SECTIONS = {
    "Überblick",
    "Werkhintergrund",
    "Musikalische Merkmale",
    "Interpretation und Übung",
    "Quellen",
}

APPROVED_WORK_TYPES = {"Einzelstück", "Sammlung", "Satz"}


def route_card(card_type: str) -> str:
    """Return the active module for a supported card type."""
    try:
        return SUPPORTED_CARD_TYPES[card_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported card type: {card_type}") from exc


def select_active_standards(standards: list[dict]) -> list[dict]:
    """Exclude legacy or explicitly inactive standards."""
    return [
        standard
        for standard in standards
        if standard.get("status") == "active" and standard.get("active", True)
    ]


def validate_repertoire_card(card: dict) -> list[str]:
    """Return validation errors for the reduced public Repertoire schema."""
    errors: list[str] = []

    if card.get("card_type") != "Repertoire":
        errors.append("card_type must be Repertoire")

    if card.get("standard_status") != "active":
        errors.append("standard_status must be active")

    work_type = card.get("work_type")
    if work_type not in APPROVED_WORK_TYPES:
        errors.append(f"unsupported work_type: {work_type}")

    sections = set(card.get("sections", []))
    missing = sorted(REQUIRED_REPERTOIRE_SECTIONS - sections)
    if missing:
        errors.append("missing sections: " + ", ".join(missing))

    if not card.get("composer"):
        errors.append("composer relation is required")

    return errors
