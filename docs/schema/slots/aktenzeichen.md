---
search:
  boost: 5.0
---

# Slot: aktenzeichen 


_Aktenzeichen der Genehmigung, welche die Genehmigungsbehörde vergeben hat_



<div data-search-exclude markdown="1">



URI: [mastr:slot/aktenzeichen](https://example.org/mastr/slot/aktenzeichen)
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
| self | mastr:aktenzeichen |
| native | mastr:aktenzeichen |




## LinkML Source

<details>
```yaml
name: aktenzeichen
instantiates:
- xsd:element
description: Aktenzeichen der Genehmigung, welche die Genehmigungsbehörde vergeben
  hat
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitGenehmigung
domain_of:
- EinheitGenehmigung
range: string

```
</details></div>