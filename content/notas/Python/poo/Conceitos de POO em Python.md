---
title: Criando um objeto da classe Copo
description: A Programação Orientada a Objetos (POO) é um dos paradigmas de programação
  mais influentes e amplamente utilizados no desenvolvimento de software. Neste…
date: '2026-09-17'
draft: false
tags:
  - programador/Python/POO
---

## Conceitos de POO em Python

A Programação Orientada a Objetos (POO) é um dos paradigmas de programação mais influentes e amplamente utilizados no desenvolvimento de software. Neste artigo, exploraremos os conceitos fundamentais da POO, ilustrando com exemplos práticos em Python.

## Tabela resumida

![[Tabela de POO em Python]]

## 1. Introdução ao POO

### O que é um Paradigma de Programação?
Um paradigma de programação é um estilo ou "modelo" de programação que influencia como você pensa sobre a estrutura e execução dos programas. Exemplos de paradigmas incluem a programação procedural, funcional e orientada a objetos.

### Como a POO se Encaixa nesse Contexto?
A POO organiza o software em unidades chamadas objetos, que são instâncias de classes. Cada objeto encapsula dados e comportamentos relacionados, promovendo modularidade e reutilização de código.

### Exemplos de Solução de Problemas
Vamos considerar o problema de beber água para ilustrar diferentes paradigmas:

- **Procedural**: Você escreveria uma sequência de passos (funções) que descrevem como pegar um copo, encher de água e beber.
- **Funcional**: Focaria em funções puras, como transformar um estado "copo vazio" em "copo cheio".
- **Orientado a Objetos**: Criaria uma classe `Copo` com métodos como `encher` e `beber`.

## 2. Conceitos Fundamentais

### Classes e Objetos

- **Classe**: Um molde que define a estrutura e comportamento dos objetos. Pensa-se nela como um blueprint.
- **Objeto**: Uma instância de uma classe, contendo dados e métodos definidos pela classe.

### Exemplo de Código em Python

```python
class Copo:
 def __init__(self, volume):
 self.volume = volume
 
 def encher(self):
 print("O copo está cheio.")
 
 def beber(self):
 print("Você bebeu a água.")
 
meu_copo = Copo(300)
meu_copo.encher()
meu_copo.beber()
```

## 3. Construtores e Destrutores

### Método `__init__`

O método `__init__` é o construtor em Python, usado para inicializar o estado de um objeto.
### Método `__del__`
O método `__del__` é o destrutor, chamado quando um objeto é destruído.

### Exemplo de Código em Python

```python
class Copo:
 def __init__(self, volume):
 self.volume = volume
 print("Copo criado com volume:", volume)
 
 def __del__(self):
 print("Copo destruído.")

meu_copo = Copo(300)
del meu_copo
```

## 4. Herança

### Herança Simples e Múltipla
- **Herança Simples**: Uma classe herda de uma única classe base.
- **Herança Múltipla**: Uma classe herda de múltiplas classes base.

### Exemplo de Código em Python

```python
class Animal:
 def som(self):
 pass

class Cachorro(Animal):
 def som(self):
 return "Latido"

class Gato(Animal):
 def som(self):
 return "Miau"

# Herança Múltipla
class Chimera(Cachorro, Gato):
 pass

chimera = Chimera()
print(chimera.som()) # Latido
```

## 5. Encapsulamento

### Proteção de Acesso

Encapsulamento envolve restringir o acesso direto a alguns componentes do objeto.

### Recursos Públicos e Privados

- **Públicos**: Acessíveis de qualquer lugar.
- **Privados**: Acessíveis apenas dentro da classe.

### Exemplo de Código em Python

```python
class ContaBancaria:
 def __init__(self, saldo):
 self.__saldo = saldo # Variável privada
 
 def depositar(self, valor):
 self.__saldo += valor
 
 def obter_saldo(self):
 return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.obter_saldo()) # 1500
```

## 6. Polimorfismo

### Definição

Polimorfismo permite que o mesmo nome de função opere de maneiras diferentes, dependendo do contexto.

### Exemplo de Polimorfismo com Herança

```python
class Animal:
 def som(self):
 pass

class Cachorro(Animal):
 def som(self):
 return "Latido"

class Gato(Animal):
 def som(self):
 return "Miau"

def fazer_som(animal):
 print(animal.som())

fazer_som(Cachorro()) # Latido
fazer_som(Gato()) # Miau
```

## 7. Variáveis de Classe e Instância

### Diferenças

- **Variáveis de Classe**: Compartilhadas por todas as instâncias.
- **Variáveis de Instância**: Únicas para cada instância.

### Exemplo de Código em Python

```python
class Pessoa:
 populacao = 0 # Variável de classe
 
 def __init__(self, nome):
 self.nome = nome # Variável de instância
 Pessoa.populacao += 1

p1 = Pessoa("Alice")
p2 = Pessoa("Bob")
print(Pessoa.populacao) # 2
```

## 8. Métodos de Classe e Estáticos

### Métodos de Classe

Podem modificar o estado da classe.

### Métodos Estáticos

Não podem modificar o estado da classe ou da instância.

### Exemplo de Código em Python

```python
class Matematica:
 @staticmethod
 def adicionar(a, b):
 return a + b
 
 @classmethod
 def multiplicar(cls, a, b):
 return a * b

print(Matematica.adicionar(3, 5)) # 8
print(Matematica.multiplicar(3, 5)) # 15
```

## 9. Classes Abstratas

### Uso de Classes Abstratas

Definem contratos para subclasses, garantindo a implementação de métodos específicos.

### Exemplo de Código em Python com o Módulo `abc`

```python
from abc import ABC, abstractmethod

class Forma(ABC):
 @abstractmethod
 def area(self):
 pass

class Quadrado(Forma):
 def __init__(self, lado):
 self.lado = lado
 
 def area(self):
 return self.lado ** 2

quadrado = Quadrado(4)
print(quadrado.area()) # 16
```

## Conclusão

A Programação Orientada a Objetos é um paradigma poderoso que permite organizar e modularizar o código de maneira eficiente. Compreender os conceitos fundamentais como classes, objetos, herança, encapsulamento e polimorfismo é essencial para se tornar proficiente nesse estilo de programação. Utilize os exemplos fornecidos para praticar e consolidar seu entendimento.
