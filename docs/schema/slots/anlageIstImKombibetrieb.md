---
search:
  boost: 5.0
---

# Slot: anlageIstImKombibetrieb 


_Angabe ob die Stromerzeugungseinheit im Kombibetrieb betrieben wird_



<div data-search-exclude markdown="1">



URI: [mastr:slot/anlageIstImKombibetrieb](https://example.org/mastr/slot/anlageIstImKombibetrieb)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:anlageIstImKombibetrieb |
| native | mastr:anlageIstImKombibetrieb |




## LinkML Source

<details>
```yaml
name: anlageIstImKombibetrieb
instantiates:
- xsd:element
description: Angabe ob die Stromerzeugungseinheit im Kombibetrieb betrieben wird
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitVerbrennung
domain_of:
- EinheitVerbrennung
range: integer

```
</details></div>