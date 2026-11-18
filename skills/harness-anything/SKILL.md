---
name: harness-anything
description: Design, build, and verify a custom multi-agent automation for a user's recurring work after thorough discovery and explicit design approval.
---

# Harness Anything (HAT)

Help people who know Codex or Claude Code automate recurring work without assuming technical knowledge. Speak in the user's preferred language and explain technical terms simply.

The primary deliverable is a task-specific, host-discoverable skill and appropriate agent role instructions. The end user invokes the generated skill in conversation, supplies the requested files or information, and receives results there or in an agreed artifact. The skill coordinates available agents and invokes any bundled helper tools itself; do not make the user operate a CLI or internal scripts as the normal workflow. Explain unavoidable setup or access requirements plainly. If the user explicitly wants a different interface, follow their choice.

## Discover before building

Do not create or modify project files, deploy, connect services, or run the automation until the user approves a concrete design. Read available context and ask all relevant initial questions together in an approachable numbered list; tailor them to the task. Group questions by topic and allow the user to answer “I do not know”. Ask for redacted examples and expected outputs. Cover goals, current steps, exceptions, data sources and destinations, timing, volume, approvals, delivery, privacy, available accounts and tools, budget, operating environment, maintenance, and missing-service behavior. Ask which external actions need confirmation.

Explain options when the user does not know an answer. Ask follow-up questions until all material decisions are resolved. Never invent user-specific requirements or treat a guess as consent.

## Review and obtain approval

Read and apply the dedicated [outcome and verification reviewer](references/reviewer.md) throughout discovery, design and implementation. Read [role and handoff instructions](references/roles.md), select roles appropriate to the task, and follow the approval and evidence gates. Include a reviewer independent of the builder: use a real subagent when available and authorized; otherwise perform a separate review pass and disclose that it is not an independent agent. The reviewer challenges whether the workflow produces the user's expected outcome, examines omissions and edge cases, and asks substantive follow-up questions.

Present a plain-language design with a workflow diagram, examples, inputs and outputs, triggers, delivery, roles, security and privacy, failure handling, acceptance criteria, operation, dependencies, prices, alternatives, and unresolved decisions. Verify current prices and capabilities with authoritative sources when available; label estimates and unverified details. Explain account, subscription, permission and hosting needs. Do not promise zero errors or costs. Wait for explicit design approval before building.

Approval to build does not by itself authorize payment, publishing, sending messages to others, or changing third-party services. Obtain appropriate authorization before such actions and follow platform permissions.

## Build and verify

After approval, create a complete task-specific SKILL.md with instructions to obtain and validate inputs, find and safely invoke necessary skill-relative helpers through available host tools, interpret actual output and errors, ask for required human decisions, and present the result. Include task-specific agent instructions and only the internal scripts or resources the workflow needs. Do not invent access to attachments, tools, accounts or agent execution; explain and resolve missing capabilities with the user. Use secure credential handling; do not ask users to paste secrets into chat or commit them.

Test representative examples and meaningful failure cases. When the host permits, test the generated skill in a fresh session using an ordinary user request and sample file through the actual skill-to-helper-to-result path, including missing files, invalid input, unavailable tools, and human decision points as relevant. Distinguish helper tests and simulated reviews from observed skill execution; report any host-level test not performed. The reviewer checks actual outputs and implementation against agreed acceptance criteria, returns actionable findings to the builder, and rechecks fixes in the review loop described in the reviewer contract. Do not declare success while blocking findings remain unresolved. Fix defects and rerun relevant checks. If a dependency, authorization, subscription, tool or test is unavailable, explain its impact and ask whether the user wants to provide it, choose an alternative, accept a partial result or stop. Never claim an untested integration works.

Deliver plain-language installation and conversation examples showing how to invoke the generated skill, supply files and understand results, plus observed test results, limitations, costs, dependencies and next steps. Hide internal commands from the normal user flow; disclose them when needed for setup or troubleshooting. Explain how to monitor and stop recurring automation. Read [workflow guidance](references/workflow.md) when planning or reviewing a workflow.
