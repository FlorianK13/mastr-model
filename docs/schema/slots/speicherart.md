---
search:
  boost: 5.0
---

# Slot: speicherart 


_Art der Gasspeicherung. Katalogkategorie: GasSpeicherart_



<div data-search-exclude markdown="1">



URI: [mastr:slot/speicherart](https://example.org/mastr/slot/speicherart)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGasSpeicher](../classes/EinheitGasSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitGasSpeicher](../classes/EinheitGasSpeicher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitGasSpeicher](../classes/EinheitGasSpeicher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:speicherart |
| native | mastr:speicherart |




## LinkML Source

<details>
```yaml
name: speicherart
instantiates:
- xsd:element
description: 'Art der Gasspeicherung. Katalogkategorie: GasSpeicherart'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGasSpeicher
domain_of:
- EinheitGasSpeicher
range: integer

```
</details></div>