---
search:
  boost: 5.0
---

# Slot: nutzbareSpeicherkapazitaet 


_Nutzbare Speicherkapazität in kWh_



<div data-search-exclude markdown="1">



URI: [mastr:slot/nutzbareSpeicherkapazitaet](https://example.org/mastr/slot/nutzbareSpeicherkapazitaet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageStromSpeicher](../classes/AnlageStromSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [AnlageStromSpeicher](../classes/AnlageStromSpeicher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageStromSpeicher](../classes/AnlageStromSpeicher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:nutzbareSpeicherkapazitaet |
| native | mastr:nutzbareSpeicherkapazitaet |




## LinkML Source

<details>
```yaml
name: nutzbareSpeicherkapazitaet
instantiates:
- xsd:element
description: Nutzbare Speicherkapazität in kWh
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageStromSpeicher
domain_of:
- AnlageStromSpeicher
range: float

```
</details></div>