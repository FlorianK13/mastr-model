---
search:
  boost: 5.0
---

# Slot: messlokation 


_Messlokation gemäß Metering Code, VDE-AR-N 4400_



<div data-search-exclude markdown="1">



URI: [mastr:slot/messlokation](https://example.org/mastr/slot/messlokation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Netzanschlusspunkt](../classes/Netzanschlusspunkt.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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
| self | mastr:messlokation |
| native | mastr:messlokation |




## LinkML Source

<details>
```yaml
name: messlokation
instantiates:
- xsd:element
description: Messlokation gemäß Metering Code, VDE-AR-N 4400
from_schema: https://example.org/mastr
rank: 1000
owner: Netzanschlusspunkt
domain_of:
- Netzanschlusspunkt
range: string

```
</details></div>