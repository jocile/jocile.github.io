---
title: "Gestão de Produtos 2: vendas e controle de estoque"
date: 2026-10-27
draft: false
tags:
  - banco-de-dados
  - python/bd
  - sqlite
  - pandas
description: "Desafio com SQLite: criar a tabela Vendas com chave estrangeira, registrar vendas com baixa de estoque em transação e descobrir o produto mais vendido."
---

Até aqui o banco só guarda produtos. Nesta atividade você registra **vendas**, dá baixa no estoque de forma segura e descobre qual produto é o campeão de vendas.

> [!info] Ficha da atividade
>
> - **Ambiente:** Google Colab
> - **Tempo estimado:** 40 minutos
> - **Pré-requisito:** [[produtos-01-crud-analise|Nota 1]] concluída (arquivo `gestao_produtos.db` com 5 produtos)
> - **Resultado esperado:** tabela `Vendas` com 6 registros, estoque atualizado e o ranking de vendas por produto
> - **Próxima nota:** [[produtos-03-visualizacao|Visualização]]

> [!tip]- Perdeu o banco? Recomece daqui
> Se o ambiente do Colab foi reiniciado, execute este script para recriar exatamente o estado ao final da Nota 1.
>
> ```python
> import sqlite3
>
> conn = sqlite3.connect("gestao_produtos.db")
> conn.execute("PRAGMA foreign_keys = ON;")
> conn.executescript('''
> DROP TABLE IF EXISTS Vendas;
> DROP TABLE IF EXISTS Produto;
> DROP TABLE IF EXISTS Categoria;
>
> CREATE TABLE Categoria (
>     id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
>     nome_categoria TEXT NOT NULL
> );
> CREATE TABLE Produto (
>     id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
>     nome TEXT NOT NULL,
>     preco REAL NOT NULL CHECK(preco >= 0.0),
>     estoque INTEGER NOT NULL CHECK(estoque >= 0),
>     id_categoria INTEGER,
>     FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
> );
>
> INSERT INTO Categoria (nome_categoria) VALUES ('Eletrônicos'), ('Móveis'), ('Vestuário');
> INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES
>     ('Smartphone', 1600.00, 10, 1),
>     ('Notebook', 3500.00, 5, 1),
>     ('Sofá', 800.00, 3, 2),
>     ('Cadeira de Escritório', 350.00, 12, 2),
>     ('Camisa Polo', 80.00, 25, 3);
> ''')
> conn.close()
> print("Base restaurada.")
> ```

## Desafio

> [!question] O que você deve fazer
>
> 1. Crie a tabela `Vendas` com `id_venda`, `id_produto` (chave estrangeira para `Produto`), `quantidade` (maior que zero) e `data_venda` (preenchida automaticamente).
> 2. Registre as vendas abaixo e **dê baixa no estoque** de cada produto vendido.
> 3. Descubra o **produto mais vendido** em unidades.
>
> | id_produto | Produto | Quantidade |
> | --- | --- | --- |
> | 1 | Smartphone | 3 |
> | 2 | Notebook | 2 |
> | 1 | Smartphone | 4 |
> | 3 | Sofá | 1 |
> | 4 | Cadeira de Escritório | 5 |
> | 5 | Camisa Polo | 10 |

Antes de abrir a solução, pense nestas perguntas:

- Em qual ordem devem acontecer o registro da venda e a baixa do estoque?
- O que deve acontecer se faltar estoque para uma venda?
- Como garantir que a venda e a baixa aconteçam **juntas ou não aconteçam**?

> [!tip]- Dica 1: transação
> Em `sqlite3`, o bloco `with conn:` confirma (`commit`) tudo se não houver erro e desfaz (`rollback`) tudo se ocorrer uma exceção.

> [!tip]- Dica 2: proteção contra estoque negativo
> A coluna `estoque` já tem `CHECK(estoque >= 0)`. Se o `UPDATE` deixar o estoque negativo, o banco levanta `IntegrityError` e a transação inteira é desfeita.

## Solução

