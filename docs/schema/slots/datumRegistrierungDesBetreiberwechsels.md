---
search:
  boost: 5.0
---

# Slot: datumRegistrierungDesBetreiberwechsels 


_Datum der Registrierung des Betreiberwechsels_



<div data-search-exclude markdown="1">



URI: [mastr:slot/datumRegistrierungDesBetreiberwechsels](https://example.org/mastr/slot/datumRegistrierungDesBetreiberwechsels)
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
| Range | [Date](../types/Date.md) |
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
| self | mastr:datumRegistrierungDesBetreiberwechsels |
| native | mastr:datumRegistrierungDesBetreiberwechsels |




## LinkML Source

<details>
```yaml
name: datumRegistrierungDesBetreiberwechsels
instantiates:
- xsd:element
description: Datum der Registrierung des Betreiberwechsels
from_schema: https://example.org/mastr
rank: 1000
owner: Einheit
domain_of:
- Einheit
range: date

```
</details></div>