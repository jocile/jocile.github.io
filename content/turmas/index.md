---
title: 🧑‍💼 Minhas turmas
description: "Minhas turmas no [SENAC](https://cursos.ce.senac.br/unidade/senac-sobral/)"
---

## Acompanhe aqui o cronograma e materiais usados nas aulas

```base
filters:
  and:
    - file.tags.contains("turma")
    - file.folder.startsWith("turmas")
views:
  - type: table
    name: Tabela
    order:
      - title
      - status
      - Carga-horária
      - description
    sort:
      - property: title
        direction: ASC
    columnSize:
      note.title: 293
      note.status: 92

```
