---
search:
  boost: 5.0
---

# Slot: gemeinsamRegistrierteSolareinheitMastrNummer 


_Zum Speicher registrierte Solareinheit_



<div data-search-exclude markdown="1">



URI: [mastr:slot/gemeinsamRegistrierteSolareinheitMastrNummer](https://example.org/mastr/slot/gemeinsamRegistrierteSolareinheitMastrNummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:gemeinsamRegistrierteSolareinheitMastrNummer |
| native | mastr:gemeinsamRegistrierteSolareinheitMastrNummer |




## LinkML Source

<details>
```yaml
name: gemeinsamRegistrierteSolareinheitMastrNummer
instantiates:
- xsd:element
description: Zum Speicher registrierte Solareinheit
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitStromSpeicher
domain_of:
- EinheitStromSpeicher
range: string

```
</details></div>