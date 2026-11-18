# Contributing

Thanks for helping make HAT easier to use and more reliable. Before proposing a change, describe the user problem and provide a small, sanitized example where possible.

## Ways to help

- Try HAT on a realistic task and report what it asked, the approved design, and what actually happened.
- Improve beginner-facing instructions or clarify an ambiguous workflow.
- Contribute a fictional example or a test that exercises an observable behavior.

## Local checks

Review `skills/harness-anything/SKILL.md` and the relevant files in `references/`. If the skill-creator validator is available, run it against `skills/harness-anything`. Run any tests included with an example you change. See `evaluation/scenarios.md` for behavioral checks; a listed scenario is not proof it has been executed.

For changes to instructions, include a realistic prompt and record observed behavior, including what could not be tested. Separate a simulation from a real service integration. Respect the discovery and approval gates and do not claim unverified agent, platform, or external-service behavior.

Do not commit passwords, API keys, private documents, customer records, or real employee data. Use synthetic examples. Keep contributions focused and preserve the MIT license.
