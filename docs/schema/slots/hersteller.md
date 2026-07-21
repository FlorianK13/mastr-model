---
search:
  boost: 5.0
---

# Slot: hersteller 


_Hersteller der Einheit. Katalogwert: Hersteller_



<div data-search-exclude markdown="1">



URI: [mastr:slot/hersteller](https://example.org/mastr/slot/hersteller)
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
| self | mastr:hersteller |
| native | mastr:hersteller |




## LinkML Source

<details>
```yaml
name: hersteller
instantiates:
- xsd:element
description: 'Hersteller der Einheit. Katalogwert: Hersteller'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: integer

```
</details></div>