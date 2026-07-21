---
search:
  boost: 5.0
---

# Slot: kundenAngeschlossen 


_Sind Kunden angeschlossen_



<div data-search-exclude markdown="1">



URI: [mastr:slot/kundenAngeschlossen](https://example.org/mastr/slot/kundenAngeschlossen)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Netz](../classes/Netz.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [Netz](../classes/Netz.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Netz](../classes/Netz.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:kundenAngeschlossen |
| native | mastr:kundenAngeschlossen |




## LinkML Source

<details>
```yaml
name: kundenAngeschlossen
instantiates:
- xsd:element
description: Sind Kunden angeschlossen
from_schema: https://example.org/mastr
rank: 1000
owner: Netz
domain_of:
- Netz
range: integer

```
</details></div>