# End-to-End Example: Repertoire Card

This reduced example demonstrates the workflow without connecting to a private Heptabase workspace.

## 1. User request

> Create an MKA repertoire card for Bach's Goldberg Variations, BWV 988, Variation 2.

## 2. Routing decision

```json
{
  "intent": "create_card",
  "card_type": "repertoire",
  "modules": ["core", "repertoire"],
  "standard_status": "active"
}
```

The agent selects the Repertoire module. Musician, music-history and log standards are not loaded.

## 3. Retrieved context

In the production workflow, the agent searches for existing related cards before creating content. A reduced result might be:

```json
{
  "composer_card": "Johann Sebastian Bach",
  "parent_work_card": "Bach – Goldberg-Variationen, BWV 988",
  "duplicate_found": false
}
```

## 4. Generated draft

```yaml
title: "Bach – Goldberg-Variationen, BWV 988 – Variation 2"
card_type: "Repertoire"
composer: "Johann Sebastian Bach"
parent_work: "Bach – Goldberg-Variationen, BWV 988"
work_type: "Einzelstück"
standard_status: "active"
sections:
  - Überblick
  - Werkhintergrund
  - Musikalische Merkmale
  - Interpretation und Übung
  - Quellen
```

## 5. Validation

| Check | Expected outcome | Demo outcome |
|---|---|---|
| Supported card type | `Repertoire` | Pass |
| Active standard | Legacy rules excluded | Pass |
| Required sections | All present | Pass |
| Approved `work_type` | `Einzelstück` | Pass |
| Composer relation | Existing card reused | Pass |
| Parent-work relation | Existing card reused | Pass |

## 6. Persistence boundary

After Final QA passes, the production agent sends a structured create request through MCP. The public demo stops at this boundary and does not include credentials or private endpoint details.

## 7. Post-write verification

The production workflow re-reads the created card and compares the persisted title, properties, sections and relations with the validated draft. A discrepancy is reported instead of being silently accepted.

## Result

The example demonstrates controlled routing, selective rule loading, relation reuse, pre-write validation and post-write verification. It does not claim to reproduce the complete private MKA rule set.
