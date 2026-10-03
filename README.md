# autoresearch-skills

Reusable Codex skills for long-running Harbor-style AutoResearch tasks.

## Included skill

`autoresearch-harbor-submission/` covers the operational path from a live task contract to two isolated research Agents, effective-time accounting, same-Goal recovery, independent Private/NOP acceptance, actual-ZIP QA, and atomic Feishu submission. It deliberately excludes research algorithms, hidden evaluation feedback, and credentials.

Install or copy the skill directory into your Codex skills directory, then invoke it explicitly with `$autoresearch-harbor-submission` or let normal skill discovery select it for a matching Harbor submission task.

The offline gate can validate completed upload and download receipts without network access:

```bash
python3 autoresearch-harbor-submission/scripts/validate_evidence.py \
  --receipts-dir /path/to/media-uploads \
  --row-json /path/to/final-row-readback.json
```
