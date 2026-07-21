---
search:
  boost: 5.0
---

# Slot: nameWindpark 


_Vom Betreiber frei wählbare Bezeichnung des Windparks, dessen Teil die Einheit ist_



<div data-search-exclude markdown="1">



URI: [mastr:slot/nameWindpark](https://example.org/mastr/slot/nameWindpark)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [EinheitWind](../classes/EinheitWind.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitWind](../classes/EinheitWind.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:nameWindpark |
| native | mastr:nameWindpark |




## LinkML Source

<details>
```yaml
name: nameWindpark
instantiates:
- xsd:element
description: Vom Betreiber frei wählbare Bezeichnung des Windparks, dessen Teil die
  Einheit ist
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: string

```
</details></div>