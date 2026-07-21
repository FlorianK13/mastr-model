---
search:
  boost: 5.0
---

# Slot: flugradius 


_Flugradius einer Flugwindenergieanlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/flugradius](https://example.org/mastr/slot/flugradius)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [EinheitWind](../classes/EinheitWind.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitWind](../classes/EinheitWind.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:flugradius |
| native | mastr:flugradius |




## LinkML Source

<details>
```yaml
name: flugradius
instantiates:
- xsd:element
description: Flugradius einer Flugwindenergieanlage
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: float

```
</details></div>