#!/usr/bin/env python3
"""Turn MaStR "Katalogkategorie" attributes into LinkML enumerations.

A number of attributes in the merged schema (``linkml/mastr.yml``) are
book-catalog ("Katalogkategorie") lookups: their XSD type is an integer whose
value is the *Id* of a row in the ``Katalogwerte`` lookup table, not the final
human-readable label. The MaStR export database resolves those Ids and stores
the ``Wert`` (label) string instead.

This script inspects every attribute whose ``description`` carries the marker
``Katalogkategorie: <Name>`` (injected from the PDF documentation) and
replaces its ``range: integer`` with a reference to a new top-level LinkML
``enums:`` block. Each enum's ``permissible_values`` are the resolved labels
(``Katalogwert.Wert``) for that category, keyed by the label, with the
original catalog Id kept as an annotation for traceability::

    Energietraeger:
      permissible_values:
        Braunkohle:
          annotations:
            catalog_id: { value: "2408" }

Source data
-----------
The enumerated values come from the MaStR export's two lookup tables:

    * ``Katalogkategorien.xml`` -- Id -> category name
    * ``Katalogwerte.xml``      -- Id -> label (``Wert``), per category

Both are populated by ``fetch-catalog.py`` (run first) into the open-mastr
data directory. The script locates them under that directory and parses them
with a tolerant XML reader (matching stripped local tag names) to absorb
casing/namespace drift across open-mastr versions. Katalogwerte.xml is
UTF-16 encoded in the export, which the reader handles transparently.

Name matching
-------------
A description marker is matched to a ``Katalogkategorie.Name`` with descending
confidence:

1. **Exact** -- the marker equals the category name after normalization
   (lowercase, umlaut folding ``ä/ö/ü/ß -> ae/oe/ue/ss``, non-alphanumerics
   stripped). This is always correct.
2. **Unique containment** -- with exactly one category candidate whose
   normalized name is a substring of the marker (or vice versa). Handles
   unambiguous drift such as ``Anlagenbetriebsstatus -> Betriebsstatus`` or
   ``BundeslaenderEinheit -> BundeslaenderEinheiten``.
3. Every other marker category is **reported loudly on stderr** and its slots
   are left with their existing ``range`` (kept as ``integer`` / ``string``) so
   the build never silently drops a valid enumeration. A curator then fixes the
   cause (a PDF marker typo or naming drift between the PDF and the export) and
   re-runs. Ambiguous containment hits (multiple candidates) are also reported
   rather than guessed.

Usage
-----
    python scripts/04-fetch-catalog.py   # populate the catalog cache (prerequisite)
    python scripts/05-build-enums.py     # rewrite linkml/mastr.yml in place
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml
from catalog_dirs import KATALOGKATEGORIEN, KATALOGWERTE, find_catalog_dir

SCHEMA = Path("linkml/mastr.yml")
MARKER = "Katalogkategorie:"

# Marker categories are matched against Katalogkategorie.Name with this much
# effort. Names that still cannot be resolved are reported and left untouched.


# --------------------------------------------------------------------------- #
# Catalog data loading
# --------------------------------------------------------------------------- #
def _local_tag(tag: str) -> str:
    """Stripped local tag name, absorbing any XML namespace prefix."""
    return tag.rsplit("}", 1)[-1].rsplit(":", 1)[-1]


def _iter_records(path: Path, collection: str, record: str):
    """Tolerant iterator over <record> children of a <collection> root.

    Automatically decodes UTF-16 (as used by the MaStR export) via the XML
    declaration on the first element, and ignores namespaces.
    """
    raw = path.read_bytes()
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        # UTF-16 without a readable declaration -> force decode and reparse.
        text = raw.decode("utf-16")
        root = ET.fromstring(text)
    if _local_tag(root.tag) != collection:
        raise ValueError(
            f"Unexpected root element <{_local_tag(root.tag)}> in {path} "
            f"(expected <{collection}>)"
        )
    for el in root:
        if _local_tag(el.tag) != record:
            continue
        yield {_local_tag(ch.tag): (ch.text or "").strip() for ch in el}


def load_catalog() -> tuple[dict[int, str], dict[int, list[tuple[str, str]]]]:
    """Return (category_id -> name, category_id -> [(wert, id), ...]).

    The value table groups ``Katalogwerte`` by ``KatalogKategorieId``, keeping
    the Id of each value alongside its label.
    """
    catalog_dir = find_catalog_dir()
    if catalog_dir is None:
        raise SystemExit(
            "build-enums.py: could not find Katalogkategorien.xml and "
            "Katalogwerte.xml under the open-mastr data directory.\n"
            "Run `python scripts/04-fetch-catalog.py` first to populate them."
        )
    kategorien_path = catalog_dir / KATALOGKATEGORIEN
    werte_path = catalog_dir / KATALOGWERTE

    categories: dict[int, str] = {}
    for rec in _iter_records(kategorien_path, "Katalogkategorien", "Katalogkategorie"):
        categories[int(rec["Id"])] = rec["Name"]

    values: dict[int, list[tuple[str, str]]] = {}
    for rec in _iter_records(werte_path, "Katalogwerte", "Katalogwert"):
        cat_id = int(rec["KatalogKategorieId"])
        # (wert, id) - first occurrence of a label wins within a category.
        wert, value_id = rec["Wert"], rec["Id"]
        lst = values.setdefault(cat_id, [])
        if not any(w == wert for w, _ in lst):
            lst.append((wert, value_id))

    return categories, values


# --------------------------------------------------------------------------- #
# Marker scanning
# --------------------------------------------------------------------------- #
MARKER_RE = re.compile(re.escape(MARKER) + r"\s*([\wüäöÜÄÖß]+)")


def _scan_markers(schema: dict) -> dict[str, list[dict]]:
    """Map each distinct marker category name to its affected attributes.

    Each value is a list of ``{"class": ..., "attr": ..., "attr_def": ...}``.
    """
    found: dict[str, list[dict]] = {}
    for class_name, class_def in (schema.get("classes") or {}).items():
        for attr_name, attr_def in (class_def.get("attributes") or {}).items():
            desc = attr_def.get("description") or ""
            m = MARKER_RE.search(desc)
            if m:
                found.setdefault(m.group(1), []).append(
                    {"class": class_name, "attr": attr_name, "attr_def": attr_def}
                )
    return found


# --------------------------------------------------------------------------- #
# Tolerant name matching
# --------------------------------------------------------------------------- #
def _normalize(name: str) -> str:
    """Lowercase, umlaut-fold and strip non-alphanumerics for matching."""
    text = unicodedata.normalize("NFC", name).lower()
    for src, dst in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(src, dst)
    return re.sub(r"[^a-z0-9]", "", text)


def _resolve_category(
    marker: str, categories: dict[int, str]
) -> tuple[int | None, str]:
    """Match a marker name to a category.

    Returns ``(category_id, resolution)`` where resolution is one of
    ``"exact"``, ``"containment"``, ``"ambiguous"`` or ``"unmatched"``. For
    "ambiguous"/"unmatched" the id is None and the caller reports + leaves the
    slots untouched.
    """
    key = _normalize(marker)

    exact = [cid for cid, name in categories.items() if _normalize(name) == key]
    if exact:
        return exact[0], "exact"

    # Unique containment (either direction).
    contained = [
        (cid, name)
        for cid, name in categories.items()
        if (_normalize(name) in key and len(_normalize(name)) >= 4)
        or (len(key) >= 4 and key in _normalize(name))
    ]
    if len(contained) == 1:
        return contained[0][0], "containment"
    if len(contained) > 1:
        return None, "ambiguous"

    return None, "unmatched"


def _enum_name(category_name: str) -> str:
    """Sanitize a category name into a valid, ASCII PascalCase LinkML enum id.

    Umlauts are transliterated (ae/oe/ue/ss) to keep the identifier ASCII-safe
    for docgen/validation (e.g. ``Energieträger -> Energietraeger``), matching
    the convention used elsewhere in this schema.
    """
    folded = "".join(
        {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}.get(ch, ch)
        for ch in unicodedata.normalize("NFC", category_name)
    )
    words = re.findall(r"[A-Za-z0-9]+", folded)
    if not words:
        words = ["Enum"]
    return "".join(w[:1].upper() + w[1:] for w in words)


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def _report(summary: dict) -> None:
    print("\n===== build-enums.py report =====", file=sys.stderr)
    print(f"Resolved exact:             {len(summary['exact'])}", file=sys.stderr)
    print(f"Resolved by containment:    {len(summary['containment'])}", file=sys.stderr)
    print(f"Ambiguous (left unchanged): {len(summary['ambiguous'])}", file=sys.stderr)
    print(f"Unmatched (left unchanged): {len(summary['unmatched'])}", file=sys.stderr)

    if summary["ambiguous"] or summary["unmatched"]:
        print(
            "\nThe following marker categories could NOT be resolved to a "
            "Katalogkategorie and are left as their existing range for manual "
            "curation. Fix the marker in the PDF description or the category "
            "naming, then re-run:",
            file=sys.stderr,
        )
        for resolution, names in (
            ("ambiguous", summary["ambiguous"]),
            ("unmatched", summary["unmatched"]),
        ):
            for name in names:
                print(f"  [{resolution}] {name}", file=sys.stderr)
        print("\nResolved markers (for reference):", file=sys.stderr)
        for name in sorted(summary["exact"]):
            print(f"  [exact] {name}", file=sys.stderr)
        for name in sorted(summary["containment"]):
            print(f"  [containment] {name}", file=sys.stderr)
    print("=================================", file=sys.stderr)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    categories, values = load_catalog()

    schema = yaml.safe_load(SCHEMA.read_text())
    markers = _scan_markers(schema)

    enums: dict[str, dict] = {}
    enum_owner: dict[str, int] = {}  # enum name -> category id that owns it
    summary = {"exact": [], "containment": [], "ambiguous": [], "unmatched": []}
    slots_rewritten = 0

    for marker, slots in sorted(markers.items()):
        cat_id, resolution = _resolve_category(marker, categories)
        summary[resolution].append(marker)

        if cat_id is None:
            # Ambiguous or unmatched: leave every slot untouched, report loudly.
            continue

        category_name = categories[cat_id]
        enum_name = _enum_name(category_name)
        payload = []
        for label, value_id in values.get(cat_id, []):
            payload.append(
                (label, {"annotations": {"catalog_id": {"value": value_id}}})
            )
        if not payload:
            continue

        # Enum names are keyed by category. Two markers that resolve to the
        # *same* category share one enum; only when two *different* categories
        # sanitize to the same name do we disambiguate so no values are lost.
        existing_owner = enum_owner.get(enum_name)
        if existing_owner is not None and existing_owner != cat_id:
            print(
                f"WARNING: enum name collision between categories "
                f"{existing_owner} and {cat_id}; disambiguating "
                f"{enum_name!r}",
                file=sys.stderr,
            )
            enum_name = f"{enum_name}{cat_id}"
        if enum_name not in enums:
            enums[enum_name] = {"permissible_values": {k: v for k, v in payload}}
            enum_owner[enum_name] = cat_id

        # Rewrite affected slots.
        for slot in slots:
            slot["attr_def"]["range"] = enum_name
            slots_rewritten += 1

    # Insert enums block at the top of the schema (before classes).
    new_doc = {}
    inserted = False
    for key, value in schema.items():
        if key == "classes" and enums and not inserted:
            new_doc["enums"] = dict(sorted(enums.items()))
            inserted = True
        if key != "enums":  # drop any stale enums block
            new_doc[key] = value
    if enums and not inserted:
        new_doc["enums"] = dict(sorted(enums.items()))
    # If there are no enums, the schema is unchanged aside from being re-dumped.
    schema = new_doc

    SCHEMA.write_text(yaml.safe_dump(schema, sort_keys=False, allow_unicode=True))

    _report(summary)
    print(
        f"build-enums.py: wrote {len(enums)} enums; rewrote {slots_rewritten} "
        f"slot range(s) in {SCHEMA}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
