---
search:
  boost: 5.0
---

# Slot: taetigkeitsende 


_Das Tätigkeitsende des Marktakteurs_



<div data-search-exclude markdown="1">



URI: [mastr:slot/taetigkeitsende](https://example.org/mastr/slot/taetigkeitsende)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marktakteur](../classes/Marktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
| Domain Of | [Marktakteur](../classes/Marktakteur.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Marktakteur](../classes/Marktakteur.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:taetigkeitsende |
| native | mastr:taetigkeitsende |




## LinkML Source

<details>
```yaml
name: taetigkeitsende
instantiates:
- xsd:element
description: Das Tätigkeitsende des Marktakteurs
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: date

```
</details></div>