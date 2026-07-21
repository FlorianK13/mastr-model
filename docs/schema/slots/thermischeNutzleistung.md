---
search:
  boost: 5.0
---

# Slot: thermischeNutzleistung 


_Die höchste Nutzwärmeerzeugung unter Nennbedingungen, die die KWKG-Anlage abgeben kann._



<div data-search-exclude markdown="1">



URI: [mastr:slot/thermischeNutzleistung](https://example.org/mastr/slot/thermischeNutzleistung)
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
| self | mastr:thermischeNutzleistung |
| native | mastr:thermischeNutzleistung |




## LinkML Source

<details>
```yaml
name: thermischeNutzleistung
instantiates:
- xsd:element
description: Die höchste Nutzwärmeerzeugung unter Nennbedingungen, die die KWKG-Anlage
  abgeben kann.
from_schema: https://example.org/mastr
rank: 1000
owner: AnlageKwk
domain_of:
- AnlageKwk
range: float

```
</details></div>