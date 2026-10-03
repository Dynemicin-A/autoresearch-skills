#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ARCHIVES = {
    "harbor-task": "harbor task代码仓（按论文标题命名）",
    "final": "完整提交包.zip",
    "optimization-evidence": "优化面证明包",
}


def read_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def find_field(fields, prefix):
    for name in fields:
        if name.startswith(prefix):
            return name
    raise ValueError(f"row is missing a field beginning with {prefix!r}")


def validate_receipts(receipts_dir):
    expected = {}
    for kind in ARCHIVES:
        upload = read_json(receipts_dir / f"{kind}.json")
        verification = read_json(receipts_dir / f"{kind}-download-verification.json")
        if upload.get("status") != "COMPLETE":
            raise ValueError(f"{kind}: upload status is {upload.get('status')!r}")
        if verification.get("status") != "PASS":
            raise ValueError(f"{kind}: download verification is {verification.get('status')!r}")
        token = verification.get("file_token")
        archive = verification.get("archive") or {}
        if not token or not archive.get("sha256") or not archive.get("bytes"):
            raise ValueError(f"{kind}: missing token, SHA-256, or byte count")
        if verification.get("downloaded_bytes") != archive["bytes"]:
            raise ValueError(f"{kind}: downloaded byte count does not match archive size")
        expected[kind] = {
            "file_token": token,
            "sha256": archive["sha256"],
            "bytes": archive["bytes"],
        }
    return expected


def validate_row(row_path, expected, completion_value, field_overrides, small_trial_policy):
    row = read_json(row_path)
    fields = ((row.get("data") or {}).get("record") or {}).get("fields") or {}
    harbor_field = field_overrides.get("harbor") or find_field(fields, ARCHIVES["harbor-task"])
    final_field = field_overrides.get("final") or "完整提交包.zip"
    optimization_field = field_overrides.get("optimization") or find_field(fields, ARCHIVES["optimization-evidence"])
    for kind, field_name in (("harbor-task", harbor_field), ("final", final_field), ("optimization-evidence", optimization_field)):
        values = fields.get(field_name)
        if not isinstance(values, list) or len(values) != 1:
            raise ValueError(f"{field_name}: expected exactly one latest attachment")
        if values[0].get("file_token") != expected[kind]["file_token"]:
            raise ValueError(f"{field_name}: token does not match verified upload")
    if completion_value is not None and fields.get("是否已完成") != completion_value:
        raise ValueError(f"completion field is {fields.get('是否已完成')!r}, expected {completion_value!r}")
    for name in ("baseline分数", "参考解分数", "自检checklist"):
        if not fields.get(name):
            raise ValueError(f"row field {name} is empty")
    small_trial_field = next((name for name in fields if name.startswith("小规模试跑结论")), None)
    small_trial_value = fields.get(small_trial_field) if small_trial_field else None
    if small_trial_policy == "required" and small_trial_field and not small_trial_value:
        raise ValueError("小规模试跑结论 is empty; pass a reviewed conclusion or use --small-trial-policy not-required")
    return fields, {"field": small_trial_field, "value": small_trial_value, "policy": small_trial_policy}


def main():
    parser = argparse.ArgumentParser(description="Validate Harbor upload/readback receipts and an optional live-row snapshot.")
    parser.add_argument("--receipts-dir", type=Path, required=True)
    parser.add_argument("--row-json", type=Path)
    parser.add_argument("--completion-value", default="已完成")
    parser.add_argument("--harbor-field")
    parser.add_argument("--final-field")
    parser.add_argument("--optimization-field")
    parser.add_argument("--small-trial-policy", choices=("required", "not-required", "ignore"), default="required")
    args = parser.parse_args()
    expected = validate_receipts(args.receipts_dir)
    fields = None
    if args.row_json:
        overrides = {"harbor": args.harbor_field, "final": args.final_field, "optimization": args.optimization_field}
        fields, small_trial = validate_row(args.row_json, expected, args.completion_value, overrides, args.small_trial_policy)
    result = {"status": "PASS", "archives": expected, "row_checked": fields is not None}
    if fields is not None:
        result["small_trial"] = small_trial
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
