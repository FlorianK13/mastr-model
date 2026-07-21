---
search:
  boost: 5.0
---

# Slot: wasserrechtsNummer 


_Nummer der wasserrechtlichen Genehmigung_



<div data-search-exclude markdown="1">



URI: [mastr:slot/wasserrechtsNummer](https://example.org/mastr/slot/wasserrechtsNummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:wasserrechtsNummer |
| native | mastr:wasserrechtsNummer |




## LinkML Source

<details>
```yaml
name: wasserrechtsNummer
instantiates:
- xsd:element
description: Nummer der wasserrechtlichen Genehmigung
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: string

```
</details></div>