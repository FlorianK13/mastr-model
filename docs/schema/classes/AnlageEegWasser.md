---
search:
  boost: 10.0
---

# Class: AnlageEegWasser 

<div data-search-exclude markdown="1">



URI: [mastr:class/AnlageEegWasser](https://example.org/mastr/class/AnlageEegWasser)





```mermaid
 classDiagram
    class AnlageEegWasser
    click AnlageEegWasser href "../../classes/AnlageEegWasser/"
      Anlage <|-- AnlageEegWasser
        click Anlage href "../../classes/Anlage/"
      
      AnlageEegWasser : anlageBetriebsstatus
        
      AnlageEegWasser : anlagenkennzifferAnlagenregister
        
      AnlageEegWasser : anlagenkennzifferAnlagenregisterNv
        
      AnlageEegWasser : anlagenschluesselEeg
        
      AnlageEegWasser : datumLetzteAktualisierung
        
      AnlageEegWasser : eegInbetriebnahmedatum
        
      AnlageEegWasser : eegMaStRNummer
        
      AnlageEegWasser : ertuechtigungIds
        
      AnlageEegWasser : installierteLeistung
        
      AnlageEegWasser : registrierungsdatum
        
      AnlageEegWasser : verknuepfteEinheitenMaStRNummern
        
      
```





## Inheritance
* [Anlage](../classes/Anlage.md)
    * **AnlageEegWasser**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [eegInbetriebnahmedatum](../slots/eegInbetriebnahmedatum.md) | 0..1 <br/> [Date](../types/Date.md) | Inbetriebnahmedatum der EEG-Anlage | direct |
| [eegMaStRNummer](../slots/eegMaStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der Anlage | direct |
| [anlagenschluesselEeg](../slots/anlagenschluesselEeg.md) | 0..1 <br/> [String](../types/String.md) | Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage | direct |
| [anlagenkennzifferAnlagenregister](../slots/anlagenkennzifferAnlagenregister.md) | 0..1 <br/> [String](../types/String.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [anlagenkennzifferAnlagenregisterNv](../slots/anlagenkennzifferAnlagenregisterNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [installierteLeistung](../slots/installierteLeistung.md) | 0..1 <br/> [Float](../types/Float.md) | Installierte Nettonennleistung der EEG-Anlage | direct |
| [anlageBetriebsstatus](../slots/anlageBetriebsstatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten ergibt | direct |
| [ertuechtigungIds](../slots/ertuechtigungIds.md) | 0..1 <br/> [String](../types/String.md) | Ertüchtigungen | direct |
| [registrierungsdatum](../slots/registrierungsdatum.md) | 0..1 <br/> [Date](../types/Date.md) | Registrierungsdatum der EEG- Anlage | [Anlage](../classes/Anlage.md) |
| [datumLetzteAktualisierung](../slots/datumLetzteAktualisierung.md) | 0..1 <br/> [Datetime](../types/Datetime.md) | Datum der letzten Aktualisierung an diesem Objekt | [Anlage](../classes/Anlage.md) |
| [verknuepfteEinheitenMaStRNummern](../slots/verknuepfteEinheitenMaStRNummern.md) | 0..1 <br/> [String](../types/String.md) | Liste von MaStR Nummern mit den verknüpften Stromerzeugern | [Anlage](../classes/Anlage.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:AnlageEegWasser |
| native | mastr:AnlageEegWasser |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnlageEegWasser
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG-Anlage
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    range: date
  eegMaStRNummer:
    name: eegMaStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der Anlage
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitWasser
    - EinheitWind
    range: string
  anlagenschluesselEeg:
    name: anlagenschluesselEeg
    instantiates:
    - xsd:element
    description: Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    range: string
  anlagenkennzifferAnlagenregister:
    name: anlagenkennzifferAnlagenregister
    instantiates:
    - xsd:element
    description: Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: string
  anlagenkennzifferAnlagenregisterNv:
    name: anlagenkennzifferAnlagenregisterNv
    instantiates:
    - xsd:element
    description: Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister.
      Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: integer
  installierteLeistung:
    name: installierteLeistung
    instantiates:
    - xsd:element
    description: Installierte Nettonennleistung der EEG-Anlage
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: float
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebsstatus'
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
  ertuechtigungIds:
    name: ertuechtigungIds
    instantiates:
    - xsd:element
    description: Ertüchtigungen
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegWasser
    range: string

```
</details>

### Induced

<details>
```yaml
name: AnlageEegWasser
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG-Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    range: date
  eegMaStRNummer:
    name: eegMaStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitWasser
    - EinheitWind
    range: string
  anlagenschluesselEeg:
    name: anlagenschluesselEeg
    instantiates:
    - xsd:element
    description: Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWasser
    - AnlageEegWind
    range: string
  anlagenkennzifferAnlagenregister:
    name: anlagenkennzifferAnlagenregister
    instantiates:
    - xsd:element
    description: Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: string
  anlagenkennzifferAnlagenregisterNv:
    name: anlagenkennzifferAnlagenregisterNv
    instantiates:
    - xsd:element
    description: Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister.
      Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: integer
  installierteLeistung:
    name: installierteLeistung
    instantiates:
    - xsd:element
    description: Installierte Nettonennleistung der EEG-Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: float
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebsstatus'
    from_schema: https://example.org/mastr
    owner: AnlageEegWasser
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
  ertuechtigungIds:
    name: ertuechtigungIds
    instantiates:
    - xsd:element
    description: Ertüchtigungen
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegWasser
    domain_of:
    - AnlageEegWasser
    range: string
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum der EEG- Anlage
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegWasser
    domain_of:
    - Anlage
    - AnlageEegSpeicher
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    - Einheit
    - EinheitGenehmigung
    range: date
  datumLetzteAktualisierung:
    name: datumLetzteAktualisierung
    instantiates:
    - xsd:element
    description: Datum der letzten Aktualisierung an diesem Objekt
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegWasser
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
    owner: AnlageEegWasser
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string

```
</details></div>