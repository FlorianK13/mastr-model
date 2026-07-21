---
search:
  boost: 5.0
---

# Slot: telefon 


_Telefonnummer des Marktakteurs_



<div data-search-exclude markdown="1">



URI: [mastr:slot/telefon](https://example.org/mastr/slot/telefon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marktakteur](../classes/Marktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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
| self | mastr:telefon |
| native | mastr:telefon |




## LinkML Source

<details>
```yaml
name: telefon
instantiates:
- xsd:element
description: Telefonnummer des Marktakteurs
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>