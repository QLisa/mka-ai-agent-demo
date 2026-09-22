# Testing strategy

**Reference:** active MKA Test Governance v1.3, read 2026-09-22. This is a summary, not the complete private standard.

| Change | QA | Regression | Plan and report |
|---|---|---|---|
| Individual card | Core QA plus applicable card QA | Normally no | Normally no |
| Factual correction without rule change | Applicable QA | Only if rule affected | Normally no |
| Card-type standard change | Core QA plus applicable QA | Affected module tests | Yes |
| Core, Core QA or Index change | Core QA | Core and affected modules | Yes |
| MCP update or bug fix | Core QA | Core and affected end-to-end cases | Yes |
| New card type or module | Core QA plus new QA | New and affected shared tests | Yes |

A **Test Plan** defines scope, cases and entry/exit criteria. A **separate Test Report per execution** records the date, actual module versions, outcomes, evidence, defects, corrections, risks and activation decision. It also records post-activation read-back.

## Representative acceptance cases

| ID | Input/change | Expected outcome | Evidence required |
|---|---|---|---|
| ML-ROUTE-01 | Reusable practice method | Wissenskarte route; no Log Type | Active Index and stored properties |
| ML-ROUTE-02 | Dated practice event | Log / Practice route; actual date | Stored properties and read-back |
| ML-ROUTE-03 | Competency/feedback model | Lernsystem under Musiklernen; no independent template | Index, Structure and properties |
| ML-LEGACY-01 | Obsolete separate Lernsystem modules exist | Excluded from active route | Index and inactive module status |
| ML-CHANGE-01 | Shared Musiklernen Structure changes | Affected cases before activation | Plan, report and final read-back |
| MCP-01 | Card created or updated | Persisted content/properties match draft | MCP result and independent read-back |

These are **portfolio examples of expected checks**, not additional claimed passes.

Run the small offline demo with `python -m unittest discover -s tests -v`. Its seven tests cover a reduced Repertoire validator and generic active/legacy selection. They do not test live Musiklernen routing or MCP.
