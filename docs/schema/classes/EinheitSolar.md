---
search:
  boost: 10.0
---

# Class: EinheitSolar 

<div data-search-exclude markdown="1">



URI: [mastr:class/EinheitSolar](https://example.org/mastr/class/EinheitSolar)





```mermaid
 classDiagram
    class EinheitSolar
    click EinheitSolar href "../../classes/EinheitSolar/"
      Einheit <|-- EinheitSolar
        click Einheit href "../../classes/Einheit/"
      
      EinheitSolar : adresszusatz
        
      EinheitSolar : altAnlagenbetreiberMastrNummer
        
      EinheitSolar : anlagenbetreiberMastrNummer
        
      EinheitSolar : anschlussAnHoechstOderHochSpannung
        
      EinheitSolar : anzahlModule
        
      EinheitSolar : artDerSolaranlage
        
      EinheitSolar : bestandsanlageMastrNummer
        
      EinheitSolar : breitengrad
        
      EinheitSolar : bruttoleistung
        
      EinheitSolar : buergerenergie
        
      EinheitSolar : bundesland
        
      EinheitSolar : datumBeginnVoruebergehendeStilllegung
        
      EinheitSolar : datumDesBetreiberwechsels
        
      EinheitSolar : datumEndgueltigeStilllegung
        
      EinheitSolar : datumLetzteAktualisierung
        
      EinheitSolar : datumRegistrierungDesBetreiberwechsels
        
      EinheitSolar : datumWiederaufnahmeBetrieb
        
      EinheitSolar : eegMaStRNummer
        
      EinheitSolar : einheitBetriebsstatus
        
      EinheitSolar : einheitlicheAusrichtungUndNeigungswinkel
        
      EinheitSolar : einheitMastrNummer
        
      EinheitSolar : einheitSystemstatus
        
      EinheitSolar : einsatzverantwortlicher
        
      EinheitSolar : einspeisungsart
        
      EinheitSolar : energietraeger
        
      EinheitSolar : fernsteuerbarkeitDv
        
      EinheitSolar : fernsteuerbarkeitNb
        
      EinheitSolar : flurFlurstuecknummern
        
      EinheitSolar : gemarkung
        
      EinheitSolar : gemeinde
        
      EinheitSolar : gemeindeschluessel
        
      EinheitSolar : genMastrNummer
        
      EinheitSolar : geplantesInbetriebnahmedatum
        
      EinheitSolar : groesseDerInAnspruchGenommenenFlaecheInHektar
        
      EinheitSolar : hauptausrichtung
        
      EinheitSolar : hauptausrichtungNeigungswinkel
        
      EinheitSolar : hausnummer
        
      EinheitSolar : hausnummerNichtGefunden
        
      EinheitSolar : hausnummerNv
        
      EinheitSolar : inbetriebnahmedatum
        
      EinheitSolar : inbetriebnahmedatumAmAktuellenStandort
        
      EinheitSolar : kraftwerksnummer
        
      EinheitSolar : kraftwerksnummerNv
        
      EinheitSolar : laengengrad
        
      EinheitSolar : land
        
      EinheitSolar : landkreis
        
      EinheitSolar : leistungsbegrenzung
        
      EinheitSolar : lichteHoehe
        
      EinheitSolar : lokationMaStRNummer
        
      EinheitSolar : nameDesSolarparks
        
      EinheitSolar : nameStromerzeugungseinheit
        
      EinheitSolar : nebenausrichtung
        
      EinheitSolar : nebenausrichtungNeigungswinkel
        
      EinheitSolar : nettonennleistung
        
      EinheitSolar : netzbetreiberpruefungDatum
        
      EinheitSolar : netzbetreiberpruefungStatus
        
      EinheitSolar : nichtVorhandenInMigriertenEinheiten
        
      EinheitSolar : nutzungsbereich
        
      EinheitSolar : ort
        
      EinheitSolar : postleitzahl
        
      EinheitSolar : registrierungsdatum
        
      EinheitSolar : speicherAmGleichenOrt
        
      EinheitSolar : strasse
        
      EinheitSolar : strasseNichtGefunden
        
      EinheitSolar : ueberwiegendeNutzungsartDerFlaecheVorErrichtung
        
      EinheitSolar : vorherigerNutzungsartenbereichDerFlaeche
        
      EinheitSolar : weic
        
      EinheitSolar : weicDisplayName
        
      EinheitSolar : weicNv
        
      EinheitSolar : zugeordneteWirkleistungWechselrichter
        
      EinheitSolar : zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung
        
      
```





## Inheritance
* [Einheit](../classes/Einheit.md)
    * **EinheitSolar**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [strasseNichtGefunden](../slots/strasseNichtGefunden.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, dass die angegebene Straße nicht aus dem BKG-Adressdatenbestand stamm... | direct |
| [hausnummerNv](../slots/hausnummerNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Standort der Einheit: Hausnummer | direct |
| [hausnummerNichtGefunden](../slots/hausnummerNichtGefunden.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, dass die angegebene Hausnummer nicht aus dem BKG-Adressdatenbestand s... | direct |
| [adresszusatz](../slots/adresszusatz.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Adresszusatz | direct |
| [bestandsanlageMastrNummer](../slots/bestandsanlageMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | Angaben über optional vorhandene MaStR- Nummer aus der Bestandsanlagenverwalt... | direct |
| [nameStromerzeugungseinheit](../slots/nameStromerzeugungseinheit.md) | 0..1 <br/> [String](../types/String.md) | Vom Betreiber frei wählbare Bezeichnung der Stromerzeugungseinheit | direct |
| [weic](../slots/weic.md) | 0..1 <br/> [String](../types/String.md) | W-Code der Stromerzeugungseinheit | direct |
| [weicNv](../slots/weicNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | W-Code der Stromerzeugungseinheit | direct |
| [weicDisplayName](../slots/weicDisplayName.md) | 0..1 <br/> [String](../types/String.md) | Displayname des W-EIC | direct |
| [kraftwerksnummer](../slots/kraftwerksnummer.md) | 0..1 <br/> [String](../types/String.md) | Bundesnetzagentur-Kraftwerksnummer | direct |
| [kraftwerksnummerNv](../slots/kraftwerksnummerNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Bundesnetzagentur-Kraftwerksnummer | direct |
| [energietraeger](../slots/energietraeger.md) | 0..1 <br/> [Integer](../types/Integer.md) | Energieträger der Einheit | direct |
| [bruttoleistung](../slots/bruttoleistung.md) | 0..1 <br/> [Float](../types/Float.md) | Bruttoleistung in kW | direct |
| [nettonennleistung](../slots/nettonennleistung.md) | 0..1 <br/> [Float](../types/Float.md) | Nettonennleistung in kW | direct |
| [anschlussAnHoechstOderHochSpannung](../slots/anschlussAnHoechstOderHochSpannung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Die Stromerzeugungseinheit ist an ein Höchst- oder Hochspannungsnetz angeschl... | direct |
| [fernsteuerbarkeitNb](../slots/fernsteuerbarkeitNb.md) | 0..1 <br/> [Integer](../types/Integer.md) | Fernsteuerbarkeit der Einheit durch einen Netzbetreiber | direct |
| [fernsteuerbarkeitDv](../slots/fernsteuerbarkeitDv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Fernsteuerbarkeit der Einheit durch einen Direktvermarkter | direct |
| [einspeisungsart](../slots/einspeisungsart.md) | 0..1 <br/> [Integer](../types/Integer.md) | Volleinspeisung oder Teileinspeisung | direct |
| [zugeordneteWirkleistungWechselrichter](../slots/zugeordneteWirkleistungWechselrichter.md) | 0..1 <br/> [Float](../types/Float.md) | Wechselrichterleistung der Stromerzeugungseinheit | direct |
| [anzahlModule](../slots/anzahlModule.md) | 0..1 <br/> [Integer](../types/Integer.md) | Anzahl der Module dieser Stromerzeugungseinheit | direct |
| [artDerSolaranlage](../slots/artDerSolaranlage.md) | 0..1 <br/> [Integer](../types/Integer.md) | Art der Solaranlage | direct |
| [leistungsbegrenzung](../slots/leistungsbegrenzung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Die Leistung der Stromerzeugungseinheit ist auf einen bestimmten prozentualen... | direct |
| [einheitlicheAusrichtungUndNeigungswinkel](../slots/einheitlicheAusrichtungUndNeigungswinkel.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, ob einheitliche Ausrichtung und Neigungswinkel bestehen | direct |
| [hauptausrichtung](../slots/hauptausrichtung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Die Ausrichtung bezeichnet die Himmelsrichtung | direct |
| [hauptausrichtungNeigungswinkel](../slots/hauptausrichtungNeigungswinkel.md) | 0..1 <br/> [Integer](../types/Integer.md) | Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen | direct |
| [nebenausrichtung](../slots/nebenausrichtung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Die Ausrichtung bezeichnet die Himmelsrichtung | direct |
| [nebenausrichtungNeigungswinkel](../slots/nebenausrichtungNeigungswinkel.md) | 0..1 <br/> [Integer](../types/Integer.md) | Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen (Nebenaus... | direct |
| [nutzungsbereich](../slots/nutzungsbereich.md) | 0..1 <br/> [Integer](../types/Integer.md) | Vorrangige Nutzung des in Anspruch genommenen Gebäudes | direct |
| [buergerenergie](../slots/buergerenergie.md) | 0..1 <br/> [Integer](../types/Integer.md) | Bürgerenergieeigenschaft der Einheit | direct |
| [eegMaStRNummer](../slots/eegMaStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der zugeordneten EEG-Anlage | direct |
| [groesseDerInAnspruchGenommenenFlaecheInHektar](../slots/groesseDerInAnspruchGenommenenFlaecheInHektar.md) | 0..1 <br/> [Float](../types/Float.md) | Größe der in Anspruch genommene Fläche | direct |
| [ueberwiegendeNutzungsartDerFlaecheVorErrichtung](../slots/ueberwiegendeNutzungsartDerFlaecheVorErrichtung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Überwiegende Nutzungsart der Fläche vor Errichtung der Anlage | direct |
| [einsatzverantwortlicher](../slots/einsatzverantwortlicher.md) | 0..1 <br/> [String](../types/String.md) | Marktpartner-ID des Einsatzverantwortlichen | direct |
| [genMastrNummer](../slots/genMastrNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStRNummer der zu dieser Einheit zugeordneten Genehmigung | direct |
| [speicherAmGleichenOrt](../slots/speicherAmGleichenOrt.md) | 0..1 <br/> [Integer](../types/Integer.md) | Speicher am gleichen Ort | direct |
| [nameDesSolarparks](../slots/nameDesSolarparks.md) | 0..1 <br/> [String](../types/String.md) | Der Name des Solarparks | direct |
| [vorherigerNutzungsartenbereichDerFlaeche](../slots/vorherigerNutzungsartenbereichDerFlaeche.md) | 0..1 <br/> [Integer](../types/Integer.md) | Katalog: Vorheriger Nutzungsartenbereich der Fläche | direct |
| [zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung](../slots/zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung.md) | 0..1 <br/> [Integer](../types/Integer.md) |  | direct |
| [lichteHoehe](../slots/lichteHoehe.md) | 0..1 <br/> [Float](../types/Float.md) | Lichte Höhe in Meter | direct |
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
| [hausnummer](../slots/hausnummer.md) | 0..1 <br/> [String](../types/String.md) | Standort der Einheit: Hausnummer | [Einheit](../classes/Einheit.md) |
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
| self | mastr:EinheitSolar |
| native | mastr:EinheitSolar |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EinheitSolar
from_schema: https://example.org/mastr
is_a: Einheit
attributes:
  strasseNichtGefunden:
    name: strasseNichtGefunden
    instantiates:
    - xsd:element
    description: Angabe, dass die angegebene Straße nicht aus dem BKG-Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: integer
  hausnummerNv:
    name: hausnummerNv
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Hausnummer. Nicht- vorhanden Flag'
    from_schema: https://example.org/mastr
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
    description: Angabe, dass die angegebene Hausnummer nicht aus dem BKG-Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitStromVerbraucher
    - EinheitWasser
    - EinheitWind
    range: integer
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
  bestandsanlageMastrNummer:
    name: bestandsanlageMastrNummer
    instantiates:
    - xsd:element
    description: Angaben über optional vorhandene MaStR- Nummer aus der Bestandsanlagenverwaltung
    from_schema: https://example.org/mastr
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: string
  nameStromerzeugungseinheit:
    name: nameStromerzeugungseinheit
    instantiates:
    - xsd:element
    description: Vom Betreiber frei wählbare Bezeichnung der Stromerzeugungseinheit.
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  weic:
    name: weic
    instantiates:
    - xsd:element
    description: W-Code der Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGasSpeicher
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  weicNv:
    name: weicNv
    instantiates:
    - xsd:element
    description: W-Code der Stromerzeugungseinheit. Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  weicDisplayName:
    name: weicDisplayName
    instantiates:
    - xsd:element
    description: Displayname des W-EIC
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  kraftwerksnummer:
    name: kraftwerksnummer
    instantiates:
    - xsd:element
    description: Bundesnetzagentur-Kraftwerksnummer
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  kraftwerksnummerNv:
    name: kraftwerksnummerNv
    instantiates:
    - xsd:element
    description: Bundesnetzagentur-Kraftwerksnummer. Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  energietraeger:
    name: energietraeger
    instantiates:
    - xsd:element
    description: 'Energieträger der Einheit. Katalogkategorie: Energieträger'
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  bruttoleistung:
    name: bruttoleistung
    instantiates:
    - xsd:element
    description: Bruttoleistung in kW
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: float
  nettonennleistung:
    name: nettonennleistung
    instantiates:
    - xsd:element
    description: Nettonennleistung in kW
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: float
  anschlussAnHoechstOderHochSpannung:
    name: anschlussAnHoechstOderHochSpannung
    instantiates:
    - xsd:element
    description: Die Stromerzeugungseinheit ist an ein Höchst- oder Hochspannungsnetz
      angeschlossen
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  fernsteuerbarkeitNb:
    name: fernsteuerbarkeitNb
    instantiates:
    - xsd:element
    description: Fernsteuerbarkeit der Einheit durch einen Netzbetreiber
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  fernsteuerbarkeitDv:
    name: fernsteuerbarkeitDv
    instantiates:
    - xsd:element
    description: Fernsteuerbarkeit der Einheit durch einen Direktvermarkter
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  einspeisungsart:
    name: einspeisungsart
    instantiates:
    - xsd:element
    description: 'Volleinspeisung oder Teileinspeisung. Katalogkategorie: Einspeisungsart'
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  zugeordneteWirkleistungWechselrichter:
    name: zugeordneteWirkleistungWechselrichter
    instantiates:
    - xsd:element
    description: Wechselrichterleistung der Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: float
  anzahlModule:
    name: anzahlModule
    instantiates:
    - xsd:element
    description: Anzahl der Module dieser Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  artDerSolaranlage:
    name: artDerSolaranlage
    instantiates:
    - xsd:element
    description: 'Art der Solaranlage. Katalogkategorie: ArtDerSolaranlage'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  leistungsbegrenzung:
    name: leistungsbegrenzung
    instantiates:
    - xsd:element
    description: 'Die Leistung der Stromerzeugungseinheit ist auf einen bestimmten
      prozentualen Leistungsanteil begrenzt. Katalogkategorie: SolarLeistungsbegrenzung'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  einheitlicheAusrichtungUndNeigungswinkel:
    name: einheitlicheAusrichtungUndNeigungswinkel
    instantiates:
    - xsd:element
    description: Angabe, ob einheitliche Ausrichtung und Neigungswinkel bestehen.
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  hauptausrichtung:
    name: hauptausrichtung
    instantiates:
    - xsd:element
    description: 'Die Ausrichtung bezeichnet die Himmelsrichtung. Katalogkategorie:
      AnlagenartSolarAusrichtung'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  hauptausrichtungNeigungswinkel:
    name: hauptausrichtungNeigungswinkel
    instantiates:
    - xsd:element
    description: 'Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen.
      Katalogkategorie: AnlagenartSolarNeigungswinkel'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  nebenausrichtung:
    name: nebenausrichtung
    instantiates:
    - xsd:element
    description: 'Die Ausrichtung bezeichnet die Himmelsrichtung. Katalogkategorie:
      AnlagenartSolarAusrichtung'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  nebenausrichtungNeigungswinkel:
    name: nebenausrichtungNeigungswinkel
    instantiates:
    - xsd:element
    description: 'Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen
      (Nebenausrichtung). Katalogkategorie: AnlagenartSolarNeigungswinkel'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  nutzungsbereich:
    name: nutzungsbereich
    instantiates:
    - xsd:element
    description: 'Vorrangige Nutzung des in Anspruch genommenen Gebäudes. Katalogkategorie:
      Nutzungsbereich'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  buergerenergie:
    name: buergerenergie
    instantiates:
    - xsd:element
    description: Bürgerenergieeigenschaft der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  eegMaStRNummer:
    name: eegMaStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der zugeordneten EEG-Anlage
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
  groesseDerInAnspruchGenommenenFlaecheInHektar:
    name: groesseDerInAnspruchGenommenenFlaecheInHektar
    instantiates:
    - xsd:element
    description: Größe der in Anspruch genommene Fläche
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: float
  ueberwiegendeNutzungsartDerFlaecheVorErrichtung:
    name: ueberwiegendeNutzungsartDerFlaecheVorErrichtung
    instantiates:
    - xsd:element
    description: 'Überwiegende Nutzungsart der Fläche vor Errichtung der Anlage. Katalogkategorie:
      VorherigeNutzungsartengruppe'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  einsatzverantwortlicher:
    name: einsatzverantwortlicher
    instantiates:
    - xsd:element
    description: Marktpartner-ID des Einsatzverantwortlichen
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitStromVerbraucher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  genMastrNummer:
    name: genMastrNummer
    instantiates:
    - xsd:element
    description: MaStRNummer der zu dieser Einheit zugeordneten Genehmigung
    from_schema: https://example.org/mastr
    domain_of:
    - EinheitBiomasse
    - EinheitGenehmigung
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  speicherAmGleichenOrt:
    name: speicherAmGleichenOrt
    instantiates:
    - xsd:element
    description: Speicher am gleichen Ort
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  nameDesSolarparks:
    name: nameDesSolarparks
    instantiates:
    - xsd:element
    description: Der Name des Solarparks
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: string
  vorherigerNutzungsartenbereichDerFlaeche:
    name: vorherigerNutzungsartenbereichDerFlaeche
    instantiates:
    - xsd:element
    description: 'Katalog: Vorheriger Nutzungsartenbereich der Fläche'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung:
    name: zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: integer
  lichteHoehe:
    name: lichteHoehe
    instantiates:
    - xsd:element
    description: Lichte Höhe in Meter
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - EinheitSolar
    range: float

```
</details>

### Induced

<details>
```yaml
name: EinheitSolar
from_schema: https://example.org/mastr
is_a: Einheit
attributes:
  strasseNichtGefunden:
    name: strasseNichtGefunden
    instantiates:
    - xsd:element
    description: Angabe, dass die angegebene Straße nicht aus dem BKG-Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: integer
  hausnummerNv:
    name: hausnummerNv
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Hausnummer. Nicht- vorhanden Flag'
    from_schema: https://example.org/mastr
    owner: EinheitSolar
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
    description: Angabe, dass die angegebene Hausnummer nicht aus dem BKG-Adressdatenbestand
      stammt
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitStromVerbraucher
    - EinheitWasser
    - EinheitWind
    range: integer
  adresszusatz:
    name: adresszusatz
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Adresszusatz'
    from_schema: https://example.org/mastr
    owner: EinheitSolar
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
  bestandsanlageMastrNummer:
    name: bestandsanlageMastrNummer
    instantiates:
    - xsd:element
    description: Angaben über optional vorhandene MaStR- Nummer aus der Bestandsanlagenverwaltung
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - Einheit
    - EinheitSolar
    - EinheitWind
    range: string
  nameStromerzeugungseinheit:
    name: nameStromerzeugungseinheit
    instantiates:
    - xsd:element
    description: Vom Betreiber frei wählbare Bezeichnung der Stromerzeugungseinheit.
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  weic:
    name: weic
    instantiates:
    - xsd:element
    description: W-Code der Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGasSpeicher
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  weicNv:
    name: weicNv
    instantiates:
    - xsd:element
    description: W-Code der Stromerzeugungseinheit. Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  weicDisplayName:
    name: weicDisplayName
    instantiates:
    - xsd:element
    description: Displayname des W-EIC
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  kraftwerksnummer:
    name: kraftwerksnummer
    instantiates:
    - xsd:element
    description: Bundesnetzagentur-Kraftwerksnummer
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  kraftwerksnummerNv:
    name: kraftwerksnummerNv
    instantiates:
    - xsd:element
    description: Bundesnetzagentur-Kraftwerksnummer. Nicht- vorhanden Flag
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  energietraeger:
    name: energietraeger
    instantiates:
    - xsd:element
    description: 'Energieträger der Einheit. Katalogkategorie: Energieträger'
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  bruttoleistung:
    name: bruttoleistung
    instantiates:
    - xsd:element
    description: Bruttoleistung in kW
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: float
  nettonennleistung:
    name: nettonennleistung
    instantiates:
    - xsd:element
    description: Nettonennleistung in kW
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: float
  anschlussAnHoechstOderHochSpannung:
    name: anschlussAnHoechstOderHochSpannung
    instantiates:
    - xsd:element
    description: Die Stromerzeugungseinheit ist an ein Höchst- oder Hochspannungsnetz
      angeschlossen
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  fernsteuerbarkeitNb:
    name: fernsteuerbarkeitNb
    instantiates:
    - xsd:element
    description: Fernsteuerbarkeit der Einheit durch einen Netzbetreiber
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  fernsteuerbarkeitDv:
    name: fernsteuerbarkeitDv
    instantiates:
    - xsd:element
    description: Fernsteuerbarkeit der Einheit durch einen Direktvermarkter
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  einspeisungsart:
    name: einspeisungsart
    instantiates:
    - xsd:element
    description: 'Volleinspeisung oder Teileinspeisung. Katalogkategorie: Einspeisungsart'
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: integer
  zugeordneteWirkleistungWechselrichter:
    name: zugeordneteWirkleistungWechselrichter
    instantiates:
    - xsd:element
    description: Wechselrichterleistung der Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: float
  anzahlModule:
    name: anzahlModule
    instantiates:
    - xsd:element
    description: Anzahl der Module dieser Stromerzeugungseinheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  artDerSolaranlage:
    name: artDerSolaranlage
    instantiates:
    - xsd:element
    description: 'Art der Solaranlage. Katalogkategorie: ArtDerSolaranlage'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  leistungsbegrenzung:
    name: leistungsbegrenzung
    instantiates:
    - xsd:element
    description: 'Die Leistung der Stromerzeugungseinheit ist auf einen bestimmten
      prozentualen Leistungsanteil begrenzt. Katalogkategorie: SolarLeistungsbegrenzung'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  einheitlicheAusrichtungUndNeigungswinkel:
    name: einheitlicheAusrichtungUndNeigungswinkel
    instantiates:
    - xsd:element
    description: Angabe, ob einheitliche Ausrichtung und Neigungswinkel bestehen.
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  hauptausrichtung:
    name: hauptausrichtung
    instantiates:
    - xsd:element
    description: 'Die Ausrichtung bezeichnet die Himmelsrichtung. Katalogkategorie:
      AnlagenartSolarAusrichtung'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  hauptausrichtungNeigungswinkel:
    name: hauptausrichtungNeigungswinkel
    instantiates:
    - xsd:element
    description: 'Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen.
      Katalogkategorie: AnlagenartSolarNeigungswinkel'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  nebenausrichtung:
    name: nebenausrichtung
    instantiates:
    - xsd:element
    description: 'Die Ausrichtung bezeichnet die Himmelsrichtung. Katalogkategorie:
      AnlagenartSolarAusrichtung'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  nebenausrichtungNeigungswinkel:
    name: nebenausrichtungNeigungswinkel
    instantiates:
    - xsd:element
    description: 'Der Neigungswinkel bezeichnet den Winkel gegenüber der Horizontalen
      (Nebenausrichtung). Katalogkategorie: AnlagenartSolarNeigungswinkel'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  nutzungsbereich:
    name: nutzungsbereich
    instantiates:
    - xsd:element
    description: 'Vorrangige Nutzung des in Anspruch genommenen Gebäudes. Katalogkategorie:
      Nutzungsbereich'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  buergerenergie:
    name: buergerenergie
    instantiates:
    - xsd:element
    description: Bürgerenergieeigenschaft der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  eegMaStRNummer:
    name: eegMaStRNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der zugeordneten EEG-Anlage
    from_schema: https://example.org/mastr
    owner: EinheitSolar
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
  groesseDerInAnspruchGenommenenFlaecheInHektar:
    name: groesseDerInAnspruchGenommenenFlaecheInHektar
    instantiates:
    - xsd:element
    description: Größe der in Anspruch genommene Fläche
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: float
  ueberwiegendeNutzungsartDerFlaecheVorErrichtung:
    name: ueberwiegendeNutzungsartDerFlaecheVorErrichtung
    instantiates:
    - xsd:element
    description: 'Überwiegende Nutzungsart der Fläche vor Errichtung der Anlage. Katalogkategorie:
      VorherigeNutzungsartengruppe'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  einsatzverantwortlicher:
    name: einsatzverantwortlicher
    instantiates:
    - xsd:element
    description: Marktpartner-ID des Einsatzverantwortlichen
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitStromVerbraucher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  genMastrNummer:
    name: genMastrNummer
    instantiates:
    - xsd:element
    description: MaStRNummer der zu dieser Einheit zugeordneten Genehmigung
    from_schema: https://example.org/mastr
    owner: EinheitSolar
    domain_of:
    - EinheitBiomasse
    - EinheitGenehmigung
    - EinheitGeothermieGrubengasDruckentspannung
    - EinheitKernkraft
    - EinheitSolar
    - EinheitStromSpeicher
    - EinheitVerbrennung
    - EinheitWasser
    - EinheitWind
    range: string
  speicherAmGleichenOrt:
    name: speicherAmGleichenOrt
    instantiates:
    - xsd:element
    description: Speicher am gleichen Ort
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  nameDesSolarparks:
    name: nameDesSolarparks
    instantiates:
    - xsd:element
    description: Der Name des Solarparks
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: string
  vorherigerNutzungsartenbereichDerFlaeche:
    name: vorherigerNutzungsartenbereichDerFlaeche
    instantiates:
    - xsd:element
    description: 'Katalog: Vorheriger Nutzungsartenbereich der Fläche'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    - EinheitWind
    range: integer
  zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung:
    name: zusaetzlicheMerkmaleDerFlaecheUndDerAktuellenFlaechennutzung
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: integer
  lichteHoehe:
    name: lichteHoehe
    instantiates:
    - xsd:element
    description: Lichte Höhe in Meter
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - EinheitSolar
    range: float
  einheitMastrNummer:
    name: einheitMastrNummer
    instantiates:
    - xsd:element
    description: MaStR-Nummer der Einheit
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
    domain_of:
    - Einheit
    range: string
  hausnummer:
    name: hausnummer
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Hausnummer'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
    domain_of:
    - Einheit
    - Marktakteur
    range: string
  ort:
    name: ort
    instantiates:
    - xsd:element
    description: 'Standort der Einheit: Ort'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
    domain_of:
    - Einheit
    range: float
  registrierungsdatum:
    name: registrierungsdatum
    instantiates:
    - xsd:element
    description: Registrierungsdatum der Einheit
    from_schema: https://example.org/mastr
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
    domain_of:
    - Einheit
    - GeloeschteUndDeaktivierteEinheit
    range: integer
  nichtVorhandenInMigriertenEinheiten:
    name: nichtVorhandenInMigriertenEinheiten
    instantiates:
    - xsd:element
    description: Angabe über das Nichtvorhandensein in den migrierten Einheiten
    from_schema: https://example.org/mastr
    rank: 1000
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
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
    owner: EinheitSolar
    domain_of:
    - Einheit
    - EinheitGasSpeicher
    range: datetime

```
</details></div>