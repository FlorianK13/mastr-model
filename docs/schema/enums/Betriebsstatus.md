---
search:
  boost: 2.0
---


# Enum: Betriebsstatus 



<div data-search-exclude markdown="1">

URI: [mastr:enum/Betriebsstatus](https://example.org/mastr/enum/Betriebsstatus)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| In Planung | None |  |
| In Betrieb | None |  |
| Vorübergehend stillgelegt | None |  |
| Endgültig stillgelegt | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [anlageBetriebsstatus](../slots/anlageBetriebsstatus.md) | Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten ergibt |
| [einheitBetriebsstatus](../slots/einheitBetriebsstatus.md) | Betriebsstatus der Einheit |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr






## LinkML Source

<details>
```yaml
name: Betriebsstatus
from_schema: https://example.org/mastr
rank: 1000
permissible_values:
  In Planung:
    text: In Planung
    annotations:
      catalog_id:
        tag: catalog_id
        value: '31'
  In Betrieb:
    text: In Betrieb
    annotations:
      catalog_id:
        tag: catalog_id
        value: '35'
  Vorübergehend stillgelegt:
    text: Vorübergehend stillgelegt
    annotations:
      catalog_id:
        tag: catalog_id
        value: '37'
  Endgültig stillgelegt:
    text: Endgültig stillgelegt
    annotations:
      catalog_id:
        tag: catalog_id
        value: '38'

```
</details>

</div>