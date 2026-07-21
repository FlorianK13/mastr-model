---
search:
  boost: 5.0
---

# Slot: biogasHoechstbemessungsleistung 


_Höchstbemessungsleistung der Anlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/biogasHoechstbemessungsleistung](https://example.org/mastr/slot/biogasHoechstbemessungsleistung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegBiomasse](../classes/AnlageEegBiomasse.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [AnlageEegBiomasse](../classes/AnlageEegBiomasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageEegBiomasse](../classes/AnlageEegBiomasse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:biogasHoechstbemessungsleistung |
| native | mastr:biogasHoechstbemessungsleistung |




## LinkML Source

<details>
```yaml
name: biogasHoechstbemessungsleistung
instantiates:
- xsd:element
description: Höchstbemessungsleistung der Anlage
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegBiomasse
domain_of:
- AnlageEegBiomasse
range: float

```
</details></div>