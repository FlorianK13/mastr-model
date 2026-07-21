---
search:
  boost: 5.0
---

# Slot: datumBaubeginn 


_Tatsächlicher bzw. geplanter Spatenstich auf der Baustelle_



<div data-search-exclude markdown="1">



URI: [mastr:slot/datumBaubeginn](https://example.org/mastr/slot/datumBaubeginn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
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
| self | mastr:datumBaubeginn |
| native | mastr:datumBaubeginn |




## LinkML Source

<details>
```yaml
name: datumBaubeginn
instantiates:
- xsd:element
description: Tatsächlicher bzw. geplanter Spatenstich auf der Baustelle
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitVerbrennung
domain_of:
- EinheitVerbrennung
range: date

```
</details></div>