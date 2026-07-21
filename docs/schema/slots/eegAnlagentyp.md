---
search:
  boost: 5.0
---

# Slot: eegAnlagentyp 


_Typ der Einheit. Katalogkategorie: Einheitentyp_



<div data-search-exclude markdown="1">



URI: [mastr:slot/eegAnlagentyp](https://example.org/mastr/slot/eegAnlagentyp)
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
| self | mastr:eegAnlagentyp |
| native | mastr:eegAnlagentyp |




## LinkML Source

<details>
```yaml
name: eegAnlagentyp
instantiates:
- xsd:element
description: 'Typ der Einheit. Katalogkategorie: Einheitentyp'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitStromSpeicher
domain_of:
- EinheitStromSpeicher
range: integer

```
</details></div>