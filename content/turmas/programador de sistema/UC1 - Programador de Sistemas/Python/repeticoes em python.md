---
title: Repetições em Python
date: 2026-09-17
draft: false
tags: [logica, exercicios, python]
description: "Criando algoritmos com repetições para programas de computador resolvendo problemas."
---

Em Python, há três formas principais de repetição:

1. O loop for, que é usado para iterar sobre uma sequência de valores.
2. O loop while, que é usado para repetir um bloco de código enquanto uma condição é verdadeira.
3. O iterador, que é usado para acessar os elementos de uma sequência um a um.

A escolha de qual forma de repetição utilizar depende do problema que você está tentando resolver.

## Loop com for

Em geral, o loop for é mais utilizado quando você sabe exatamente quantas vezes deseja repetir um bloco de código.

Exemplo:

Usando o loop for com a função range para repetir um número fixo de vezes:

```python
for i in range(5):
    print(i)

```

Escreva um programa em Python que imprima todos os números pares de 0 a 100.

```python
for i in range(0, 101, 2):
    print(i)
```

Nesse algoritmo, usamos a função range() para criar uma sequência de números de 0 a 100 com um passo de 2 (para que apenas os números pares sejam incluídos). Em seguida, usamos um loop for para percorrer essa sequência e imprimir cada número.

## Loop com while

O loop while é mais utilizado quando você precisa repetir um bloco de código enquanto uma condição é verdadeira.
Usando o loop while para repetir um bloco de código enquanto uma condição for verdadeira:

Exemplo:

```python
# Usando o loop while para repetir um bloco de código
i = 0
while i < 5:
    print(i)
    i += 1

```

## Iterator de loop

O iterador é utilizado quando você precisa acessar os elementos de uma sequência de forma individual.

Exemplos:

```python
# Iterando sobre uma lista usando o loop for
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

```

Escreva um programa em Python que calcule a média aritmética de uma lista de números.

```python
numeros = [3, 5, 8, 12, 15]

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

print("A média é:", media)

```

Nesse algoritmo, definimos uma lista de números e usamos um loop for para percorrer a lista e somar todos os números. Em seguida, dividimos essa soma pelo número de elementos na lista (usando a função len()) para calcular a média. Por fim, exibimos a média usando a função print().

> Lembre-se que repetição é uma parte fundamental da programação e é útil para tarefas como cálculos, filtragem de dados, busca, entre outros.
{: .prompt-info }

## Saindo do loop

Algumas vezes necessitamos sair do loop, para isso podemos usar o comando break:

Usando a instrução break para sair de um loop prematuramente:

```python
# Usando a instrução break para sair de um loop prematuramente
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

```

## Pulando a iteração

Usando a instrução continue para pular para a próxima iteração do loop:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)

```

## Lista de exercícios com repetições

1. Escreva um programa que imprima todos os números pares de 0 a 20.
2. Escreva um programa que peça ao usuário para digitar um número inteiro positivo e calcule a soma de todos os números ímpares de 1 até esse número.
3. Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.
4. Escreva um programa que peça ao usuário para digitar uma lista de números e imprima o maior número da lista.
5. Escreva um programa que peça ao usuário para digitar uma palavra e imprima a palavra invertida.
6. Escreva um programa que calcule a média aritmética de uma lista de números.
7. Escreva um programa que peça ao usuário para digitar um número inteiro e verifique se ele é um número primo.
8. Escreva um programa que peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (ou seja, se a palavra é igual quando lida de trás para frente).

%%
## Solução em Python

### 1. números pares

Escreva um programa que imprima todos os números pares de 0 a 20.

```python
for i in range(0, 21, 2):
    print(i)

```

### 2. cálculos com números

Escreva um programa que peça ao usuário para digitar um número inteiro positivo e calcule a soma de todos os números ímpares de 1 até esse número.

```python
n = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, n+1, 2):
    soma += i
print("A soma dos números ímpares de 1 a", n, "é", soma)

```

### 3. contando as vogais

Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.

```python
frase = input("Digite uma frase: ")
vogais = "aeiou"
contagem = 0
for letra in frase:
    if letra.lower() in vogais:
        contagem += 1
print("A frase digitada possui", contagem, "vogais.")

```

### 4. o maior número

Escreva um programa que peça ao usuário para digitar uma lista de números e imprima o maior número da lista.

```python
numeros = input("Digite uma lista de números separados por vírgulas: ")
numeros = numeros.split(",")
maior = int(numeros[0])
for numero in numeros:
    if int(numero) > maior:
        maior = int(numero)
print("O maior número da lista é", maior)

```

### 5. palavra invertida

Escreva um programa que peça ao usuário para digitar uma palavra e imprima a palavra invertida.

```python
palavra = input("Digite uma palavra: ")
inversa = ""
for letra in palavra:
    inversa = letra + inversa
print("A palavra invertida é", inversa)

```

### 6. calculando a média

Escreva um programa que calcule a média aritmética de uma lista de números.

```python
palavra = input("Digite uma palavra: ")
inversa = ""
for letra in palavra:
    inversa = letra + inversa
print("A palavra invertida é", inversa)

```

### 7. número primo

Escreva um programa que peça ao usuário para digitar um número inteiro e verifique se ele é um número primo.

```python
numero = int(input("Digite um número inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")

```

### 8. palíndromo

Escreva um programa que peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (ou seja, se a palavra é igual quando lida de trás para frente).

```python
palavra = input("Digite uma palavra: ")
inversa = ""
for letra in palavra:
    inversa = letra + inversa
if palavra == inversa:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

```

%%

## Referências

- [W3schools Python reference](https://www.w3schools.com/python/default.asp)
- [Colab - Introdução a programação com a linguagem Python](https://colab.research.google.com/drive/17DTWLVeBgIuwp-FYGIsAxlaj_mRNNMkK?usp=sharing#scrollTo=-F7LD5SJy2eq)
- [Livro na Biblioteca Virtual - Introdução à programação em Python - Sérgio Furgeri](https://bibliotecadigitalsenac.com.br/#/?contentInfo=3011)
