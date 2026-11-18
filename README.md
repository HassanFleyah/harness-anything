# Harness Anything (HAT)

### Turn recurring work into a skill you can use in conversation.

You know the job. HAT helps your AI assistant understand it, agree on a plan with you, and build a reusable skill to carry it out. You provide the files or information; the resulting skill coordinates available agents and any internal tools.

**You stay in control:** HAT asks questions, reviews the plan, and waits for your approval before building.

> **Early-stage project.** HAT is a set of reusable instructions for an AI assistant, not a hosted service or standalone agent runtime. Results depend on the assistant, available tools, permissions, and the work requested.

## From a task to a skill

```text
Your recurring task + examples
            |
            v
  Questions and follow-ups
            |
            v
   Design + independent review*
            |
            v
      Your approval
            |
            v
    Build -> review -> improve
            |
            v
 Use your new skill with your files
```

*An independent subagent is used when the environment supports and permits it. Otherwise HAT instructs the assistant to perform a separate review and disclose that it is not independent.*

## What using HAT looks like

Imagine you spend time reviewing leave requests against a team schedule.

> **You:** “Help me review leave requests. I have a file of requests and a file of existing leave.”
>
> **HAT:** “What counts as a conflict? What information should the reviewer see? Who makes the final decision? What should happen when data is missing?”
>
> **You:** “Show the other employee and overlapping dates. Keep every decision with me.”
>
> **HAT:** Presents a proposed skill, its inputs, checks, limitations, and any setup or costs. It asks for approval before building.
>
> **Later:** You invoke the generated skill, provide the files, and review its findings in the conversation. You do not need to run its internal helper in the normal workflow.

This is an illustrative conversation, not a guarantee of a particular result. Try the [fictional leave-review example](examples/leave-review/README.md) or read the [weekly report scenario](examples/weekly-report.md).

## Get started

1. Download this project from a source you trust.
2. Copy the entire `skills/harness-anything` folder into your assistant's personal skills directory:
   - **Codex:** normally `~/.codex/skills/harness-anything`
   - **Claude Code:** `~/.claude/skills/harness-anything`
3. Start a new assistant session. Ask:

   > Use the harness-anything skill to help me automate a recurring task. Ask me what you need to know.

See the [step-by-step installation guide](GETTING-STARTED.md) for Windows, macOS, and Linux. If the assistant cannot access a file or tool, it should tell you what is missing rather than claim it completed the task.

## What HAT prepares

- A task-specific **skill** designed to be used in conversation.
- Agent role instructions chosen for the work, including review of the goal and results.
- Internal helpers when useful and supported by the environment.
- A handoff explaining setup, tested behavior, unresolved dependencies, and how to operate or stop the workflow.

HAT does not supply your accounts or subscriptions. Some workflows need services, credentials, paid plans, hosting, permissions, or a person to make decisions. A skill alone does not enable scheduled execution or a service integration.

## Safety and limitations

HAT asks for design approval before building. Approval to build does not by itself authorize purchases, publication, messages to others, or changes to external services. Use secure connection methods and avoid placing passwords, API tokens, or real confidential data in examples or repositories.

Tests and reviews reduce risk; they cannot guarantee zero errors. HAT should report failed or unavailable checks and distinguish simulated integrations from working ones. Actual subagent support and permissions depend on the host. Claude Code compatibility and live email or Telegram delivery have not been verified end to end in this project.

## Evaluation

The project includes [manual behavioral evaluation scenarios](evaluation/scenarios.md). These are test prompts, not claims that all scenarios passed. Early local trials exercised fictional CSV workflows and a reviewer-to-builder correction cycle; these do not establish general accuracy across all uses.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Distributed under the [MIT License](LICENSE).
