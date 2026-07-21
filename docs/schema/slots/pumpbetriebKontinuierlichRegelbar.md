---
search:
  boost: 5.0
---

# Slot: pumpbetriebKontinuierlichRegelbar 


_Die Wasserkraftanlage ist im Pumpbetrieb kontinuierlich regelbar_



<div data-search-exclude markdown="1">



URI: [mastr:slot/pumpbetriebKontinuierlichRegelbar](https://example.org/mastr/slot/pumpbetriebKontinuierlichRegelbar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:pumpbetriebKontinuierlichRegelbar |
| native | mastr:pumpbetriebKontinuierlichRegelbar |




## LinkML Source

<details>
```yaml
name: pumpbetriebKontinuierlichRegelbar
instantiates:
- xsd:element
description: Die Wasserkraftanlage ist im Pumpbetrieb kontinuierlich regelbar
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitStromSpeicher
domain_of:
- EinheitStromSpeicher
range: integer

```
</details></div>