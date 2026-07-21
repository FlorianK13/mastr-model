---
search:
  boost: 5.0
---

# Slot: nichtVorhandenInMigriertenEinheiten 


_Angabe über das Nichtvorhandensein in den migrierten Einheiten_



<div data-search-exclude markdown="1">



URI: [mastr:slot/nichtVorhandenInMigriertenEinheiten](https://example.org/mastr/slot/nichtVorhandenInMigriertenEinheiten)
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
| Range | [Integer](../types/Integer.md) |
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
| self | mastr:nichtVorhandenInMigriertenEinheiten |
| native | mastr:nichtVorhandenInMigriertenEinheiten |




## LinkML Source

<details>
```yaml
name: nichtVorhandenInMigriertenEinheiten
instantiates:
- xsd:element
description: Angabe über das Nichtvorhandensein in den migrierten Einheiten
from_schema: https://example.org/mastr
rank: 1000
owner: Einheit
domain_of:
- Einheit
range: integer

```
</details></div>