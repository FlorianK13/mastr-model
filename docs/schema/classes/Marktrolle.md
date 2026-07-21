---
search:
  boost: 10.0
---

# Class: Marktrolle 

<div data-search-exclude markdown="1">



URI: [mastr:class/Marktrolle](https://example.org/mastr/class/Marktrolle)





```mermaid
 classDiagram
    class Marktrolle
    click Marktrolle href "../../classes/Marktrolle/"
      Marktrolle : id
        
      Marktrolle : wert
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 0..1 <br/> [Integer](../types/Integer.md) | ID der Rolle | direct |
| [wert](../slots/wert.md) | 0..1 <br/> [String](../types/String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/mastr




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mastr:Marktrolle |
| native | mastr:Marktrolle |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Marktrolle
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: ID der Rolle
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
name: Marktrolle
from_schema: https://example.org/mastr
attributes:
  id:
    name: id
    instantiates:
    - xsd:element
    description: ID der Rolle
    from_schema: https://example.org/mastr
    owner: Marktrolle
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
    owner: Marktrolle
    domain_of:
    - Einheitentyp
    - Katalogwert
    - Lokationstyp
    - Marktfunktion
    - Marktrolle
    range: string

```
</details></div>