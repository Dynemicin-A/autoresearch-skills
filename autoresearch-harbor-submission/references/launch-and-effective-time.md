# Launch and effective-time protocol

## Required launch record

Before starting either research Agent, save a machine-readable launch record containing:

- task ID, task checksum, paper/task title, model and Base URL identity without secrets;
- editable surface, fixed data and split, evaluator command, case timeout, bundle timeout, CPU/memory limits, and container image digests;
- Baseline and Reference outputs from the minimum necessary validation;
- requested effective target, official minimum, native Goal wall-clock cap, absolute deadline, and monitoring interval;
- independent workspace, container, session, Goal, trajectory, observer, and SQLite paths for each group;
- finite API retry/backoff policy and the action for authentication, quota, transport, or OOM failure.

The launch record is an audit boundary, not research evidence. Preparation and calibration time do not count toward effective research time.

## Target arithmetic

Use seconds internally. Keep three values separate:

```text
official_minimum_seconds <= requested_effective_seconds
requested_effective_seconds < native_wall_clock_cap
native_wall_clock_cap <= original_absolute_deadline - launch_time
```

The wall-clock cap must leave room for sealing and delivery. A Goal completion event does not prove that the effective target was reached. For every counted interval, record the native activity source, start/end timestamps, action type, and the exclusion decision.

## Agent prompt requirements

The Goal prompt should tell the Agent to:

1. work autonomously on the supplied task and editable surface;
2. preserve a structured trajectory for every meaningful experiment, including method, result, validity, resource use, and retained-best decision;
3. checkpoint source, results, notes, and provenance frequently;
4. stop research at the target or earlier if the absolute deadline or a hard resource limit is reached;
5. leave a truthful final handoff with current best method, exact files, hashes, failures, and remaining uncertainty.

It should not tell the Agent the expert method, another Agent's result, hidden feedback, or a target score. Do not add a fake "run for ten hours" instruction without a timer, checkpoint path, observer, and stop guard.

## Monitoring and exclusions

At the requested operational interval, inspect both groups without changing their science:

- live observer and child process identity;
- Goal/session state and native trajectory growth;
- SQLite state/snapshot freshness;
- resource samples, OOM kills, throttling, API errors, and retries;
- source/result file changes and the current effective-time ledger.

Exclude setup, dependency installation, idle waiting, blocked retries, provider outage, VM reboot, crash recovery, acceptance, packaging, and delivery. If a segment cannot be attributed to active research from native evidence, leave it uncounted. Preserve gaps instead of interpolating them.

When a group approaches its target, begin acceptance review immediately. If a group is still active after its target, do not let the monitor merely wait for Goal completion: verify the activity, request the clean stop according to the harness, and seal the evidence.
