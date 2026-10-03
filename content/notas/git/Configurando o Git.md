---
title: "Configurando o Git"
date: 2026-09-22
tags:
  - git
  - github
  - programacao
  - configuracao
description: "Guia passo a passo para configuração inicial do Git, incluindo usuário, proxy e comandos básicos."
---

# Configurando o Git

Este guia consolida as instruções para preparar seu ambiente de desenvolvimento Git, combinando o guia prático e a explicação conceitual.

## 1. Preparação (Git Bash)

Certifique-se de ter o [Git for Windows](https://git-scm.com/download/win) instalado. Utilize o **Git Bash** para executar os comandos abaixo.

## 2. Configurações Iniciais

O Git permite definir configurações em três níveis:
*   **System:** Afeta todos os usuários do computador.
*   **Global:** Afeta todos os repositórios do seu usuário (Recomendado para nome e e-mail).
*   **Local:** Afeta apenas o repositório atual.

### Configurando Usuário e E-mail (Global)

Para que todos os seus commits sejam identificados corretamente:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Configurando Proxy (Se necessário)

Se estiver em uma rede com proxy, configure da seguinte forma:

```bash
git config --global http.proxy http://RA:Senha@ip-do-proxy:porta
git config --global https.proxy https://RA:Senha@ip-do-proxy:porta
```

> **Nota:** Para limpar as configurações de proxy ao final da aula:
> ```bash
> git config --global --unset http.proxy
> git config --global --unset https.proxy
> ```

### Alterando Branch Padrão

Para definir o nome da branch principal (ex: `main` ou `master`):

```bash
git config --global init.defaultBranch nome-da-branch
```

### Verificando Configurações

Para listar todas as configurações globais:

```bash
git config --global --list
```

## 3. Iniciando Projetos

### Criando um novo repositório local

1. Navegue até a pasta do projeto: `cd caminho/da/pasta`
2. Inicie o repositório:
```bash
git init
```

### Clonando um repositório existente

1. Navegue até a pasta de trabalho: `cd caminho/da/pasta`
2. Clone o repositório:
```bash
git clone <url-do-repositorio>
```

## 4. Referências

* [[Git Book](https://git-scm.com/book/en/v2)
* [[Git Guide](http://rogerdudler.github.io/git-guide/index.pt_BR.html)
* [[Configurando o Git detalhado]]
