---
title: 🧑‍💼 Minhas turmas
description: "Minhas turmas no [SENAC](https://cursos.ce.senac.br/unidade/senac-sobral/)"
---

## Acompanhe aqui o cronograma e materiais usados nas aulas

```base
filters:
  and:
    - file.tags.contains("turma")
    - file.inFolder(this.file.folder)
formulas:
  Título: link(file, title)
properties:
  note.description:
    displayName: descrição
views:
  - type: table
    name: Tabela
    order:
      - formula.Título
      - status
      - Carga-horária
      - description
    sort:
      - property: formula.Título
        direction: ASC
    columnSize:
      note.title: 293
      note.status: 92

```
