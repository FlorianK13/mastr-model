#!/bin/bash
set -e

echo "=== Step 1: XSD preprocessing ==="
python xsd-preprocessing.py

echo "=== Step 2: Import XSD files to LinkML parts ==="
mkdir -p linkml/parts
rm -f linkml/parts/*.yml
for xsd in xsd/*.xsd; do
    name=$(basename "$xsd" .xsd)
    echo "Importing $xsd -> linkml/parts/${name}.yml"
    schemauto import-xsd "$xsd" -o "linkml/parts/${name}.yml"
done

echo "=== Step 3: Merge LinkML parts ==="
python merge-linkml.py

echo "=== Step 4: Extract descriptions from PDF ==="
python pdf-description-extraction.py

echo "=== Step 5: Fetch MaStR catalog files (open-mastr) ==="
python fetch-catalog.py

echo "=== Step 6: Build Katalogkategorie enums ==="
python build-enums.py

echo "=== Step 7: Extract base classes ==="
python extract-base-classes.py

echo "=== Step 8: Generate documentation ==="
./gen-docs.sh

echo "=== Done ==="