---
name: autoresearch-harbor-submission
description: Prepare, run, audit, package, and safely submit Harbor-style AutoResearch tasks with independent long-running agents, effective-time evidence, fresh-process verification, and atomic Feishu attachment replacement.
---

# AutoResearch Harbor Submission

Use this skill when a task is claimed through Feishu/Xpert and must be made runnable for Harbor, explored by independent long-running research Agents, independently verified, packaged, and submitted. It is a delivery and evidence workflow; it does not solve the research problem or provide algorithm ideas to the research Agents.

## Operating boundary

- Treat the live task contract, official tutorial, scoring harness, and current table schema as authoritative. Read them before changing code or resources.
- Keep expert preparation to the minimum needed to establish an editable surface, fixed data and split, scoring, isolation, and runnable Baseline/Reference checks. Literature exploration, method design, ablations, failure analysis, and final method selection belong to the research Agents.
- Never expose credentials, hidden evaluation feedback, one Agent's work to the other, or an expert solution through prompts, mounted files, logs, or shared writable directories.
- Do not claim effective research time from Goal elapsed time, process uptime, wall-clock waiting, setup, blocked retries, downtime, recovery preparation, or acceptance runs. Count only auditable research activity from native trajectories and observer records.
- Preserve the original absolute deadline. A failed run cannot be made valid by starting a new context and adding its time.

## Workflow

1. Establish the contract and launch gates. Record task identity, editable files, fixed assets, scoring command, resource limits, Baseline/Reference outputs, requested effective duration, official minimum, absolute deadline, API budget, and submission fields. Run a cheap end-to-end smoke test before launching research.
2. Prepare two genuinely independent research sandboxes. Each needs its own writable workspace, container, native session/Goal, trajectory, SQLite state, observer, artifact directory, and resource ledger. Use the requested model and maximum reasoning setting only when the live contract authorizes it.
3. Launch in Goal mode with an explicit effective-time target, hard absolute deadline, finite retry policy, stop guard, and three-hour operational checks. The prompt must require autonomous research, checkpointing, and a clean final handoff; it must not provide hidden feedback or a pre-solved method. See [launch-and-effective-time.md](references/launch-and-effective-time.md).
4. Monitor without steering the science. Check process identity without printing command lines or environment variables containing secrets; inspect native sessions, Goal state, trajectory growth, SQLite snapshots, resource/OOM events, throttling, and quota failures. A meaningful failure gets preserved as evidence and is evaluated for same-Goal recovery before any action.
5. Review each run as it approaches the target instead of waiting for Goal completion. Recompute effective time from activity segments and exclusions, inspect deliverables and fresh-process reproducibility, then seal the run. Do not let an Agent continue indefinitely after the requested target unless the live contract explicitly requires it.
6. Run independent acceptance. Verify the selected candidate in fresh Private processes and current-version images, bind the task checksum, verifier digest, resource limits, and unchanged Starter/reference state, then run the final NOP and official self-check. Do not use one run's hidden or Private result to guide the other.
7. Freeze and package only after acceptance passes. Produce the Harbor task archive, complete submission archive, and optimization-evidence archive when required. Hash the actual ZIP files and every member, record sizes and counts, and run QA against the actual ZIP rather than only the source directory. Do not edit a frozen package after its hash is recorded.
8. Submit atomically. Upload every new attachment first, verify upload completion and remote byte readback, then perform one record update using live field names. Replace the Harbor attachment directly, preserve the other submission field and unrelated fields, retain only the latest attachment in each column, and keep at least one submission column nonempty at every step. Read the row back and mark completion only after all checks pass. See [feishu-atomic-submission.md](references/feishu-atomic-submission.md).

## Recovery and cost controls

- Persist enough state to resume the same Goal: the complete writable workspace, native session metadata, Goal/SQLite state, trajectory, observer journal, image digests, and absolute deadline. A list of logs or a synthetic compatibility test is not a recovery proof.
- Keep containers and volumes during a pause or resumable failure. Do not use `compose down` or delete the container before the archive and state snapshot are durable. Resume the same Goal only; never concatenate unrelated contexts to satisfy a duration requirement.
- Size shared VM memory from the sum of container limits plus headroom, and monitor real guest memory, swap, and OOM evidence. A GPU-free remote instance is appropriate for static packing, hash verification, and storage when it cannot run the required namespace/Docker evaluation; qualify it before using it for anything else.
- Use finite provider retries and stop on persistent authentication, quota, transport, or model failure. Preserve the error and native timeline. Do not purchase credits, upgrade plans, or silently switch models without explicit authorization.

## Reusable references

- [launch-and-effective-time.md](references/launch-and-effective-time.md): target arithmetic, prompt requirements, monitoring, and exclusions.
- [resume-and-isolation.md](references/resume-and-isolation.md): same-Goal recovery, persistence, two-Agent separation, and resource controls.
- [acceptance-and-packaging.md](references/acceptance-and-packaging.md): Private/NOP gates, image binding, ZIP QA, hashes, and freeze rules.
- [feishu-atomic-submission.md](references/feishu-atomic-submission.md): live schema, upload/readback sequence, failure handling, completion update, and the small-trial-result field.

For a deterministic offline gate, run `python3 scripts/validate_evidence.py --help` and validate the three upload/readback receipts plus the final row snapshot before any irreversible status change.
