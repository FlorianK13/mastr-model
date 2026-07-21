---
search:
  boost: 5.0
---

# Slot: mieterstromMeldedatum 

<div data-search-exclude markdown="1">



URI: [mastr:slot/mieterstromMeldedatum](https://example.org/mastr/slot/mieterstromMeldedatum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageEegSolar](../classes/AnlageEegSolar.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
| Domain Of | [AnlageEegSolar](../classes/AnlageEegSolar.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageEegSolar](../classes/AnlageEegSolar.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:mieterstromMeldedatum |
| native | mastr:mieterstromMeldedatum |




## LinkML Source

<details>
```yaml
name: mieterstromMeldedatum
instantiates:
- xsd:element
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageEegSolar
domain_of:
- AnlageEegSolar
range: date

```
</details></div>