---
title: 💻 Projetos de Software
description: "Meus projetos de desenvolvimento de software"
tags:
  - projetos
---

```base
filters:
  and:
    - file.inFolder(this.file.folder)
    - file.path != "projetos/index.md"
formulas:
  Título: link(file, title)
views:
  - type: table
    name: Tabela
    order:
      - formula.Título
      - quantidade
      - description
    sort:
      - property: quantidade
        direction: DESC

```
