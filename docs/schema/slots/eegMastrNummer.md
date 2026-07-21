---
search:
  boost: 5.0
---

# Slot: eegMastrNummer 


_Die MaStR-Nummer der zugehörigen EEG-Anlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/eegMastrNummer](https://example.org/mastr/slot/eegMastrNummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ertuechtigung](../classes/Ertuechtigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Ertuechtigung](../classes/Ertuechtigung.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Ertuechtigung](../classes/Ertuechtigung.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:eegMastrNummer |
| native | mastr:eegMastrNummer |




## LinkML Source

<details>
```yaml
name: eegMastrNummer
instantiates:
- xsd:element
description: Die MaStR-Nummer der zugehörigen EEG-Anlage
from_schema: https://example.org/mastr
rank: 1000
owner: Ertuechtigung
domain_of:
- Ertuechtigung
range: string

```
</details></div>