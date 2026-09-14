#!/usr/bin/env python3
"""Populate the MaStR catalog lookup files used by ``build-enums.py``.

``build-enums.py`` turns book-catalog ("Katalogkategorie") attributes in the
LinkML schema into proper enumerations. Its source of truth is the MaStR
export's two lookup tables:

    * ``Katalogkategorien.xml``  -- Id -> category name
    * ``Katalogwerte.xml``       -- Id -> label (``Wert``), per category

These files are not committed to the repository; they must be pulled from the
remote MaStR "Gesamtdatenexport" archive. Both live inside the same zip, so we
stream each file out with an HTTP-range request (open-mastr's own
``unzip_http.RemoteZipFile``) -- only the few-kilobyte file is transferred,
never the whole multi-hundred-MB archive, and no database is touched.

Why not use open-mastr's ``Mastr().download(...)`` bulk path? It opens a
SQLite cache and tries to drop/recreate tables on every run, which fails
against a stale DB (e.g. ``use DROP VIEW to delete view nuclear_extended``),
leaving ``Katalogwerte.xml`` unextracted. Streaming both catalog files directly
skips the DB entirely and is what this script needs. The files are still
written into open-mastr's cache dir so ``build-enums.py`` finds them.
"""

from __future__ import annotations

import time
from pathlib import Path

from catalog_dirs import KATALOGKATEGORIEN, KATALOGWERTE, find_catalog_dir


def stream_catalog_files(catalog_dir: Path) -> None:
    """Pull Katalogkategorien.xml and Katalogwerte.xml out of the remote MaStR
    export zip via HTTP-range requests into ``catalog_dir``."""
    from open_mastr.utils import unzip_http
    from open_mastr.xml_download.utils_download_bulk import gen_url

    url = gen_url(time.localtime())
    catalog_dir.mkdir(parents=True, exist_ok=True)
    print(f"[fetch-catalog] Streaming catalog files from {url} ...")

    remote = unzip_http.RemoteZipFile(url)
    for name in (KATALOGKATEGORIEN, KATALOGWERTE):
        target = catalog_dir / name
        try:
            with remote.open(name) as src:
                target.write_bytes(src.read())
        except Exception as exc:  # pragma: no cover - failure path
            raise SystemExit(
                f"[fetch-catalog] Could not retrieve {name} from the MaStR export: "
                f"{exc}\nStream the file manually (or run the open-mastr download) "
                f"into {catalog_dir} and re-run the pipeline."
            ) from exc
        print(f"[fetch-catalog] Wrote {target}")


def main() -> int:
    catalog_dir = find_catalog_dir()
    if catalog_dir is not None:
        print(f"[fetch-catalog] Catalog files already present in {catalog_dir}")
        return 0

    from open_mastr.utils.config import get_output_dir

    data = Path(get_output_dir()) / "data"
    stream_catalog_files(data / "xml_download")
    print(f"[fetch-catalog] Ready: catalog files in {data / 'xml_download'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
