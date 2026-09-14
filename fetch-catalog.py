#!/usr/bin/env python3
"""Populate the MaStR catalog lookup files used by ``build-enums.py``.

``build-enums.py`` turns book-catalog ("Katalogkategorie") attributes in the
LinkML schema into proper enumerations. Its source of truth is the MaStR
export's two lookup tables:

    * ``Katalogkategorien.xml``  -- Id -> category name
    * ``Katalogwerte.xml``       -- Id -> label (``Wert``), per category

These files are not committed to the repository; they are produced by
downloading the MaStR "Gesamtdatenexport" and live in the open-mastr project
home directory (``~/.open-MaStR/``). This script makes sure both files are
present before ``build-enums.py`` runs, and fails fast with clear instructions
if they cannot be obtained.

How the files are obtained
--------------------------
1. If both files already exist in the open-mastr data directory, nothing is
   downloaded and the script exits 0 (idempotent re-runs are cheap).
2. Otherwise open-mastr is asked to download a single light table (``nuclear``,
   the smallest import) which populates ``~/.open-MaStR/data/xml_download/``
   with the zipped export plus ``Katalogwerte.xml``.
3. ``Katalogkategorien.xml`` is not extracted by open-mastr's partial download,
   so if it is still missing it is streamed out of the remote Gesamtdatenexport
   zip (an HTTP-range request -- only the few-byte file is transferred, not the
   whole multi-hundred-MB archive).
"""

from __future__ import annotations

import time
from pathlib import Path

from catalog_dirs import KATALOGKATEGORIEN, KATALOGWERTE, find_catalog_dir

LIGHT_TABLE = "nuclear"  # smallest single-table bulk download


def run_open_mastr_download() -> None:
    """Trigger open-mastr to download the light table, populating the cache."""
    from open_mastr import Mastr

    print(f"[fetch-catalog] Running open-mastr download for table '{LIGHT_TABLE}' ...")
    db = Mastr()
    # bulk_cleansing=False keeps the raw bulk files; we only need the XMLs.
    db.download(method="bulk", data=[LIGHT_TABLE], bulk_cleansing=False)


def ensure_katalogkategorien_available(catalog_dir: Path) -> None:
    """Make sure Katalogkategorien.xml is present, pulling it from the remote
    zip (range request) if the local cache still lacks it."""
    target = catalog_dir / KATALOGKATEGORIEN
    if target.is_file():
        return

    from open_mastr.utils import unzip_http
    from open_mastr.xml_download.utils_download_bulk import gen_url

    url = gen_url(time.localtime())
    print(f"[fetch-catalog] Streaming {KATALOGKATEGORIEN} from {url} ...")
    remote = unzip_http.RemoteZipFile(url)
    try:
        with remote.open(KATALOGKATEGORIEN) as src:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(src.read())
    except Exception as exc:  # pragma: no cover - failure path
        raise SystemExit(
            f"[fetch-catalog] Could not retrieve {KATALOGKATEGORIEN} from the MaStR "
            f"export: {exc}\nRun the open-mastr bulk download manually to populate "
            f"{catalog_dir} and re-run the pipeline."
        ) from exc
    print(f"[fetch-catalog] Wrote {target}")


def main() -> int:
    catalog_dir = find_catalog_dir()
    if catalog_dir is not None:
        print(f"[fetch-catalog] Catalog files already present in {catalog_dir}")
        return 0

    # Nothing usable yet -> trigger an open-mastr download (populates the cache).
    try:
        run_open_mastr_download()
    except Exception as exc:  # pragma: no cover - failure path
        raise SystemExit(
            f"[fetch-catalog] FATAL: open-mastr download failed: {exc}\n"
            "Run open-mastr manually or place Katalogkategorien.xml and "
            "Katalogwerte.xml under ~/.open-MaStR, then re-run."
        ) from exc

    catalog_dir = find_catalog_dir()
    if catalog_dir is None:  # pragma: no cover - unexpected
        raise SystemExit("[fetch-catalog] FATAL: download finished but no catalog "
                         "directory was found; inspect the open-mastr data dir.")

    ensure_katalogkategorien_available(catalog_dir)
    print(f"[fetch-catalog] Ready: catalog files in {catalog_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
