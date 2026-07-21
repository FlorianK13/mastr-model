"""Merge the per-XSD LinkML schemas in linkml/parts/ into one schema.

schemauto emits every file with the same name/id/prefix and a flat `classes:`
block (attributes are inline, so there are no top-level slots/enums/types to
reconcile). Merging is therefore just combining the `classes` dicts.
"""

from pathlib import Path

import yaml

PARTS = Path("linkml/parts")
OUT = Path("linkml/mastr.yml")

# schemauto's XSD importer (schema_automator.importers.xsd_import_engine.TYPE_MAP)
# emits CamelCase range names such as "String"/"Integer"/"Date" that don't match
# the actual lowercase type names defined by the linkml:types import (e.g.
# "string"/"integer"/"date"). Left as-is, SchemaView can't resolve these ranges,
# which breaks downstream tooling such as the docgen mermaid class diagrams.
BUILTIN_TYPE_FIXUP = {
    "Uri": "uri",
    "Boolean": "boolean",
    "Date": "date",
    "DateTime": "datetime",
    "Decimal": "decimal",
    "Double": "double",
    "Float": "float",
    "String": "string",
    "Time": "time",
    "Integer": "integer",
}


def normalize_ranges(cls: dict) -> None:
    for attr in (cls.get("attributes") or {}).values():
        range_ = attr.get("range")
        if range_ in BUILTIN_TYPE_FIXUP:
            attr["range"] = BUILTIN_TYPE_FIXUP[range_]


merged_classes: dict = {}
for part in sorted(PARTS.glob("*.yml")):
    doc = yaml.safe_load(part.read_text())
    for name, cls in (doc.get("classes") or {}).items():
        # SchemaRoot is a synthetic per-file entry point schemauto injects;
        # it is not part of the MaStR model and collides across files.
        if name == "SchemaRoot":
            continue
        normalize_ranges(cls)
        if name in merged_classes and merged_classes[name] != cls:
            print(f"WARNING: class {name!r} differs between files "
                  f"(keeping first, skipping the one in {part.name})")
            continue
        merged_classes[name] = cls


def is_container(cls: dict) -> bool:
    """A container just wraps a list of records: exactly one attribute whose
    range is another class (e.g. AnlagenEegWind -> AnlageEegWind)."""
    attrs = cls.get("attributes") or {}
    if len(attrs) != 1:
        return False
    (attr,) = attrs.values()
    return attr.get("range") in merged_classes


containers = [n for n, c in merged_classes.items() if is_container(c)]
for name in containers:
    del merged_classes[name]
print(f"Dropped {len(containers)} container classes: {', '.join(sorted(containers))}")

schema = {
    "id": "https://example.org/mastr",
    "name": "mastr",
    "title": "Marktstammdatenregister (MaStR) Gesamtdatenexport",
    "imports": ["linkml:types"],
    "prefixes": {
        "linkml": "https://w3id.org/linkml/",
        "mastr": "https://example.org/mastr/",
        "xsd": "http://www.w3.org/2001/XMLSchema",
    },
    "default_prefix": "mastr",
    "default_range": "string",
    "classes": dict(sorted(merged_classes.items())),
}

OUT.write_text(yaml.safe_dump(schema, sort_keys=False, allow_unicode=True))
print(f"Wrote {OUT} with {len(merged_classes)} classes")
