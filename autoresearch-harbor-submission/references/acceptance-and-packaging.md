# Acceptance and packaging protocol

## Independent acceptance gates

After both research groups are sealed, review each native trajectory and effective-time ledger. A candidate is not accepted because a Goal completed or a source file says READY.

Run the acceptance gates in fresh, disposable processes while preserving the research evidence:

1. verify the candidate source and selected-best binding against the trajectory;
2. build or select the current Agent image and verify exact content, source hashes, task checksum, and verifier digest;
3. run the Private evaluation on all required cases with the unchanged resource and timeout contract;
4. run a second independent Private candidate when the contract requires model diversity or cross-checking;
5. run the current-version final NOP, bind the actual container/image identities, and verify Baseline/Reference behavior and resource/security constraints;
6. run the official self-check against the actual frozen package.

Keep failed Private attempts and timeout evidence when they are material. Do not use Private or Hidden results to steer the research Agent retroactively. Do not claim an acceptance gate from a directory-level scan, a synthetic test, or an old verifier image.

## Freeze and ZIP checks

Before freezing, confirm:

- no credentials or private provider responses are present in portable artifacts;
- the frozen source manifest covers the exact submission workspace;
- solution, task harness, evidence, and metadata obey the official layout and size rules;
- every required trajectory, time audit, acceptance receipt, and limitation disclosure is present;
- the actual ZIP, not only its source directory, passes official QA.

Create only the archives required by the live table contract. For each archive record filename, byte size, member count, expanded size, all-member hash result, and whole-file SHA-256. A remote pack is acceptable for cost or disk reasons only if the downloaded result is compared to the frozen manifest and independently rechecked locally.

Once a package is frozen and its hash is recorded, do not edit it, rebuild it from a moving workspace, or silently substitute a different image/configuration. If a correction is required, create a new version and repeat all checks.

## Final evidence bundle

Retain at least:

- launch and effective-time ledgers for both groups;
- native trajectory/Goal/session/SQLite receipts and resource monitor summary;
- Private/NOP and image-binding receipts;
- official QA report for the actual ZIP;
- upload completion and byte-readback receipts for every submitted archive;
- the final live-row readback showing tokens, checklist, scores, status, small-scale-trial conclusion, and unrelated-field preservation.

Only after this bundle is complete should the table status be changed to complete.
