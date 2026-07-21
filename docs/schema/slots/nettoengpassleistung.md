---
search:
  boost: 5.0
---

# Slot: nettoengpassleistung 


_Erzielbare Dauerleistung der Erzeugungseinheiten am jeweiligen Netzanschlusspunkt_



<div data-search-exclude markdown="1">



URI: [mastr:slot/nettoengpassleistung](https://example.org/mastr/slot/nettoengpassleistung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Netzanschlusspunkt](../classes/Netzanschlusspunkt.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [Netzanschlusspunkt](../classes/Netzanschlusspunkt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Netzanschlusspunkt](../classes/Netzanschlusspunkt.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:nettoengpassleistung |
| native | mastr:nettoengpassleistung |




## LinkML Source

<details>
```yaml
name: nettoengpassleistung
instantiates:
- xsd:element
description: Erzielbare Dauerleistung der Erzeugungseinheiten am jeweiligen Netzanschlusspunkt
from_schema: https://example.org/mastr
rank: 1000
owner: Netzanschlusspunkt
domain_of:
- Netzanschlusspunkt
range: float

```
</details></div>