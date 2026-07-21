---
search:
  boost: 5.0
---

# Slot: windAnLandOderAufSee 


_Angabe, ob die Stromerzeugungseinheit an Land oder auf See errichtet wurde. Katalogkategorie: WindAnLandOderAufSee_



<div data-search-exclude markdown="1">



URI: [mastr:slot/windAnLandOderAufSee](https://example.org/mastr/slot/windAnLandOderAufSee)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:windAnLandOderAufSee |
| native | mastr:windAnLandOderAufSee |




## LinkML Source

<details>
```yaml
name: windAnLandOderAufSee
instantiates:
- xsd:element
description: 'Angabe, ob die Stromerzeugungseinheit an Land oder auf See errichtet
  wurde. Katalogkategorie: WindAnLandOderAufSee'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: integer

```
</details></div>