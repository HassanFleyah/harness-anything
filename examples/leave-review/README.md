# Example: Review leave requests

This offline example shows what HAT can produce: a task-specific skill that reviews two CSV files, uses a bundled helper behind the scenes, and explains the findings in conversation. All sample data is fictional.

The skill compares leave requests with an existing schedule. It identifies overlapping dates for people on the same team and leaves every request pending for a human to review. It does not approve, reject, or send anything.

## Try the example

Make the [leave-review-skill](leave-review-skill) folder available to your assistant as a skill, following your host's skill installation instructions. In a session where it is available, ask:

> Use the leave-review-skill to review my sample requests. The requests are in `examples/leave-review/requests.csv` and the existing schedule is in `examples/leave-review/schedule.csv`. Tell me which requests overlap.

Your assistant should read the skill instructions, access the two files, run the bundled helper itself, and explain the output. If your assistant cannot access those paths or run Python 3, it should explain the missing requirement. Automatic discovery in a fresh Codex or Claude Code session was not tested in this example.

For the included sample, the helper reports:

- **R1, Alex:** overlaps Bea on 4 December 2026.
- **R2, Cal:** no overlap detected.
- Both remain `PENDING_REVIEW`; a person makes the decision.

The report is a snapshot. If the files change, run the review again before deciding.

## What was checked

During the fictional trial, an independent reviewer found a mismatch between the initial design and the requested overlap details. The design was clarified before fictional approval. After implementation, another review found that a malformed CSV quote was accepted; the builder fixed it and a reviewer rechecked the regression. An independent delegated agent later read the skill explicitly, ran its bundled helper on the sample files, and observed the results above.

These are local demonstration results, not evidence that a real HR workflow or automatic skill discovery works in every host. The example has no login, authorization, audit trail, leave balances, holiday rules, scheduler, or live integrations. Do not use real employee data or rely on it for employment decisions.

## For maintainers

To run the helper's automated tests from this directory with Python 3:

```sh
python -B -m unittest -v test_leave_queue
```

The tests exercise the bundled helper, including invalid CSV and missing files. They do not prove the assistant will discover or execute the skill.
