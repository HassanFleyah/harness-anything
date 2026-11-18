---
name: leave-review-skill
description: Demonstrate offline review of fictional leave requests against a fictional leave schedule, keeping all decisions with the user.
---

# Leave request review demonstration

This is an offline demonstration using fictional data, not a production HR system. The user interacts with this skill in plain language; invoke the bundled script yourself and explain its result. Never ask the user to run commands. Do not use real employee data or present its output as a leave approval.

## Inputs

Ask the user for two accessible UTF-8 CSV files: the leave requests and the existing leave schedule. If either is absent, ask for it rather than assuming an empty schedule. Both have exactly the headers `id,employee,team,start,end`; dates use YYYY-MM-DD. IDs must be unique across both files. Values are trimmed; team matching is exact and case-sensitive. Dates are inclusive. These assumptions are specific to this demonstration, not a general leave policy. If a user has a different format, do not invent a conversion or policy; explain what is needed.

## Process

1. Identify the two provided files and confirm their roles if ambiguous. Check that they are local readable files and that the environment has Python 3; if unavailable, explain the missing dependency. Use only fictional data for this demonstration.
2. Run the bundled `scripts/leave_queue.py` with the request and schedule file paths as separate arguments. Resolve the script relative to this skill folder. Use the host execution tool's safe argument handling; never interpolate untrusted paths into executable shell code. If the host only accepts shell commands, quote literal paths using that shell's rules and avoid evaluation, interpolation, or command substitution. Do not modify either input.
3. If execution fails, tell the user what input or dependency needs attention. Do not display partial or invented results. Otherwise parse the JSON output and summarize each request, the pending-review status, and any other employee and overlapping dates. Explain clearly when no overlap was detected. Offer to clarify the results; leave approval or rejection to an authorized human.
4. Describe the result as a snapshot. If either input may have changed, rerun with the current files before a human makes a decision. This script does not detect later changes. Do not send messages, write decisions, alter schedules, or run recurring jobs.

The tool does not implement authorization, audit records, leave balances, holidays, legal rules or staffing policy. Privacy and console output for unsupported Unicode encodings have not been verified. Do not claim live integrations, access controls, actual human approvals, or production readiness.
