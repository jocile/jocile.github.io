---
title: 💻 Ciência de Dados
description: Formação em Análise e Ciência de Dados
---

```base
filters:
  and:
    - file.ext == "md"
    - file.folder == "Formacao/Ciencia de dados"
    - file.path != this.file.path
formulas:
  Título: link(file, title)
views:
  - type: table
    name: Tabela
    order:
      - formula.Título
      - status
      - description
    sort:
      - property: status
        direction: ASC
      - property: formula.Título
        direction: ASC
    columnSize:
      note.title: 293
      note.status: 92

```
