---
search:
  boost: 5.0
---

# Slot: registergericht 


_Angabe des Registergerichts, bei dem die Organisation registriert ist. Katalogkategorie: Amtsgericht_



<div data-search-exclude markdown="1">



URI: [mastr:slot/registergericht](https://example.org/mastr/slot/registergericht)
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
| self | mastr:registergericht |
| native | mastr:registergericht |




## LinkML Source

<details>
```yaml
name: registergericht
instantiates:
- xsd:element
description: 'Angabe des Registergerichts, bei dem die Organisation registriert ist.
  Katalogkategorie: Amtsgericht'
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: integer

```
</details></div>