---
title: Variáveis de classe e de instancia
description: Na Programação Orientada a Objetos (POO), entender a diferença entre
  variáveis de classe e variáveis de instância é fundamental para manipular dados
  de…
date: '2026-09-17'
draft: false
tags:
- programador/Python/POO
- Python/variáveis
---

Na Programação Orientada a Objetos (POO), entender a diferença entre variáveis de classe e variáveis de instância é fundamental para manipular dados de maneira eficaz e evitar erros comuns. Vamos explorar esses conceitos em detalhes com exemplos práticos em Python.

## Variáveis de Classe

### Definição

Variáveis de classe são compartilhadas entre todas as instâncias de uma classe. Elas são definidas dentro do corpo da classe, mas fora de qualquer método. Essas variáveis são usadas para armazenar informações que são comuns a todas as instâncias da classe.

### Características

- **Compartilhadas por todas as instâncias**: O valor de uma variável de classe é o mesmo para todas as instâncias da classe.
- **Acessíveis através da classe ou da instância**: Podem ser acessadas tanto pela classe em si quanto por qualquer instância da classe.

### Exemplo de Código em Python

```python
class Animal:
 especie = "Mamífero" # Variável de classe

 def __init__(self, nome):
 self.nome = nome # Variável de instância

print(Animal.especie) # Saída: Mamífero

# Criando instâncias da classe Animal
animal1 = Animal("Elefante")
animal2 = Animal("Tigre")

# Acessando a variável de classe através das instâncias
print(animal1.especie) # Saída: Mamífero
print(animal2.especie) # Saída: Mamífero

# Modificando a variável de classe
Animal.especie = "Réptil"
print(animal1.especie) # Saída: Réptil
print(animal2.especie) # Saída: Réptil
```

## Variáveis de Instância

### Definição

Variáveis de instância são específicas para cada instância de uma classe. Elas são definidas dentro dos métodos da classe, geralmente no método `__init__`, e são prefixadas com `self`.

### Características

- **Específicas para cada instância**: Cada instância da classe tem sua própria cópia de uma variável de instância.
- **Acessíveis somente através da instância**: Só podem ser acessadas por meio da instância da classe.

### Exemplo de Código em Python

```python
class Carro:
 def __init__(self, marca, modelo):
 self.marca = marca # Variável de instância
 self.modelo = modelo # Variável de instância

# Criando instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Acessando variáveis de instância
print(f"Carro 1: {carro1.marca} {carro1.modelo}") # Saída: Toyota Corolla
print(f"Carro 2: {carro2.marca} {carro2.modelo}") # Saída: Honda Civic

# Modificando variáveis de instância
carro1.modelo = "Camry"
print(f"Carro 1 atualizado: {carro1.marca} {carro1.modelo}") # Saída: Toyota Camry
```

## Comparação entre Variáveis de Classe e Variáveis de Instância

| Característica | Variáveis de Classe | Variáveis de Instância |
|----------------------------|----------------------------------------------|----------------------------------------------|
| Definição | Dentro da classe, fora de qualquer método | Dentro de métodos, prefixadas com `self` |
| Escopo | Compartilhada por todas as instâncias | Específica para cada instância |
| Acesso | Através da classe ou instância | Através da instância |
| Uso Típico | Informação comum a todas as instâncias | Dados específicos de cada instância |

## Exemplo de Código Comparativo

Vamos criar uma classe `Pessoa` para ilustrar a diferença entre variáveis de classe e variáveis de instância.

```python
class Pessoa:
 populacao = 0 # Variável de classe

 def __init__(self, nome, idade):
 self.nome = nome # Variável de instância
 self.idade = idade # Variável de instância
 Pessoa.populacao += 1 # Incrementa a variável de classe

# Criando instâncias da classe Pessoa
p1 = Pessoa("Alice", 30)
p2 = Pessoa("Bob", 25)

# Acessando variáveis de instância
print(f"Pessoa 1: Nome={p1.nome}, Idade={p1.idade}") # Saída: Alice, 30
print(f"Pessoa 2: Nome={p2.nome}, Idade={p2.idade}") # Saída: Bob, 25

# Acessando variável de classe
print(f"População: {Pessoa.populacao}") # Saída: 2
```

## Boas Práticas

- **Nomeação Clara**: Use nomes descritivos para variáveis de classe e de instância para evitar confusão.
- **Consistência**: Seja consistente ao acessar e modificar variáveis de classe e de instância.
- **Encapsulamento**: Proteja variáveis de instância sensíveis usando métodos getters e setters para manter a integridade dos dados.

## Conclusão

Variáveis de classe e variáveis de instância desempenham papéis distintos na POO. Variáveis de classe são usadas para armazenar informações comuns a todas as instâncias, enquanto variáveis de instância mantêm dados específicos de cada objeto. Compreender essas diferenças é crucial para manipular dados de maneira eficiente e escrever código POO bem-estruturado e fácil de manter.
