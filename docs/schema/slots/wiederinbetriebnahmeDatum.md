---
search:
  boost: 5.0
---

# Slot: wiederinbetriebnahmeDatum 


_Datum der Wiederinbetriebnahme_



<div data-search-exclude markdown="1">



URI: [mastr:slot/wiederinbetriebnahmeDatum](https://example.org/mastr/slot/wiederinbetriebnahmeDatum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ertuechtigung](../classes/Ertuechtigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](../types/Datetime.md) |
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
| self | mastr:wiederinbetriebnahmeDatum |
| native | mastr:wiederinbetriebnahmeDatum |




## LinkML Source

<details>
```yaml
name: wiederinbetriebnahmeDatum
instantiates:
- xsd:element
description: Datum der Wiederinbetriebnahme
from_schema: https://example.org/mastr
rank: 1000
owner: Ertuechtigung
domain_of:
- Ertuechtigung
range: datetime

```
</details></div>