---
title: Adição
description: 'Algoritmo:'
date: '2026-09-14'
draft: false
tags:
- exercícios
- Lógica 
---

Algoritmo:

- [x]  Receber o nome
- [x]  Receber a idade
- [x]  Quero mostrar a frase:
- O nome é {nome} e a idade é {idade}

Entra com o nome e idade e mostrar a frase:

Em [Portugol](https://portugol.dev/):

```
programa {
  funcao inicio() {
    cadeia nome
    inteiro idade

	escreva("Digite seu nome: ")
	leia(nome)
    escreva("Digite a idade: ")
    leia(idade)
    escreva("O nome é ", nome)
    escreva(" e a idade é ", idade)
  }
}
```

Em [Python](https://www.online-python.com/):

```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f'O nome é {nome} e a idade é {idade}')
```

## Manipulando os valores

```
nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep=" ")
print(nome + sobrenome)
```


```
programa {
  funcao inicio() {
    inteiro x
    x = 10 - 5 * 2 
    escreva(x) 
  }
}
```

Em Python

```python
print(1 + 1)
>>> 2

# Subtração
print(10 - 2)
>>> 8

# Multiplicação
print(4 * 3)
>>> 12
```

