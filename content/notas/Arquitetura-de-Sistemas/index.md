---
title: Aquitetura de Sistemas
description: A arquitetura de software projeta e documenta o sistema, define o que vai ser usado (requisitos) e o que não vai ser usado - evitando perda de tempo
tags:
  - base
---

```base
filters:
  and:
    - file.inFolder(this.file.folder)
    - file.name != "index"
views:
  - type: table
    name: Tabela
    order:
      - file.name
      - description
    sort:
      - property: channel
        direction: ASC

```

