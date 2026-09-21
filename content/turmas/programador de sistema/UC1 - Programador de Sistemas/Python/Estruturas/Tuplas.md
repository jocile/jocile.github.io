---
title: "Tuplas em Python"
date: 2026-09-20
draft: false
tags:
  - python
  - programacao
  - estruturas-de-dados
description: "Guia sobre o funcionamento da estrutura de dados tupla em Python, incluindo criação, acesso, fatiamento e métodos."
---

## Objetivo Geral

- Compreender a imutabilidade das tuplas em relação às listas.

## Pré-requisitos

- Python 3
- VSCode

---

## Etapa 1: Criação e acesso aos dados

Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe `tuple`, ou colocando valores separados por vírgula de parênteses.

### Criando tuplas

```python
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)
```

A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

### Acesso direto

```python
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[0]  # maçã
frutas[2]  # uva
```

Sequências suportam indexação negativa. A contagem começa em -1.

### Índices negativos

```python
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[-1]  # pera
frutas[-3]  # laranja
```

Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

### Tuplas aninhadas

```python
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0]  # (1, "a", 2)
matriz[0][0]  # 1
matriz[0][-1]  # 2
matriz[-1][-1]  # "c"
```

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

### Fatiamento

```python
tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:]  # ("t", "h", "o", "n")
tupla[:2]  # ("p", "y")
tupla[1:3]  # ("y", "t")
tupla[0:3:2]  # ("p", "t")
tupla[::]  # ("p", "y", "t", "h", "o", "n")
tupla[::-1]  # ("n", "o", "h", "t", "y", "p")
```

A forma mais comum para percorrer os dados de uma tupla é utilizando o comando `for`.

### Iterar tuplas

```python
carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)
```

Às vezes é necessário saber qual o índice do objeto dentro do laço `for`. Para isso podemos usar a função `enumerate`.

### Função enumerate

```python
carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

---

## Etapa 2: Métodos da classe tuple

### `().count`

```python
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho")  # 1
cores.count("azul")  # 2
cores.count("verde")  # 1
```

### `().index`

```python
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java")  # 3
linguagens.index("python")  # 0
```

### `len`

```python
linguagens = ("python", "js", "c", "java", "csharp",)

len(linguagens)  # 5
```

---

## Atividade Prática

Com base nos conhecimentos adquiridos, realize as seguintes tarefas:

1. **Criação:** Crie uma tupla chamada `disciplinas` contendo 5 matérias do curso de Programação.
2. **Acesso:** Exiba no console a primeira e a última disciplina da tupla utilizando indexação (positiva ou negativa).
3. **Contagem:** Crie uma tupla chamada `notas` com 6 valores numéricos, sendo que um dos valores deve se repetir. Utilize o método `.count()` para contar quantas vezes um valor específico aparece.
4. **Iteração:** Utilize um laço `for` junto com a função `enumerate` para imprimir cada disciplina da tupla `disciplinas` com o seu respectivo índice no formato: `Índice: X - Disciplina: Y`.
