# MKA Card Builder Skill

**Source of this description:** current available `mka-card-builder` Skill instructions inspected 2026-09-22. This is a public summary, not a copy of the operational instructions.

## Responsibility

The Skill directs the assistant to read the **live MKA Index first**, follow the exact active route, inspect actual tag schemas, and perform authorized card work. The active Heptabase modules remain the rule authority. If a required module cannot be read or is inactive, the task is reported as blocked rather than completed.

## Card workflow

| Step | Observable output |
|---|---|
| Load | Active Index and applicable modules identified |
| Identify | Possible duplicates and the requested operation checked |
| Verify | Material facts and supplied sources checked |
| Draft | Content, tables, properties and relation targets prepared |
| Pre-write QA | Core and card-type checks applied to the full draft |
| Write | Authorized card content and actual Heptabase properties set |
| Read back | Persisted body, table shape, tags, properties and relations compared with draft |
| Report | Created / updated / unchanged / annotated / blocked distinguished |

For an inspection request, drafting and mutation are omitted. A successful write response alone does not count as verified completion. The Skill also specifies Traditional Chinese progress updates for card work.

## Standard changes

When active standards change, the Skill loads Test Governance, prepares an inactive candidate, runs required QA and regression, records Plan and execution-specific Report, verifies activation and retains the previous version as inactive Legacy according to the live lifecycle. It distinguishes `Stand` (actual edit date) from `Version` (substantive rules).

## What the public code demonstrates

The Python validator in this repository demonstrates a few deterministic checks only. It is **not** the Skill implementation, does not invoke Heptabase MCP and cannot certify the live workflow. The live Skill was inspected, but not run end to end for this documentation update.
