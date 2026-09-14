rm -rf docs/schema
uv run linkml generate doc -d docs/schema --subfolder-type-separation --no-include-top-level-diagram --no-metadata linkml/mastr.yml
