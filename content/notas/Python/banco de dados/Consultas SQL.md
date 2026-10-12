---
title: Consultas Sql
description: '!Consultas SQL-1751482986700.png'
date: '2026-09-17'
draft: false
tags:
  - banco-de-dados
---

![[Consultas SQL-1751482986700.png]]

>[!note] 1- Comece pelo básico: SELECT
> `SELECT nome, idade`
> `FROM clientes;`

>[!note] 2- Filtre dados com WHERE
> `SELECT * FROM pedidos`
> `WHERE status = 'entregue;`

>[!note] 3- Organize com ORDERBY
> `SELECT * FROM produtos`
> `ORDER BY preco DESC;`

>[!note] 4- Limite com LIMIT
> `SELECT * FROM usuarios`
> `LIMIT 10;`

>[!note] 5- Combine condições: AND & OR
> `SELECT * FROM vendas`
> `WHERE preco > 100`
> `AND data = = '2025-01-1';`

>[!caution] 6- Evite `SELECT *` em produção
> 🚫Use apenas as colunas necessârias para melhorar performance

>[!note] 7- Buscas parciais com LIKE
> `SELECT * FROM clientes`
> `WHERE nome LIKE 'JO%;`

>[!note] 8- Agrupe com GROUP BY
> `SELECT departamento,`
> `COUNT(*) FROM`
> `funcionarios GROUP`
> `BY departamento`
