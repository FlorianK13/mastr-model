---
search:
  boost: 5.0
---

# Slot: leistungsbegrenzung 


_Die Leistung der Stromerzeugungseinheit ist auf einen bestimmten prozentualen Leistungsanteil begrenzt. Katalogkategorie: SolarLeistungsbegrenzung_



<div data-search-exclude markdown="1">



URI: [mastr:slot/leistungsbegrenzung](https://example.org/mastr/slot/leistungsbegrenzung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitSolar](../classes/EinheitSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:leistungsbegrenzung |
| native | mastr:leistungsbegrenzung |




## LinkML Source

<details>
```yaml
name: leistungsbegrenzung
instantiates:
- xsd:element
description: 'Die Leistung der Stromerzeugungseinheit ist auf einen bestimmten prozentualen
  Leistungsanteil begrenzt. Katalogkategorie: SolarLeistungsbegrenzung'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitSolar
domain_of:
- EinheitSolar
range: integer

```
</details></div>