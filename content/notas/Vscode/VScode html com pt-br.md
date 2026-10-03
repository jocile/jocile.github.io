---
title: "VScode html com pt-br"
date: 2026-09-22
draft: false
tags:
  - editando-codigo
  - vscode
description: "Modificar o atalho no vscode onde cria a estrutura básica do HTML para pt-BR."
---

Pra modificar o atalho no vscode onde cria a estrutura básica do HTML é bem simples:

1. Entre em configurações (CTRL + ,) 
2. procure por Emmet
3. Em Emmet: Preferences clique em `edit settings.json`
4. Cole o seguinte código no final depois da chave `},` o seguinte:

```
"emmet.variables":{
 "lang":"pt-BR",
 "charset":"UTF-8"
}
```

[[IDE VScode]]
