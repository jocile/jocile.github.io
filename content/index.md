---
title: _🔭
description: Site de anotações sobre estudos do professor Jocilé
quartz-properties: false
enableToc: false

---

## Olá 👋

<span class="avatar-container">![[avatar.jpeg|150x150]]</span>

>[!info] 🔭 Sou o professor 🎓 [[Jocile|Jocilé]] e atualmente sou **Instrutor de Informática e Desenvolvimento de Sistemas** no 🏫 [SENAC CE](https://cursos.ce.senac.br/unidade/senac-sobral/).

- [👨‍🏫Sobre mim](https://github.com/jocile), meus [🗃projetos](https://jocile.github.io/site/projetos/), e [📚aulas passadas](https://jocile.github.io/site/blog/);
- [📖 Teologia - Páginas de estudos bíblicos](teologia/index);
- [🌐 Navegue pelas Tags (Tópicos)](/tags/).
- [👨🏻‍💻Aulas de Programador de Sistemas (Senac)](programador/index)

## Atualizações

```base
filters:
  and:
    - file.ext == "md"
formulas:
  days_alive: (today() - file.mtime).days.ceil()
  Data: (file.mtime).format("MM-DD")
properties:
  file.name:
    displayName: Notas recentes
  formula.days_alive:
    displayName: Dias atrás
  description:
    displayName: Descrição
views:
  - type: table
    name: Recentes
    order:
      - file.name
      - description
      - formula.Data
    limit: 10
```
