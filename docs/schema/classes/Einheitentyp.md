---
search:
  boost: 10.0
---

# Class: Einheitentyp 

<div data-search-exclude markdown="1">



URI: [mastr:class/Einheitentyp](https://example.org/mastr/class/Einheitentyp)





```mermaid
 classDiagram
    class Einheitentyp
    click Einheitentyp href "../../classes/Einheitentyp/"
      Einheitentyp : id
        
      Einheitentyp : wert
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 0..1 <br/> [Integer](../types/Integer.md) | ID des Einheitentyps | direct |
| [wert](../slots/wert.md) | 0..1 <br/> [String](../types/String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:Einheitentyp |
| native | mastr:Einheitentyp |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Einheitentyp
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: ID des Einheitentyps
    from_schema: https://example.org/mastr
    domain_of:
    - Bilanzierungsgebiet
    - Einheitentyp
    - Ertuechtigung
    - Katalogkategorie
    - Katalogwert
    - Lokationstyp
    - Marktfunktion
    - Marktrolle
    range: integer
  wert:
    name: wert
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - Einheitentyp
    - Katalogwert
    - Lokationstyp
    - Marktfunktion
    - Marktrolle
    range: string

```
</details>

### Induced

<details>
```yaml
name: Einheitentyp
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: ID des Einheitentyps
    from_schema: https://example.org/mastr
    owner: Einheitentyp
    domain_of:
    - Bilanzierungsgebiet
    - Einheitentyp
    - Ertuechtigung
    - Katalogkategorie
    - Katalogwert
    - Lokationstyp
    - Marktfunktion
    - Marktrolle
    range: integer
  wert:
    name: wert
    instantiates:
    - xsd:element
    from_schema: https://example.org/mastr
    rank: 1000
    owner: Einheitentyp
    domain_of:
    - Einheitentyp
    - Katalogwert
    - Lokationstyp
    - Marktfunktion
    - Marktrolle
    range: string

```
</details></div>