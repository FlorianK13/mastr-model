---
search:
  boost: 2.0
---


# Enum: Einspeisungsart 



<div data-search-exclude markdown="1">

URI: [mastr:enum/Einspeisungsart](https://example.org/mastr/enum/Einspeisungsart)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Volleinspeisung | None |  |
| Teileinspeisung (einschließlich Eigenverbrauch) | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [einspeisungsart](../slots/einspeisungsart.md) | Volleinspeisung oder Teileinspeisung |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr






## LinkML Source

<details>
```yaml
name: Einspeisungsart
from_schema: https://example.org/mastr
rank: 1000
permissible_values:
  Volleinspeisung:
    text: Volleinspeisung
    annotations:
      catalog_id:
        tag: catalog_id
        value: '688'
  Teileinspeisung (einschließlich Eigenverbrauch):
    text: Teileinspeisung (einschließlich Eigenverbrauch)
    annotations:
      catalog_id:
        tag: catalog_id
        value: '689'

```
</details>

</div>