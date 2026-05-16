"""Validation command."""

import argparse
from pathlib import Path

from judicial_record.utils.load_utils import load_fallback_version
from judicial_record.utils.orchestrate_utils import run_validate
from judicial_record.utils.ref_utils import find_repo_root


def validate_main(argv: list[str] | None = None) -> int:
    """Run validation."""
    parser = argparse.ArgumentParser(description="Validate this specification.")
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--version", default=None)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    root = find_repo_root(args.repo_root)

    if args.version is None:
        args.version = load_fallback_version(root)

    run_validate(
        version=args.version,
        root=root,
        strict=args.strict,
    )

    print("Validation passed.")
    return 0
