---
search:
  boost: 5.0
---

# Slot: faxNv 


_Faxnummer des Marktakteurs. Nicht-vorhanden Flag_



<div data-search-exclude markdown="1">



URI: [mastr:slot/faxNv](https://example.org/mastr/slot/faxNv)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marktakteur](../classes/Marktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:faxNv |
| native | mastr:faxNv |




## LinkML Source

<details>
```yaml
name: faxNv
instantiates:
- xsd:element
description: Faxnummer des Marktakteurs. Nicht-vorhanden Flag
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: integer

```
</details></div>