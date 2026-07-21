---
search:
  boost: 5.0
---

# Slot: nameStromverbrauchseinheit 


_Vom Betreiber frei wählbare Bezeichnung der Stromverbrauchseinheit._



<div data-search-exclude markdown="1">



URI: [mastr:slot/nameStromverbrauchseinheit](https://example.org/mastr/slot/nameStromverbrauchseinheit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitStromVerbraucher](../classes/EinheitStromVerbraucher.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [EinheitStromVerbraucher](../classes/EinheitStromVerbraucher.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitStromVerbraucher](../classes/EinheitStromVerbraucher.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:nameStromverbrauchseinheit |
| native | mastr:nameStromverbrauchseinheit |




## LinkML Source

<details>
```yaml
name: nameStromverbrauchseinheit
instantiates:
- xsd:element
description: Vom Betreiber frei wählbare Bezeichnung der Stromverbrauchseinheit.
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitStromVerbraucher
domain_of:
- EinheitStromVerbraucher
range: string

```
</details></div>