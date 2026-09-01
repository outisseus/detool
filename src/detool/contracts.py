from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "capability_id",
    "version",
    "name",
    "action",
    "state_transition",
    "operator",
    "input_schema",
    "output_schema",
    "side_effect",
    "data_classes",
    "verification",
    "execution_modes",
}


class ContractError(ValueError):
    """Raised when a manifest cannot satisfy the executable pre-alpha contract."""


def load_capability(path: str | Path) -> dict[str, Any]:
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_FIELDS - manifest.keys())
    if missing:
        raise ContractError(f"missing required fields: {', '.join(missing)}")
    transition = manifest["state_transition"]
    if not isinstance(transition, dict) or not {"from", "to"} <= transition.keys():
        raise ContractError("state_transition requires from and to")
    modes = manifest["execution_modes"]
    if not isinstance(modes, list) or not modes:
        raise ContractError("execution_modes must contain at least one route")
    return manifest

