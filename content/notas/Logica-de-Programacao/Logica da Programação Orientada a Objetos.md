---
title: Python com Colab
description: plataforma gratuita baseada em nuvem que permite aos usuários escrever
  e executar código Python diretamente em um navegador da web
date: '2026-09-14'
draft: false
tags:
- lógica
- poo
- Python 
---

## Lógica da Programação Orientada a Objetos

A **Programação Orientada a Objetos (POO)** é um paradigma que permite organizar o código de forma mais próxima do mundo real, agrupando dados e comportamentos em unidades chamadas **objetos**. Para alunos de lógica, o segredo é entender que, em vez de focar apenas no "passo a passo" linear, passamos a definir "quem" realiza as ações e quais são suas características.

Abaixo, explico os conceitos centrais com exemplos práticos para utilizar no **Google Colab**.

### 1. O que é Classe e Objeto?

- **Classe:** Pense nela como um **molde** ou uma planta baixa. Ela define quais dados (atributos) um objeto terá e quais ações (métodos) ele poderá realizar.
- **Objeto:** É a **instância** real criada a partir desse molde. Se "Carro" é a classe, o "seu carro azul de placa ABC-123" é o objeto.

### 2. Atributos e Métodos

- **Atributos:** São as características ou estados do objeto (variáveis internas). Exemplo: a `nota` e o `comentario` em um sistema de feedback.
- **Métodos:** São as funções que pertencem àquele objeto e definem seu comportamento. Em vez de funções soltas, os métodos operam diretamente sobre os dados do objeto.

### 3. Exemplo Prático no Google Colab

Para praticar no Colab, você deve acessar o site [colab.research.google.com](https://colab.research.google.com/), logar com sua conta Gmail e criar um "Novo Bloco de Notas".

#### Cenário: Sistema de Notas de Alunos

Imagine que queremos transformar a lógica de calcular médias em uma estrutura de objetos.

```python
# Definindo a Classe (O Molde)
class Estudante:
 # O Construtor inicializa os atributos (características)
 def __init__(self, nome, notas):
 self.nome = nome # Atributo Nome
 self.notas = notas # Atributo Notas (uma lista)

 # Método para calcular a média (comportamento)
 def calcular_media(self):
 return sum(self.notas) / len(self.notas)

# Criando Objetos (Instâncias reais)
aluno1 = Estudante("Maria",)
aluno2 = Estudante("João",)

# Acessando dados e comportamentos
print(f"Aluno: {aluno1.nome} | Média: {aluno1.calcular_media():.2f}")
print(f"Aluno: {aluno2.nome} | Média: {aluno2.calcular_media():.2f}")
```

Abaixo está outro exemplo prático de como implementar essa lógica no **Google Colab**, utilizando construtores, atributos e métodos:

#### Definição das Classes (Os Moldes)

Primeiro, definimos a estrutura básica. Cada classe agrupa seus dados (**atributos**) e seus comportamentos (**métodos**).

```python
# Definindo a classe Aluno
class Aluno:
 def __init__(self, nome, matricula):
 # O self referencia a instância específica que está sendo criada
 self.nome = nome
 self.matricula = matricula

# Definindo a classe Curso
class Curso:
 def __init__(self, nome_curso):
 self.nome_curso = nome_curso
 # Usamos uma lista para armazenar os objetos de alunos matriculados
 self.alunos_matriculados = []

 def matricular_aluno(self, aluno):
 # Método que define a ação de adicionar um objeto Aluno à lista
 self.alunos_matriculados.append(aluno)
 print(f"Aluno {aluno.nome} matriculado com sucesso no curso {self.nome_curso}!")

 def listar_alunos(self):
 print(f"\n--- Lista de Alunos em {self.nome_curso} ---")
 for aluno in self.alunos_matriculados:
 print(f"Nome: {aluno.nome} | Matrícula: {aluno.matricula}")
```

#### Instanciação e Execução (O uso Real)

Após definir o "plano", criamos as instâncias reais (**objetos**) na memória do computador.

```python
# Criando objetos da classe Aluno
aluno1 = Aluno("Maria Silva", "2023001")
aluno2 = Aluno("João Souza", "2023002")

# Criando o objeto da classe Curso
meu_curso = Curso("Lógica de Programação com Python")

# Executando o comportamento de matrícula
meu_curso.matricular_aluno(aluno1)
meu_curso.matricular_aluno(aluno2)

# Visualizando o resultado
meu_curso.listar_alunos()
```

#### Por que usar essa abordagem em vez de listas simples?

1. **Abstração e Semântica:** Em vez de lidar com strings ou números soltos, o código lida com "Alunos" e "Cursos", o que torna a lógica mais próxima do problema de negócio e mais fácil de entender por humanos.
2. **Organização de Dados Compostos:** A classe `Curso` funciona como uma **estrutura de dados composta**, capaz de gerenciar múltiplos objetos `Aluno` de forma organizada.
3. **Facilidade de Manutenção:** Se a regra de matrícula mudar (por exemplo, se houver um limite de vagas), você altera apenas o método `matricular_aluno` dentro da classe `Curso`, sem precisar modificar o restante do programa.
4. **Padronização:** O uso do construtor `__init__` garante que todo aluno criado terá obrigatoriamente um nome e uma matrícula, evitando erros comuns de chaves esquecidas em dicionários.

Essa prática prepara os alunos para sistemas mais robustos, onde a transformação de dados desestruturados em **objetos manipuláveis** é essencial para a produtividade e escalabilidade do software.

### Conclusão - vantagens do POO

- **Abstração:** Permite modelar o problema de forma mais fiel à realidade, eliminando o "gap" entre o que o negócio precisa e o que o código faz.
- **Organização e Reúso:** Facilita a manutenção do software. Por exemplo, se a regra de cálculo mudar, você altera apenas o método dentro da classe, sem precisar mexer em todo o programa.
- **Estruturas Compostas:** Você pode criar listas de objetos (como uma lista de feedbacks), o que torna a manipulação de grandes volumes de dados muito mais intuitiva e escalável.

**Dica para o Colab:** No ambiente de nuvem do Google, você pode alternar entre células de texto (para documentar sua lógica) e células de código (para executar seus algoritmos). Lembre-se que o comando `self` é essencial em Python para indicar que você está acessando uma informação daquela instância específica do objeto.
