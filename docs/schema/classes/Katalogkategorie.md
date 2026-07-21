---
search:
  boost: 10.0
---

# Class: Katalogkategorie 

<div data-search-exclude markdown="1">



URI: [mastr:class/Katalogkategorie](https://example.org/mastr/class/Katalogkategorie)





```mermaid
 classDiagram
    class Katalogkategorie
    click Katalogkategorie href "../../classes/Katalogkategorie/"
      Katalogkategorie : id
        
      Katalogkategorie : name
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 0..1 <br/> [Integer](../types/Integer.md) | Id der Katalogkategorie | direct |
| [name](../slots/name.md) | 0..1 <br/> [String](../types/String.md) | Name der Katalogkategorie | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:Katalogkategorie |
| native | mastr:Katalogkategorie |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Katalogkategorie
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: Id der Katalogkategorie
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
  name:
    name: name
    instantiates:
    - xsd:element
    description: Name der Katalogkategorie
    from_schema: https://example.org/mastr
    rank: 1000
    domain_of:
    - Katalogkategorie
    range: string

```
</details>

### Induced

<details>
```yaml
name: Katalogkategorie
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: Id der Katalogkategorie
    from_schema: https://example.org/mastr
    owner: Katalogkategorie
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
  name:
    name: name
    instantiates:
    - xsd:element
    description: Name der Katalogkategorie
    from_schema: https://example.org/mastr
    rank: 1000
    owner: Katalogkategorie
    domain_of:
    - Katalogkategorie
    range: string

```
</details></div>