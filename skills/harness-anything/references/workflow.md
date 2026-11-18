# Workflow guidance

## Discovery

Adapt the first batch of questions: What outcome is wanted and how is the task performed today? What sanitized sample inputs and ideal outputs exist? Where does data come from and go? What triggers execution? What happens on missing data, duplicates, uncertainty, or failure? What accounts, budget, privacy constraints and approvals apply? How should the process be monitored and stopped?

Ask focused follow-ups. When users are unsure, explain realistic choices without deciding for them.

## Roles

The orchestrator owns discovery, approval and handoff. A designer maps the workflow. A builder implements it. A reviewer challenges the intended outcome and examines evidence. Add specialists when needed. Agent availability varies: check it, disclose fallbacks and never invent results.

## Verification

Define observable acceptance criteria before building. Check representative and edge-case examples against actual outputs. Test failure handling and authorization without unapproved side effects. Record what was tested and what remains unverified.
