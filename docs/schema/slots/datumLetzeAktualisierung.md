---
search:
  boost: 5.0
---

# Slot: datumLetzeAktualisierung 

<div data-search-exclude markdown="1">



URI: [mastr:slot/datumLetzeAktualisierung](https://example.org/mastr/slot/datumLetzeAktualisierung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marktakteur](../classes/Marktakteur.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](../types/Datetime.md) |
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
| self | mastr:datumLetzeAktualisierung |
| native | mastr:datumLetzeAktualisierung |




## LinkML Source

<details>
```yaml
name: datumLetzeAktualisierung
instantiates:
- xsd:element
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: datetime

```
</details></div>