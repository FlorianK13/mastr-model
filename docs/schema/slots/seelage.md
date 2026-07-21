---
search:
  boost: 5.0
---

# Slot: seelage 


_Wird die Windenergieanlage in der Nordsee oder in der Ostsee betrieben? Katalogkategorie: Seelage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/seelage](https://example.org/mastr/slot/seelage)
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
| self | mastr:seelage |
| native | mastr:seelage |




## LinkML Source

<details>
```yaml
name: seelage
instantiates:
- xsd:element
description: 'Wird die Windenergieanlage in der Nordsee oder in der Ostsee betrieben?
  Katalogkategorie: Seelage'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: integer

```
</details></div>