---
title: 🎓 Formação
description: minha Formação
---

```base
filters:
  and:
    - file.tags.contains("Formação")
    - file.folder.startsWith("Formacao")
views:
  - type: table
    name: Tabela
    order:
      - file.name
      - status
      - description
    sort:
      - property: status
        direction: ASC
      - property: title
        direction: ASC
    columnSize:
      note.title: 293
      note.status: 92

```
