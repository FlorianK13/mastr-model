---
search:
  boost: 5.0
---

# Slot: art 


_Art der Genehmigung. Katalogkategorie: GenehmigungsArt_



<div data-search-exclude markdown="1">



URI: [mastr:slot/art](https://example.org/mastr/slot/art)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitGenehmigung](../classes/EinheitGenehmigung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:art |
| native | mastr:art |




## LinkML Source

<details>
```yaml
name: art
instantiates:
- xsd:element
description: 'Art der Genehmigung. Katalogkategorie: GenehmigungsArt'
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: integer

```
</details></div>