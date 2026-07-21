---
search:
  boost: 5.0
---

# Slot: verhaeltnisErtragsschaetzungReferenzertragNv 


_Verhältnis der Ertragseinschätzung zum Referenzertrag ermittelt nach Anlage 2 des EEG. Nicht- vorhanden Flag_



<div data-search-exclude markdown="1">



URI: [mastr:slot/verhaeltnisErtragsschaetzungReferenzertragNv](https://example.org/mastr/slot/verhaeltnisErtragsschaetzungReferenzertragNv)
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
| self | mastr:verhaeltnisErtragsschaetzungReferenzertragNv |
| native | mastr:verhaeltnisErtragsschaetzungReferenzertragNv |




## LinkML Source

<details>
```yaml
name: verhaeltnisErtragsschaetzungReferenzertragNv
instantiates:
- xsd:element
description: Verhältnis der Ertragseinschätzung zum Referenzertrag ermittelt nach
  Anlage 2 des EEG. Nicht- vorhanden Flag
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegWind
domain_of:
- AnlageEegWind
range: integer

```
</details></div>