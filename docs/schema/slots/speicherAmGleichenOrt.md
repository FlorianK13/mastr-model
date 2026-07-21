---
search:
  boost: 5.0
---

# Slot: speicherAmGleichenOrt 


_Speicher am gleichen Ort_



<div data-search-exclude markdown="1">



URI: [mastr:slot/speicherAmGleichenOrt](https://example.org/mastr/slot/speicherAmGleichenOrt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitSolar](../classes/EinheitSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitSolar](../classes/EinheitSolar.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitSolar](../classes/EinheitSolar.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:speicherAmGleichenOrt |
| native | mastr:speicherAmGleichenOrt |




## LinkML Source

<details>
```yaml
name: speicherAmGleichenOrt
instantiates:
- xsd:element
description: Speicher am gleichen Ort
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitSolar
domain_of:
- EinheitSolar
range: integer

```
</details></div>