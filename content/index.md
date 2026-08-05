---
title: _🔭
description: Site de anotações sobre estudos do professor Jocilé
quartz-properties: false
enableToc: false

---

## Olá 👋

<span class="avatar-container">![[avatar.jpeg|150x150]]</span>

>[!info] 🔭 Sou o professor 🎓 [[Jocile|Jocilé]] e atualmente sou **Instrutor de Informática e Desenvolvimento de Sistemas** no 🏫 [SENAC CE](https://psg.ce.senac.br/oportunidades/).

- [👨‍🏫Sobre mim](https://github.com/jocile), meus [🗃projetos](https://jocile.github.io/site/projetos/), e [📚aulas passadas](https://jocile.github.io/site/blog/);
- [📖 Teologia - Páginas de estudos bíblicos](teologia/index);
- [🌐 Navegue pelas Tags (Tópicos)](/tags/).
- [👨🏻‍💻Aulas de Programador de Sistemas (Senac)](turmas/programador%20de%20sistema/index.md)

```base
filters:
  and:
    - file.ext == "md"
    - formula.section != "tags"
    - file.name != "404"
    - "!formula.Data.isEmpty()"
    - file.folder != "private"
formulas:
  doc_type: |
    if(file.hasTag("teologia"), "teologia",
    if(file.hasTag("formacao"), "formação",
    if(file.inFolder("formacao"), "formação",
    if(file.inFolder("teologia"), "teologia",
    if(file.inFolder("programador"), "programador",
    if(file.inFolder("cli"), "cli", "guia"))))))
  last_modified: file.mtime.relative()
  section: |
    if(file.inFolder("Formacao"), "formação",
    if(file.inFolder("teologia"), "teologia",
    if(file.inFolder("programador"), "programador",
    if(file.inFolder("tags"), "tags", "core"))))
  Data: (file.mtime).format("MM-DD")
  days_alive: (today() - file.mtime).days.ceil()
properties:
  title:
    displayName: Título
  formula.doc_type:
    displayName: Tipo
  formula.last_modified:
    displayName: Atualizado
  formula.section:
    displayName: Seção
  note.title:
    displayName: Título
  description:
    displayName: descrição
  formula.days_alive:
    displayName: Dias atrás
views:
  - type: table
    name: Tabela
    order:
      - file.name
      - formula.Data
      - description
    sort:
      - property: formula.Data
        direction: DESC
    limit: 20

```

