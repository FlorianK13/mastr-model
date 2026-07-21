---
search:
  boost: 5.0
---

# Slot: registernummerAusland 


_Registernummer des Marktakteurs, wenn im Ausland_



<div data-search-exclude markdown="1">



URI: [mastr:slot/registernummerAusland](https://example.org/mastr/slot/registernummerAusland)
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
| self | mastr:registernummerAusland |
| native | mastr:registernummerAusland |




## LinkML Source

<details>
```yaml
name: registernummerAusland
instantiates:
- xsd:element
description: Registernummer des Marktakteurs, wenn im Ausland
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>