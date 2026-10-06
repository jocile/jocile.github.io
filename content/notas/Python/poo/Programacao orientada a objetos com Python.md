---
title: Programação orientada a objetos com Python
description: é um paradigma de programação que utiliza objetos – estruturas que combinam
  dados e comportamentos
date: '2026-09-17'
draft: false
tags:
- programador/Python
- Python/POO
---

A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" – estruturas que combinam dados e comportamentos. Esse paradigma é amplamente utilizado em várias linguagens de programação, incluindo Python. Vamos explorar os conceitos fundamentais da POO em Python de forma estruturada.

## 1. Introdução

A POO é um modelo que organiza o software em objetos que interagem entre si. Esses objetos são instâncias de classes, que definem os atributos (dados) e métodos (funções) que o objeto pode ter.

### Principais Conceitos da POO

- **Classe**: Um molde para criar objetos. Define um conjunto de atributos e métodos.
- **Objeto**: Uma instância de uma classe. Representa uma entidade no programa.
- **Atributo**: Variável que pertence a uma classe ou objeto.
- **Método**: Função que pertence a uma classe ou objeto.
- **Encapsulamento**: Esconde detalhes internos dos objetos e só permite a interação através de métodos.
- **Herança**: Permite que uma classe herde atributos e métodos de outra classe.
- **Polimorfismo**: Permite que diferentes classes sejam tratadas de maneira uniforme através de uma interface comum.

## 2. Criando Classes e Objetos em Python

Em Python, uma classe é criada utilizando a palavra-chave `class`. Vamos criar uma classe simples chamada `Carro`.

```python
class Carro:
 def __init__(self, marca, modelo, ano):
 self.marca = marca
 self.modelo = modelo
 self.ano = ano

 def exibir_informacoes(self):
 print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.exibir_informacoes()
```

### **Explicação:**

- **`__init__`**: Método especial chamado de construtor. Ele inicializa os atributos do objeto.
- **self**: Referência ao próprio objeto. É necessário em todos os métodos dentro da classe.

## 3. Encapsulamento em Python

O encapsulamento protege os dados internos dos objetos e só permite a manipulação desses dados através de métodos específicos.

```python
class Carro:
 def __init__(self, marca, modelo, ano):
 self.__marca = marca # Atributo privado
 self.__modelo = modelo # Atributo privado
 self.__ano = ano # Atributo privado

 def exibir_informacoes(self):
 print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Ano: {self.__ano}")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.exibir_informacoes()
```

### **Explicação:**

- Os atributos `__marca`, `__modelo` e `__ano` são privados e não podem ser acessados diretamente fora da classe.

## 4. Herança em Python

A herança permite que uma nova classe herde atributos e métodos de uma classe existente.

```python
class Veiculo:
 def __init__(self, marca, modelo):
 self.marca = marca
 self.modelo = modelo

 def exibir_informacoes(self):
 print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
 def __init__(self, marca, modelo, ano):
 super().__init__(marca, modelo)
 self.ano = ano

 def exibir_informacoes(self):
 super().exibir_informacoes()
 print(f"Ano: {self.ano}")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.exibir_informacoes()
```

### **Explicação:**

- **super()**: Chama métodos da classe base (superclasse).
- A classe `Carro` herda de `Veiculo` e pode adicionar novos atributos ou métodos.

## 5. Polimorfismo em Python

O polimorfismo permite que diferentes classes sejam tratadas através da mesma interface.

```python
class Veiculo:
 def mover(self):
 pass

class Carro(Veiculo):
 def mover(self):
 print("O carro está dirigindo")

class Aviao(Veiculo):
 def mover(self):
 print("O avião está voando")

# Usando polimorfismo
def acao_veiculo(veiculo):
 veiculo.mover()

meu_carro = Carro()
meu_aviao = Aviao()

acao_veiculo(meu_carro)
acao_veiculo(meu_aviao)
```

### **Explicação:**

- `acao_veiculo` aceita qualquer objeto que herda de `Veiculo` e chama o método `mover` apropriado.

## Conclusão

A Programação Orientada a Objetos em Python é um poderoso paradigma que permite organizar e estruturar o código de maneira eficiente e reutilizável. Entender os conceitos de classes, objetos, encapsulamento, herança e polimorfismo é essencial para aproveitar ao máximo as vantagens oferecidas pela POO.

Esses conceitos formam a base para desenvolver aplicações complexas de maneira organizada e modular, facilitando a manutenção e evolução do código ao longo do tempo.
