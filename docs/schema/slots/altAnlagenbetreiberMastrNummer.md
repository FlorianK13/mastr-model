---
search:
  boost: 5.0
---

# Slot: altAnlagenbetreiberMastrNummer 


_MaStR-Nummer des ehemaligen Betreibers der Einheit, wenn ein Betreiberwechsel durchgeführt wurde_



<div data-search-exclude markdown="1">



URI: [mastr:slot/altAnlagenbetreiberMastrNummer](https://example.org/mastr/slot/altAnlagenbetreiberMastrNummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Einheit](../classes/Einheit.md) | Gemeinsame Attribute der Einheit-Klassen |  no  |
| [EinheitBiomasse](../classes/EinheitBiomasse.md) |  |  no  |
| [EinheitGasErzeuger](../classes/EinheitGasErzeuger.md) |  |  no  |
| [EinheitGasSpeicher](../classes/EinheitGasSpeicher.md) |  |  no  |
| [EinheitGasverbraucher](../classes/EinheitGasverbraucher.md) |  |  no  |
| [EinheitGeothermieGrubengasDruckentspannung](../classes/EinheitGeothermieGrubengasDruckentspannung.md) |  |  no  |
| [EinheitKernkraft](../classes/EinheitKernkraft.md) |  |  no  |
| [EinheitSolar](../classes/EinheitSolar.md) |  |  no  |
| [EinheitStromSpeicher](../classes/EinheitStromSpeicher.md) |  |  no  |
| [EinheitStromVerbraucher](../classes/EinheitStromVerbraucher.md) |  |  no  |
| [EinheitVerbrennung](../classes/EinheitVerbrennung.md) |  |  no  |
| [EinheitWasser](../classes/EinheitWasser.md) |  |  no  |
| [EinheitWind](../classes/EinheitWind.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Einheit](../classes/Einheit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Einheit](../classes/Einheit.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:altAnlagenbetreiberMastrNummer |
| native | mastr:altAnlagenbetreiberMastrNummer |




## LinkML Source

<details>
```yaml
name: altAnlagenbetreiberMastrNummer
instantiates:
- xsd:element
description: MaStR-Nummer des ehemaligen Betreibers der Einheit, wenn ein Betreiberwechsel
  durchgeführt wurde
from_schema: https://example.org/mastr
rank: 1000
owner: Einheit
domain_of:
- Einheit
range: string

```
</details></div>