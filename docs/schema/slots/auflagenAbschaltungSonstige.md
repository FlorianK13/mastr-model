---
search:
  boost: 5.0
---

# Slot: auflagenAbschaltungSonstige 


_Angabe, ob Auflagen zur Abschaltung auf Grund von sonstigen Gründen bestehen_



<div data-search-exclude markdown="1">



URI: [mastr:slot/auflagenAbschaltungSonstige](https://example.org/mastr/slot/auflagenAbschaltungSonstige)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitWind](../classes/EinheitWind.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitWind](../classes/EinheitWind.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:auflagenAbschaltungSonstige |
| native | mastr:auflagenAbschaltungSonstige |




## LinkML Source

<details>
```yaml
name: auflagenAbschaltungSonstige
instantiates:
- xsd:element
description: Angabe, ob Auflagen zur Abschaltung auf Grund von sonstigen Gründen bestehen
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitWind
domain_of:
- EinheitWind
range: integer

```
</details></div>