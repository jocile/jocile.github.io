---
title: Conjuntos em Python
date: 2026-09-20
draft: false
tags:
  - diagrama
  - programador/Python/estruturas
description: Guia sobre o funcionamento da estrutura de dados set (conjunto) em Python, incluindo criação, manipulação, métodos matemáticos e iteração.
aliases:
  - Sets
---

## Objetivo Geral

- Entender o funcionamento da estrutura de dados `set`.

## Pré-requisitos

- Python 3
- VSCode

---

## Etapa 1: Criação e acesso aos dados

Um `set` é uma coleção que não possui objetos repetidos. Usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

### Criando sets

```python
set([1, 2, 3, 1, 3, 4])  # {1, 2, 3, 4}

set("abacaxi")  # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio"))  # {"gol", "celta", "palio"}
```

Conjuntos em Python não suportam indexação e nem fatiamento. Caso queira acessar os seus valores, é necessário converter o conjunto para lista.

### Acessando os dados

```python
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
```

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando `for`.

### Iterar conjuntos

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)
```

Às vezes é necessário saber qual o índice do objeto dentro do laço `for`. Para isso podemos usar a função `enumerate`.

### Função enumerate

```python
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

---

## Etapa 2: Métodos da classe set

### `.union`

```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)  # {1, 2, 3, 4}
```

### `.intersection`

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)  # {2, 3}
```

### `.difference`

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)  # {1}
conjunto_b.difference(conjunto_a)  # {4}
```

### `.symmetric_difference`

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)  # {1, 4}
```

### `.issubset`

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b)  # True
conjunto_b.issubset(conjunto_a)  # False
# todos os elementos de a estão presentes em b?
```

### `.issuperset`

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)  # False
conjunto_b.issuperset(conjunto_a)  # True
# todos os elementos de b estão presentes em a?
```

### `.isdisjoint`

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)  # True
conjunto_a.isdisjoint(conjunto_c)  # False
# conjuntos disjuntos ocorrem quando não existe intersecção
```

### `.add`

```python
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
sorteio.add(42)  # {1, 23, 25, 42}
sorteio.add(25)  # {1, 23, 25, 42}
```

### `.clear`

```python
sorteio = {1, 23}

sorteio  # {1,23}
sorteio.clear()
sorteio  # {}
```

### `.copy`

```python
sorteio = {1, 23}

sorteio  # {1, 23}
sorteio.copy()
sorteio  # {1, 23}
```

### `.discard`

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```

### `.pop`

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop()  # 0
numeros.pop()  # 1
numeros  # {2, 3, 4, 5, 6, 7, 8, 9}
```

### `.remove`

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0)  # 0
numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### `len`

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros)  # 10
```

### `in`

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros  # True
10 in numeros  # False
```

---

## Atividade Prática

Com base nos conhecimentos adquiridos, realize as seguintes tarefas:

1. **Criação:** Crie um conjunto chamado `frutas` contendo 5 nomes de frutas, sendo que uma delas deve ser inserida duas vezes (para testar o comportamento do set).
2. **Manipulação:** Utilize o método `.add()` para adicionar uma nova fruta ao conjunto e o método `.discard()` para remover uma fruta existente.
3. **Operações de Conjuntos:** Crie dois conjuntos: `conjunto_a = {1, 2, 3}` e `conjunto_b = {3, 4, 5}`. Realize a união, intersecção e diferença entre eles, imprimindo os resultados.
4. **Verificação:** Verifique se o elemento `3` está presente no `conjunto_a` utilizando o operador `in`.
