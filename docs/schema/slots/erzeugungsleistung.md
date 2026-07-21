---
search:
  boost: 5.0
---

# Slot: erzeugungsleistung 


_Leistung der Gaserzeugungseinheit_



<div data-search-exclude markdown="1">



URI: [mastr:slot/erzeugungsleistung](https://example.org/mastr/slot/erzeugungsleistung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGasErzeuger](../classes/EinheitGasErzeuger.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [EinheitGasErzeuger](../classes/EinheitGasErzeuger.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitGasErzeuger](../classes/EinheitGasErzeuger.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:erzeugungsleistung |
| native | mastr:erzeugungsleistung |




## LinkML Source

<details>
```yaml
name: erzeugungsleistung
instantiates:
- xsd:element
description: Leistung der Gaserzeugungseinheit
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGasErzeuger
domain_of:
- EinheitGasErzeuger
range: float

```
</details></div>