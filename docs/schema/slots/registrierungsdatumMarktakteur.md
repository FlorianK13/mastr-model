---
search:
  boost: 5.0
---

# Slot: registrierungsdatumMarktakteur 


_Registrierungsdatum_



<div data-search-exclude markdown="1">



URI: [mastr:slot/registrierungsdatumMarktakteur](https://example.org/mastr/slot/registrierungsdatumMarktakteur)
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
| self | mastr:registrierungsdatumMarktakteur |
| native | mastr:registrierungsdatumMarktakteur |




## LinkML Source

<details>
```yaml
name: registrierungsdatumMarktakteur
instantiates:
- xsd:element
description: Registrierungsdatum
from_schema: https://example.org/mastr
rank: 1000
owner: Marktakteur
domain_of:
- Marktakteur
range: datetime

```
</details></div>