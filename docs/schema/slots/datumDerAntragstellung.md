---
search:
  boost: 5.0
---

# Slot: datumDerAntragstellung 


_Datum der Antragstellung_



<div data-search-exclude markdown="1">



URI: [mastr:slot/datumDerAntragstellung](https://example.org/mastr/slot/datumDerAntragstellung)
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
| self | mastr:datumDerAntragstellung |
| native | mastr:datumDerAntragstellung |




## LinkML Source

<details>
```yaml
name: datumDerAntragstellung
instantiates:
- xsd:element
description: Datum der Antragstellung
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: date

```
</details></div>