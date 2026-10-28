"""Validate the small GitOps desired-state example with the Python standard library."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    manifest = json.loads(Path("ops/desired-state.json").read_text(encoding="utf-8"))
    required = {"application", "environment", "image", "replicas", "change_policy"}
    missing = required - manifest.keys()
    if missing:
        raise SystemExit(f"Missing required fields: {', '.join(sorted(missing))}")
    if not isinstance(manifest["replicas"], int) or manifest["replicas"] < 1:
        raise SystemExit("replicas must be a positive integer")
    if manifest["change_policy"] != "pull-request":
        raise SystemExit("change_policy must keep desired-state changes reviewable")
    print(
        f"Desired state valid: {manifest['application']} in "
        f"{manifest['environment']} ({manifest['replicas']} replicas)"
    )


if __name__ == "__main__":
    main()
