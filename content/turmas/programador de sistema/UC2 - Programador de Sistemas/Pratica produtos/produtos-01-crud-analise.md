---
title: "Gestão de Produtos 1: CRUD e análise com SQLite e Pandas"
date: 2026-10-27
draft: false
tags:
  - banco-de-dados
  - python/bd
  - sqlite
  - pandas
description: "Atividade guiada de CRUD com Python e SQLite: criar tabelas, inserir, consultar, atualizar, excluir e analisar o estoque com SQL e Pandas."
---

Nesta atividade você cria um banco relacional de **Gestão de Produtos e Categorias**, executa o ciclo completo do **CRUD** (Create, Read, Update, Delete) e responde a perguntas de negócio sobre o estoque usando SQL e Pandas.

> [!info] Ficha da atividade
>
> - **Ambiente:** [Google Colab](https://colab.research.google.com/)
> - **Tempo estimado:** 60 minutos
> - **Pré-requisitos:** noções de Python e do comando `SELECT`. O módulo `sqlite3` já vem com o Python, e o Pandas já está instalado no Colab.
> - **Resultado esperado:** um arquivo `gestao_produtos.db` com 3 categorias e 5 produtos, mais três consultas de análise respondidas.
> - **Próxima nota:** [[produtos-02-vendas-estoque|Vendas e estoque]]

## Objetivo

Desenvolver um script em Python que cria o banco, executa as operações de escrita de forma segura e responde a perguntas de análise sobre o estoque.

> [!tip] Cada passo em uma célula
> No Colab, coloque cada bloco de código em uma célula separada e execute na ordem. Se precisar recomeçar, volte ao Passo 1 e execute tudo de novo. O Passo 2 recria as tabelas do zero.

## Passo a passo

### Passo 1: conectar ao banco

Importe as bibliotecas e abra a conexão com o arquivo `.db`. Se o arquivo não existir, o SQLite o cria automaticamente.

```python
import sqlite3
import pandas as pd

# Abre (ou cria) o banco de dados local
conn = sqlite3.connect("gestao_produtos.db")

# O cursor envia comandos SQL e recebe os resultados
cursor = conn.cursor()

print("Conexão estabelecida com sucesso!")
```

> [!warning] Erro de digitação cria outro banco
> Se você escrever `gestao_produto.db` (sem o "s"), o SQLite não avisa: cria um banco novo e vazio. Se aparecer `no such table`, confira o nome do arquivo.

### Passo 2: criar as tabelas (DDL)

Defina duas tabelas, `Categoria` e `Produto`, com **chave primária**, **chave estrangeira** e validações `CHECK`.

```python
# O SQLite só verifica chaves estrangeiras se você pedir, a cada conexão
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript('''
DROP TABLE IF EXISTS Vendas;
DROP TABLE IF EXISTS Produto;
DROP TABLE IF EXISTS Categoria;

CREATE TABLE Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);

CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL CHECK(estoque >= 0),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);
''')

conn.commit()
print("Tabelas 'Categoria' e 'Produto' criadas com sucesso!")
```

> [!danger] O DROP apaga dados
> Os comandos `DROP TABLE` no início do script apagam as tabelas e todo o conteúdo. Eles garantem que a atividade possa ser repetida sem duplicar registros, mas **nunca** devem ser usados assim em um sistema real.

### Passo 3: inserir registros (Create)

Para evitar **SQL Injection**, nunca monte o comando juntando textos. Use **marcadores de posição** (`?`) com `cursor.executemany()`, que insere vários registros de uma vez.

```python
categorias_iniciais = [
    ("Eletrônicos",),
    ("Móveis",),
    ("Vestuário",),
]

# (nome, preço, estoque, id_categoria)
produtos_iniciais = [
    ("Smartphone", 1500.00, 10, 1),
    ("Notebook", 3500.00, 5, 1),
    ("Sofá", 800.00, 3, 2),
    ("Cadeira de Escritório", 350.00, 12, 2),
    ("Camisa Polo", 80.00, 25, 3),
    ("Calça Jeans", 120.00, 15, 3),
]

cursor.executemany(
    "INSERT INTO Categoria (nome_categoria) VALUES (?);", categorias_iniciais
)
cursor.executemany(
    "INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);",
    produtos_iniciais,
)

conn.commit()
print(f"{len(categorias_iniciais)} categorias e {len(produtos_iniciais)} produtos inseridos.")
```

> [!note] Por que o commit?
> Os comandos `INSERT`, `UPDATE` e `DELETE` ficam pendentes em uma transação. Sem `conn.commit()`, nada é gravado de forma definitiva no arquivo.

### Passo 4: consultar os dados (Read)

Use `SELECT` para recuperar as linhas e `fetchall()` para trazê-las ao Python.

```python
cursor.execute("SELECT id_produto, nome, preco, estoque FROM Produto;")
linhas = cursor.fetchall()

print("\n--- Lista de Produtos Cadastrados ---")
for id_p, nome, preco, estoque in linhas:
    print(f"ID: {id_p} | Produto: {nome} | Preço: R$ {preco:.2f} | Estoque: {estoque}")
```

> [!example] Saída esperada
>
> ```text
> ID: 1 | Produto: Smartphone | Preço: R$ 1500.00 | Estoque: 10
> ID: 2 | Produto: Notebook | Preço: R$ 3500.00 | Estoque: 5
> ID: 3 | Produto: Sofá | Preço: R$ 800.00 | Estoque: 3
> ID: 4 | Produto: Cadeira de Escritório | Preço: R$ 350.00 | Estoque: 12
> ID: 5 | Produto: Camisa Polo | Preço: R$ 80.00 | Estoque: 25
> ID: 6 | Produto: Calça Jeans | Preço: R$ 120.00 | Estoque: 15
> ```

### Passo 5: atualizar e excluir (Update e Delete)

Edições e remoções pontuais sempre usam a cláusula `WHERE`. Sem ela, o comando atinge **todas** as linhas da tabela.

```python
# 1. Atualizar o preço de um produto
cursor.execute(
    "UPDATE Produto SET preco = ? WHERE nome = ?;", (1600.00, "Smartphone")
)
print("Linhas atualizadas:", cursor.rowcount)

# 2. Excluir um produto
cursor.execute("DELETE FROM Produto WHERE nome = ?;", ("Calça Jeans",))
print("Linhas excluídas:", cursor.rowcount)

conn.commit()
```

> [!tip] Confira o `rowcount`
> Se `rowcount` for `0`, o `WHERE` não encontrou nada, normalmente por erro de digitação no nome. O SQLite não considera isso um erro, então a verificação é sua.

Execute novamente o código do Passo 4 e confirme que o Smartphone custa R$ 1600,00 e que a Calça Jeans sumiu.

### Passo 6: análise de dados

Agora cruze as tabelas com `JOIN` e use funções de agregação para responder perguntas de negócio.

#### Pergunta 1 (SQL): qual o valor investido em estoque por categoria?

```python
query_estoque_categoria = """
SELECT
    c.nome_categoria,
    COUNT(p.id_produto) AS total_produtos,
    SUM(p.preco * p.estoque) AS valor_total_estoque
FROM Categoria c
JOIN Produto p ON c.id_categoria = p.id_categoria
GROUP BY c.nome_categoria
ORDER BY valor_total_estoque DESC;
"""

cursor.execute(query_estoque_categoria)
print("\n--- Valor Total de Estoque por Categoria ---")
for categoria, qtd, valor in cursor.fetchall():
    print(f"Categoria: {categoria} | Variedade: {qtd} item(ns) | Valor em Estoque: R$ {valor:.2f}")
```

> [!example] Resultado esperado
>
> | Categoria | Itens | Valor em estoque |
> | --- | --- | --- |
> | Eletrônicos | 2 | R$ 33.500,00 |
> | Móveis | 2 | R$ 6.600,00 |
> | Vestuário | 1 | R$ 2.000,00 |

#### Pergunta 2 (Pandas): qual o resumo estatístico dos preços e estoques?

O Pandas lê o resultado de uma consulta direto em um `DataFrame` com `pd.read_sql_query()`.

```python
df_produtos = pd.read_sql_query("""
    SELECT p.nome, p.preco, p.estoque, c.nome_categoria
    FROM Produto p
    JOIN Categoria c ON p.id_categoria = c.id_categoria
""", conn)

print("\n--- Visão Geral do DataFrame ---")
print(df_produtos.head())

print("\n--- Resumo Estatístico ---")
print(df_produtos.describe())
```

> [!example] Resultado esperado
> No `describe()`, a coluna `preco` deve mostrar média **1266.00** e a coluna `estoque`, média **11.00**, ambas com `count` igual a 5.

### Passo 7: fechar a conexão

Encerre o cursor e a conexão para liberar os recursos.

```python
cursor.close()
conn.close()
print("Conexão encerrada com segurança.")
```

## Exercícios de fixação

> [!question] Exercício 1
> Liste os produtos com **estoque menor que 10**, do menor para o maior estoque. (Reabra a conexão antes, repetindo o Passo 1.)

> [!success]- Solução do exercício 1
>
> ```python
> cursor.execute("SELECT nome, estoque FROM Produto WHERE estoque < ? ORDER BY estoque;", (10,))
> print(cursor.fetchall())
> # [('Sofá', 3), ('Notebook', 5)]
> ```

> [!question] Exercício 2
> Com o `DataFrame` `df_produtos`, calcule o **preço médio por categoria**.

> [!success]- Solução do exercício 2
>
> ```python
> print(df_produtos.groupby("nome_categoria")["preco"].mean())
> # Eletrônicos    2550.0
> # Móveis          575.0
> # Vestuário        80.0
> ```

> [!question] Exercício 3
> Tente inserir um produto com **preço negativo**. O que acontece e por quê?

> [!success]- Solução do exercício 3
> O banco recusa a linha com `sqlite3.IntegrityError: CHECK constraint failed`, porque a coluna `preco` foi definida com `CHECK(preco >= 0.0)`. A regra de negócio fica protegida no próprio banco, mesmo que o código Python esqueça de validar.

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| Inseriu um produto com `id_categoria` inexistente e nada aconteceu | `PRAGMA foreign_keys = ON` não foi executado nesta conexão | Execute o `PRAGMA` toda vez que abrir uma conexão |
| Os dados somem ao reabrir o banco | `commit()` esquecido | Chame `conn.commit()` após `INSERT`, `UPDATE` e `DELETE` |
| `Cannot operate on a closed database` | Executou uma célula depois do Passo 7 | Repita o Passo 1 para abrir nova conexão |
| `no such table` | Banco aberto com nome errado ou tabelas ainda não criadas | Confira o nome do arquivo e execute o Passo 2 |
| Registros duplicados | Executou o Passo 3 duas vezes sem recriar as tabelas | Execute a partir do Passo 2, que recria tudo |

## Checklist de verificação

- [ ] O arquivo `gestao_produtos.db` foi criado
- [ ] O Passo 4 lista 6 produtos antes do Passo 5
- [ ] Após o Passo 5, o Smartphone custa R$ 1600,00 e a Calça Jeans não aparece
- [ ] A Pergunta 1 retorna Eletrônicos como categoria de maior valor em estoque
- [ ] A conexão foi fechada no Passo 7
- [ ] Os três exercícios de fixação foram resolvidos

>>[!done] [Resolução no Google Colab - atividade-produtos.ipynb - Colab](https://colab.research.google.com/drive/1sMVT0nM1iLU0fDJ3lrhq5io5IjTUC5zQ?usp=sharing)

## Próximo passo

Continue em [[produtos-02-vendas-estoque|Vendas e estoque]], onde você adiciona a tabela de vendas e descobre o produto mais vendido.
