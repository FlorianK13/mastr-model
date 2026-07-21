---
search:
  boost: 5.0
---

# Slot: flughoehe 


_Flughöhe einer Flugwindenergieanlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/flughoehe](https://example.org/mastr/slot/flughoehe)
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
| self | mastr:flughoehe |
| native | mastr:flughoehe |




## LinkML Source

<details>
```yaml
name: flughoehe
instantiates:
- xsd:element
description: Flughöhe einer Flugwindenergieanlage
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: float

```
</details></div>