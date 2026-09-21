---
title: Listas com Python soluções
date: 2026-09-17
draft: false
tags:
  - python
  - programador/Python/estruturas
description: "Soluções dos exercícios de listas e métodos da classe list."
---

Solução dos exercícios propostos em [Exercícios](Listas%20com%20Python.md#Exercícios)

## Ex. 1

1. Crie um programa que receba uma lista de números e retorne o maior valor dessa lista.

```python
lista = [3, 7, 1, 9, 5]
maior = lista[0]
for numero in lista:
  if numero > maior:
    maior = numero
print(f"O maior número da lista é {maior}")
```

## Ex. 2

2. Crie um programa que receba uma lista de números e retorne a soma de todos os valores.

```python
lista = [3, 7, 1, 9, 5]
soma = 0
for numero in lista:
  soma += numero
print(f"A soma dos valores da lista é {soma}")
```

## Ex. 3

3. Crie um programa que receba duas listas e retorne uma terceira lista com a interseção dos elementos das duas listas.

```python
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 5, 7, 9, 11]
intersecao = []
for elemento in lista1:
  if elemento in lista2:
    intersecao.append(elemento)
print(f"A interseção das duas listas é {intersecao}")
```

## Ex. 4

4. Crie um programa que receba uma lista de números e retorne uma lista com os números pares dessa lista.

```python
lista = [3, 7, 1, 9, 5, 2, 8, 4]
pares = []
for numero in lista:
  if numero % 2 == 0:
    pares.append(numero)
print(f"Os números pares da lista são {pares}")
```

## Ex. 5

5. Crie um programa que receba uma lista de nomes e retorne uma nova lista com os nomes em ordem alfabética.

```python
lista = ['João', 'Ana', 'Pedro', 'Maria', 'Mariana']
lista_ordenada = sorted(lista)
print(f"A lista em ordem alfabética é {lista_ordenada}")
```

## Ex. 6

6. Crie um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números positivos.

```python
lista = [-2, 4, -5, 7, 0, 2, -1]
lista_positivos = []
for numero in lista:
    if numero > 0:
        lista_positivos.append(numero)
print(f"A lista de números positivos é {lista_positivos}")
```

## Ex. 7

7. Crie um programa que receba uma lista de nomes e retorne uma nova lista contendo apenas os nomes que começam com a letra 'A'.

```python
lista = ['Ana', 'João', 'André', 'Mariana', 'Felipe']
lista_A = []
for nome in lista:
    if nome[0] == 'A':
        lista_A.append(nome)
print(f"A lista de nomes que começam com 'A' é {lista_A}")
```

## Ex. 8

8. Crie um programa que receba uma lista de números e retorne o segundo maior número da lista.

```python
lista = [5, 2, 9, 1, 7, 3]
maior = max(lista)
segundo_maior = lista[0]
for numero in lista:
    if numero != maior and numero > segundo_maior:
        segundo_maior = numero
print(f"O segundo maior número da lista é {segundo_maior}")
```

## Ex. 9

9. Crie um programa que receba uma lista de nomes e retorne o nome mais longo da lista.

```python
lista = ['Ana', 'João', 'André', 'Mariana', 'Felipe']
maior_nome = lista[0]
for nome in lista:
    if len(nome) > len(maior_nome):
        maior_nome = nome
print(f"O maior nome da lista é {maior_nome}")
```

## Ex. 10

10. Crie um programa que receba uma lista de números e retorne o número que aparece com maior frequência na lista.

```python
lista = [3, 2, 5, 3, 7, 3, 5, 2, 5, 5]
frequencias = {}
for numero in lista:
    if numero in frequencias:
        frequencias[numero] += 1
    else:
        frequencias[numero] = 1
mais_frequente = lista[0]
for numero, frequencia in frequencias.items():
    if frequencia > frequencias[mais_frequente]:
        mais_frequente = numero
print(f"O número mais frequente na lista é {mais_frequente}")
```

#programador/Python/estruturas
