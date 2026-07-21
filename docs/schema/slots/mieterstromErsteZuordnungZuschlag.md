---
search:
  boost: 5.0
---

# Slot: mieterstromErsteZuordnungZuschlag 


_Datum, an dem die Anlage erstmalig der Veräußerungsform des Mieterstromzuschlags zugeordnet worden ist._



<div data-search-exclude markdown="1">



URI: [mastr:slot/mieterstromErsteZuordnungZuschlag](https://example.org/mastr/slot/mieterstromErsteZuordnungZuschlag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegSolar](../classes/AnlageEegSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
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
| self | mastr:mieterstromErsteZuordnungZuschlag |
| native | mastr:mieterstromErsteZuordnungZuschlag |




## LinkML Source

<details>
```yaml
name: mieterstromErsteZuordnungZuschlag
instantiates:
- xsd:element
description: Datum, an dem die Anlage erstmalig der Veräußerungsform des Mieterstromzuschlags
  zugeordnet worden ist.
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: date

```
</details></div>