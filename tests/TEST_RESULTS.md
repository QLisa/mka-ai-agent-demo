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

Proposed cases, card QA, pre-activation approval and completed activation are distinct outcomes. Future results should state exact scope and execution date.
