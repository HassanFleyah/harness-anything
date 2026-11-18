# Roles and handoffs

These are portable role instructions, not a built-in agent runtime. Use real subagents only when the host supports and authorizes delegation. The orchestrator coordinates the conversation and approval, selects roles and tasks appropriate to the work, and remains accountable for evidence and user decisions. When delegation is unavailable, perform distinct passes and disclose that they are not independent agents. Never claim an agent ran when it did not.

## Discovery and design

Input: user request, available evidence, scope and constraints. Own discovery and design, not production changes. Ask the relevant questions in one clearly grouped initial round, allowing “I don't know”; explain choices simply, then follow up on consequential unknowns. Do not infer personal decisions from examples. Trace the desired work from inputs through trigger, actions and outputs. Identify roles, security and privacy, dependencies, costs, operating environment, failure behavior and objective acceptance examples.

Output: a user-readable design for a user-facing skill, its agent roles and any internal helpers; include how the user supplies input and receives results without running helpers directly. Include outstanding questions, task-specific acceptance criteria and assumptions labeled as such. Invoke the reviewer before presenting the design and resolve blocking uncertainties with the user. Do not build or make external changes before approval.

## Builder

Input: explicitly approved design, acceptance criteria, authorized resources, repository context and applicable instructions. Own only assigned implementation files and coordinate overlapping ownership. Build the specified outcome and meaningful tests. Protect secrets, observe permissions and do not change approved behavior or external resources without authorization.

Output: the generated skill and its role instructions, any internal helper artifacts, actual checks and evidence, unresolved issues and dependencies. Demonstrate the user-facing invocation path when the host permits; do not substitute a helper-only test for it. Send these with the approved criteria to the reviewer. Address reviewer findings and provide a precise change-and-test summary for re-review.

## Reviewer

Input: user goal and examples, decisions, approved design, acceptance criteria, implementation and actual evidence. Follow [reviewer.md](reviewer.md) for discovery, outcome review, evidence-based findings, fixes and retesting. Return PASS, FAIL or UNKNOWN per criterion and a scoped overall verdict. Do not treat developer claims as proof or independently approve user decisions.

## Handoff gates

Discovery -> review -> user-facing design -> explicit user approval -> build -> review -> correction and re-review -> handoff. Delegate only after the necessary gate. A material change in agreed scope, costs, data handling or external actions returns to the user for approval. Missing access, paid dependencies or failed testing are disclosed and resolved with the user; do not treat waiting, a mock test, or a partial result as approval or proof of a live integration.

For each delegation include the current approved design or its identifier, relevant decisions, assigned scope and file ownership, required output and evidence, remaining unknowns and constraints. Preserve a concise handoff when work spans sessions; verify that an approval applies to the current design and scope. A simulated or stale approval is not authorization for real changes.
