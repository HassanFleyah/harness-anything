# Getting started

HAT is a skill for an AI assistant. Install it once, then describe a recurring task in a new assistant session. You can say “I don't know” when HAT asks about an option; it should explain the choices before you decide.

## Before you begin

- Have Codex or Claude Code installed and working.
- Download or clone this project from a source you trust and extract it if needed.
- Use example files with sensitive information removed during discovery.
- The following commands assume your terminal is open **inside the downloaded project folder**, where you can see the `skills` folder.

Installing HAT does not create accounts or enable integrations. Availability of subagents, file access, and other tools depends on your assistant and configuration. Claude Code has not been tested end to end with this project.

## Windows: PowerShell

Choose one destination. The commands stop if that skill folder already exists, so you can inspect your existing installation before changing it.

For Codex:

```powershell
$target = Join-Path $env:USERPROFILE '.codex\skills\harness-anything'
if (Test-Path -LiteralPath $target) { throw "Skill already exists: $target" }
New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
Copy-Item -LiteralPath '.\skills\harness-anything' -Destination $target -Recurse
```

For Claude Code:

```powershell
$target = Join-Path $env:USERPROFILE '.claude\skills\harness-anything'
if (Test-Path -LiteralPath $target) { throw "Skill already exists: $target" }
New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
Copy-Item -LiteralPath '.\skills\harness-anything' -Destination $target -Recurse
```

## macOS and Linux: terminal

Choose one destination and run its block from the project folder. The guard avoids overwriting an existing skill.

For Codex:

```sh
target="$HOME/.codex/skills/harness-anything"
if [ -e "$target" ]; then echo "Skill already exists: $target"; else
  mkdir -p "$HOME/.codex/skills"
  cp -R skills/harness-anything "$target"
fi
```

For Claude Code:

```sh
target="$HOME/.claude/skills/harness-anything"
if [ -e "$target" ]; then echo "Skill already exists: $target"; else
  mkdir -p "$HOME/.claude/skills"
  cp -R skills/harness-anything "$target"
fi
```

## Start a conversation

Start a new session and ask:

> Use the harness-anything skill to help me automate a recurring task. Ask me what you need to know.

Describe what you do today and share sanitized examples of the inputs and the result you want. HAT should ask follow-up questions, present a design, and wait for your approval before building. Later, use the generated skill in conversation and provide the files it requests.

If a skill does not appear, check that its `SKILL.md` is directly inside the `harness-anything` folder, then start a new session. Check your assistant's current documentation if your installation uses a different skill location. Any missing account, permission, subscription, tool, or hosting requirement should be explained before it is needed.

## Learn more

Return to the [project overview](README.md), try the [fictional leave-review example](examples/leave-review/README.md), or read the [weekly report scenario](examples/weekly-report.md). The scenarios are demonstrations; the weekly report is not a working email integration.
