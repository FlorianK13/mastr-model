---
search:
  boost: 5.0
---

# Slot: biogasGaserzeugungskapazitaetNv 


_Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe. Nicht-vorhanden Flag_



<div data-search-exclude markdown="1">



URI: [mastr:slot/biogasGaserzeugungskapazitaetNv](https://example.org/mastr/slot/biogasGaserzeugungskapazitaetNv)
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
| self | mastr:biogasGaserzeugungskapazitaetNv |
| native | mastr:biogasGaserzeugungskapazitaetNv |




## LinkML Source

<details>
```yaml
name: biogasGaserzeugungskapazitaetNv
instantiates:
- xsd:element
description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
  nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe. Nicht-vorhanden
  Flag'
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegBiomasse
domain_of:
- AnlageEegBiomasse
range: integer

```
</details></div>