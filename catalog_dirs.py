"""Locate the MaStR catalog lookup files under the open-mastr data directory.

Shared by fetch-catalog.py (populates the cache) and build-enums.py
(consumes it). The bulk download extracts the two XML lookup tables
straight into ``<output_dir>/data/xml_download/``.
"""

from __future__ import annotations

from pathlib import Path

KATALOGKATEGORIEN = "Katalogkategorien.xml"
KATALOGWERTE = "Katalogwerte.xml"
REQUIRED = {KATALOGKATEGORIEN, KATALOGWERTE}


def find_catalog_dir() -> Path | None:
    """Return the directory containing *both* catalog files, if any."""
    try:
        from open_mastr.utils.config import get_output_dir
    except Exception:  # pragma: no cover - open-mastr not importable
        candidates = []
    else:
        data = Path(get_output_dir()) / "data"
        candidates = [data / "xml_download", data]

    # Fallback: any ~/.open-MaStR directory, in case the layout drifts.
    candidates += [Path.home() / ".open-MaStR", Path.home() / ".open-mastr"]

    for base in candidates:
        if base.is_dir() and all((base / name).is_file() for name in REQUIRED):
            return base
    return None
