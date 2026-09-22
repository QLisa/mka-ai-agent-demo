# Test results and evidence boundary

## Public offline demo

Executed on **2026-09-22** with `python -m unittest discover -s tests -v`.

| Suite | Passed | Failed |
|---|---:|---:|
| Reduced Repertoire validation | 4 | 0 |
| Simplified routing | 2 | 0 |
| Active/legacy selection | 1 | 0 |
| **Total** | **7** | **0** |

The hard-coded schema is smaller than the live standards. These passes do **not** certify a production MKA card.

## Live MKA evidence read for this update

The private **“MKA Test Report — Musiklernen Datenmodell und Lernsystem-Routing v1.0 — 2026-09-22”** was read on 2026-09-22. It records `Durchführungsstatus=Abgeschlossen` and `Freigabe=Freigegeben`, refers to its Test Plan, lists tested versions and cases ML-01 to ML-09, and documents both pre-activation results and post-activation read-back of Index v2.10, Test Governance v1.3 and Musiklernen Structure v1.0. Separate obsolete Lernsystem modules were excluded.

This is evidence recorded in a **private live system**, not an independently reproducible test run from the public repository. The public documentation does not expose personal card contents or credentials.

## Skill and GPT evidence

| Component | Checked for this update | Not established by this check |
|---|---|---|
| Card Builder Skill | Current available instructions inspected on 2026-09-22; they require live Index loading, pre-write QA, actual property edits and read-back QA | No end-to-end Skill execution was run for this portfolio update |
| MKA GPT | Owner clarified that three languages are displayed as entry examples; conversation and generated-output languages can be chosen separately, including other languages | Current editor configuration, systematic language tests, enabled integrations and direct Skill invocation have not been independently verified |
| Daily practice automation | Enabled daily 09:00 Europe/Berlin schedule, prompt and two dated Heptabase cards inspected | On-time delivery for every day, actual practice progress, and the outcome of the next run after the prompt edit |

## Practice Log format regression observed

The 2026-09-21 card contains the active Template's explanatory paragraph under “練習後紀錄”. The 2026-09-22 card lacks that paragraph. Both cards have the expected basic properties and practice tables, with empty user-result cells. The saved automation prompt was updated after the 22 September run to require live Template loading and read-back. **Status: prompt updated, subsequent scheduled output not verified.** See [case study](../examples/daily-practice-planning.md).

Proposed cases, card QA, pre-activation approval and completed activation are distinct outcomes. Future results should state exact scope and execution date.
