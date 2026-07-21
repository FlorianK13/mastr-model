---
search:
  boost: 5.0
---

# Slot: biogasLeistungserhoehung 


_Angabe, ob die Leistung der Anlage im Zusammenhang mit der Flexibilitätsprämie erhöht wird_



<div data-search-exclude markdown="1">



URI: [mastr:slot/biogasLeistungserhoehung](https://example.org/mastr/slot/biogasLeistungserhoehung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegBiomasse](../classes/AnlageEegBiomasse.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:biogasLeistungserhoehung |
| native | mastr:biogasLeistungserhoehung |




## LinkML Source

<details>
```yaml
name: biogasLeistungserhoehung
instantiates:
- xsd:element
description: Angabe, ob die Leistung der Anlage im Zusammenhang mit der Flexibilitätsprämie
  erhöht wird
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegBiomasse
domain_of:
- AnlageEegBiomasse
range: integer

```
</details></div>