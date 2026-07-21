"""Factor shared attributes of the MaStR classes into `Anlage`/`Einheit` bases.

The schemauto-derived schema (linkml/mastr.yml) has no inheritance: every
concrete class carries its own copy of the attributes. Yet the `Einheit*`
classes (and, to a lesser extent, the `Anlage*` classes) repeat a large block
of identically-defined attributes (address, operating status, dates, ...).

This script rewrites the schema in place so that:

  * a `abstract: true` base class `Anlage` / `Einheit` holds the shared
    attributes, and
  * each concrete class gets `is_a: <base>` and keeps only the attributes that
    differ from (or are absent in) the base.

Membership of a group is `^<Base>[A-Z]` (so `Anlagen*` containers, `Einheiten*`
and `Einheitentyp` are not swept in). A member that barely overlaps the group's
shared block -- e.g. `EinheitGenehmigung`, a permit record that happens to start
with "Einheit" -- is treated as an outlier and left standalone (no `is_a`), so
its fields never leak into the base.
"""

from collections import Counter
from pathlib import Path
import math
import re

import yaml

SCHEMA = Path("linkml/mastr.yml")

BASES = ["Anlage", "Einheit"]

# A member whose share of the group's candidate-common fields is below this is
# not really an instance of the base (it only shares the name prefix) and is
# excluded from the base entirely. EinheitGenehmigung sits at ~0.06 here while
# every genuine Einheit is >= 0.70.
OUTLIER_OVERLAP = 0.2

# Minimum fraction of the (non-outlier) members that must *possess* an attribute
# for it to be pulled into the base. At the default 1.0 the attribute must be
# present in every subclass, so no class inherits a field it did not already
# have (zero widening -- the refactor is semantically exact). Lower it to dedup
# more aggressively at the cost of granting some members optional fields they
# previously lacked. Where members disagree on an attribute's definition, the
# majority definition goes into the base and the others override it locally.
BASE_FIELD_THRESHOLD = 1.0


def defkey(attr_def: dict) -> str:
    """Stable string identity of an attribute definition, for equality tests."""
    return yaml.safe_dump(attr_def, sort_keys=True, allow_unicode=True)


def members_of(base: str, classes: dict) -> list[str]:
    return [n for n in classes if re.match(base + r"[A-Z]", n)]


def split_outliers(members: list[str], classes: dict) -> tuple[list[str], list[str]]:
    """Partition members into (core, outliers) by their overlap with the fields
    that at least half of the members share."""
    freq = Counter()
    for m in members:
        freq.update((classes[m].get("attributes") or {}).keys())
    candidate = {k for k, c in freq.items() if c >= math.ceil(len(members) / 2)}
    if not candidate:
        return members, []
    core, outliers = [], []
    for m in members:
        have = set(classes[m].get("attributes") or {})
        overlap = len(have & candidate) / len(candidate)
        (outliers if overlap < OUTLIER_OVERLAP else core).append(m)
    return core, outliers


def base_attributes(core: list[str], classes: dict) -> dict:
    """For every attribute name possessed by >= BASE_FIELD_THRESHOLD of the core
    members, take its majority definition into the base. Attribute order follows
    the first core member that declares each."""
    min_count = math.ceil(BASE_FIELD_THRESHOLD * len(core))
    order: list[str] = []
    def_votes: dict[str, Counter] = {}
    def_by_key: dict[str, dict] = {}
    for m in core:
        for name, attr in (classes[m].get("attributes") or {}).items():
            if name not in def_votes:
                def_votes[name] = Counter()
                order.append(name)
            key = defkey(attr)
            def_votes[name][key] += 1
            def_by_key.setdefault(key, attr)

    base_attrs: dict = {}
    for name in order:
        if sum(def_votes[name].values()) >= min_count:
            majority_key = def_votes[name].most_common(1)[0][0]
            base_attrs[name] = def_by_key[majority_key]
    return base_attrs


def strip_inherited(cls: dict, base_attrs: dict) -> dict:
    """Return a new class dict with `is_a` set and every attribute that the base
    already provides identically removed (attributes that differ are kept as an
    override)."""
    kept = {}
    for name, attr in (cls.get("attributes") or {}).items():
        if name in base_attrs and defkey(attr) == defkey(base_attrs[name]):
            continue  # identical to base -> inherit
        kept[name] = attr
    new_cls = {k: v for k, v in cls.items() if k != "attributes"}
    if kept:
        new_cls["attributes"] = kept
    return new_cls


def main() -> None:
    doc = yaml.safe_load(SCHEMA.read_text())
    classes: dict = doc["classes"]

    new_base_classes: dict = {}
    for base in BASES:
        members = members_of(base, classes)
        if not members:
            continue
        core, outliers = split_outliers(members, classes)
        base_attrs = base_attributes(core, classes)
        if not base_attrs:
            print(f"{base}: no shared attributes found, skipping")
            continue

        new_base_classes[base] = {
            "abstract": True,
            "description": f"Gemeinsame Attribute der {base}-Klassen.",
            "attributes": base_attrs,
        }
        for m in core:
            cls = strip_inherited(classes[m], base_attrs)
            cls = {"is_a": base, **{k: v for k, v in cls.items()}}
            classes[m] = cls

        print(
            f"{base}: base with {len(base_attrs)} attributes; "
            f"{len(core)} subclasses"
            + (f"; outliers left standalone: {', '.join(sorted(outliers))}"
               if outliers else "")
        )

    classes.update(new_base_classes)
    doc["classes"] = dict(sorted(classes.items()))

    SCHEMA.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True)
    )
    print(f"Wrote {SCHEMA}")


if __name__ == "__main__":
    main()
