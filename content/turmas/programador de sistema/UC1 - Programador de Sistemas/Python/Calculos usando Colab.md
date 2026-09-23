---
title: "Cálculos usando Colab"
date: 2026-09-23
draft: false
tags:
  - python
  - colab
  - programador
description: "Exercícios de lógica de programação utilizando Python e Google Colab."
---

## 1. Problema

Sendo X, Z, Y e W variáveis numéricas, qual o resultado de cada variável no final do algoritmo?

```
início

	X, Y, Z, W: numérico
	X ← 10
	Z ← ( X + (X ^ 2) % (X \ 3))
	Y ← ( X – ((X ↑ 2) / 5))
	W ← (( Z – 64 ^ (1/2)) \ 10)

fim...
```

```Python
X = 10
Z = ( X + (X ** 2) % (X // 3))


Y = ( X - ((X ** 2) / 5))
W = (( Z - 64 ** (1/2)) // 10)
print ("X =", X)
print ("Z =", Z)
print ("Y = ", Y)
print ("W =", W)
```

Resultado: 

```Python
	X = 10
	Z = 11
	Y =  -10.0
	W = 0.0
```

## 2. Problema

Sendo X, Y e Z as variáveis literais, qual o resultado de cada variável no final do algoritmo?

```
início
	X,  Z, Y: literal
	X ← “ Banana”
	Z ← X + “da”
	Y ← “A “ + Z + “ é feita de “ + X + “.”
fim...
```

```Python
X = 'Banana'
Z = X + 'da'
Y = 'A ' + Z + ' é feita de ' + X + '.'
print(Y)
```

## 3. Problema lógico

Sendo X, Y, Z variáveis numéricas e W, T variáveis lógicas, qual o valor de cada variável no final do algoritmo?

```
início

	X, Z, Y: numérico
	W, T: lógico
	X ←	 5
	Z ←	 (X + 4) / 3
	Y ←	 ((X + 4) ^ (1/2))
	W ←	 (X >= Z)
	T ←	 (Z <> Y)

fim...
```

```Python
X = 5
Z = (X + 4) / 3
Y = ((X + 4) ** (1/2))
W = (X >= Z)
T = (Z != Y)
print("X =", X)
print("Z =", Z)
print("Y =", Y)
print("W =", W)
print("T =", T)
```

## 4. Problema

Sendo:\
X e Y variáveis numéricas, \
Z e W variáveis literais e \
T e K variá­veis lógicas, \
qual o resultado de cada variável no final do algoritmo?

```
início

	X, Y: numérico
	Z, W: literal
	T, K: lógico
	X ← 3
	Y ← X ↑ 2
	Z ← “Abaca”
	W ← Z + “xi”
	T ← (X <= Y) e (não (Z + “te” <> W))
	K ← não (T e  (“Abaca” = Z))

fim...

```

```Python
X = 3
Y = X ** 2
Z = 'Abaca'
W = Z + 'xi'
n = (Z + 'te')
T = (X <= Y) and (Z + "te " == W)
K = not(T and ('Abaca' == Z))
print("X =", X)
print("Y =", Y)
print("Z =", Z)
print("W =", W)
print("T =", T)
print("K =", K)
```

Veja a seguir a resposta do problema.

```Python
			X = 3
			Y = 9
			Z = “Abaca”
			W = “Abacaxi”
			T = falso
			K = verdadeiro...
```

[Original: Cálculos no Google Colab](https://colab.research.google.com/drive/1tlZY7_2hEwxEch0UkDbagLCNrxIhRar4?usp=sharing)
