---
search:
  boost: 5.0
---

# Slot: biogasGaserzeugungskapazitaet 


_Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe._



<div data-search-exclude markdown="1">



URI: [mastr:slot/biogasGaserzeugungskapazitaet](https://example.org/mastr/slot/biogasGaserzeugungskapazitaet)
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
| self | mastr:biogasGaserzeugungskapazitaet |
| native | mastr:biogasGaserzeugungskapazitaet |




## LinkML Source

<details>
```yaml
name: biogasGaserzeugungskapazitaet
instantiates:
- xsd:element
description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
  nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe.'
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegBiomasse
domain_of:
- AnlageEegBiomasse
range: float

```
</details></div>