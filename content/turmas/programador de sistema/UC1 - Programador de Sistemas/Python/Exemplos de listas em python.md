---
description: "criando algoritmos com listas para programas de computador resolvendo problemas"
tags:
  - python
  - listas
  - programacao
  - exercícios
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

Criando uma lista e acessando elementos:

```python
lista = ['maçã', 'banana', 'laranja']
print(lista[0]) # imprime 'maçã'
print(lista[1]) # imprime 'banana'
print(lista[2]) # imprime 'laranja'
```

Adicionando elementos a uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
lista.append('uva')
print(lista) # imprime ['maçã', 'banana', 'laranja', 'uva']
```

Removendo elementos de uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
lista.remove('banana')
print(lista) # imprime ['maçã', 'laranja']
```

Iterando sobre uma lista:

```python
lista = ['maçã', 'banana', 'laranja']
for fruta in lista:
  print(fruta) # imprime 'maçã', 'banana', 'laranja' em linhas separadas
```

Ordenando uma lista:

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

## Solução

1. Crie um programa que receba uma lista de números e retorne o maior valor dessa lista.

```python
lista = [3, 7, 1, 9, 5]
maior = lista[0]
for numero in lista:
  if numero > maior:
    maior = numero
print(f"O maior número da lista é {maior}")
```

2. Crie um programa que receba uma lista de números e retorne a soma de todos os valores.

```python
lista = [3, 7, 1, 9, 5]
soma = 0
for numero in lista:
  soma += numero
print(f"A soma dos valores da lista é {soma}")
```

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

%%

4. Crie um programa que receba uma lista de números e retorne uma lista com os números pares dessa lista.

```python
lista = [3, 7, 1, 9, 5, 2, 8, 4]
pares = []
for numero in lista:
  if numero % 2 == 0:
    pares.append(numero)
print(f"Os números pares da lista são {pares}")
```

5. Crie um programa que receba uma lista de nomes e retorne uma nova lista com os nomes em ordem alfabética.

```python
lista = ['João', 'Ana', 'Pedro', 'Maria', 'Mariana']
lista_ordenada = sorted(lista)
print(f"A lista em ordem alfabética é {lista_ordenada}")
```

6. Crie um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números positivos.

```python
lista = [-2, 4, -5, 7, 0, 2, -1]
lista_positivos = []
for numero in lista:
    if numero > 0:
        lista_positivos.append(numero)
print(f"A lista de números positivos é {lista_positivos}")
```

7. Crie um programa que receba uma lista de nomes e retorne uma nova lista contendo apenas os nomes que começam com a letra 'A'.

```python
lista = ['Ana', 'João', 'André', 'Mariana', 'Felipe']
lista_A = []
for nome in lista:
    if nome[0] == 'A':
        lista_A.append(nome)
print(f"A lista de nomes que começam com 'A' é {lista_A}")
```

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

9. Crie um programa que receba uma lista de nomes e retorne o nome mais longo da lista.

```python
lista = ['Ana', 'João', 'André', 'Mariana', 'Felipe']
maior_nome = lista[0]
for nome in lista:
    if len(nome) > len(maior_nome):
        maior_nome = nome
print(f"O maior nome da lista é {maior_nome}")
```

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
%%

## Referências

Xavier, Gley Fabiano Cardoso
Lógica de programação
E-book. Disponível em: [https://bibliotecadigitalsenac.com.br/?from=busca%3FcontentInfo%3D1306%26term%3Dlogica#/legacy/epub/1306](https://bibliotecadigitalsenac.com.br/?from=busca%3FcontentInfo%3D1306%26term%3Dlogica#/legacy/epub/1306)
Acesso em 10/04/2023

[Coleções no Python: Listas, Tuplas e Dicionários](https://www.devmedia.com.br/colecoes-no-python-listas-tuplas-e-dicionarios/40678)

[Python Lists](https://www.w3schools.com/python/python_lists.asp)
