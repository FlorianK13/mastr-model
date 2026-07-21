---
search:
  boost: 5.0
---

# Slot: speichername 


_Name des Gas Speichers_



<div data-search-exclude markdown="1">



URI: [mastr:slot/speichername](https://example.org/mastr/slot/speichername)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageGasSpeicher](../classes/AnlageGasSpeicher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AnlageGasSpeicher](../classes/AnlageGasSpeicher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageGasSpeicher](../classes/AnlageGasSpeicher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:speichername |
| native | mastr:speichername |




## LinkML Source

<details>
```yaml
name: speichername
instantiates:
- xsd:element
description: Name des Gas Speichers
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageGasSpeicher
domain_of:
- AnlageGasSpeicher
range: string

```
</details></div>