---
search:
  boost: 5.0
---

# Slot: pumpbetriebLeistungsaufnahme 


_Höchste elektrische Dauerleistung, die dem Netz für den Pumpbetrieb unter Nennbedingungen entnommen werden kann_



<div data-search-exclude markdown="1">



URI: [mastr:slot/pumpbetriebLeistungsaufnahme](https://example.org/mastr/slot/pumpbetriebLeistungsaufnahme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
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
| self | mastr:pumpbetriebLeistungsaufnahme |
| native | mastr:pumpbetriebLeistungsaufnahme |




## LinkML Source

<details>
```yaml
name: pumpbetriebLeistungsaufnahme
instantiates:
- xsd:element
description: Höchste elektrische Dauerleistung, die dem Netz für den Pumpbetrieb unter
  Nennbedingungen entnommen werden kann
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitStromSpeicher
domain_of:
- EinheitStromSpeicher
range: float

```
</details></div>