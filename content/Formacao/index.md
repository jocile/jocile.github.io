---
title: 🎓 Formação
description: minha Formação
---

```base
filters:
  and:
    - file.tags.contains("Formação")
    - file.folder.startsWith("Formacao")
formulas:
  section: |
    if(file.inFolder("Formacao/Ciencia de dados"), "Ciência de dados",
    if(file.inFolder("Formacao/Desenvolvimento web"), "Desenvolvimento Web",
    if(file.inFolder("Formacao/Design"), "Design",
    if(file.inFolder("Formacao/Fundamentos em ti"), "Fundamentos em TI",
    if(file.inFolder("ci"), "ci", "core")))))
  Título: link(file, title)
views:
  - type: table
    name: Tabela
    order:
      - formula.section
      - formula.Título
      - status
      - description
    sort:
      - property: status
        direction: ASC
      - property: formula.section
        direction: ASC
      - property: formula.Título
        direction: ASC
    columnSize:
      note.title: 293
      note.status: 92

```
