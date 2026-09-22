# My contributions and evidence

| Contribution | Public evidence |
|---|---|
| Defined domain and card-type boundaries, including Log / Wissenskarte / Lernsystem | [Architecture](architecture.md) and [example](../examples/music-learning-workflow.md) |
| Designed single active Index, selective rule loading and module ownership | Architecture and README |
| Specified property dependencies, relations and read-back requirements | Example and architecture |
| Defined QA, Test Plan, Test Report and regression selection | [Testing strategy](../tests/TESTING_STRATEGY.md) |
| Defined active/legacy and version/Stand lifecycle | Architecture and [results](../tests/TEST_RESULTS.md) |
| Reviewed actual cards and rule changes, identified mismatches and refined requirements | Anonymised live test report summary in results |
| Defined the Card Builder Skill's loading, QA, write, read-back and reporting procedure | [Skill summary](card-builder-skill.md); current instructions inspected 2026-09-22 |
| Designed the MKA GPT's multilingual conversation, independently selectable output language, three-language entry examples and prompts for offering cards | [GPT design](mka-gpt.md); current editor configuration still requires verification |
| Designed the scheduled Practice Log use case, including priority of actual learner decisions, no fabricated results, live-template loading and post-write checks | [Daily practice planning](../examples/daily-practice-planning.md); saved schedule and two cards inspected |

The operational workflow uses AI instructions/skills, active Heptabase standards and Heptabase MCP capabilities. The public `src/public_validator.py` and its tests are a **standalone illustrative subset** made for this portfolio. They do not imply that I wrote ChatGPT, Heptabase or the full operational system in Python.

My authorship here concerns requirements, structure, prompts/instructions, test criteria and iterative validation. Where generated text or assistant help was used, the claim is the design and review work, not sole manual authorship of every line of prose. The exact Skill and GPT configuration are separate deliverables.

In an interview, I can explain why the router has one active entry point, how event/knowledge/system boundaries were chosen, how test scope changes with a rule edit, and how failed persistence or property read-back is reported.
