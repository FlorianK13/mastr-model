---
search:
  boost: 5.0
---

# Slot: behoerde 


_Behörde, die Genehmigung ausgestellt hat_



<div data-search-exclude markdown="1">



URI: [mastr:slot/behoerde](https://example.org/mastr/slot/behoerde)
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
| self | mastr:behoerde |
| native | mastr:behoerde |




## LinkML Source

<details>
```yaml
name: behoerde
instantiates:
- xsd:element
description: Behörde, die Genehmigung ausgestellt hat
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: string

```
</details></div>