---
search:
  boost: 10.0
---

# Class: AnlageEegBiomasse 

<div data-search-exclude markdown="1">



URI: [mastr:class/AnlageEegBiomasse](https://example.org/mastr/class/AnlageEegBiomasse)





```mermaid
 classDiagram
    class AnlageEegBiomasse
    click AnlageEegBiomasse href "../../classes/AnlageEegBiomasse/"
      Anlage <|-- AnlageEegBiomasse
        click Anlage href "../../classes/Anlage/"
      
      AnlageEegBiomasse : anlageBetriebsstatus
        
      AnlageEegBiomasse : anlagenkennzifferAnlagenregister
        
      AnlageEegBiomasse : anlagenkennzifferAnlagenregisterNv
        
      AnlageEegBiomasse : anlagenschluesselEeg
        
      AnlageEegBiomasse : ausschliesslicheVerwendungBiomasse
        
      AnlageEegBiomasse : ausschreibungZuschlag
        
      AnlageEegBiomasse : biogasDatumInanspruchnahmeFlexiPraemie
        
      AnlageEegBiomasse : biogasDatumLeistungserhoehung
        
      AnlageEegBiomasse : biogasGaserzeugungskapazitaet
        
      AnlageEegBiomasse : biogasGaserzeugungskapazitaetNv
        
      AnlageEegBiomasse : biogasHoechstbemessungsleistung
        
      AnlageEegBiomasse : biogasInanspruchnahmeFlexiPraemie
        
      AnlageEegBiomasse : biogasLeistungserhoehung
        
      AnlageEegBiomasse : biogasUmfangLeistungserhoehung
        
      AnlageEegBiomasse : biomethanErstmaligerEinsatz
        
      AnlageEegBiomasse : biomethanErstmaligerEinsatzNv
        
      AnlageEegBiomasse : datumLetzteAktualisierung
        
      AnlageEegBiomasse : eegInbetriebnahmedatum
        
      AnlageEegBiomasse : eegMaStRNummer
        
      AnlageEegBiomasse : installierteLeistung
        
      AnlageEegBiomasse : registrierungsdatum
        
      AnlageEegBiomasse : verknuepfteEinheitenMaStRNummern
        
      AnlageEegBiomasse : zuschlagsnummer
        
      
```





## Inheritance
* [Anlage](../classes/Anlage.md)
    * **AnlageEegBiomasse**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [eegInbetriebnahmedatum](../slots/eegInbetriebnahmedatum.md) | 0..1 <br/> [Date](../types/Date.md) | Inbetriebnahmedatum der EEG- Anlage | direct |
| [eegMaStRNummer](../slots/eegMaStRNummer.md) | 0..1 <br/> [String](../types/String.md) | MaStR-Nummer der Anlage | direct |
| [anlagenschluesselEeg](../slots/anlagenschluesselEeg.md) | 0..1 <br/> [String](../types/String.md) | Vom Netzbetreiber vergebene Kennziffer zur Identifikation der EEG-Anlage | direct |
| [anlagenkennzifferAnlagenregister](../slots/anlagenkennzifferAnlagenregister.md) | 0..1 <br/> [String](../types/String.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [anlagenkennzifferAnlagenregisterNv](../slots/anlagenkennzifferAnlagenregisterNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Anlagenkennziffer aus der Registrierungsbestätigung des Anlagenregister | direct |
| [installierteLeistung](../slots/installierteLeistung.md) | 0..1 <br/> [Float](../types/Float.md) | Installierte Nettonennleistung der EEG-Anlage | direct |
| [ausschliesslicheVerwendungBiomasse](../slots/ausschliesslicheVerwendungBiomasse.md) | 0..1 <br/> [Integer](../types/Integer.md) | Ausschließliche Verwendung von Biomasse im Sinne der Biomasse-Verordnung | direct |
| [ausschreibungZuschlag](../slots/ausschreibungZuschlag.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren der Bundes... | direct |
| [zuschlagsnummer](../slots/zuschlagsnummer.md) | 0..1 <br/> [String](../types/String.md) | Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens vergebene Nu... | direct |
| [biogasInanspruchnahmeFlexiPraemie](../slots/biogasInanspruchnahmeFlexiPraemie.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe ob für die Anlage Flexibilitätsprämie in anspruch genommen wird | direct |
| [biogasDatumInanspruchnahmeFlexiPraemie](../slots/biogasDatumInanspruchnahmeFlexiPraemie.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der erstmaligen Inanspruchnahme der Flexibilitätsprämie | direct |
| [biogasLeistungserhoehung](../slots/biogasLeistungserhoehung.md) | 0..1 <br/> [Integer](../types/Integer.md) | Angabe, ob die Leistung der Anlage im Zusammenhang mit der Flexibilitätsprämi... | direct |
| [biogasDatumLeistungserhoehung](../slots/biogasDatumLeistungserhoehung.md) | 0..1 <br/> [Date](../types/Date.md) | Datum der Inbetriebnahme der Leistungserhöhung | direct |
| [biogasUmfangLeistungserhoehung](../slots/biogasUmfangLeistungserhoehung.md) | 0..1 <br/> [Float](../types/Float.md) | Umfang der Leistungserhöhung bei dieser Biogas-Anlage nach dem 31 | direct |
| [biogasGaserzeugungskapazitaet](../slots/biogasGaserzeugungskapazitaet.md) | 0..1 <br/> [Float](../types/Float.md) | Leistungsangabe: Kapazität an Gas, das erzeugt werden kann | direct |
| [biogasGaserzeugungskapazitaetNv](../slots/biogasGaserzeugungskapazitaetNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Leistungsangabe: Kapazität an Gas, das erzeugt werden kann | direct |
| [biogasHoechstbemessungsleistung](../slots/biogasHoechstbemessungsleistung.md) | 0..1 <br/> [Float](../types/Float.md) | Höchstbemessungsleistung der Anlage | direct |
| [biomethanErstmaligerEinsatz](../slots/biomethanErstmaligerEinsatz.md) | 0..1 <br/> [Date](../types/Date.md) | Datum des erstmaligen ausschließlichen Einsatzes von Biomethan | direct |
| [biomethanErstmaligerEinsatzNv](../slots/biomethanErstmaligerEinsatzNv.md) | 0..1 <br/> [Integer](../types/Integer.md) | Datum des erstmaligen ausschließlichen Einsatzes von Biomethan | direct |
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
| self | mastr:AnlageEegBiomasse |
| native | mastr:AnlageEegBiomasse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnlageEegBiomasse
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG- Anlage
    from_schema: https://example.org/mastr
    rank: 1000
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
    rank: 1000
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
    rank: 1000
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
    rank: 1000
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
    rank: 1000
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
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: float
  ausschliesslicheVerwendungBiomasse:
    name: ausschliesslicheVerwendungBiomasse
    instantiates:
    - xsd:element
    description: Ausschließliche Verwendung von Biomasse im Sinne der Biomasse-Verordnung
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: integer
  ausschreibungZuschlag:
    name: ausschreibungZuschlag
    instantiates:
    - xsd:element
    description: Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren
      der Bundesnetzagentur ein Zuschlag erlangt wurde
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    - AnlageKwk
    range: integer
  zuschlagsnummer:
    name: zuschlagsnummer
    instantiates:
    - xsd:element
    description: Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens
      vergebene Nummern
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    range: string
  biogasInanspruchnahmeFlexiPraemie:
    name: biogasInanspruchnahmeFlexiPraemie
    instantiates:
    - xsd:element
    description: Angabe ob für die Anlage Flexibilitätsprämie in anspruch genommen
      wird
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasDatumInanspruchnahmeFlexiPraemie:
    name: biogasDatumInanspruchnahmeFlexiPraemie
    instantiates:
    - xsd:element
    description: Datum der erstmaligen Inanspruchnahme der Flexibilitätsprämie
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: date
  biogasLeistungserhoehung:
    name: biogasLeistungserhoehung
    instantiates:
    - xsd:element
    description: Angabe, ob die Leistung der Anlage im Zusammenhang mit der Flexibilitätsprämie
      erhöht wird
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasDatumLeistungserhoehung:
    name: biogasDatumLeistungserhoehung
    instantiates:
    - xsd:element
    description: Datum der Inbetriebnahme der Leistungserhöhung
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: date
  biogasUmfangLeistungserhoehung:
    name: biogasUmfangLeistungserhoehung
    instantiates:
    - xsd:element
    description: Umfang der Leistungserhöhung bei dieser Biogas-Anlage nach dem 31.07.2014
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: float
  biogasGaserzeugungskapazitaet:
    name: biogasGaserzeugungskapazitaet
    instantiates:
    - xsd:element
    description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
      nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe.'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: float
  biogasGaserzeugungskapazitaetNv:
    name: biogasGaserzeugungskapazitaetNv
    instantiates:
    - xsd:element
    description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
      nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe. Nicht-vorhanden
      Flag'
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasHoechstbemessungsleistung:
    name: biogasHoechstbemessungsleistung
    instantiates:
    - xsd:element
    description: Höchstbemessungsleistung der Anlage
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: float
  biomethanErstmaligerEinsatz:
    name: biomethanErstmaligerEinsatz
    instantiates:
    - xsd:element
    description: Datum des erstmaligen ausschließlichen Einsatzes von Biomethan
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: date
  biomethanErstmaligerEinsatzNv:
    name: biomethanErstmaligerEinsatzNv
    instantiates:
    - xsd:element
    description: Datum des erstmaligen ausschließlichen Einsatzes von Biomethan. Nicht-vorhanden
      Flag
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - AnlageEegBiomasse
    range: integer
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebsstatus'
    from_schema: https://example.org/mastr
    rank: 1000
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
name: AnlageEegBiomasse
from_schema: https://example.org/mastr
is_a: Anlage
attributes:
  eegInbetriebnahmedatum:
    name: eegInbetriebnahmedatum
    instantiates:
    - xsd:element
    description: Inbetriebnahmedatum der EEG- Anlage
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
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
    rank: 1000
    owner: AnlageEegBiomasse
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
    rank: 1000
    owner: AnlageEegBiomasse
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
    rank: 1000
    owner: AnlageEegBiomasse
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
    rank: 1000
    owner: AnlageEegBiomasse
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
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegGeothermieGrubengasDruckentspannung
    - AnlageEegSolar
    - AnlageEegWasser
    - AnlageEegWind
    range: float
  ausschliesslicheVerwendungBiomasse:
    name: ausschliesslicheVerwendungBiomasse
    instantiates:
    - xsd:element
    description: Ausschließliche Verwendung von Biomasse im Sinne der Biomasse-Verordnung
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: integer
  ausschreibungZuschlag:
    name: ausschreibungZuschlag
    instantiates:
    - xsd:element
    description: Angabe ob für die EEG-Anlage Im Rahmen des Ausschreibungsverfahren
      der Bundesnetzagentur ein Zuschlag erlangt wurde
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    - AnlageKwk
    range: integer
  zuschlagsnummer:
    name: zuschlagsnummer
    instantiates:
    - xsd:element
    description: Von der Bundesnetzagentur im Rahmen des Ausschreibungsverfahrens
      vergebene Nummern
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    - AnlageEegSolar
    - AnlageEegSpeicher
    - AnlageEegWind
    range: string
  biogasInanspruchnahmeFlexiPraemie:
    name: biogasInanspruchnahmeFlexiPraemie
    instantiates:
    - xsd:element
    description: Angabe ob für die Anlage Flexibilitätsprämie in anspruch genommen
      wird
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasDatumInanspruchnahmeFlexiPraemie:
    name: biogasDatumInanspruchnahmeFlexiPraemie
    instantiates:
    - xsd:element
    description: Datum der erstmaligen Inanspruchnahme der Flexibilitätsprämie
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: date
  biogasLeistungserhoehung:
    name: biogasLeistungserhoehung
    instantiates:
    - xsd:element
    description: Angabe, ob die Leistung der Anlage im Zusammenhang mit der Flexibilitätsprämie
      erhöht wird
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasDatumLeistungserhoehung:
    name: biogasDatumLeistungserhoehung
    instantiates:
    - xsd:element
    description: Datum der Inbetriebnahme der Leistungserhöhung
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: date
  biogasUmfangLeistungserhoehung:
    name: biogasUmfangLeistungserhoehung
    instantiates:
    - xsd:element
    description: Umfang der Leistungserhöhung bei dieser Biogas-Anlage nach dem 31.07.2014
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: float
  biogasGaserzeugungskapazitaet:
    name: biogasGaserzeugungskapazitaet
    instantiates:
    - xsd:element
    description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
      nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe.'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: float
  biogasGaserzeugungskapazitaetNv:
    name: biogasGaserzeugungskapazitaetNv
    instantiates:
    - xsd:element
    description: 'Leistungsangabe: Kapazität an Gas, das erzeugt werden kann. Gasproduktionskapazität
      nach Genehmigungsbescheid, bzw. anhand der eingesetzten Inputstoffe. Nicht-vorhanden
      Flag'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: integer
  biogasHoechstbemessungsleistung:
    name: biogasHoechstbemessungsleistung
    instantiates:
    - xsd:element
    description: Höchstbemessungsleistung der Anlage
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: float
  biomethanErstmaligerEinsatz:
    name: biomethanErstmaligerEinsatz
    instantiates:
    - xsd:element
    description: Datum des erstmaligen ausschließlichen Einsatzes von Biomethan
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: date
  biomethanErstmaligerEinsatzNv:
    name: biomethanErstmaligerEinsatzNv
    instantiates:
    - xsd:element
    description: Datum des erstmaligen ausschließlichen Einsatzes von Biomethan. Nicht-vorhanden
      Flag
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
    domain_of:
    - AnlageEegBiomasse
    range: integer
  anlageBetriebsstatus:
    name: anlageBetriebsstatus
    instantiates:
    - xsd:element
    description: 'Betriebsstatus der Anlage, welche sich aus den zugeordneten Einheiten
      ergibt. Katalogkategorie: Anlagenbetriebsstatus'
    from_schema: https://example.org/mastr
    rank: 1000
    owner: AnlageEegBiomasse
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
    owner: AnlageEegBiomasse
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
    owner: AnlageEegBiomasse
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
    owner: AnlageEegBiomasse
    domain_of:
    - Anlage
    - EinheitGasverbraucher
    - EinheitGenehmigung
    - Lokation
    range: string

```
</details></div>