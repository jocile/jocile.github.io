---
title: cadastro_alunos.py
description: Neste artigo, vamos abordar a importância dos testes em desenvolvimento
  de software e como criar testes em Python utilizando a biblioteca unittest. Faremos…
date: '2026-09-17'
draft: false
---

## Criando Testes com `unittest` em Python para um Sistema de Cadastro de Alunos

### Introdução

Neste artigo, vamos abordar a importância dos testes em desenvolvimento de software e como criar testes em Python utilizando a biblioteca `unittest`. Faremos isso através de um exemplo prático: um sistema de cadastro de alunos. Veremos como testar as funcionalidades de cadastro de um aluno que possui nome, curso, data de nascimento e endereço.

### 1. Introdução aos Testes em Python

Testes são essenciais para garantir que nosso código funciona corretamente e que novas alterações não introduzem bugs. O Python oferece várias bibliotecas para testes, sendo uma das mais populares o `unittest`, que é baseada no modelo de teste unitário xUnit.

### 2. Estrutura do Projeto

Nosso projeto será estruturado da seguinte forma:

```
projeto_cadastro_alunos/
│
├── cadastro_alunos.py
├── test_cadastro_alunos.py
└── README.md
```

### 3. Implementação do Sistema de Cadastro de Alunos

Primeiro, vamos criar a funcionalidade de cadastro em `cadastro_alunos.py`.

```python

class Aluno:
    def __init__(self, nome, curso, data_nascimento, endereco):
        self.nome = nome
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"Aluno(nome={self.nome}, curso={self.curso}, data_nascimento={self.data_nascimento}, endereco={self.endereco})"
```

### 4. Criando os Testes com `unittest`

Agora, vamos criar os testes para a nossa classe `Aluno`. Criaremos um arquivo chamado `test_cadastro_alunos.py`.

```python
# test_cadastro_alunos.py
import unittest
from cadastro_alunos import Aluno

class TestCadastroAlunos(unittest.TestCase):

    def test_criacao_aluno(self):
        aluno = Aluno("João Silva", "Engenharia", "01/01/2000", "Rua A, 123")
        self.assertEqual(aluno.nome, "João Silva")
        self.assertEqual(aluno.curso, "Engenharia")
        self.assertEqual(aluno.data_nascimento, "01/01/2000")
        self.assertEqual(aluno.endereco, "Rua A, 123")

    def test_str_aluno(self):
        aluno = Aluno("João Silva", "Engenharia", "01/01/2000", "Rua A, 123")
        self.assertEqual(str(aluno), "Aluno(nome=João Silva, curso=Engenharia, data_nascimento=01/01/2000, endereco=Rua A, 123)")

if __name__ == '__main__':
    unittest.main()
```

### 5. Explicação dos Testes

- **test_criacao_aluno**: Este teste verifica se o objeto `Aluno` é criado corretamente com todos os atributos fornecidos. Utilizamos o método `assertEqual` para comparar os valores esperados com os valores reais dos atributos do objeto `Aluno`.
- **test_str_aluno**: Este teste verifica se a representação em string do objeto `Aluno` está correta. Usamos o método `assertEqual` para comparar a string esperada com a string retornada pelo método `__str__` da classe `Aluno`.

### 6. Executando os Testes

Para executar os testes, basta rodar o arquivo `test_cadastro_alunos.py` no terminal:

```bash
python -m unittest test_cadastro_alunos.py
```

### Conclusão

Neste artigo, vimos a importância dos testes em desenvolvimento de software e como criar testes unitários em Python utilizando a biblioteca `unittest`. Através do exemplo prático de um sistema de cadastro de alunos, aprendemos a criar testes para verificar se nossos objetos estão sendo criados corretamente e se suas representações em string estão corretas. Pratique criando mais testes e explore outras funcionalidades do `unittest` para garantir a qualidade do seu código.

### Exercício para os Alunos

Como exercício adicional, adicione novos métodos à classe `Aluno`, como a atualização dos dados do aluno, e crie testes para verificar se essas atualizações estão sendo realizadas corretamente.

```python
# Adicione este método à classe Aluno
def atualizar_endereco(self, novo_endereco):
    self.endereco = novo_endereco

# E crie um teste para ele
def test_atualizar_endereco(self):
    aluno = Aluno("João Silva", "Engenharia", "01/01/2000", "Rua A, 123")
    aluno.atualizar_endereco("Rua B, 456")
    self.assertEqual(aluno.endereco, "Rua B, 456")
```

Pratique e aprofunde-se no mundo dos testes unitários para se tornar um programador mais eficiente e seguro!

---

Espero que este guia tenha sido útil. Se tiverem dúvidas, sintam-se à vontade para perguntar. Vamos praticar!
