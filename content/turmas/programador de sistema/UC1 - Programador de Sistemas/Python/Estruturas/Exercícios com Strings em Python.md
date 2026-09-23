---
title: "Exercícios com Strings em Python"
date: 2026-09-23
draft: false
tags:
  - python
  - strings
  - exercicios
description: "Lista de exercícios e métodos úteis para manipulação de strings em Python."
---

## Principais Métodos com Strings em Python:

As strings em Python são objetos poderosos que suportam uma variedade de métodos úteis para manipulação e processamento de texto. Alguns dos métodos mais comuns incluem:

- **len():** Retorna o comprimento da string.
- **upper():** Converte todos os caracteres para maiúsculas.
- **lower():** Converte todos os caracteres para minúsculas.
- **strip():** Remove espaços em branco no início e no final da string.
- **replace():** Substitui uma substring por outra.
- **split():** Divide a string em uma lista de substrings com base em um delimitador.
- **join():** Une uma lista de strings em uma única string.

## Exercícios de Programação com Strings em Python:

1. **Contagem de vogais e consoantes**
   - Escreva um programa que conta o número de vogais e consoantes em uma string.

2. **Verificar palíndromo**
   - Escreva um programa que verifica se uma string é um palíndromo.

3. **Contar palavras em uma frase**
   - Escreva um programa que conta o número de palavras em uma frase.

4. **Inverter ordem das palavras**
   - Escreva um programa que inverte a ordem das palavras em uma frase.

5. **Capitalizar primeira letra de cada palavra**
   - Escreva um programa que capitalize a primeira letra de cada palavra em uma frase.

%%

## Exemplos de Soluções:

```python
# Exemplo para contar vogais e consoantes
string = input("Digite uma string: ")
vogais = sum(1 for char in string if char in 'aeiouAEIOU')
consoantes = sum(1 for char in string if char.isalpha() and char not in 'aeiouAEIOU')
print(f"Vogais: {vogais}, Consoantes: {consoantes}")
```

```python
# Exemplo para verificar palíndromo
string = input("Digite uma string: ")
if string == string[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
```

```python
# Exemplo para contar palavras em uma frase
frase = input("Digite uma frase: ")
num_palavras = len(frase.split())
print(f"Número de palavras na frase: {num_palavras}")
```

```python
# Exemplo para inverter ordem das palavras
frase = input("Digite uma frase: ")
frase_invertida = ' '.join(frase.split()[::-1])
print(f"Frase com ordem das palavras invertida: {frase_invertida}")
```

```python
# Exemplo para capitalizar primeira letra de cada palavra
frase = input("Digite uma frase: ")
frase_capitalizada = ' '.join(word.capitalize() for word in frase.split())
print(f"Frase com primeira letra de cada palavra capitalizada: {frase_capitalizada}")
```

Esses exemplos demonstram como você pode manipular strings em Python sem a necessidade de definir funções separadas.

## Soluções usando funções

Organizando em funções:

```python
# Exemplo para contar vogais e consoantes
def contar_vogais_e_consoantes(string):
    vogais = 'aeiouAEIOU'
    num_vogais = sum(1 for char in string if char in vogais)
    num_consoantes = sum(1 for char in string if char.isalpha() and char not in vogais)
    return num_vogais, num_consoantes

entrada = input("Digite uma string: ")
vogais, consoantes = contar_vogais_e_consoantes(entrada)
print(f"Vogais: {vogais}, Consoantes: {consoantes}")
```

```python
# Exemplo para verificar palíndromo
def verificar_palindromo(string):
    return string == string[::-1]

entrada = input("Digite uma string: ")
if verificar_palindromo(entrada):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
```

```python
# Exemplo para contar palavras em uma frase
def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

entrada = input("Digite uma frase: ")
num_palavras = contar_palavras(entrada)
print(f"Número de palavras na frase: {num_palavras}")
```

```python
# Exemplo para inverter ordem das palavras
def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    return ' '.join(palavras_invertidas)

entrada = input("Digite uma frase: ")
frase_invertida = inverter_ordem_palavras(entrada)
print(f"Frase com ordem das palavras invertida: {frase_invertida}")
```

```python
# Exemplo para capitalizar primeira letra de cada palavra
def capitalizar_primeira_letra(frase):
    return ' '.join(word.capitalize() for word in frase.split())

entrada = input("Digite uma frase: ")
frase_capitalizada = capitalizar_primeira_letra(entrada)
print(f"Frase com primeira letra de cada palavra capitalizada: {frase_capitalizada}")
```

Esses exemplos ilustram como os métodos de strings podem ser aplicados para resolver diferentes problemas e cenários de uso.
%%
