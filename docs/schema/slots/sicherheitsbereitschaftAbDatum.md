---
search:
  boost: 5.0
---

# Slot: sicherheitsbereitschaftAbDatum 


_Datum des Übergangs in die Sicherheitsbereitschaft_



<div data-search-exclude markdown="1">



URI: [mastr:slot/sicherheitsbereitschaftAbDatum](https://example.org/mastr/slot/sicherheitsbereitschaftAbDatum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
| Domain Of | [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:sicherheitsbereitschaftAbDatum |
| native | mastr:sicherheitsbereitschaftAbDatum |




## LinkML Source

<details>
```yaml
name: sicherheitsbereitschaftAbDatum
instantiates:
- xsd:element
description: Datum des Übergangs in die Sicherheitsbereitschaft
from_schema: https://example.org/mastr
rank: 1000
owner: EinheitVerbrennung
domain_of:
- EinheitVerbrennung
range: date

```
</details></div>