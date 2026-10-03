# Feishu atomic submission protocol

Use the user identity (`--as user`) for a Base operation unless the live task explicitly requires an application identity. Resolve the current Base, table, record, writable field names, field types, and submission columns immediately before the final update; do not rely on stale field IDs or an old row snapshot.

## Safe sequence

1. Keep the current row unchanged while preparing the new files.
2. Upload each new archive to the project Base media store. Save the returned file token, upload status, part checksums, archive SHA-256, and byte count.
3. Finish each upload and perform a remote ranged download/readback. Require every downloaded byte to match the accepted archive. An upload marked complete without readback is not a submission proof.
4. Read the live row and confirm the current Harbor attachment and the other submission column. Prepare one record update containing the new Harbor token and any new complete/optimization tokens, scores, checklist, small-scale-trial conclusion, and only the intended changed fields. Never clear the old attachment first.
5. Send the single update, then read the full row back. Confirm each submission column has exactly the newest token, no old duplicate remains, at least one submission column is nonempty, and unrelated fields are unchanged.
6. Only after all three readbacks, QA, and the row comparison pass, update the completion field. For a single-select field, use the live field's native value shape; a direct native PUT commonly expects a scalar option string even when a normalized read displays a one-element array.
7. Read the row back one final time and archive the response. If any write or readback is ambiguous, stop and inspect the live row before retrying.

## Small-scale-trial field

Treat `小规模试跑结论` as an explicit release field whenever it exists. It is often a plain text field and may be null even when engineering smoke or calibration artifacts exist. Before final submission, decide whether the live contract requires a concise real-asset pilot conclusion, an explicitly labeled engineering-only smoke conclusion, or a truthful `未完成/不适用` value. Never promote `SMOKE_ONLY`, synthetic diagnostics, or an internal calibration result to a formal research result without stating its scope. If the field is not required, preserve its null value and record that decision in the local final audit.

## Failure handling

- A failed or ambiguous update must leave the existing attachment in place. Never use delete-then-add as a fallback.
- Never make both submission columns empty. This can trigger automation that releases the claimed topic.
- Keep only the latest version in each attachment field. Do not add a second copy as a way to avoid replacing the old one.
- Do not mark completion while an archive is still being downloaded, a verifier is stale, an official check is pending, or the row readback is incomplete.
- Do not include access tokens, API keys, cookies, or full secret-bearing command lines in receipts, trajectories, commits, or GitHub.