> [!success]- Solução completa (tente antes de abrir)
> **1. Criar a tabela `Vendas`**
>
> ```python
> import sqlite3
> import pandas as pd
>
> conn = sqlite3.connect("gestao_produtos.db")
> conn.execute("PRAGMA foreign_keys = ON;")
> cursor = conn.cursor()
>
> cursor.execute('''
> CREATE TABLE IF NOT EXISTS Vendas (
>     id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
>     id_produto INTEGER NOT NULL,
>     quantidade INTEGER NOT NULL CHECK(quantidade > 0),
>     data_venda TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
>     FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
> );
> ''')
> conn.commit()
> print("Tabela 'Vendas' criada com sucesso!")
> ```
>
> **2. Registrar vendas e dar baixa no estoque**
>
> Execute esta etapa **uma única vez**. Rodá-la de novo registra as vendas em duplicidade e baixa o estoque duas vezes. Para repetir, use o script de restauração do início da nota.
>
> ```python
> def registrar_venda(conn, id_produto, quantidade):
>     """Baixa o estoque e registra a venda na mesma transação."""
>     with conn:  # commit se der certo, rollback se der erro
>         conn.execute(
>             "UPDATE Produto SET estoque = estoque - ? WHERE id_produto = ?;",
>             (quantidade, id_produto),
>         )
>         conn.execute(
>             "INSERT INTO Vendas (id_produto, quantidade) VALUES (?, ?);",
>             (id_produto, quantidade),
>         )
>
>
> novas_vendas = [(1, 3), (2, 2), (1, 4), (3, 1), (4, 5), (5, 10)]
>
> for id_produto, quantidade in novas_vendas:
>     try:
>         registrar_venda(conn, id_produto, quantidade)
>     except sqlite3.IntegrityError as erro:
>         print(f"Venda recusada ({id_produto}, {quantidade}): {erro}")
>
> print("Processamento de vendas concluído.")
> ```
>
> **3. Produto mais vendido (SQL)**
>
> ```python
> query_campeao = """
> SELECT
>     p.id_produto,
>     p.nome AS produto,
>     c.nome_categoria AS categoria,
>     SUM(v.quantidade) AS total_unidades_vendidas,
>     SUM(v.quantidade * p.preco) AS faturamento_total
> FROM Vendas v
> INNER JOIN Produto p ON v.id_produto = p.id_produto
> INNER JOIN Categoria c ON p.id_categoria = c.id_categoria
> GROUP BY p.id_produto, p.nome, c.nome_categoria
> ORDER BY total_unidades_vendidas DESC
> LIMIT 1;
> """
>
> cursor.execute(query_campeao)
> resultado = cursor.fetchone()
>
> if resultado:
>     id_p, nome, categoria, total_qtd, faturamento = resultado
>     print("\n--- PRODUTO MAIS VENDIDO ---")
>     print(f"Produto: {nome} (ID: {id_p})")
>     print(f"Categoria: {categoria}")
>     print(f"Unidades vendidas: {total_qtd}")
>     print(f"Faturamento gerado: R$ {faturamento:.2f}")
> ```
>
> **4. Ranking completo (Pandas)**
>
> ```python
> query_ranking = """
> SELECT
>     p.nome AS Produto,
>     c.nome_categoria AS Categoria,
>     p.preco AS Preco_Unitario,
>     SUM(v.quantidade) AS Qtd_Vendida,
>     SUM(v.quantidade * p.preco) AS Faturamento_Total,
>     p.estoque AS Estoque_Restante
> FROM Produto p
> LEFT JOIN Vendas v ON p.id_produto = v.id_produto
> LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
> GROUP BY p.id_produto, p.nome, c.nome_categoria
> ORDER BY Qtd_Vendida DESC;
> """
>
> df_vendas = pd.read_sql_query(query_ranking, conn)
>
> # Produtos sem nenhuma venda aparecem com NULL; troque por zero
> df_vendas["Qtd_Vendida"] = df_vendas["Qtd_Vendida"].fillna(0).astype(int)
> df_vendas["Faturamento_Total"] = df_vendas["Faturamento_Total"].fillna(0.0)
>
> print("\n--- RANKING DE VENDAS POR PRODUTO ---")
> print(df_vendas.to_string(index=False))
>
> conn.close()
> ```

