---
title: Usando métodos de fábrica para criar objetos
description: Métodos de fábrica são métodos de classe que encapsulam a lógica de criação
  de objetos e retornam instâncias da própria classe. Eles são úteis para criar…
date: '2026-09-17'
draft: false
tags:
- programador/Python/POO
- Python/Funcoes 
---

Métodos de fábrica são métodos de classe que encapsulam a lógica de criação de objetos e retornam instâncias da própria classe. Eles são úteis para criar objetos de maneira mais flexível, controlada e encapsulada, permitindo a personalização do processo de criação sem a necessidade de expor a complexidade ao usuário final.

### Vantagens dos Métodos de Fábrica

- **Encapsulamento da Lógica de Criação**: Permite esconder a complexidade da criação de objetos dentro da classe.
- **Flexibilidade**: Permite criar objetos de maneiras diferentes sem modificar o código da classe principal.
- **Legibilidade**: Métodos de fábrica bem nomeados tornam o código mais intuitivo e fácil de entender.
- **Reuso de Código**: Facilita o reuso de lógica de criação em diferentes partes da aplicação.

### Exemplo de Código em Python

Vamos explorar como criar e utilizar métodos de fábrica com exemplos práticos.

#### Exemplo 1: Método de Fábrica com Parâmetros Alternativos

Imagine uma classe `Data` que representa uma data. Podemos querer criar instâncias dessa classe a partir de diferentes tipos de dados, como strings ou timestamps.

```python
class Data:
 def __init__(self, dia, mes, ano):
 self.dia = dia
 self.mes = mes
 self.ano = ano

 @classmethod
 def from_string(cls, data_str):
 dia, mes, ano = map(int, data_str.split('-'))
 return cls(dia, mes, ano)

 @classmethod
 def from_timestamp(cls, timestamp):
 from datetime import datetime
 dt = datetime.fromtimestamp(timestamp)
 return cls(dt.day, dt.month, dt.year)

data1 = Data.from_string('01-06-2024')
data2 = Data.from_timestamp(1719907200)

print(f"Data1: {data1.dia}/{data1.mes}/{data1.ano}")
print(f"Data2: {data2.dia}/{data2.mes}/{data2.ano}")
```

#### Exemplo 2: Método de Fábrica para Validação

Métodos de fábrica também podem ser usados para validar e preprocessar dados antes de criar uma instância.

```python
class Produto:
 def __init__(self, nome, preco):
 self.nome = nome
 self.preco = preco

 @classmethod
 def from_dict(cls, dados):
 nome = dados.get('nome')
 preco = dados.get('preco')
 if preco < 0:
 raise ValueError("O preço não pode ser negativo")
 return cls(nome, preco)

# Usando método de fábrica para criar objeto com validação
dados_produto = {'nome': 'Cadeira', 'preco': 150}
produto = Produto.from_dict(dados_produto)

print(f"Produto: {produto.nome}, Preço: {produto.preco}")
```

### Aplicações Comuns dos Métodos de Fábrica

1. **Conversão de Formatos**: Criar objetos a partir de diferentes formatos de dados, como strings, dicionários, ou JSON.
2. **Validação e Pré-processamento**: Validar dados de entrada e preprocessar informações antes de criar a instância.
3. **Singletons**: Controlar a criação de instâncias para garantir que apenas uma instância de uma classe seja criada.
4. **Objetos Complexos**: Facilitar a criação de objetos que requerem vários passos ou configuração complexa.

### Diferença entre Construtores e Métodos de Fábrica

- **Construtores (`__init__`)**: Usados para inicializar uma nova instância da classe. São chamados automaticamente quando uma nova instância é criada.
- **Métodos de Fábrica**: Métodos de classe que retornam uma nova instância da classe. Eles encapsulam a lógica de criação e podem ser usados para criar instâncias de diferentes maneiras ou para adicionar lógica adicional durante a criação.

### Exemplo Comparativo

```python
class Pessoa:
 def __init__(self, nome, idade):
 self.nome = nome
 self.idade = idade

 @classmethod
 def from_birth_year(cls, nome, ano_nascimento):
 from datetime import datetime
 idade = datetime.now().year - ano_nascimento
 return cls(nome, idade)

# Usando construtor
p1 = Pessoa("Alice", 30)

# Usando método de fábrica
p2 = Pessoa.from_birth_year("Bob", 1994)

print(f"Pessoa 1: Nome={p1.nome}, Idade={p1.idade}")
print(f"Pessoa 2: Nome={p2.nome}, Idade={p2.idade}")
```

## Conclusão

Métodos de fábrica são uma poderosa técnica na POO, oferecendo flexibilidade e controle sobre a criação de objetos. Eles permitem encapsular a lógica de criação, adicionar validações e criar instâncias de diferentes maneiras, tornando o código mais modular e fácil de manter. Compreender e aplicar métodos de fábrica pode melhorar significativamente a qualidade e a legibilidade do seu código.
