---
title: "Gestão de Produtos: roteiro da atividade"
date: 2026-10-27
draft: false
tags:
  - banco-de-dados
  - python/bd
  - sqlite
description: "Roteiro de cinco práticas que levam um banco SQLite de produtos do CRUD até uma aplicação web com login, usando Python, Pandas e Bottle."
---

Esta sequência de atividades parte de um banco de dados vazio e termina em uma aplicação web protegida por login. Cada nota depende da anterior e entrega algo que será reaproveitado na próxima.

> [!abstract] O que você vai construir
> Um sistema de **Gestão de Produtos e Categorias** com banco SQLite, controle de estoque, análise de vendas, gráfico, API JSON, relatório em HTML e acesso restrito por usuário e senha.

## Sequência

| Nota | Tema | Ambiente | Tempo |
| --- | --- | --- | --- |
| [[produtos-01-crud-analise\|1. CRUD e análise de dados]] | Tabelas, inserção, consulta, atualização, exclusão, SQL e Pandas | Google Colab | 60 min |
| [[produtos-02-vendas-estoque\|2. Vendas e estoque]] | Chave estrangeira, transação e produto mais vendido | Google Colab | 40 min |
| [[produtos-03-visualizacao\|3. Visualização]] | Gráfico de barras e exportação do PNG | Google Colab | 30 min |
| [[produtos-04-api-bottle\|4. API e relatório com Bottle]] | Rota JSON, página HTML e arquivos estáticos | Computador local | 50 min |
| [[produtos-05-autenticacao\|5. Autenticação]] | Hash de senha, cookie assinado e rota protegida | Computador local | 60 min |

## Onde cada parte roda

> [!warning] O Bottle não funciona no Colab
> O Colab executa seu código em um servidor remoto do Google. Quando o Bottle informa `localhost:8080`, esse endereço aponta para a máquina do Google, e não para o seu navegador. Por isso, as notas 1 a 3 usam o Colab, e as notas 4 e 5 devem ser feitas **no seu computador**, com VS Code e terminal.

**Para as notas 1 a 3:** uma conta Google e o [Google Colab](https://colab.research.google.com/).

**Para as notas 4 e 5:**

- Python 3.10 ou superior
- VS Code (ou outro editor) e um terminal
- Pacote `bottle` na versão 0.13 ou superior

## Como estudar

- Tente resolver cada **desafio** antes de abrir a solução.
- As soluções ficam em blocos recolhidos, como este:

> [!success]- Exemplo de solução recolhida
> Clique no título do bloco para abrir ou fechar.

- Ao final de cada nota, marque o checklist de verificação. Se algum item falhar, consulte a seção **Erros comuns**.

## Mapa CRUD

O mesmo conjunto de operações aparece em quatro camadas ao longo das notas:

| Operação | SQL | Python (`sqlite3`) | HTTP (Bottle) |
| --- | --- | --- | --- |
| Create | `INSERT` | `execute` / `executemany` + `commit` | `POST` |
| Read | `SELECT` | `execute` + `fetchall` / `fetchone` | `GET` |
| Update | `UPDATE` | `execute` + `commit` | `PUT` / `PATCH` |
| Delete | `DELETE` | `execute` + `commit` | `DELETE` |

## Critérios de avaliação (sugestão)

| Critério | O que evidencia | Nota |
| --- | --- | --- |
| Modelagem | Tabelas com chave primária, chave estrangeira e `CHECK` funcionando | 1 e 2 |
| Segurança de dados | Uso de `?` nas consultas, sem montar SQL por concatenação | 1 a 5 |
| Integridade | Venda e baixa de estoque na mesma transação, com `rollback` testado | 2 |
| Análise | Respostas corretas às perguntas de negócio | 1 a 3 |
| Comunicação visual | Gráfico com título, rótulos e destaque coerentes | 3 |
| Aplicação web | API e página funcionando, com acentos corretos | 4 |
| Autenticação | Senha armazenada como hash, rota protegida, segredo fora do código | 5 |

> [!tip] Ajuste os pesos
> A tabela indica *o que observar*. Defina a pontuação de cada critério conforme a carga horária e o objetivo da sua turma.
