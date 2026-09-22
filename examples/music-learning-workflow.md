# Example: classify a music-learning request

This is an **illustrative walkthrough of active routing rules**, not a claim that this exact conversation was executed and stored.

> “I have trouble memorising a passage. I want a reusable method, and I also want to record what happened in today's practice.”

| Part | Card type | Reason |
|---|---|---|
| A reusable memorisation method | Musiklernen → Wissenskarte | Reusable skill for later sessions |
| Today's observations and next exercise | Musiklernen → Log, Practice | Concrete dated practice event |

**Wissenskarte route:** Core → Musiklernen Structure → Wissenskarte Structure/Standard/Template → Core QA → Wissenskarte QA.

**Practice Log route:** Core → Musiklernen Structure → shared Log Structure/Standard → Practice Log Standard/Template → Core QA → shared Log QA → Practice Log QA.

| Property | Wissenskarte | Practice Log |
|---|---|---|
| Kartentyp | Wissenskarte | Log |
| Log Type | Empty | Practice |
| Datum | Normally empty | Actual practice date |
| Instrument | Actual instrument if relevant | Actual instrument |
| Repertoire | Only for a specific-work connection | Only for works actually practised |

The system checks **actual Heptabase properties**, not merely a Markdown table in a card body. After an authorised create/update it reads the card back to verify content, properties and relations. A request only for advice can be answered without creating cards.

A Lernsystem card describes how evidence from practice, lessons and performances informs goals and priorities. It is a **Musiklernen card type**, not an MKA Standard module. No separate Lernsystem template is loaded.
