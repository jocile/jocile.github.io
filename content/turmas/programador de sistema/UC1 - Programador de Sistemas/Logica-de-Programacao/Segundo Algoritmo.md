---
title: Faça um algoritmo para ler dois números
description: criando algoritmos para programas de computador resolvendo problemas
date: '2026-09-14'
draft: false
tags:
- exercícios
- Lógica 
---

```js
// Faça um algoritmo para ler dois números
// e imprimir o maior, o menor 
// ou então dizer se são iguais

programa {
 funcao inicio() {
 inteiro x, y 
 escreva("Digite o primeiro numero: ")
 leia(x)
 escreva("Digite o segundo numero: ")
 leia(y)
 se (x > y)
 {
 escreva("O maior número é ", x)
 escreva("O menor número é ", y)
 }
 se (x < y)
 {
 escreva("O maior número é ", y)
 escreva("O menor número é ", x)
 }
 se (x == y)
 {
 escreva("Os números são iguais")
 }
 }
}

```

Em Python

```python
# e imprimir o maior, o menor 
# ou então dizer se são iguais
 
x = input("Digite o primeiro numero: ")
y = input("Digite o segundo numero: ")
if (x > y):
 print("O maior número é ", x)
 print("O menor número é ", y)
if(x < y):
 print("O maior número é ", y)
 print("O menor número é ", x)
if(x == y):
 print("Os números são iguais")
```

[[Exercicios de Logica condicional]]
