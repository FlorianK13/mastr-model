---
search:
  boost: 5.0
---

# Slot: kwkMastrNummer 


_MaStR-Nummer der Anlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/kwkMastrNummer](https://example.org/mastr/slot/kwkMastrNummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageKwk](../classes/AnlageKwk.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AnlageKwk](../classes/AnlageKwk.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageKwk](../classes/AnlageKwk.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:kwkMastrNummer |
| native | mastr:kwkMastrNummer |




## LinkML Source

<details>
```yaml
name: kwkMastrNummer
instantiates:
- xsd:element
description: MaStR-Nummer der Anlage
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageKwk
domain_of:
- AnlageKwk
range: string

```
</details></div>