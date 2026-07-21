---
search:
  boost: 10.0
---

# Class: AnlageEegSolar 

<div data-search-exclude markdown="1">



URI: [mastr:class/AnlageEegSolar](https://example.org/mastr/class/AnlageEegSolar)





```mermaid
 classDiagram
    class AnlageEegSolar
    click AnlageEegSolar href "../../classes/AnlageEegSolar/"
      Anlage <|-- AnlageEegSolar
        click Anlage href "../../classes/Anlage/"
      
      AnlageEegSolar : anlageBetriebsstatus
        
      AnlageEegSolar : anlagenkennzifferAnlagenregister
        
      AnlageEegSolar : anlagenkennzifferAnlagenregisterNv
        
      AnlageEegSolar : anlagenschluesselEeg
        
      AnlageEegSolar : ausschreibungZuschlag
        
      AnlageEegSolar : datumLetzteAktualisierung
        
      AnlageEegSolar : eegInbetriebnahmedatum
        
      AnlageEegSolar : eegMaStRNummer
        
      AnlageEegSolar : inanspruchnahmeZahlungNachEeg
        
      AnlageEegSolar : installierteLeistung
        
      AnlageEegSolar : mieterstromErsteZuordnungZuschlag
        
      AnlageEegSolar : mieterstromMeldedatum
        
      AnlageEegSolar : mieterstromZugeordnet
        
      AnlageEegSolar : registrierungsdatum
        
      AnlageEegSolar : registrierungsnummerPvMeldeportal
        
      AnlageEegSolar : registrierungsnummerPvMeldeportalNv
        
      AnlageEegSolar : verknuepfteEinheitenMaStRNummern
        
      AnlageEegSolar : zugeordneteGebotsmenge
        
      AnlageEegSolar : zuschlagsnummer
        
      
```





## Inheritance
* [Anlage](../classes/Anlage.md)
    * **AnlageEegSolar**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [eegInbetriebnahmedatum](../slots/eegInbetriebnahmedatum.md) | 0..1 <br/> [Date](../types/Date.md) | Inbetriebnahmedatum der EEG- Anlage | direct |
| [eegMaStRNummer](../slots/eegMaStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der Anlage | direct |
| [inanspruchnahmeZahlungNachEeg](../slots/inanspruchnahmeZahlungNachEeg.md) | 0..1 <br/> [Integer](../types/Integer.md) | Werden oder wurden für die Solaranlage Zahlungen des Netzbetreibers in Anspru... | direct |
| [anlagenschluesselEeg](../slots/anlagenschluesselEeg.md) | 0..1 <br/> [String](../types/String.md) | Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage | direct |
| [anlagenkennzifferAnlagenregister](../slots/anlagenkennzifferAnlagenregister.md) | 0..1 <br/> [String](../types/String.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [anlagenkennzifferAnlagenregisterNv](../slots/anlagenkennzifferAnlagenregisterNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [installierteLeistung](../slots/installierteLeistung.md) | 0..1 <br/> [Float](../types/Float.md) | Installierte Nettonennleistung der EEG-Anlage | direct |
| [registrierungsnummerPvMeldeportal](../slots/registrierungsnummerPvMeldeportal.md) | 0..1 <br/> [String](../types/String.md) | Durch die Bundesagentur vergeben Nummer bei der Registrierung im PV- Meldepor... | direct |
| [registrierungsnummerPvMeldeportalNv](../slots/registrierungsnummerPvMeldeportalNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Durch die Bundesagentur vergeben Nummer bei der Registrierung im PV- Meldepor... | direct |
| [mieterstromZugeordnet](../slots/mieterstromZugeordnet.md) | 0..1 <br/> [Integer](../types/Integer.md) | Gibt an, ob die Solaranlage der Veräußerungsform des Mieterstromzuschlags zug... | direct |
| [mieterstromMeldedatum](../slots/mieterstromMeldedatum.md) | 0..1 <br/> [Date](../types/Date.md) |  | direct |
| [mieterstromErsteZuordnungZuschlag](../slots/mieterstromErsteZuordnungZuschlag.md) | 0..1 <br/> [Date](../types/Date.md) | Datum, an dem die Anlage erstmalig der Veräußerungsform des Mieterstromzuschl... | direct |
| [ausschreibungZuschlag](../slots/ausschreibungZuschlag.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren der Bundes... | direct |
| [zugeordneteGebotsmenge](../slots/zugeordneteGebotsmenge.md) | 0..1 <br/> [Float](../types/Float.md) | Bezuschlagte Gebotsmenge, die der EEG-Anlage zugeordnet wurde | direct |
| [zuschlagsnummer](../slots/zuschlagsnummer.md) | 0..1 <br/> [String](../types/String.md) | Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens vergebene Nu... | direct |
| [anlageBetriebsstatus](../slots/anlageBetriebsstatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten ergibt | direct |
| [registrierungsdatum](../slots/registrierungsdatum.md) | 0..1 <br/> [Date](../types/Date.md) | Registrierungsdatum der EEG- Anlage | [Anlage](../classes/Anlage.md) |
| [datumLetzteAktualisierung](../slots/datumLetzteAktualisierung.md) | 0..1 <br/> [Datetime](../types/Datetime.md) | Datum der letzten Aktualisierung an diesem Objekt | [Anlage](../classes/Anlage.md) |
| [verknuepfteEinheitenMaStRNummern](../slots/verknuepfteEinheitenMaStRNummern.md) | 0..1 <br/> [String](../types/String.md) | Liste von MaStR Nummern mit den verknüpften Stromerzeugern | [Anlage](../classes/Anlage.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:AnlageEegSolar |
| native | mastr:AnlageEegSolar |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnlageEegSolar
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG- Anlage
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
  inanspruchnahmeZahlungNachEeg:
    name: inanspruchnahmeZahlungNachEeg
    instantiates:
    - xsd:element
    description: Werden oder wurden für die Solaranlage Zahlungen des Netzbetreibers
      in Anspruch genommen?
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: integer
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
  registrierungsnummerPvMeldeportal:
    name: registrierungsnummerPvMeldeportal
    instantiates:
    - xsd:element
    description: Durch die Bundesagentur vergeben Nummer bei der Registrierung im
      PV- Meldeportal
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: string
  registrierungsnummerPvMeldeportalNv:
    name: registrierungsnummerPvMeldeportalNv
    instantiates:
    - xsd:element
    description: Durch die Bundesagentur vergeben Nummer bei der Registrierung im
      PV- Meldeportal. Nicht-vorhanden Flag
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: integer
  mieterstromZugeordnet:
    name: mieterstromZugeordnet
    instantiates:
    - xsd:element
    description: Gibt an, ob die Solaranlage der Veräußerungsform des Mieterstromzuschlags
      zugeordnet wurde
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: integer
  mieterstromMeldedatum:
    name: mieterstromMeldedatum
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: date
  mieterstromErsteZuordnungZuschlag:
    name: mieterstromErsteZuordnungZuschlag
    instantiates:
    - xsd:element
    description: Datum, an dem die Anlage erstmalig der Veräußerungsform des Mieterstromzuschlags
      zugeordnet worden ist.
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: date
  ausschreibungZuschlag:
    name: ausschreibungZuschlag
    instantiates:
    - xsd:element
    description: Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren
      der Bundesnetzagentur ein Zuschlag erlangt wurde
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    - AnlageKwk
    range: integer
  zugeordneteGebotsmenge:
    name: zugeordneteGebotsmenge
    instantiates:
    - xsd:element
    description: Bezuschlagte Gebotsmenge, die der EEG-Anlage zugeordnet wurde
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegSolar
    range: float
  zuschlagsnummer:
    name: zuschlagsnummer
    instantiates:
    - xsd:element
    description: Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens
      vergebene Nummern (Mehrfachnennung möglich)
    from_schema: https://example.org/mastr
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    range: string
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

```
</details>

### Induced

<details>
```yaml
name: AnlageEegSolar
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG- Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
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
  inanspruchnahmeZahlungNachEeg:
    name: inanspruchnahmeZahlungNachEeg
    instantiates:
    - xsd:element
    description: Werden oder wurden für die Solaranlage Zahlungen des Netzbetreibers
      in Anspruch genommen?
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: integer
  anlagenschluesselEeg:
    name: anlagenschluesselEeg
    instantiates:
    - xsd:element
    description: Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage
    from_schema: https://example.org/mastr
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: float
  registrierungsnummerPvMeldeportal:
    name: registrierungsnummerPvMeldeportal
    instantiates:
    - xsd:element
    description: Durch die Bundesagentur vergeben Nummer bei der Registrierung im
      PV- Meldeportal
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: string
  registrierungsnummerPvMeldeportalNv:
    name: registrierungsnummerPvMeldeportalNv
    instantiates:
    - xsd:element
    description: Durch die Bundesagentur vergeben Nummer bei der Registrierung im
      PV- Meldeportal. Nicht-vorhanden Flag
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: integer
  mieterstromZugeordnet:
    name: mieterstromZugeordnet
    instantiates:
    - xsd:element
    description: Gibt an, ob die Solaranlage der Veräußerungsform des Mieterstromzuschlags
      zugeordnet wurde
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: integer
  mieterstromMeldedatum:
    name: mieterstromMeldedatum
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: date
  mieterstromErsteZuordnungZuschlag:
    name: mieterstromErsteZuordnungZuschlag
    instantiates:
    - xsd:element
    description: Datum, an dem die Anlage erstmalig der Veräußerungsform des Mieterstromzuschlags
      zugeordnet worden ist.
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: date
  ausschreibungZuschlag:
    name: ausschreibungZuschlag
    instantiates:
    - xsd:element
    description: Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren
      der Bundesnetzagentur ein Zuschlag erlangt wurde
    from_schema: https://example.org/mastr
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    - AnlageKwk
    range: integer
  zugeordneteGebotsmenge:
    name: zugeordneteGebotsmenge
    instantiates:
    - xsd:element
    description: Bezuschlagte Gebotsmenge, die der EEG-Anlage zugeordnet wurde
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegSolar
    range: float
  zuschlagsnummer:
    name: zuschlagsnummer
    instantiates:
    - xsd:element
    description: Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens
      vergebene Nummern (Mehrfachnennung möglich)
    from_schema: https://example.org/mastr
    owner: AnlageEegSolar
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    range: string
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebsstatus'
    from_schema: https://example.org/mastr
    owner: AnlageEegSolar
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
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum der EEG- Anlage
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
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
    owner: AnlageEegSolar
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string

```
</details></div>