> [!example] Resultado esperado
> O produto mais vendido deve ser a **Camisa Polo**, com 10 unidades e R$ 800,00 de faturamento. O ranking completo:
>
> | Produto | Qtd. vendida | Faturamento | Estoque restante |
> | --- | --- | --- | --- |
> | Camisa Polo | 10 | R$ 800,00 | 15 |
> | Smartphone | 7 | R$ 11.200,00 | 3 |
> | Cadeira de Escritório | 5 | R$ 1.750,00 | 7 |
> | Notebook | 2 | R$ 7.000,00 | 3 |
> | Sofá | 1 | R$ 800,00 | 2 |

## Por que usar uma transação?

Registrar a venda e baixar o estoque são duas operações que precisam acontecer **juntas**. Se apenas uma delas fosse gravada, o banco ficaria inconsistente: estoque reduzido sem venda registrada, ou venda registrada sem baixa.

O bloco `with conn:` garante essa propriedade, chamada de **atomicidade**: ou as duas operações são confirmadas, ou nenhuma é.

## Experimentos

Reabra a conexão (lembre-se do `PRAGMA foreign_keys = ON`) e teste os cenários abaixo.

> [!question] Experimento 1: estoque insuficiente
> Tente registrar a venda de **100 notebooks**: `registrar_venda(conn, 2, 100)`. Depois, consulte o estoque do Notebook e a tabela `Vendas`. O que mudou?

> [!success]- Resultado do experimento 1
> O `UPDATE` deixaria o estoque negativo e viola o `CHECK(estoque >= 0)`. O banco levanta `IntegrityError`, o `with conn:` desfaz a transação e **nada muda**: o estoque do Notebook continua em 3 e nenhuma linha nova aparece em `Vendas`.

> [!question] Experimento 2: excluir produto com vendas
> Tente excluir o Smartphone com `DELETE FROM Produto WHERE id_produto = 1;`. O que acontece?

> [!success]- Resultado do experimento 2
> O banco recusa com `IntegrityError: FOREIGN KEY constraint failed`, pois existem vendas apontando para esse produto. Isso protege o histórico. Em sistemas reais, em vez de excluir, costuma-se marcar o produto como inativo.

## Análise de dados

Use o `df_vendas` para responder:

1. Qual produto gerou o **maior faturamento**?
2. Qual **categoria** vendeu mais unidades?
3. Qual **categoria** teve o maior faturamento?

> [!success]- Respostas esperadas
>
> 1. **Smartphone**, com R$ 11.200,00. O produto mais vendido em unidades (Camisa Polo) *não* é o que mais fatura.
> 2. **Vestuário**, com 10 unidades (Eletrônicos vendeu 9 e Móveis, 6).
> 3. **Eletrônicos**, com R$ 18.200,00.

## Desafio extra

> [!question] O faturamento está correto?
> A consulta calcula o faturamento com `p.preco`, o preço **atual** do produto. O que acontece com o histórico de vendas se o preço do Smartphone mudar amanhã? Como alterar a tabela `Vendas` para guardar o preço praticado em cada venda?

> [!tip]- Dica
> Acrescente uma coluna `preco_unitario` em `Vendas`, preenchida no momento da venda com o preço do produto, e some `quantidade * preco_unitario` no cálculo do faturamento.

## Checklist de verificação

- [ ] A tabela `Vendas` tem chave estrangeira para `Produto`
- [ ] Os 6 registros de venda foram inseridos uma única vez
- [ ] O estoque final é: Smartphone 3, Notebook 3, Sofá 2, Cadeira 7, Camisa Polo 15
- [ ] O produto mais vendido é a Camisa Polo (10 unidades)
- [ ] O experimento de estoque insuficiente não alterou nenhum dado
- [ ] O experimento de exclusão foi recusado pelo banco

## Próximo passo

Continue em [[produtos-03-visualizacao|Visualização]] para transformar o ranking em gráfico.
