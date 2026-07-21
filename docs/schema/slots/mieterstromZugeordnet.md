---
search:
  boost: 5.0
---

# Slot: mieterstromZugeordnet 


_Gibt an, ob die Solaranlage der Veräußerungsform des Mieterstromzuschlags zugeordnet wurde_



<div data-search-exclude markdown="1">



URI: [mastr:slot/mieterstromZugeordnet](https://example.org/mastr/slot/mieterstromZugeordnet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegSolar](../classes/AnlageEegSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:mieterstromZugeordnet |
| native | mastr:mieterstromZugeordnet |




## LinkML Source

<details>
```yaml
name: mieterstromZugeordnet
instantiates:
- xsd:element
description: Gibt an, ob die Solaranlage der Veräußerungsform des Mieterstromzuschlags
  zugeordnet wurde
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: integer

```
</details></div>