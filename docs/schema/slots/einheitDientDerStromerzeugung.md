---
search:
  boost: 5.0
---

# Slot: einheitDientDerStromerzeugung 


_Angabe ob die Gasverbrauchseinheit zur Stromerzeugung dient (Gaskraftwerk)_



<div data-search-exclude markdown="1">



URI: [mastr:slot/einheitDientDerStromerzeugung](https://example.org/mastr/slot/einheitDientDerStromerzeugung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGasverbraucher](../classes/EinheitGasverbraucher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitGasverbraucher](../classes/EinheitGasverbraucher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitGasverbraucher](../classes/EinheitGasverbraucher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:einheitDientDerStromerzeugung |
| native | mastr:einheitDientDerStromerzeugung |




## LinkML Source

<details>
```yaml
name: einheitDientDerStromerzeugung
instantiates:
- xsd:element
description: Angabe ob die Gasverbrauchseinheit zur Stromerzeugung dient (Gaskraftwerk)
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGasverbraucher
domain_of:
- EinheitGasverbraucher
range: integer

```
</details></div>