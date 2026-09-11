# Testing Strategy

## Purpose

The testing approach verifies that changes to MKA rules do not silently break routing, content structure, metadata validity or legacy separation. This public suite covers a reduced and privacy-safe subset of the production behaviour.

## Test levels

| Level | Purpose | Public example |
|---|---|---|
| Unit | Verify one deterministic rule | Reject an unsupported `work_type` |
| Component | Verify routing or standard selection | Exclude legacy standards |
| Acceptance | Verify a complete card against agreed criteria | Accept a conforming Repertoire card |
| Regression | Re-run stable cases after a rule change | Existing routing and validation cases remain green |
| Integration | Verify MCP search/write/read behaviour | Documented but excluded from the public offline suite |

## Core quality risks

1. The agent selects the wrong card module.
2. Unrelated or legacy rules influence new content.
3. A required section is omitted.
4. An unsupported property value is written.
5. An existing relation is duplicated instead of reused.
6. The stored result differs from the validated draft.
7. A shared-rule change causes regressions in another module.

## Public acceptance criteria

| ID | Given | When | Then |
|---|---|---|---|
| ROUTE-01 | A supported Repertoire request | The router evaluates the card type | The Repertoire module is selected |
| ROUTE-02 | An unknown card type | The router evaluates it | The request is rejected explicitly |
| STD-01 | Active, inactive and legacy standards | Standards are selected | Only explicitly active standards remain |
| REP-01 | A complete conforming card | Validation runs | No validation error is returned |
| REP-02 | `Variation` as an unsupported `work_type` | Validation runs | The value is rejected |
| REP-03 | A required section is absent | Validation runs | The missing section is reported |
| REP-04 | The composer relation is empty | Validation runs | The missing relation is reported |

## Regression policy

A change to a core rule requires all public tests and all affected private module suites to pass. A module-specific change requires that module's tests plus shared routing and metadata tests. Active routing is updated only after the relevant regression suite passes.

## Integration-test boundary

The public suite does not contact Heptabase. Production integration tests cover search, relation reuse, create/update operations and post-write verification using protected credentials and non-public workspace data.

## Reproduction

From the repository root:

```bash
python -m unittest discover -s tests -v
```

The command uses only Python's standard library.
