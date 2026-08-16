---
title: Novo Testamento
description: 'Evangelhos, Atos, cartas e Apocalipse '
date: '2026-08-16'
draft: false
---

```base
formulas:
  description: 'note.description'

properties:
  formula.description:
    displayName: "Descrição"

views:
  - type: table
    name: Tabela
    filters:
      and:
        - file.folder == this.file.folder
        - file.name != this.file.name
    order:
      - file.name
      - formula.description
    sort:
      - property: file.name
        direction: ASC
      - property: formula.description
        direction: ASC

```

