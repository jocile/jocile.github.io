---
title: Dicionários com Python soluções
date: 2026-09-21
draft: false
tags:
  - python
  - programador/Python/estruturas
description: "Soluções dos exercícios de dicionários em Python."
---

Solução dos exercícios propostos em [[uc1.07 - estrutura de dados com dicionarios]]

## Ex. 1

1. Criação: Crie um dicionário chamado `alunos` contendo 3 alunos como chaves e seus respectivos dicionários internos com `nome`, `idade` e `curso`.

```python
alunos = {
    "aluno1": {"nome": "Alice", "idade": 20, "curso": "Sistemas"},
    "aluno2": {"nome": "Bob", "idade": 22, "curso": "Redes"},
    "aluno3": {"nome": "Charlie", "idade": 21, "curso": "Dados"}
}
```

## Ex. 2

2. Acesso: Exiba no console o nome e o curso do primeiro aluno do dicionário `alunos`.

```python
primeira_chave = list(alunos.keys())[0]
print(f"Nome: {alunos[primeira_chave]['nome']} - Curso: {alunos[primeira_chave]['curso']}")
```

## Ex. 3

3. Métodos: Utilize o método `.update()` para adicionar um novo aluno ao dicionário `alunos`.

```python
alunos.update({"aluno4": {"nome": "Diana", "idade": 23, "curso": "Segurança"}})
```

## Ex. 4

4. Iteração: Utilize um laço `for` junto com o método `.items()` para imprimir cada chave e valor do dicionário `alunos` no formato: `Chave: X - Dados: Y`.

```python
for chave, valor in alunos.items():
    print(f"Chave: {chave} - Dados: {valor}")
```
