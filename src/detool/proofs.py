from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any


def _digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_synthetic_usage_proof(manifest: dict[str, Any]) -> dict[str, Any]:
    """Build a non-executing fixture proof; no external service is contacted."""
    now = datetime.now(timezone.utc).isoformat()
    request = {
        "role_id": "synthetic-role-17",
        "candidate_projection": {"profile_ref": "synthetic-candidate-1"},
        "authorization_id": "synthetic-approval-1",
    }
    result = {"state": manifest["state_transition"]["to"], "confirmation_id": "SYNTHETIC-001"}
    return {
        "proof_id": "proof_synthetic_001",
        "request_digest": _digest(request),
        "result_digest": _digest(result),
        "before_state_digest": _digest(manifest["state_transition"]["from"]),
        "after_state_digest": _digest(manifest["state_transition"]["to"]),
        "confirmation_id": result["confirmation_id"],
        "capability_id": manifest["capability_id"],
        "capability_version": manifest["version"],
        "provider_route": manifest["execution_modes"][0]["uri"],
        "started_at": now,
        "completed_at": now,
        "outcome": "verified",
        "verification": {
            "method": manifest["verification"]["method"],
            "verifier": "synthetic-fixture",
            "evidence_uri": "fixture://job-application/SYNTHETIC-001",
        },
        "metering": {"requests": 1, "external_calls": 0},
        "chargeable": False,
        "signature": None,
    }
