# autoresearch-skills

Reusable Codex skills for long-running Harbor-style AutoResearch tasks.

## Included skill

`autoresearch-harbor-submission/` covers the full path from a paper-only prompt or live task contract to a narrow runnable benchmark, two isolated research Agents, effective-time accounting, same-Goal recovery, independent Private/NOP acceptance, actual-ZIP QA, and atomic Feishu submission. It keeps expert calibration separate from Agent research and excludes hidden evaluation feedback, credentials, and leaked expert solutions.

Install or copy the skill directory into your Codex skills directory, then invoke it explicitly with `$autoresearch-harbor-submission` or let normal skill discovery select it for a matching Harbor submission task.

The offline gate can validate completed upload and download receipts without network access:

```bash
python3 autoresearch-harbor-submission/scripts/validate_evidence.py \
  --receipts-dir /path/to/media-uploads \
  --row-json /path/to/final-row-readback.json
```
