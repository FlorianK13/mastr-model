---
search:
  boost: 5.0
---

# Slot: marktakteurStatus 


_Der Status des Marktakteurs. Katalogkategorie: MarktakteurStatusKatalog_



<div data-search-exclude markdown="1">



URI: [mastr:slot/marktakteurStatus](https://example.org/mastr/slot/marktakteurStatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeloeschterUndDeaktivierterMarktakteur](../classes/GeloeschterUndDeaktivierterMarktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [GeloeschterUndDeaktivierterMarktakteur](../classes/GeloeschterUndDeaktivierterMarktakteur.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeloeschterUndDeaktivierterMarktakteur](../classes/GeloeschterUndDeaktivierterMarktakteur.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:marktakteurStatus |
| native | mastr:marktakteurStatus |




## LinkML Source

<details>
```yaml
name: marktakteurStatus
instantiates:
- xsd:element
description: 'Der Status des Marktakteurs. Katalogkategorie: MarktakteurStatusKatalog'
from_schema: https://example.org/mastr
rank: 1000
owner: GeloeschterUndDeaktivierterMarktakteur
domain_of:
- GeloeschterUndDeaktivierterMarktakteur
range: string

```
</details></div>