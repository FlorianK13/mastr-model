---
search:
  boost: 5.0
---

# Slot: registergerichtAusland 


_Angabe des Registergerichts, bei dem die Organisation registriert ist, wenn im Ausland_



<div data-search-exclude markdown="1">



URI: [mastr:slot/registergerichtAusland](https://example.org/mastr/slot/registergerichtAusland)
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
| self | mastr:registergerichtAusland |
| native | mastr:registergerichtAusland |




## LinkML Source

<details>
```yaml
name: registergerichtAusland
instantiates:
- xsd:element
description: Angabe des Registergerichts, bei dem die Organisation registriert ist,
  wenn im Ausland
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>