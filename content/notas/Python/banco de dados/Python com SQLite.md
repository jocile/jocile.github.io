---
title: Python Com Sqlite
description: Funções para manipular tabelas no SQLite.
date: '2026-09-17'
draft: false
tags:
  - banco-de-dados
  - Python
---

Funções para manipular tabelas no SQLite.

Para adicionar comandos SQL importamos o módulo `sqlite3`, e usamos a função `cursor.execute()`.

## Criar Banco de dados

```python
import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "teste_banco.sqlite")
cursor = conexao.cursor()
```

## Criar tabela

```python
def criar_tabela(conexao, cursor):
	cursor.execute(
	"CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
	)
	conexao.commit()
criar_tabela(conexao, cursor)
```

## Inserir um registro

```python
def inserir_registro(conexao, cursor, nome, email):
	data = (nome, email)
	cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
	conexao.commit()
inserir_registro(conexao, cursor, "João", "joao@gmail.com")
```

## Atualizar um registro

```python
def atualizar_registro(conexao, cursor, nome, email, id):
	data = (nome, email, id)
	cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
	conexao.commit()
atualizar_registro(conexao, cursor, "João Atualizado", "joao.atualizado@gmail.com", 1)
```

## Inserir vários registros

```python
def inserir_varios(conexao, cursor, dados):
	cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
	conexao.commit()
dados = [
	("Guilherme", "guilherme@gmail.com"),
	("Chappie", "chappie@gmail.com"),
	("Melaine", "melaine@gmail.com"),
	]
inserir_varios(conexao, cursor, dados)
```

## Excluir um registro

```python
def excluir_registro(conexao, cursor, id):
	data = (id,)
	cursor.execute("DELETE FROM clientes WHERE id=?;", data)
	conexao.commit()
excluir_registro(conexao, cursor, 2)
```

## Recuperar um registro

```python
def recuperar_cliente(cursor, id):
	cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
	return cursor.fetchone()
cliente = recuperar_cliente(cursor, 5)
print(cliente)
```

## Recuperar um dicionário do registro

É necessário um novo cursor para converter a tupla em dicionário, para isso adicione:

`cursor.row_factory = sqlite3.Row`

```python

def recuperar_cliente(cursor, id):
	cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
	return cursor.fetchone()
cliente = recuperar_cliente(cursor, 5)
print(dict(cliente))
print(cliente["email"], cliente["id"], cliente["nome"])
print(f'Seja bem vindo ao sistema {cliente["nome"]}')
```

## Listar os nomes do dicionário de registros

```python
def listar_clientes(cursor):
	return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")
clientes = listar_clientes(cursor)
for cliente in clientes:
	print(dict(cliente))
```

>[!info] Para saber mais: [Python sqlite3 Module](https://www.w3schools.com/python/ref_module_sqlite3.asp)
