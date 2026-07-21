---
search:
  boost: 5.0
---

# Slot: zugeordneteGebotsmenge 


_Bezuschlagte Gebotsmenge, die der EEG-Anlage zugeordnet wurde_



<div data-search-exclude markdown="1">



URI: [mastr:slot/zugeordneteGebotsmenge](https://example.org/mastr/slot/zugeordneteGebotsmenge)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegSolar](../classes/AnlageEegSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [AnlageEegSolar](../classes/AnlageEegSolar.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageEegSolar](../classes/AnlageEegSolar.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:zugeordneteGebotsmenge |
| native | mastr:zugeordneteGebotsmenge |




## LinkML Source

<details>
```yaml
name: zugeordneteGebotsmenge
instantiates:
- xsd:element
description: Bezuschlagte Gebotsmenge, die der EEG-Anlage zugeordnet wurde
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: float

```
</details></div>