---
search:
  boost: 5.0
---

# Slot: netzMaStRNummer 


_MaStR-Nummer des Netzes an dem der Netzanschlusspunkt angeschlossen ist_



<div data-search-exclude markdown="1">



URI: [mastr:slot/netzMaStRNummer](https://example.org/mastr/slot/netzMaStRNummer)
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
| self | mastr:netzMaStRNummer |
| native | mastr:netzMaStRNummer |




## LinkML Source

<details>
```yaml
name: netzMaStRNummer
instantiates:
- xsd:element
description: MaStR-Nummer des Netzes an dem der Netzanschlusspunkt angeschlossen ist
from_schema: https://example.org/mastr
rank: 1000
owner: Netzanschlusspunkt
domain_of:
- Netzanschlusspunkt
range: string

```
</details></div>