---
search:
  boost: 5.0
---

# Slot: fristNv 


_Datum, bis zu dem gemäß der Genehmigung mit der Errichtung oder dem Betrieb der Anlage begonnen werden muss. Nicht-vorhanden Flag_



<div data-search-exclude markdown="1">



URI: [mastr:slot/fristNv](https://example.org/mastr/slot/fristNv)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:fristNv |
| native | mastr:fristNv |




## LinkML Source

<details>
```yaml
name: fristNv
instantiates:
- xsd:element
description: Datum, bis zu dem gemäß der Genehmigung mit der Errichtung oder dem Betrieb
  der Anlage begonnen werden muss. Nicht-vorhanden Flag
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: integer

```
</details></div>