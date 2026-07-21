---
search:
  boost: 5.0
---

# Slot: inanspruchnahmeZahlungNachEeg 


_Werden oder wurden für die Solaranlage Zahlungen des Netzbetreibers in Anspruch genommen?_



<div data-search-exclude markdown="1">



URI: [mastr:slot/inanspruchnahmeZahlungNachEeg](https://example.org/mastr/slot/inanspruchnahmeZahlungNachEeg)
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
| self | mastr:inanspruchnahmeZahlungNachEeg |
| native | mastr:inanspruchnahmeZahlungNachEeg |




## LinkML Source

<details>
```yaml
name: inanspruchnahmeZahlungNachEeg
instantiates:
- xsd:element
description: Werden oder wurden für die Solaranlage Zahlungen des Netzbetreibers in
  Anspruch genommen?
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: integer

```
</details></div>