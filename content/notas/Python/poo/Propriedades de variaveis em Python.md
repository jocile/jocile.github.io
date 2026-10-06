---
title: Propriedades de variáveis em Python
description: Na Programação Orientada a Objetos (POO), o uso de propriedades é uma
  técnica poderosa que permite controlar o acesso e a modificação de variáveis de…
date: '2026-09-17'
draft: false
tags:
- programador/Python/POO /
- Python/variáveis
---

Na Programação Orientada a Objetos (POO), o uso de propriedades é uma técnica poderosa que permite controlar o acesso e a modificação de variáveis de instância. Propriedades ajudam a **encapsular dados**e a aplicar lógica adicional ao acessar ou modificar esses dados, sem alterar a interface pública da classe.

## O que são Propriedades?

Propriedades são atributos de uma classe que permitem o acesso controlado às variáveis de instância. Em Python, as propriedades são definidas usando os decoradores `@property`, `@<nome>.setter` e `@<nome>.deleter`.

## Vantagens das Propriedades

- **Encapsulamento**: Protege o acesso direto às variáveis de instância.
- **Validação de Dados**: Permite adicionar validações e lógica ao acessar ou modificar uma variável.
- **Interface Uniforme**: Mantém uma interface de acesso uniforme, sem expor a implementação interna.
- **Facilidade de Mudanças Futuras**: Facilita mudanças futuras na lógica de acesso ou modificação sem alterar a interface pública.

## Exemplo de Código em Python

Vamos criar uma classe `ContaBancaria` que usa propriedades para controlar o acesso ao saldo de uma conta bancária.

### Definição da Classe sem Propriedades

```python
class ContaBancaria:
 def __init__(self, titular, saldo_inicial):
 self.titular = titular
 self.saldo = saldo_inicial

conta = ContaBancaria("João", 1000)

# Acessando e modificando diretamente a variável de instância
print(conta.saldo) # Saída: 1000
conta.saldo = 2000
print(conta.saldo) # Saída: 2000
```

### Definição da Classe com Propriedades

```python
class ContaBancaria:
 def __init__(self, titular, saldo_inicial):
 self.titular = titular
 self._saldo = saldo_inicial # Usando underscore para indicar variável privada

 @property
 def saldo(self):
 return self._saldo

 @saldo.setter
 def saldo(self, valor):
 if valor < 0:
 raise ValueError("O saldo não pode ser negativo")
 self._saldo = valor

 @saldo.deleter
 def saldo(self):
 del self._saldo

# Criando uma instância da classe
conta = ContaBancaria("João", 1000)

# Usando a propriedade para acessar e modificar o saldo
print(conta.saldo) # Saída: 1000
conta.saldo = 2000
print(conta.saldo) # Saída: 2000

# Tentando definir um saldo negativo (lançará uma exceção)
try:
 conta.saldo = -500
except ValueError as e:
 print(e) # Saída: O saldo não pode ser negativo
```

## Aplicações Comuns de Propriedades

1. **Validação de Dados**: Verificar e validar dados antes de permitir a modificação de uma variável.
2. **Cálculos Dinâmicos**: Realizar cálculos dinâmicos ao acessar uma variável.
3. **Encapsulamento**: Proteger variáveis de instância sensíveis ou complexas.
4. **Notificações e Logs**: Executar código adicional, como gerar logs ou notificações, ao acessar ou modificar uma variável.

## Exemplo de Classe com Cálculo Dinâmico

Vamos criar uma classe `Retangulo` que calcula a área e o perímetro dinamicamente usando propriedades.

```python
class Retangulo:
 def __init__(self, largura, altura):
 self._largura = largura
 self._altura = altura

 @property
 def largura(self):
 return self._largura

 @largura.setter
 def largura(self, valor):
 if valor <= 0:
 raise ValueError("A largura deve ser maior que zero")
 self._largura = valor

 @property
 def altura(self):
 return self._altura

 @altura.setter
 def altura(self, valor):
 if valor <= 0:
 raise ValueError("A altura deve ser maior que zero")
 self._altura = valor

 @property
 def area(self):
 return self._largura * self._altura

 @property
 def perimetro(self):
 return 2 * (self._largura + self._altura)

# Criando uma instância da classe
retangulo = Retangulo(5, 10)

# Acessando propriedades
print(f"Largura: {retangulo.largura}") # Saída: 5
print(f"Altura: {retangulo.altura}") # Saída: 10
print(f"Área: {retangulo.area}") # Saída: 50
print(f"Perímetro: {retangulo.perimetro}") # Saída: 30

# Modificando valores
retangulo.largura = 7
retangulo.altura = 14

# Acessando propriedades novamente após modificação
print(f"Nova largura: {retangulo.largura}") # Saída: 7
print(f"Nova altura: {retangulo.altura}") # Saída: 14
print(f"Nova área: {retangulo.area}") # Saída: 98
print(f"Novo perímetro: {retangulo.perimetro}") # Saída: 42
```

## Conclusão

O uso de propriedades em Python permite um controle mais refinado sobre o acesso e a modificação de variáveis de instância. Elas ajudam a manter o código limpo, seguro e fácil de manter, proporcionando um mecanismo para encapsular dados e adicionar lógica adicional sem alterar a interface pública da classe. Ao aplicar propriedades de forma adequada, você pode melhorar significativamente a robustez e a qualidade do seu código POO.
