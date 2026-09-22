# MKA GPT: learner-facing design

**Evidence status:** This page records the owner's stated design and recent configuration work. The GPT editor configuration and a complete current test transcript were not directly inspected for this portfolio snapshot.

## Intended role

The GPT starts with a learner's question, establishes a conversation language and, where relevant, a separate language for generated material. It determines existing knowledge and learning goals through dialogue, explains a concept or suggests a next practice step, and offers a knowledge card when useful. A card proposal is not itself proof that a card was written to Heptabase.

The entry page shows language-selection guidance in **Traditional Chinese, German and English**. These are visible examples, **not the full set of selectable languages**. Learners may choose another language for the conversation and set the language of a resulting explanation, learning material or card draft separately. For example, they can discuss a concept in German while requesting a card draft in Traditional Chinese. The owner has also designed conversation starters and follow-up prompts. The exact currently published configuration, knowledge-file versions and enabled actions should be added here only after checking the GPT editor.

## Example interaction (illustrative)

1. Learner selects German for the conversation and Traditional Chinese for a possible card draft, then asks: “Was ist eine Tonart?”
2. GPT checks what the learner already knows about scales and intervals.
3. GPT explains the concept with an example and asks a targeted follow-up.
4. If a reusable explanation would help, GPT asks whether to create a Wissenskarte.
5. Actual creation is claimed only after a verified write and read-back in a capable workflow.

## Verification checklist before public claims

| Claim | Required evidence |
|---|---|
| Additional conversation languages work | Current editor settings; samples in the three displayed languages and at least one additional selected language |
| Conversation and output languages can differ | One observed exchange in which the discussion language and generated material language differ |
| Knowledge files match current MKA standards | File inventory, update date and comparison against the live Index |
| GPT can create or update a card | Enabled integration/action, test run and Heptabase read-back |
| GPT invokes Card Builder Skill | Explicit supported integration and observed end-to-end invocation |

Until these checks are recorded, the GitHub page presents the GPT as a **separate learner-facing design and configuration**, not as a proven automated caller of the Skill.
