---
search:
  boost: 5.0
---

# Slot: nabenhoehe 


_Die Nabenhöhe der Erzeugungseinheit_



<div data-search-exclude markdown="1">



URI: [mastr:slot/nabenhoehe](https://example.org/mastr/slot/nabenhoehe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
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
| self | mastr:nabenhoehe |
| native | mastr:nabenhoehe |




## LinkML Source

<details>
```yaml
name: nabenhoehe
instantiates:
- xsd:element
description: Die Nabenhöhe der Erzeugungseinheit
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: float

```
</details></div>