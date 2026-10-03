---
title: "Dicionários em Python"
date: 2026-09-21
draft: false
tags:
  - python
  - programacao
  - estruturas-de-dados
description: "Guia sobre o funcionamento da estrutura de dados dicionário em Python, incluindo criação, acesso, manipulação e métodos."
---

## Objetivo Geral

- Entender o funcionamento da estrutura de dados dicionário.

## Pré-requisitos

- Python 3
- VSCode

---

## Etapa 1: Criação e acesso aos dados

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: `{}`, e contêm uma lista de pares chave:valor separada por vírgulas.

### Criando dicionários

```python
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
```

Os dados são acessados e modificados através da chave.

### Acesso aos dados

```python
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]  # "Guilherme"
dados["idade"]  # 28
dados["telefone"]  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
```

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável (como strings e números).

### Dicionários aninhados

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
```

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando `for`.

### Iterar dicionários

```python
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
```

---

## Etapa 2: Métodos da classe dict

### `{}.clear`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
contatos  # {}
```

### `{}.copy`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"]  # {"nome": "Guilherme", "telefone": "3333-2221"}
copia["guilherme@gmail.com"]  # {"nome": "Gui"}
```

### `{}.fromkeys`

```python
dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
```

### `{}.get`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.get("chave")  # None
contatos.get("chave", {})  # {}
contatos.get("guilherme@gmail.com", {})  # {"nome": "Guilherme", "telefone": "3333-2221"}
```

### `{}.items`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
```

### `{}.keys`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.keys()  # dict_keys(['guilherme@gmail.com'])
```

### `{}.pop`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
```

### `{}.popitem`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
```

### `{}.setdefault`

```python
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
contato.setdefault("idade", 28)  # 28
```

### `{}.update`

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
```

### `{}.values`

```python
contatos.values()  # dict_values(...)
```

### `in`

```python
"guilherme@gmail.com" in contatos  # True
```

### `del`

```python
del contatos["guilherme@gmail.com"]["telefone"]
```

## Atividade Prática

Com base nos conhecimentos adquiridos, realize as seguintes tarefas:

1. **Criação:** Crie um dicionário chamado `alunos` contendo 3 alunos como chaves e seus respectivos dicionários internos com `nome`, `idade` e `curso`.
2. **Acesso:** Exiba no console o nome e o curso do primeiro aluno do dicionário `alunos`.
3. **Métodos:** Utilize o método `.update()` para adicionar um novo aluno ao dicionário `alunos`.
4. **Iteração:** Utilize um laço `for` junto com o método `.items()` para imprimir cada chave e valor do dicionário `alunos` no formato: `Chave: X - Dados: Y`.
