---
title: Aquitetura de Sistemas
description: A arquitetura de software projeta e documenta o sistema, define o que vai ser usado (requisitos) e o que não vai ser usado - evitando perda de tempo, focando na estratégia e estrutura global do sistema, tomando as decisões técnicas de alto nível que definem como o software será sustentável a longo prazo.
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

