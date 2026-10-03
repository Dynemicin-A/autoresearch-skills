# Resume, isolation, and resource protocol

## Persistence required for a real resume

Store these items outside disposable container layers before pausing or recovering:

- the full writable Agent workspace, including source, results, notes, trajectory, provenance, and untracked files;
- native session identifiers, Goal identifier, Goal/SQLite state, observer journal, resource ledger, and last checkpoint;
- exact Agent/verifier image digests, task/data manifest hashes, configuration, and the original absolute deadline;
- a resume receipt that names the same thread/Goal, restored workspace, restored native state, and the next valid action.

Archives containing only logs, a solution directory, or a mocked compatibility check are not sufficient. If the workspace or same-Goal entry cannot be restored and verified, treat the run as stopped at its last auditable effective segment.

## Safe recovery sequence

1. Stop new research actions and capture process, container, Goal, SQLite, and filesystem evidence.
2. Determine whether the original Goal and its writable workspace still exist. Do not create a replacement context while this is unresolved.
3. Restore the frozen image and workspace at the same paths or an explicitly recorded equivalent, preserving ownership and permissions.
4. Reattach to the same native Goal/session and verify the last trajectory event, checkpoint hash, and absolute deadline.
5. Resume only after a dry-run or read-only identity check proves continuity. The resumed intervals remain separate ledger segments and cannot retroactively count preparation or downtime.

Do not run `compose down`, delete volumes, reset the deadline, rerun the pair launcher, or append a new context merely to make the total duration look complete. Enable keep-containers/keep-volumes behavior in the harness and test it before the long run.

## Two-Agent separation

Each group must have a distinct writable root, container/network identity, native session and Goal, trajectory, SQLite state, observer, and archive. Shared read-only task assets are allowed after hashing; shared writable result paths, prompt files, API histories, caches that reveal another result, and acceptance feedback are not. During research, report only infrastructure state and each group's own evidence.

## Resource budget

For a shared VM, budget:

```text
guest_memory >= sum(container_memory_limits) + runtime_headroom + monitor_headroom
```

Record the actual guest memory, swap, CPU, disk, and container limits. Keep a live resource monitor with samples and a summary. If OOM or host pressure appears, preserve the evidence and follow the contract's recovery/stop policy; do not silently raise limits or change the algorithm. Use a remote GPU-free instance only for work it is qualified to run, such as static assembly, packing, and hash verification.
