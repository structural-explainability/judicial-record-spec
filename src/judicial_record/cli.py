"""cli.py - Public command-line entry points."""

from judicial_record.commands.manifest import (
    sync_main,
)
from judicial_record.commands.reference import (
    ref_export_main,
    ref_validate_main,
)
from judicial_record.commands.root import main
from judicial_record.commands.validate import validate_main

__all__ = [
    "main",
    "ref_export_main",
    "ref_validate_main",
    "sync_main",
    "validate_main",
]


if __name__ == "__main__":
    raise SystemExit(main())
