---
title: "Listas em Python"
date: 2026-09-17
draft: false
tags:
  - python
  - programador/Python/estruturas
description: "Guia completo sobre a estrutura de dados lista em Python, incluindo criação, acesso, fatiamento, iteração, compreensão de listas e métodos da classe list."
---

Em Python, listas e vetores são tipos de dados que permitem armazenar uma coleção de elementos, como números, strings, objetos, entre outros.

Uma lista é uma sequência ordenada e mutável de elementos, onde cada elemento é identificado por um índice. É possível adicionar, remover e alterar elementos da lista. Para criar uma lista em Python, basta colocar os elementos entre colchetes, separados por vírgulas:

`minha_lista = [1, 2, 3, 4, 5]`

Um vetor é um tipo especial de lista, que possui elementos todos do mesmo tipo e pode ser acessado diretamente por seu índice. Em Python, a biblioteca NumPy fornece suporte para vetores e operações numéricas em arrays. Para criar um vetor em NumPy, é necessário importar a biblioteca e utilizar a função `array()`:

```java
import numpy as np

meu_vetor = np.array([1, 2, 3, 4, 5])

```

Diferentemente das listas comuns, os vetores em NumPy são otimizados para operações numéricas e matemáticas, além de serem mais eficientes em termos de memória. Além disso, os vetores podem ter mais de uma dimensão, possibilitando o armazenamento de matrizes e tensores.

## Exemplos

### Criando uma lista e acessando elementos:

```python
lista = ['maçã', 'banana', 'laranja']
print(lista[0]) # imprime 'maçã'
print(lista[1]) # imprime 'banana'
print(lista[2]) # imprime 'laranja'
```

### Adicionando elementos a uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
lista.append('uva')
print(lista) # imprime ['maçã', 'banana', 'laranja', 'uva']
```

### Removendo elementos de uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
lista.remove('banana')
print(lista) # imprime ['maçã', 'laranja']
```

### Iterando sobre uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
for fruta in lista:
  print(fruta) # imprime 'maçã', 'banana', 'laranja' em linhas separadas
```

### Ordenando uma lista:

```python
lista = [3, 6, 1, 8, 2, 10]
lista.sort()
print(lista) # imprime [1, 2, 3, 6, 8, 10]
```

## Exercícios

1. Crie um programa que receba uma lista de números e retorne o maior valor dessa lista.
2. Crie um programa que receba uma lista de números e retorne a soma de todos os valores.
3. Crie um programa que receba duas listas e retorne uma terceira lista com a interseção dos elementos das duas listas.
4. Crie um programa que receba uma lista de números e retorne uma lista com os números pares dessa lista.
5. Crie um programa que receba uma lista de nomes e retorne uma nova lista com os nomes em ordem alfabética.
6. Crie um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números positivos.
7. Crie um programa que receba uma lista de nomes e retorne uma nova lista contendo apenas os nomes que começam com a letra 'A'.
8. Crie um programa que receba uma lista de números e retorne o segundo maior número da lista.
9. Crie um programa que receba uma lista de nomes e retorne o nome mais longo da lista.
10. Crie um programa que receba uma lista de números e retorne o número que aparece com maior frequência na lista.

## Resolução

![Listas com Python solucoes](Listas%20com%20Python%20solucoes.md)

## Referências

#programador/Python 

- [Coleções no Python: Listas, Tuplas e Dicionários](https://www.devmedia.com.br/colecoes-no-python-listas-tuplas-e-dicionarios/40678)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [[Listas]]

![Referencias sobre Python](Referencias%20sobre%20Python.md)
