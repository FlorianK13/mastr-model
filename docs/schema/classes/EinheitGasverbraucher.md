---
search:
  boost: 10.0
---

# Class: EinheitGasverbraucher 

<div data-search-exclude markdown="1">



URI: [mastr:class/EinheitGasverbraucher](https://example.org/mastr/class/EinheitGasverbraucher)





```mermaid
 classDiagram
    class EinheitGasverbraucher
    click EinheitGasverbraucher href "../../classes/EinheitGasverbraucher/"
      Einheit <|-- EinheitGasverbraucher
        click Einheit href "../../classes/Einheit/"
      
      EinheitGasverbraucher : adresszusatz
        
      EinheitGasverbraucher : altAnlagenbetreiberMastrNummer
        
      EinheitGasverbraucher : anlagenbetreiberMastrNummer
        
      EinheitGasverbraucher : bestandsanlageMastrNummer
        
      EinheitGasverbraucher : breitengrad
        
      EinheitGasverbraucher : bundesland
        
      EinheitGasverbraucher : datumBeginnVoruebergehendeStilllegung
        
      EinheitGasverbraucher : datumDesBetreiberwechsels
        
      EinheitGasverbraucher : datumEndgueltigeStilllegung
        
      EinheitGasverbraucher : datumLetzteAktualisierung
        
      EinheitGasverbraucher : datumRegistrierungDesBetreiberwechsels
        
      EinheitGasverbraucher : datumWiederaufnahmeBetrieb
        
      EinheitGasverbraucher : einheitBetriebsstatus
        
      EinheitGasverbraucher : einheitDientDerStromerzeugung
        
      EinheitGasverbraucher : einheitMastrNummer
        
      EinheitGasverbraucher : einheitSystemstatus
        
      EinheitGasverbraucher : flurFlurstuecknummern
        
      EinheitGasverbraucher : gemarkung
        
      EinheitGasverbraucher : gemeinde
        
      EinheitGasverbraucher : gemeindeschluessel
        
      EinheitGasverbraucher : geplantesInbetriebnahmedatum
        
      EinheitGasverbraucher : hausnummer
        
      EinheitGasverbraucher : hausnummerNichtGefunden
        
      EinheitGasverbraucher : hausnummerNv
        
      EinheitGasverbraucher : inbetriebnahmedatum
        
      EinheitGasverbraucher : inbetriebnahmedatumAmAktuellenStandort
        
      EinheitGasverbraucher : laengengrad
        
      EinheitGasverbraucher : land
        
      EinheitGasverbraucher : landkreis
        
      EinheitGasverbraucher : lokationMaStRNummer
        
      EinheitGasverbraucher : maximaleGasbezugsleistung
        
      EinheitGasverbraucher : nameGasverbrauchsseinheit
        
      EinheitGasverbraucher : netzbetreiberpruefungDatum
        
      EinheitGasverbraucher : netzbetreiberpruefungStatus
        
      EinheitGasverbraucher : nichtVorhandenInMigriertenEinheiten
        
      EinheitGasverbraucher : ort
        
      EinheitGasverbraucher : postleitzahl
        
      EinheitGasverbraucher : registrierungsdatum
        
      EinheitGasverbraucher : strasse
        
      EinheitGasverbraucher : strasseNichtGefunden
        
      EinheitGasverbraucher : verknuepfteEinheitenMaStRNummern
        
      
```





## Inheritance
* [Einheit](../classes/Einheit.md)
    * **EinheitGasverbraucher**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adresszusatz](../slots/adresszusatz.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Adresszusatz | direct |
| [nameGasverbrauchsseinheit](../slots/nameGasverbrauchsseinheit.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [maximaleGasbezugsleistung](../slots/maximaleGasbezugsleistung.md) | 0..1 <br/> [Float](../types/Float.md) | Maximale Gasbezugsleistung zur Stromerzeugung | direct |
| [einheitDientDerStromerzeugung](../slots/einheitDientDerStromerzeugung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe ob die Gasverbrauchseinheit zur Stromerzeugung dient (Gaskraftwerk) | direct |
| [verknuepfteEinheitenMaStRNummern](../slots/verknuepfteEinheitenMaStRNummern.md) | 0..1 <br/> [String](../types/String.md) | Liste von MaStR Nummern mit den verknüpften Stromerzeugern | direct |
| [einheitMastrNummer](../slots/einheitMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der Einheit | [Einheit](../classes/Einheit.md) |
| [datumLetzteAktualisierung](../slots/datumLetzteAktualisierung.md) | 0..1 <br/> [Datetime](../types/Datetime.md) | Datum der letzten Aktualisierung an diesem Objekt | [Einheit](../classes/Einheit.md) |
| [lokationMaStRNummer](../slots/lokationMaStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der Lokation | [Einheit](../classes/Einheit.md) |
| [netzbetreiberpruefungStatus](../slots/netzbetreiberpruefungStatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Der Status der letzten Netzbetreiberprüfung, insofern eine durchgeführt wurde | [Einheit](../classes/Einheit.md) |
| [netzbetreiberpruefungDatum](../slots/netzbetreiberpruefungDatum.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der letzten Netzbetreiberprüfung, insofern eine durchgeführt wurde | [Einheit](../classes/Einheit.md) |
| [anlagenbetreiberMastrNummer](../slots/anlagenbetreiberMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStRNummer des Betreibers der Einheit | [Einheit](../classes/Einheit.md) |
| [land](../slots/land.md) | 0..1 <br/> [Integer](../types/Integer.md) | Standort der Einheit: Land: Katalogkategorie: Land | [Einheit](../classes/Einheit.md) |
| [bundesland](../slots/bundesland.md) | 0..1 <br/> [Integer](../types/Integer.md) | Standort der Einheit: Bundesland | [Einheit](../classes/Einheit.md) |
| [landkreis](../slots/landkreis.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Landkreis | [Einheit](../classes/Einheit.md) |
| [gemeinde](../slots/gemeinde.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Gemeinde | [Einheit](../classes/Einheit.md) |
| [gemeindeschluessel](../slots/gemeindeschluessel.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Gemeindeschlüssel | [Einheit](../classes/Einheit.md) |
| [postleitzahl](../slots/postleitzahl.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Postleitzahl | [Einheit](../classes/Einheit.md) |
| [strasse](../slots/strasse.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Straße | [Einheit](../classes/Einheit.md) |
| [gemarkung](../slots/gemarkung.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Gemarkung | [Einheit](../classes/Einheit.md) |
| [flurFlurstuecknummern](../slots/flurFlurstuecknummern.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Flur und/oder Flurstücke | [Einheit](../classes/Einheit.md) |
| [strasseNichtGefunden](../slots/strasseNichtGefunden.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, dass die angegebene Straße nicht aus dem BKG- Adressdatenbestand stam... | [Einheit](../classes/Einheit.md) |
| [hausnummer](../slots/hausnummer.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Hausnummer | [Einheit](../classes/Einheit.md) |
| [hausnummerNv](../slots/hausnummerNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Standort der Einheit: Hausnummer | [Einheit](../classes/Einheit.md) |
| [hausnummerNichtGefunden](../slots/hausnummerNichtGefunden.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, dass die angegebene Hausnummer nicht aus dem BKG- Adressdatenbestand ... | [Einheit](../classes/Einheit.md) |
| [ort](../slots/ort.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Ort | [Einheit](../classes/Einheit.md) |
| [laengengrad](../slots/laengengrad.md) | 0..1 <br/> [Float](../types/Float.md) | Koordinaten der Einheit: Längengrad | [Einheit](../classes/Einheit.md) |
| [breitengrad](../slots/breitengrad.md) | 0..1 <br/> [Float](../types/Float.md) | Koordinaten der Einheit: Breitengrad | [Einheit](../classes/Einheit.md) |
| [registrierungsdatum](../slots/registrierungsdatum.md) | 0..1 <br/> [Date](../types/Date.md) | Registrierungsdatum der Einheit | [Einheit](../classes/Einheit.md) |
| [inbetriebnahmedatum](../slots/inbetriebnahmedatum.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der Inbetriebnahme | [Einheit](../classes/Einheit.md) |
| [datumEndgueltigeStilllegung](../slots/datumEndgueltigeStilllegung.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der endgültigen Stilllegung der Einheit | [Einheit](../classes/Einheit.md) |
| [datumBeginnVoruebergehendeStilllegung](../slots/datumBeginnVoruebergehendeStilllegung.md) | 0..1 <br/> [Date](../types/Date.md) | Beginn der vorläufigen Stilllegung der Einheit | [Einheit](../classes/Einheit.md) |
| [datumWiederaufnahmeBetrieb](../slots/datumWiederaufnahmeBetrieb.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der Wiederaufnahme des Betriebs | [Einheit](../classes/Einheit.md) |
| [geplantesInbetriebnahmedatum](../slots/geplantesInbetriebnahmedatum.md) | 0..1 <br/> [Date](../types/Date.md) | Geplantes Inbetriebnahmedatum der Stromerzeugungsseinheit | [Einheit](../classes/Einheit.md) |
| [einheitSystemstatus](../slots/einheitSystemstatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Systemstatus der Einheit | [Einheit](../classes/Einheit.md) |
| [einheitBetriebsstatus](../slots/einheitBetriebsstatus.md) | 0..1 <br/> [Integer](../types/Integer.md) | Betriebsstatus der Einheit | [Einheit](../classes/Einheit.md) |
| [bestandsanlageMastrNummer](../slots/bestandsanlageMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | Angaben über optional vorhandene MaStR-Nummer aus der Bestandsanlagenverwaltu... | [Einheit](../classes/Einheit.md) |
| [nichtVorhandenInMigriertenEinheiten](../slots/nichtVorhandenInMigriertenEinheiten.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe über das Nichtvorhandensein in den migrierten Einheiten | [Einheit](../classes/Einheit.md) |
| [altAnlagenbetreiberMastrNummer](../slots/altAnlagenbetreiberMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer des ehemaligen Betreibers der Einheit, wenn ein Betreiberwechsel... | [Einheit](../classes/Einheit.md) |
| [datumDesBetreiberwechsels](../slots/datumDesBetreiberwechsels.md) | 0..1 <br/> [Date](../types/Date.md) | Datum des realen Betreiberwechsels | [Einheit](../classes/Einheit.md) |
| [datumRegistrierungDesBetreiberwechsels](../slots/datumRegistrierungDesBetreiberwechsels.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der Registrierung des Betreiberwechsels | [Einheit](../classes/Einheit.md) |
| [inbetriebnahmedatumAmAktuellenStandort](../slots/inbetriebnahmedatumAmAktuellenStandort.md) | 0..1 <br/> [Datetime](../types/Datetime.md) | Datum der Inbetriebnahme am aktuellen Standort | [Einheit](../classes/Einheit.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:EinheitGasverbraucher |
| native | mastr:EinheitGasverbraucher |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EinheitGasverbraucher
from_schema: https://example.org/mastr
is_a: Einheit
attributes:
  adresszusatz:
    name: adresszusatz
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Adresszusatz'
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGasErzeuger
    - EinheitGasSpeicher
    - EinheitGasverbraucher
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitStromVerbraucher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    - Marktakteur
    range: string
  nameGasverbrauchsseinheit:
    name: nameGasverbrauchsseinheit
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitGasverbraucher
    range: string
  maximaleGasbezugsleistung:
    name: maximaleGasbezugsleistung
    instantiates:
    - xsd:element
    description: Maximale Gasbezugsleistung zur Stromerzeugung
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitGasverbraucher
    range: float
  einheitDientDerStromerzeugung:
    name: einheitDientDerStromerzeugung
    instantiates:
    - xsd:element
    description: Angabe ob die Gasverbrauchseinheit zur Stromerzeugung dient (Gaskraftwerk)
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitGasverbraucher
    range: integer
  verknuepfteEinheitenMaStRNummern:
    name: verknuepfteEinheitenMaStRNummern
    instantiates:
    - xsd:element
    description: Liste von MaStR Nummern mit den verknüpften Stromerzeugern
    from_schema: https://example.org/mastr
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string

```
</details>

### Induced

<details>
```yaml
name: EinheitGasverbraucher
from_schema: https://example.org/mastr
is_a: Einheit
attributes:
  adresszusatz:
    name: adresszusatz
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Adresszusatz'
    from_schema: https://example.org/mastr
    owner: EinheitGasverbraucher
    domain_of:
    - EinheitBiomasse
    - EinheitGasErzeuger
    - EinheitGasSpeicher
    - EinheitGasverbraucher
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitStromVerbraucher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    - Marktakteur
    range: string
  nameGasverbrauchsseinheit:
    name: nameGasverbrauchsseinheit
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - EinheitGasverbraucher
    range: string
  maximaleGasbezugsleistung:
    name: maximaleGasbezugsleistung
    instantiates:
    - xsd:element
    description: Maximale Gasbezugsleistung zur Stromerzeugung
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - EinheitGasverbraucher
    range: float
  einheitDientDerStromerzeugung:
    name: einheitDientDerStromerzeugung
    instantiates:
    - xsd:element
    description: Angabe ob die Gasverbrauchseinheit zur Stromerzeugung dient (Gaskraftwerk)
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - EinheitGasverbraucher
    range: integer
  verknuepfteEinheitenMaStRNummern:
    name: verknuepfteEinheitenMaStRNummern
    instantiates:
    - xsd:element
    description: Liste von MaStR Nummern mit den verknüpften Stromerzeugern
    from_schema: https://example.org/mastr
    owner: EinheitGasverbraucher
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string
  einheitMastrNummer:
    name: einheitMastrNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitenAenderungNetzbetreiberzuordnung
    - GeloeschteUndDeaktivierteEinheit
    range: string
  datumLetzteAktualisierung:
    name: datumLetzteAktualisierung
    instantiates:
    - xsd:element
    description: Datum der letzten Aktualisierung an diesem Objekt
    from_schema: https://example.org/mastr
    owner: EinheitGasverbraucher
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
  lokationMaStRNummer:
    name: lokationMaStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der Lokation
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Netzanschlusspunkt
    range: string
  netzbetreiberpruefungStatus:
    name: netzbetreiberpruefungStatus
    instantiates:
    - xsd:element
    description: 'Der Status der letzten Netzbetreiberprüfung, insofern eine durchgeführt
      wurde. Systemkatalog: Status der Netzbetreiberprüfung'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: integer
  netzbetreiberpruefungDatum:
    name: netzbetreiberpruefungDatum
    instantiates:
    - xsd:element
    description: Datum der letzten Netzbetreiberprüfung, insofern eine durchgeführt
      wurde
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  anlagenbetreiberMastrNummer:
    name: anlagenbetreiberMastrNummer
    instantiates:
    - xsd:element
    description: MaStRNummer des Betreibers der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitBiomasse
    range: string
  land:
    name: land
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Land: Katalogkategorie: Land'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    range: integer
  bundesland:
    name: bundesland
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Bundesland. Katalogkategorie: BundesländerEinheit'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    - Netz
    range: integer
  landkreis:
    name: landkreis
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Landkreis'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  gemeinde:
    name: gemeinde
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Gemeinde'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  gemeindeschluessel:
    name: gemeindeschluessel
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Gemeindeschlüssel'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  postleitzahl:
    name: postleitzahl
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Postleitzahl'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    range: string
  strasse:
    name: strasse
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Straße'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    range: string
  gemarkung:
    name: gemarkung
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Gemarkung'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  flurFlurstuecknummern:
    name: flurFlurstuecknummern
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Flur und/oder Flurstücke'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  strasseNichtGefunden:
    name: strasseNichtGefunden
    instantiates:
    - xsd:element
    description: Angabe, dass die angegebene Straße nicht aus dem BKG- Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: integer
  hausnummer:
    name: hausnummer
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Hausnummer'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    range: string
  hausnummerNv:
    name: hausnummerNv
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Hausnummer. Nicht-vorhanden Flag'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWasser
    - EinheitWind
    - Marktakteur
    range: integer
  hausnummerNichtGefunden:
    name: hausnummerNichtGefunden
    instantiates:
    - xsd:element
    description: Angabe, dass die angegebene Hausnummer nicht aus dem BKG- Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitStromVerbraucher
    - EinheitWasser
    - EinheitWind
    range: integer
  ort:
    name: ort
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Ort'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - Marktakteur
    range: string
  laengengrad:
    name: laengengrad
    instantiates:
    - xsd:element
    description: 'Koordinaten der Einheit: Längengrad'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: float
  breitengrad:
    name: breitengrad
    instantiates:
    - xsd:element
    description: 'Koordinaten der Einheit: Breitengrad'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: float
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum der Einheit
    from_schema: https://example.org/mastr
    owner: EinheitGasverbraucher
    domain_of:
    - Anlage
    - AnlageEegSpeicher
    - AnlageGasSpeicher
    - AnlageKwk
    - AnlageStromSpeicher
    - Einheit
    - EinheitGenehmigung
    range: date
  inbetriebnahmedatum:
    name: inbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Datum der Inbetriebnahme
    from_schema: https://example.org/mastr
    owner: EinheitGasverbraucher
    domain_of:
    - AnlageKwk
    - Einheit
    range: date
  datumEndgueltigeStilllegung:
    name: datumEndgueltigeStilllegung
    instantiates:
    - xsd:element
    description: Datum der endgültigen Stilllegung der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  datumBeginnVoruebergehendeStilllegung:
    name: datumBeginnVoruebergehendeStilllegung
    instantiates:
    - xsd:element
    description: Beginn der vorläufigen Stilllegung der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  datumWiederaufnahmeBetrieb:
    name: datumWiederaufnahmeBetrieb
    instantiates:
    - xsd:element
    description: Datum der Wiederaufnahme des Betriebs
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  geplantesInbetriebnahmedatum:
    name: geplantesInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Geplantes Inbetriebnahmedatum der Stromerzeugungsseinheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  einheitSystemstatus:
    name: einheitSystemstatus
    instantiates:
    - xsd:element
    description: 'Systemstatus der Einheit. Katalogkategorie: AnlagenSystemStatus'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - GeloeschteUndDeaktivierteEinheit
    range: integer
  einheitBetriebsstatus:
    name: einheitBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Einheit. Katalogkategorie: Anlagenbetriebsstatus'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - GeloeschteUndDeaktivierteEinheit
    range: integer
  bestandsanlageMastrNummer:
    name: bestandsanlageMastrNummer
    instantiates:
    - xsd:element
    description: Angaben über optional vorhandene MaStR-Nummer aus der Bestandsanlagenverwaltung
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: string
  nichtVorhandenInMigriertenEinheiten:
    name: nichtVorhandenInMigriertenEinheiten
    instantiates:
    - xsd:element
    description: Angabe über das Nichtvorhandensein in den migrierten Einheiten
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: integer
  altAnlagenbetreiberMastrNummer:
    name: altAnlagenbetreiberMastrNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer des ehemaligen Betreibers der Einheit, wenn ein Betreiberwechsel
      durchgeführt wurde
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: string
  datumDesBetreiberwechsels:
    name: datumDesBetreiberwechsels
    instantiates:
    - xsd:element
    description: Datum des realen Betreiberwechsels
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  datumRegistrierungDesBetreiberwechsels:
    name: datumRegistrierungDesBetreiberwechsels
    instantiates:
    - xsd:element
    description: Datum der Registrierung des Betreiberwechsels
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    range: date
  inbetriebnahmedatumAmAktuellenStandort:
    name: inbetriebnahmedatumAmAktuellenStandort
    instantiates:
    - xsd:element
    description: Datum der Inbetriebnahme am aktuellen Standort
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitGasverbraucher
    domain_of:
    - Einheit
    - EinheitGasSpeicher
    range: datetime

```
</details></div>