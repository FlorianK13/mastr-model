---
search:
  boost: 5.0
---

# Slot: personenart 


_Angabe der Personenart des Marktakteurs: Natürliche Person oder Organisation mit Personenbezug oder Organisation. Katalogkategorie: Personenart_



<div data-search-exclude markdown="1">



URI: [mastr:slot/personenart](https://example.org/mastr/slot/personenart)
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
| self | mastr:personenart |
| native | mastr:personenart |




## LinkML Source

<details>
```yaml
name: personenart
instantiates:
- xsd:element
description: 'Angabe der Personenart des Marktakteurs: Natürliche Person oder Organisation
  mit Personenbezug oder Organisation. Katalogkategorie: Personenart'
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: integer

```
</details></div>