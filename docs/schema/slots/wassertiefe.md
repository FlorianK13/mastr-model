---
search:
  boost: 5.0
---

# Slot: wassertiefe 


_Wassertiefe am Standort der Stromerzeugungseinheit_



<div data-search-exclude markdown="1">



URI: [mastr:slot/wassertiefe](https://example.org/mastr/slot/wassertiefe)
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
| self | mastr:wassertiefe |
| native | mastr:wassertiefe |




## LinkML Source

<details>
```yaml
name: wassertiefe
instantiates:
- xsd:element
description: Wassertiefe am Standort der Stromerzeugungseinheit
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: float

```
</details></div>