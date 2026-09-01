from __future__ import annotations

import argparse
import json

from .contracts import ContractError, load_capability
from .proofs import build_synthetic_usage_proof


def main() -> int:
    parser = argparse.ArgumentParser(prog="detool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "proof"):
        child = subparsers.add_parser(command)
        child.add_argument("manifest")
    args = parser.parse_args()
    try:
        manifest = load_capability(args.manifest)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        parser.error(str(exc))
    if args.command == "validate":
        print(f"valid pre-alpha capability: {manifest['capability_id']}@{manifest['version']}")
        return 0
    print(json.dumps(build_synthetic_usage_proof(manifest), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

