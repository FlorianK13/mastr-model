#!/usr/bin/env python3
"""Extract attribute descriptions from the MaStR PDF and add them to a LinkML schema.

Why this is needed
-------------------
The MaStR XSD files carry no documentation, but the accompanying PDF
("Dokumentation MaStR Gesamtdatenexport.pdf") has one table per XML element,
with columns ``Name | Beschreibung | Typ | Pflicht | Beispiel``. This script
locates each such table by its ``Element: <Name>`` heading, reconstructs the
``Beschreibung`` (description) text per attribute -- table cells can wrap
across multiple lines and even across page breaks -- and writes it into the
matching class/attribute of a LinkML schema as a ``description:`` field.

Column boundaries are *not* consistent across tables (each table's columns
are sized to their own content), so column x-ranges are detected freshly
from the header row of every "Element:" block rather than assumed globally.

This runs against the merged ``linkml/mastr.yml`` schema (which holds every
MaStR class in one flat ``classes:`` block), as well as any single-table
schema: the PDF is parsed once into a dict keyed by element name, and any
class in the given LinkML schema that matches an "Element: <Name>" block
gets its attribute descriptions filled in. Class names are matched
case/separator-insensitively and, as a fallback, fuzzily -- the PDF headings
contain occasional typos ("EinheitGasSpeicherr", "Einheiten...") and plural
forms that do not exactly equal the schema's class names.

Usage
-----
    python pdf-description-extraction.py \\
        --pdf "Dokumentation MaStR Gesamtdatenexport.pdf" \\
        --yml linkml/mastr.yml
"""

from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path

import pdfplumber
from ruamel.yaml import YAML

ELEMENT_HEADING_RE = re.compile(r"Element:\s*(\S+)")
BOILERPLATE_PREFIXES = ("MaStR Gesamtdatenexport", "Element:", "Dateiname:", "Revision", "Datum:")
ROW_TOLERANCE = 3  # px tolerance for clustering words onto the same visual line
COLUMN_PAD = 2  # px slack on column boundaries: a column's content shares its
# header word's left edge only up to sub-pixel float noise, so the first
# description word can sit a hair left of the "Beschreibung" header x0 (and be
# wrongly counted as part of the attribute name) without this slack.


def heading_name(line: list[dict]) -> str | None:
    """Return the element name if this line is an ``Element: <Name>`` heading."""
    text = " ".join(w["text"] for w in sorted(line, key=lambda w: w["x0"]))
    m = ELEMENT_HEADING_RE.search(text)
    return m.group(1) if m else None


def header_columns(line: list[dict]) -> tuple[float, float, float] | None:
    """Detect the ``Name | Beschreibung | Typ`` header row within a line.

    Returns (name_x0, description_x0, typ_x0) or None if this line is not the
    column-header row. This is detected per-line rather than per-page because
    the header repeats at the top of every continuation page of a table.
    """
    name_w = next((w for w in line if w["text"] == "Name"), None)
    besch_w = next((w for w in line if w["text"] == "Beschreibung"), None)
    typ_w = next((w for w in line if w["text"] == "Typ"), None)
    if not (name_w and besch_w and typ_w):
        return None
    return name_w["x0"], besch_w["x0"], typ_w["x0"]


def cluster_lines(words: list[dict]) -> list[list[dict]]:
    """Group words into visual lines by their 'top' coordinate."""
    lines: list[list[dict]] = []
    for w in sorted(words, key=lambda w: (w["top"], w["x0"])):
        if lines and abs(lines[-1][0]["top"] - w["top"]) <= ROW_TOLERANCE:
            lines[-1].append(w)
        else:
            lines.append([w])
    return lines


def is_boilerplate_line(line: list[dict]) -> bool:
    text = " ".join(w["text"] for w in sorted(line, key=lambda w: w["x0"]))
    if text in ("Name Beschreibung Typ Pflich", "t Beispiel", "Pflich", "t"):
        return True
    return any(text.startswith(p) for p in BOILERPLATE_PREFIXES)


