---
search:
  boost: 5.0
---

# Slot: kuestenentfernung 


_Küstenentfernung des Standort der Stromerzeugungseinheit_



<div data-search-exclude markdown="1">



URI: [mastr:slot/kuestenentfernung](https://example.org/mastr/slot/kuestenentfernung)
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
| self | mastr:kuestenentfernung |
| native | mastr:kuestenentfernung |




## LinkML Source

<details>
```yaml
name: kuestenentfernung
instantiates:
- xsd:element
description: Küstenentfernung des Standort der Stromerzeugungseinheit
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: float

```
</details></div>