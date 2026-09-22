# My contributions and evidence

| Contribution | Public evidence |
|---|---|
| Defined domain and card-type boundaries, including Log / Wissenskarte / Lernsystem | [Architecture](architecture.md) and [example](../examples/music-learning-workflow.md) |
| Designed single active Index, selective rule loading and module ownership | Architecture and README |
| Specified property dependencies, relations and read-back requirements | Example and architecture |
| Defined QA, Test Plan, Test Report and regression selection | [Testing strategy](../tests/TESTING_STRATEGY.md) |
| Defined active/legacy and version/Stand lifecycle | Architecture and [results](../tests/TEST_RESULTS.md) |
| Reviewed actual cards and rule changes, identified mismatches and refined requirements | Anonymised live test report summary in results |

The operational workflow uses AI instructions/skills, active Heptabase standards and Heptabase MCP capabilities. The public `src/public_validator.py` and its tests are a **standalone illustrative subset** made for this portfolio. They do not imply that I wrote ChatGPT, Heptabase or the full operational system in Python.

In an interview, I can explain why the router has one active entry point, how event/knowledge/system boundaries were chosen, how test scope changes with a rule edit, and how failed persistence or property read-back is reported.
