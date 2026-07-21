---
search:
  boost: 5.0
---

# Slot: maximaleAusspeiseleistung 


_Technisch maximale Ausspeiseleistung am jeweiligen Netzanschlusspunkt (nur bei Gasverbrauchern)_



<div data-search-exclude markdown="1">



URI: [mastr:slot/maximaleAusspeiseleistung](https://example.org/mastr/slot/maximaleAusspeiseleistung)
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
| self | mastr:maximaleAusspeiseleistung |
| native | mastr:maximaleAusspeiseleistung |




## LinkML Source

<details>
```yaml
name: maximaleAusspeiseleistung
instantiates:
- xsd:element
description: Technisch maximale Ausspeiseleistung am jeweiligen Netzanschlusspunkt
  (nur bei Gasverbrauchern)
from_schema: https://example.org/mastr
rank: 1000
owner: Netzanschlusspunkt
domain_of:
- Netzanschlusspunkt
range: float

```
</details></div>