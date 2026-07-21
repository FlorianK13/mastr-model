---
search:
  boost: 5.0
---

# Slot: verhaeltnisErtragsschaetzungReferenzertrag 


_Verhältnis der Ertragseinschätzung zum Referenzertrag ermittelt nach Anlage 2 des EEG_



<div data-search-exclude markdown="1">



URI: [mastr:slot/verhaeltnisErtragsschaetzungReferenzertrag](https://example.org/mastr/slot/verhaeltnisErtragsschaetzungReferenzertrag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegWind](../classes/AnlageEegWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
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
| self | mastr:verhaeltnisErtragsschaetzungReferenzertrag |
| native | mastr:verhaeltnisErtragsschaetzungReferenzertrag |




## LinkML Source

<details>
```yaml
name: verhaeltnisErtragsschaetzungReferenzertrag
instantiates:
- xsd:element
description: Verhältnis der Ertragseinschätzung zum Referenzertrag ermittelt nach
  Anlage 2 des EEG
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegWind
domain_of:
- AnlageEegWind
range: float

```
</details></div>