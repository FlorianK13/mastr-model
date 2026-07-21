---
search:
  boost: 5.0
---

# Slot: biogasDatumLeistungserhoehung 


_Datum der Inbetriebnahme der Leistungserhöhung_



<div data-search-exclude markdown="1">



URI: [mastr:slot/biogasDatumLeistungserhoehung](https://example.org/mastr/slot/biogasDatumLeistungserhoehung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegBiomasse](../classes/AnlageEegBiomasse.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
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
| self | mastr:biogasDatumLeistungserhoehung |
| native | mastr:biogasDatumLeistungserhoehung |




## LinkML Source

<details>
```yaml
name: biogasDatumLeistungserhoehung
instantiates:
- xsd:element
description: Datum der Inbetriebnahme der Leistungserhöhung
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegBiomasse
domain_of:
- AnlageEegBiomasse
range: date

```
</details></div>