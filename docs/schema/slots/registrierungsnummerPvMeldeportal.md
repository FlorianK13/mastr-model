---
search:
  boost: 5.0
---

# Slot: registrierungsnummerPvMeldeportal 


_Durch die Bundesagentur vergeben Nummer bei der Registrierung im PV- Meldeportal_



<div data-search-exclude markdown="1">



URI: [mastr:slot/registrierungsnummerPvMeldeportal](https://example.org/mastr/slot/registrierungsnummerPvMeldeportal)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegSolar](../classes/AnlageEegSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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
| self | mastr:registrierungsnummerPvMeldeportal |
| native | mastr:registrierungsnummerPvMeldeportal |




## LinkML Source

<details>
```yaml
name: registrierungsnummerPvMeldeportal
instantiates:
- xsd:element
description: Durch die Bundesagentur vergeben Nummer bei der Registrierung im PV-
  Meldeportal
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: string

```
</details></div>