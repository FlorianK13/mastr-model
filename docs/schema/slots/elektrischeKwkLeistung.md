---
search:
  boost: 5.0
---

# Slot: elektrischeKwkLeistung 


_Die höchste an den Generatorklemmen abgebbare elektrische Wirkleistung der Anlage_



<div data-search-exclude markdown="1">



URI: [mastr:slot/elektrischeKwkLeistung](https://example.org/mastr/slot/elektrischeKwkLeistung)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnlageKwk](../classes/AnlageKwk.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [AnlageKwk](../classes/AnlageKwk.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnlageKwk](../classes/AnlageKwk.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:elektrischeKwkLeistung |
| native | mastr:elektrischeKwkLeistung |




## LinkML Source

<details>
```yaml
name: elektrischeKwkLeistung
instantiates:
- xsd:element
description: Die höchste an den Generatorklemmen abgebbare elektrische Wirkleistung
  der Anlage
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageKwk
domain_of:
- AnlageKwk
range: float

```
</details></div>