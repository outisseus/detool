from __future__ import annotations

import unittest
from pathlib import Path

from detool import build_synthetic_usage_proof, load_capability


ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_manifest_describes_state_transition(self) -> None:
        manifest = load_capability(ROOT / "examples" / "synthetic-capability.json")
        self.assertEqual(manifest["action"], "job.application.submit")
        self.assertEqual(manifest["state_transition"]["to"], "APPLICATION_SUBMITTED")

    def test_fixture_proof_is_verified_but_not_chargeable(self) -> None:
        manifest = load_capability(ROOT / "examples" / "synthetic-capability.json")
        proof = build_synthetic_usage_proof(manifest)
        self.assertEqual(proof["outcome"], "verified")
        self.assertFalse(proof["chargeable"])
        self.assertEqual(proof["metering"]["external_calls"], 0)


if __name__ == "__main__":
    unittest.main()

