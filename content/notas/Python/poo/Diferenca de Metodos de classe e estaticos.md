---
title: Diferença de Métodos de classe e estaticos
description: Na Programação Orientada a Objetos (POO), entender a diferença entre
  métodos de classe e métodos estáti cos é fundamental para utilizar as classes de
  maneira…
date: '2026-09-17'
draft: false
tags:
- programador/Python/POO
- Python/Funcoes 
---

Na Programação Orientada a Objetos (POO), entender a diferença entre métodos de classe e métodos estáti cos é fundamental para utilizar as classes de maneira eficiente. Vamos explorar esses conceitos em detalhes com exemplos práticos em Python.

## Vantagens dos Métodos Estáticos

- **Independência da Classe e Instância**: Métodos estáticos não precisam acessar ou modificar o estado da classe ou de suas instâncias.
- **Utilidade como Funções Utilitárias**: São ideais para funções utilitárias que realizam tarefas relacionadas à classe, mas não dependem de seu estado.

## Comparação entre Métodos de Classe e Métodos Estáticos

| Característica | Método de Classe | Método Estático |
| ------------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Decorador | `@classmethod` | `@staticmethod` |
| Primeiro Parâmetro | `cls` (representa a classe) | Nenhum |
| Acesso a Variáveis | Pode acessar e modificar variáveis de classe | Não pode acessar diretamente variáveis de instância ou de classe |
| Uso Típico | Acessar/modificar o estado da classe, [Metodos de fabrica](Metodos%20de%20fabrica.md) | [Funções utilitárias](Funcoes%20utilitarias.md) independentes do estado da classe |

## Métodos de Classe

### Definição

Métodos de classe são métodos que estão associados à classe em si, e não a instâncias individuais da classe. Eles podem acessar e modificar o estado da classe, o que inclui variáveis de classe. Para definir um método de classe, utiliza-se o decorador `@classmethod`.

### Sintaxe

Para definir um método de classe, você deve passar `cls` (que representa a própria classe) como o primeiro parâmetro.

### Exemplo de Código em Python

```python
class Pessoa:
 populacao = 0 # Variável de classe
 
 def __init__(self, nome):
 self.nome = nome
 Pessoa.populacao += 1
 
 @classmethod
 def obter_populacao(cls):
 return cls.populacao

p1 = Pessoa("Alice")
p2 = Pessoa("Bob")

# Usando o método de classe
print(Pessoa.obter_populacao()) # Saída: 2
```

### Vantagens dos Métodos de Classe

- **Acesso a Variáveis de Classe**: Métodos de classe podem acessar e modificar variáveis de classe.
- **Criação de Métodos de Fábrica**: São ideais para criar [Metodos de fabrica](Metodos%20de%20fabrica.md) que retornam instâncias da classe.

## Métodos Estáticos

### Definição

Métodos estáticos, ou [Funções utilitárias](Funcoes%20utilitarias.md), são métodos que não dependem de uma instância ou da própria classe para funcionar. Eles são definidos usando o decorador `@staticmethod` e não recebem nenhum parâmetro especial como `self` ou `cls`.

### Sintaxe

Métodos estáticos são definidos como funções normais dentro da classe, mas com o decorador `@staticmethod`.

### Exemplo de Código em Python

```python
class Matematica:
 @staticmethod
 def adicionar(a, b):
 return a + b
 
 @staticmethod
 def subtrair(a, b):
 return a - b

# Usando métodos estáticos
print(Matematica.adicionar(5, 3)) # Saída: 8
print(Matematica.subtrair(10, 4)) # Saída: 6
```

## Conclusão

Métodos de classe e métodos estáticos oferecem diferentes níveis de acesso e funcionalidade dentro de uma classe. Métodos de classe (`@classmethod`) permitem interagir com variáveis de classe e são ideais para criar métodos de fábrica. Métodos estáticos (`@staticmethod`), por outro lado, são independentes do estado da classe e são úteis para implementar funções utilitárias. Compreender essas diferenças é crucial para escrever código POO eficiente e bem estruturado.
