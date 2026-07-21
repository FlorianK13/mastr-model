---
search:
  boost: 5.0
---

# Slot: pilotAnlage 


_Die Windenergieanlage ist eine Pilotwindanlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/pilotAnlage](https://example.org/mastr/slot/pilotAnlage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegWind](../classes/AnlageEegWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [AnlageEegWind](../classes/AnlageEegWind.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageEegWind](../classes/AnlageEegWind.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:pilotAnlage |
| native | mastr:pilotAnlage |




## LinkML Source

<details>
```yaml
name: pilotAnlage
instantiates:
- xsd:element
description: Die Windenergieanlage ist eine Pilotwindanlage
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegWind
domain_of:
- AnlageEegWind
range: integer

```
</details></div>