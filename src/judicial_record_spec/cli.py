"""cli.py - Public command-line entry points."""

from judicial_record_spec.commands.manifest import (
    sync_main,
)
from judicial_record_spec.commands.reference import (
    ref_export_main,
    ref_validate_main,
)
from judicial_record_spec.commands.root import main
from judicial_record_spec.commands.validate import validate_main

__all__ = [
    "main",
    "ref_export_main",
    "ref_validate_main",
    "sync_main",
    "validate_main",
]


if __name__ == "__main__":
    raise SystemExit(main())
