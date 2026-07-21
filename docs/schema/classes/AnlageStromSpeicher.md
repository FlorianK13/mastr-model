---
search:
  boost: 10.0
---

# Class: AnlageStromSpeicher 

<div data-search-exclude markdown="1">



URI: [mastr:class/AnlageStromSpeicher](https://example.org/mastr/class/AnlageStromSpeicher)





```mermaid
 classDiagram
    class AnlageStromSpeicher
    click AnlageStromSpeicher href "../../classes/AnlageStromSpeicher/"
      Anlage <|-- AnlageStromSpeicher
        click Anlage href "../../classes/Anlage/"
      
      AnlageStromSpeicher : anlageBetriebsstatus
        
      AnlageStromSpeicher : datumLetzteAktualisierung
        
      AnlageStromSpeicher : maStRNummer
        
      AnlageStromSpeicher : nutzbareSpeicherkapazitaet
        
      AnlageStromSpeicher : registrierungsdatum
        
      AnlageStromSpeicher : verknuepfteEinheitenMaStRNummern
        
      
```





## Inheritance
* [Anlage](../classes/Anlage.md)
    * **AnlageStromSpeicher**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [maStRNummer](../slots/maStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer des Strom Speichers | direct |
| [registrierungsdatum](../slots/registrierungsdatum.md) | 0..1 <br/> [Date](../types/Date.md) | Registrierungsdatum des Speichers | direct |
| [nutzbareSpeicherkapazitaet](../slots/nutzbareSpeicherkapazitaet.md) | 0..1 <br/> [Float](../types/Float.md) | Nutzbare Speicherkapazität in kWh | direct |
| [anlageBetriebsstatus](../slots/anlageBetriebsstatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten ergibt | direct |
| [datumLetzteAktualisierung](../slots/datumLetzteAktualisierung.md) | 0..1 <br/> [Datetime](../types/Datetime.md) | Datum der letzten Aktualisierung an diesem Objekt | [Anlage](../classes/Anlage.md) |
| [verknuepfteEinheitenMaStRNummern](../slots/verknuepfteEinheitenMaStRNummern.md) | 0..1 <br/> [String](../types/String.md) | Liste von MaStR Nummern mit den verknüpften Stromerzeugern | [Anlage](../classes/Anlage.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:AnlageStromSpeicher |
| native | mastr:AnlageStromSpeicher |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnlageStromSpeicher
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  maStRNummer:
    name: maStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer des Strom Speichers
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageGasSpeicher
    - AnlageStromSpeicher
    range: string
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum des Speichers
    from_schema: https://example.org/mastr
    domain_of:
    - Anlage
    - AnlageEegSpeicher
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    - Einheit
    - EinheitGenehmigung
    range: date
  nutzbareSpeicherkapazitaet:
    name: nutzbareSpeicherkapazitaet
    instantiates:
    - xsd:element
    description: Nutzbare Speicherkapazität in kWh
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageStromSpeicher
    range: float
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebstatus'
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    range: integer

```
</details>

### Induced

<details>
```yaml
name: AnlageStromSpeicher
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  maStRNummer:
    name: maStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer des Strom Speichers
    from_schema: https://example.org/mastr
    owner: AnlageStromSpeicher
    domain_of:
    - AnlageGasSpeicher
    - AnlageStromSpeicher
    range: string
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum des Speichers
    from_schema: https://example.org/mastr
    owner: AnlageStromSpeicher
    domain_of:
    - Anlage
    - AnlageEegSpeicher
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    - Einheit
    - EinheitGenehmigung
    range: date
  nutzbareSpeicherkapazitaet:
    name: nutzbareSpeicherkapazitaet
    instantiates:
    - xsd:element
    description: Nutzbare Speicherkapazität in kWh
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageStromSpeicher
    domain_of:
    - AnlageStromSpeicher
    range: float
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebstatus'
    from_schema: https://example.org/mastr
    owner: AnlageStromSpeicher
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    range: integer
  datumLetzteAktualisierung:
    name: datumLetzteAktualisierung
    instantiates:
    - xsd:element
    description: Datum der letzten Aktualisierung an diesem Objekt
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageStromSpeicher
    domain_of:
    - Anlage
    - Einheit
    - EinheitGenehmigung
    - Ertuechtigung
    - GeloeschteUndDeaktivierteEinheit
    - GeloeschterUndDeaktivierterMarktakteur
    - Lokation
    - MarktakteurUndRolle
    - Netz
    range: datetime
  verknuepfteEinheitenMaStRNummern:
    name: verknuepfteEinheitenMaStRNummern
    instantiates:
    - xsd:element
    description: Liste von MaStR Nummern mit den verknüpften Stromerzeugern
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageStromSpeicher
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string

```
</details></div>