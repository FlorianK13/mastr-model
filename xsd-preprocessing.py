#!/usr/bin/env python3
"""Preprocess the MaStR XSD files so schema-automator can import them.

Why this is needed
-------------------
The MaStR schemas declare several numeric fields with the bounded XSD integer
types ``xs:byte`` (-128..127), ``xs:short`` (-32768..32767) and ``xs:long``.
These are perfectly valid XML Schema, but schema-automator's XSD importer does
not map them to a LinkML type: in
``schema_automator/importers/xsd_import_engine.py`` they are listed in
``MISSING_TYPES`` rather than ``TYPE_MAP``, so importing aborts with e.g.

    ValueError: Atomic type {http://www.w3.org/2001/XMLSchema}byte
                does not have a corresponding LinkML type
    ValueError: Atomic type {http://www.w3.org/2001/XMLSchema}short
                does not have a corresponding LinkML type

``xs:integer`` *is* mapped (to LinkML ``Integer``), and since byte/short/long
are just range-restricted integers, substituting them is lossless for our
purposes (LinkML does not model those bounds anyway). This script rewrites every
such occurrence to ``xs:integer`` in-place so that, e.g.

    schemauto import-xsd xsd/AnlagenEegWind.xsd -o wind.yml
    schemauto import-xsd xsd/EinheitenWind.xsd -o wind_einheiten.yml

succeeds.

Usage
-----
    python xsd-preprocessing.py            # process all *.xsd in ./xsd
    python xsd-preprocessing.py path/to.xsd path/to/other.xsd
"""

from __future__ import annotations

import sys
from pathlib import Path

# XSD types that schema-automator cannot import -> equivalent type that it can.
# All are range-restricted integers, so xs:integer is a lossless replacement.
REPLACEMENT = "xs:integer"
UNSUPPORTED_TYPES = ("xs:byte", "xs:short", "xs:long")

XSD_DIR = Path(__file__).parent / "xsd"


def preprocess(path: Path) -> int:
    """Replace unsupported bounded integer types with xs:integer in ``path``.

    Returns the number of replacements made.
    """
    text = path.read_text(encoding="utf-8")
    count = sum(text.count(t) for t in UNSUPPORTED_TYPES)
    if count:
        for unsupported in UNSUPPORTED_TYPES:
            text = text.replace(unsupported, REPLACEMENT)
        path.write_text(text, encoding="utf-8")
    return count


def main(argv: list[str]) -> None:
    if argv:
        paths = [Path(a) for a in argv]
    else:
        paths = sorted(XSD_DIR.glob("*.xsd"))

    total = 0
    for path in paths:
        replaced = preprocess(path)
        total += replaced
        if replaced:
            print(f"{path}: replaced {replaced} occurrence(s)")

    print(f"Done. {total} total replacement(s) across {len(paths)} file(s).")


if __name__ == "__main__":
    main(sys.argv[1:])
