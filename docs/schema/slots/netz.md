---
search:
  boost: 5.0
---

# Slot: netz 


_Netz des Netzbetreibers (nur bei Netzbetreibern)_



<div data-search-exclude markdown="1">



URI: [mastr:slot/netz](https://example.org/mastr/slot/netz)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marktakteur](../classes/Marktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Marktakteur](../classes/Marktakteur.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Marktakteur](../classes/Marktakteur.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:netz |
| native | mastr:netz |




## LinkML Source

<details>
```yaml
name: netz
instantiates:
- xsd:element
description: Netz des Netzbetreibers (nur bei Netzbetreibern)
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>