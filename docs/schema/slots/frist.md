---
search:
  boost: 5.0
---

# Slot: frist 


_Datum, bis zu dem gemäß der Genehmigung mit der Errichtung oder dem Betrieb der Anlage begonnen werden muss_



<div data-search-exclude markdown="1">



URI: [mastr:slot/frist](https://example.org/mastr/slot/frist)
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
| self | mastr:frist |
| native | mastr:frist |




## LinkML Source

<details>
```yaml
name: frist
instantiates:
- xsd:element
description: Datum, bis zu dem gemäß der Genehmigung mit der Errichtung oder dem Betrieb
  der Anlage begonnen werden muss
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: date

```
</details></div>