---
search:
  boost: 5.0
---

# Slot: datum 


_Datum, ab dem die Genehmigung für Bau oder Betrieb der Stromerzeugungseinheit erteilt ist_



<div data-search-exclude markdown="1">



URI: [mastr:slot/datum](https://example.org/mastr/slot/datum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
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
| self | mastr:datum |
| native | mastr:datum |




## LinkML Source

<details>
```yaml
name: datum
instantiates:
- xsd:element
description: Datum, ab dem die Genehmigung für Bau oder Betrieb der Stromerzeugungseinheit
  erteilt ist
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: date

```
</details></div>