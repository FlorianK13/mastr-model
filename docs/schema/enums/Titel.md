---
search:
  boost: 2.0
---


# Enum: Titel 



<div data-search-exclude markdown="1">

URI: [mastr:enum/Titel](https://example.org/mastr/enum/Titel)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Dr. | None |  |
| Prof. | None |  |
| Prof. Dr. | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [marktakteurTitel](../slots/marktakteurTitel.md) | Titel der natürlichen Person |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr






## LinkML Source

<details>
```yaml
name: Titel
from_schema: https://example.org/mastr
rank: 1000
permissible_values:
  Dr.:
    text: Dr.
    annotations:
      catalog_id:
        tag: catalog_id
        value: '1000'
  Prof.:
    text: Prof.
    annotations:
      catalog_id:
        tag: catalog_id
        value: '1001'
  Prof. Dr.:
    text: Prof. Dr.
    annotations:
      catalog_id:
        tag: catalog_id
        value: '1002'

```
</details>

</div>