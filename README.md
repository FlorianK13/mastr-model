# Marktstammdatenregister (MaStR) Datenmodell

This site documents a [LinkML](https://linkml.io/) data model for the
Marktstammdatenregister (MaStR) Gesamtdatenexport.

## How these docs are built

The source data is the XSD schema files and the PDF documentation
"Dokumentation des Exports" (Beschreibung des Exports) retrieved from the
[Marktstammdatenregister](https://www.marktstammdatenregister.de/MaStR/Datendownload).

The build pipeline is:

1. `xsd-preprocessing.py` patches the XSD files so schema-automator can import
   them (replacing unsupported bounded integer types with `xs:integer`).
2. `merge-linkml.py` merges the per-XSD LinkML schemas from `linkml/parts/` into
   `linkml/mastr.yml`.
3. `pdf-description-extraction.py` parses the PDF automatically and injects
   attribute descriptions from the "Beschreibung" column into the matching
   schema classes.
4. `extract-base-classes.py` induces inheritance: it creates abstract `Einheit`
   and `Anlage` base classes that hold attributes shared across the concrete
   `Einheit*` and `Anlage*` classes, determined by identifying slots that appear
   in multiple of these classes with identical definitions.

The schema is defined in `linkml/mastr.yml` as a LinkML schema. The reference
pages under Schema (classes, slots,
types) are generated directly from that schema using LinkML's `generate doc`
command and should not be edited by hand — any changes belong in the schema
source instead. This page, however, is maintained separately and is not
touched by the generator.
