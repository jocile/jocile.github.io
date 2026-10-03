---
title: fetch e pull
description: A diferença fundamental entre esses comandos está em como eles lidam com as alterações
tags:
  - github
---

A diferença fundamental entre **`git fetch`** e **`git pull`** está em como eles lidam com as alterações existentes no repositório remoto e na sua cópia local.

Em termos simples: **`git pull` é, na verdade, um `git fetch` seguido de um `git merge`.**

---

## 🛠️ `git fetch` (Apenas baixa, sem alterar seu trabalho)

O `git fetch` vai até o repositório remoto e traz todos os novos commits, branches e referências para a sua máquina, **mas não altera nenhum código nos seus arquivos de trabalho nem na sua branch atual**.

- **O que faz:** Atualiza as branches remotas locais (ex.: `origin/main` ou `upstream/v5`).

- **Segurança:** É 100% seguro. Ele não gera conflitos e não substitui nada que você esteja editando no momento.

- **Para que serve:** Ideal para inspecionar o que mudou no projeto antes de decidir mesclar (_merge_) ou aplicar (_rebase_) no seu código.

**Fluxo de uso típico:**

```Bash
git fetch origin
git diff main origin/main   # Compara seu código com o que veio do servidor
```

---

## 🔄 `git pull` (Baixa e aplica as mudanças)

O `git pull` faz o trabalho completo de uma vez só: ele busca as atualizações do servidor (executa o `git fetch`) e **imediatamente tenta mesclar** (_merge_) essas novidades na branch em que você está trabalhando no momento.

- **O que faz:** `git fetch` + `git merge` (ou `git rebase`, se configurado).

- **Segurança:** Se você e outra pessoa alteraram o mesmo arquivo nas mesmas linhas, o `git pull` pode gerar **conflitos de merge** que você precisará resolver na hora.

- **Para que serve:** É a forma mais rápida de atualizar seu ambiente de trabalho quando você já sabe que quer integrar tudo o que está no servidor.

**Fluxo de uso típico:**

```Bash
git pull origin main
```

---

## 📊 Resumo Comparativo

|**Ação**|**git fetch**|**git pull**|
|---|---|---|
|**Baixa novos commits do remoto?**|Sim|Sim|
|**Atualiza suas branches de acompanhamento (`origin/...`)?**|Sim|Sim|
|**Modifica seus arquivos locais de trabalho?**|Não|**Sim**|
|**Pode gerar conflitos de merge na hora?**|Não|**Sim**|
|**Nível de controle/segurança**|Alto (permite revisar antes)|Direto (aplica imediatamente)|

## Referêncas

- [Pull Request: o que é, como fazer importância no GitHub](https://hub.asimov.academy/blog/pull-request/)
