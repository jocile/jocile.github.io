---
title: "Desafio POO A Bicicletaria do João"
date: 2026-10-05
draft: false
description: "Ajudar o João a registrar as vendas de suas bicicletas utilizando Programação Orientada a Objetos (POO) em Python."
aliases:
  - Desafio Bicicletaria
  - Exercício POO Python
tags:
  - python
  - poo
  - orientacao-a-objetos
  - exercicio
---

> [!info] Objetivo
> Ajudar o João a registrar as vendas de suas bicicletas utilizando Programação Orientada a Objetos (POO) em Python. 

## Contexto

João tem uma bicicletaria e deseja um programa para registrar e exibir as bicicletas vendidas. Cada bicicleta possui características próprias e é capaz de executar alguns comportamentos básicos.

- **Características (Atributos):** Cor, modelo, ano e valor.
- **Comportamentos (Métodos):** Buzinar, parar e correr.

---

## Passo a Passo

### Passo 1: Criando a Classe e o Construtor

Tudo em POO começa com a definição de uma `class`. Para inicializar os atributos da nossa bicicleta no momento da criação da instância, utilizamos o método construtor `__init__`.

> [!warning] A importância do `self`
> Em Python, o `self` é uma referência explícita à instância do objeto. Ele **deve ser sempre o primeiro parâmetro** de qualquer método de instância dentro da classe. Um erro muito comum para iniciantes é esquecer de adicioná-lo nas declarações de método!

```python
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
```

### Passo 2: Adicionando Comportamentos (Métodos)

Agora, definiremos os métodos que representam as ações que a bicicleta pode realizar: `buzinar`, `parar` e `correr`. 

```python
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Bicicleta parada.")

    def correr(self):
        print("Vrummmmm!")
```

### Passo 3: Instanciando e Testando Objetos

Com a nossa classe definida, podemos "dar vida" às bicicletas criando instâncias (objetos) reais a partir do molde.

```python
# Instanciando os objetos (criando bicicletas)
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b2 = Bicicleta("Verde", "Monark", 2000, 189)

# Chamando os comportamentos (métodos)
b1.buzinar()
b1.correr()
b1.parar()

# Acessando atributos diretamente
print(b1.cor) # Saída: Vermelha
```

### Passo 4 (Avançado): Melhorando a Representação da Classe com `__str__`

Se usarmos um `print(b1)` com o código atual, o Python exibirá apenas um endereço de memória pouco legível. Para melhorar isso e montar uma exibição agradável, podemos sobrescrever o método mágico `__str__`.

> [!tip] Dica Profissional
> Uma forma inteligente e dinâmica de retornar valores sem precisar digitar cada atributo manualmente é utilizar `__class__.__name__` (para pegar o nome da classe) e `__dict__` (que retorna os atributos da instância em formato de dicionário).

```python
    def __str__(self):
        # Formata dinamicamente: NomeDaClasse: chave1=valor1, chave2=valor2...
        return f"{self.__class__.__name__}: {', '.join([f'{k}={v}' for k, v in self.__dict__.items()])}"
```

Com essa adição, ao executar `print(b2)`, a saída ficará clara, flexível e legível, não precisando de atualizações manuais no `__str__` mesmo se você adicionar novos atributos (como um tamanho de "aro") no futuro:

`Bicicleta: cor=Verde, modelo=Monark, ano=2000, valor=189`