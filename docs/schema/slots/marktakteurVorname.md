---
search:
  boost: 5.0
---

# Slot: marktakteurVorname 


_Vorname der natürlichen Person_



<div data-search-exclude markdown="1">



URI: [mastr:slot/marktakteurVorname](https://example.org/mastr/slot/marktakteurVorname)
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
| self | mastr:marktakteurVorname |
| native | mastr:marktakteurVorname |




## LinkML Source

<details>
```yaml
name: marktakteurVorname
instantiates:
- xsd:element
description: Vorname der natürlichen Person
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>