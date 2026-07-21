---
search:
  boost: 5.0
---

# Slot: lichteHoehe 


_Lichte Höhe in Meter_



<div data-search-exclude markdown="1">



URI: [mastr:slot/lichteHoehe](https://example.org/mastr/slot/lichteHoehe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitSolar](../classes/EinheitSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [EinheitSolar](../classes/EinheitSolar.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitSolar](../classes/EinheitSolar.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:lichteHoehe |
| native | mastr:lichteHoehe |




## LinkML Source

<details>
```yaml
name: lichteHoehe
instantiates:
- xsd:element
description: Lichte Höhe in Meter
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitSolar
domain_of:
- EinheitSolar
range: float

```
</details></div>