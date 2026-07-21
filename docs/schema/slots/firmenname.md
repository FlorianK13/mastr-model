---
search:
  boost: 5.0
---

# Slot: firmenname 


_Name der Firma mit dem rechtsformergänzenden Namenszusatz_



<div data-search-exclude markdown="1">



URI: [mastr:slot/firmenname](https://example.org/mastr/slot/firmenname)
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
| self | mastr:firmenname |
| native | mastr:firmenname |




## LinkML Source

<details>
```yaml
name: firmenname
instantiates:
- xsd:element
description: Name der Firma mit dem rechtsformergänzenden Namenszusatz
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: string

```
</details></div>