def build_description_index(pdf_path: Path) -> dict[str, dict[str, str]]:
    """Return {ElementName: {AttributeName: description}} for the whole PDF.

    The whole document is parsed as one continuous stream of visual lines
    rather than as page-bounded blocks. A single page frequently holds the
    tail of one table and the ``Element:`` heading + start of the next, so
    per-page block boundaries mis-assign rows and pick the wrong column
    header. Instead a small state machine switches the "current element" on
    every ``Element:`` heading and re-reads the column x-ranges from every
    header row it sees (including the ones repeated on continuation pages).
    """
    index: dict[str, dict[str, str]] = {}

    descriptions: dict[str, str] | None = None
    cols: tuple[float, float, float] | None = None
    current_name: str | None = None
    current_desc: list[str] = []

    def flush():
        if descriptions is not None and current_name is not None:
            descriptions[current_name] = " ".join(current_desc).strip()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for line in cluster_lines(page.extract_words()):
                name = heading_name(line)
                if name is not None:
                    flush()
                    descriptions = index.setdefault(name, {})
                    cols = None  # its header row follows on a later line
                    current_name = None
                    current_desc = []
                    continue

                new_cols = header_columns(line)
                if new_cols is not None:
                    cols = new_cols
                    continue

                if is_boilerplate_line(line) or descriptions is None or cols is None:
                    continue

                name_x0, desc_x0, typ_x0 = cols
                name_text = " ".join(w["text"] for w in line if name_x0 - COLUMN_PAD <= w["x0"] < desc_x0 - COLUMN_PAD).strip()
                desc_text = " ".join(w["text"] for w in line if desc_x0 - COLUMN_PAD <= w["x0"] < typ_x0 - COLUMN_PAD).strip()

                if name_text and name_text[0].isupper():
                    flush()
                    current_name = name_text
                    current_desc = [desc_text] if desc_text else []
                else:
                    # A lowercase-leading fragment in the Name column is a
                    # word-wrapped continuation of the current attribute's name
                    # (e.g. "GebietNachDemFlaechenentwicklungsplanNords" / "ee"),
                    # not a new entry -- attribute names in this PDF always start
                    # with an uppercase letter.
                    if name_text and current_name is not None:
                        current_name += name_text
                    if desc_text and current_name is not None:
                        current_desc.append(desc_text)
        flush()
    return index


def normalize(name: str) -> str:
    """Collapse a name to lowercase alphanumerics for fuzzy matching.

    PDF names sometimes use a trailing underscore for boolean "not found"
    flags (e.g. "Hausnummer_nv") where the yml uses camelCase
    ("hausnummerNv"); comparing case- and separator-insensitively matches
    both without hardcoding the convention.
    """
    return re.sub(r"[^a-z0-9]", "", name.lower())


CLASS_FUZZY_CUTOFF = 0.85  # difflib ratio needed to accept a fuzzy class match


def match_class(class_name: str, index: dict[str, dict[str, str]]) -> dict[str, str] | None:
    """Find the PDF element block for a schema class name.

    Tries an exact normalized match first, then a fuzzy fallback to absorb
    PDF heading typos/plural forms (e.g. schema "EinheitGasSpeicher" vs PDF
    "EinheitGasSpeicherr"). Returns the {AttributeName: description} dict or
    None when no block is close enough.
    """
    by_normalized = {normalize(name): descs for name, descs in index.items()}
    target = normalize(class_name)
    if target in by_normalized:
        return by_normalized[target]
    close = difflib.get_close_matches(target, list(by_normalized), n=1, cutoff=CLASS_FUZZY_CUTOFF)
    return by_normalized[close[0]] if close else None


def apply_descriptions(yml_path: Path, index: dict[str, dict[str, str]]) -> tuple[int, int]:
    """Insert descriptions into the schema's classes/attributes in place.

    Returns (attributes_updated, classes_matched).
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    with yml_path.open("r", encoding="utf-8") as f:
        schema = yaml.load(f)

    updated = 0
    classes_matched = 0
    for class_name, class_def in schema.get("classes", {}).items():
        attr_descriptions = match_class(class_name, index)
        if not attr_descriptions:
            continue
        classes_matched += 1
        by_normalized = {normalize(k): v for k, v in attr_descriptions.items()}
        for attr_name, attr_def in (class_def.get("attributes") or {}).items():
            desc = by_normalized.get(normalize(attr_name))
            if desc:
                attr_def["description"] = desc
                updated += 1

    with yml_path.open("w", encoding="utf-8") as f:
        yaml.dump(schema, f)
    return updated, classes_matched


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("Dokumentation MaStR Gesamtdatenexport.pdf"),
        help="Path to the MaStR documentation PDF.",
    )
    parser.add_argument(
        "--yml",
        type=Path,
        default=Path("linkml/mastr.yml"),
        help="LinkML schema to update in place.",
    )
    args = parser.parse_args()

    index = build_description_index(args.pdf)
    updated, classes_matched = apply_descriptions(args.yml, index)
    print(f"Matched {classes_matched} class(es); updated {updated} attribute description(s) in {args.yml}")


if __name__ == "__main__":
    main()
