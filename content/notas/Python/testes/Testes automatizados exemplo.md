---
title: aluno.py
description: Vamos implementar testes automatizados para a funcionalidade de cadastro
  de alunos utilizando as bibliotecas unittest e pytest. Esses testes garantirão que
  as…
date: '2026-09-17'
draft: false
---

### Implementando Testes Automatizados com Python

Vamos implementar testes automatizados para a funcionalidade de cadastro de alunos utilizando as bibliotecas `unittest` e `pytest`. Esses testes garantirão que as funções de adicionar novos alunos ao sistema funcionem conforme o esperado.

#### 1. Estrutura Básica do Código

Primeiro, definimos a estrutura básica do nosso código de cadastro de alunos:

```python

class Aluno:
    def __init__(self, nome, idade, matricula, curso):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.curso = curso

class SistemaCadastro:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome, idade, matricula, curso):
        novo_aluno = Aluno(nome, idade, matricula, curso)
        self.alunos.append(novo_aluno)
        return novo_aluno
```

#### 2. Testando com `unittest`

Para testar a funcionalidade de adicionar alunos, utilizamos a biblioteca `unittest` que é integrada ao Python:

```python
# test_aluno_unittest.py
import unittest
from aluno import SistemaCadastro, Aluno

class TestSistemaCadastro(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaCadastro()

    def test_adicionar_aluno(self):
        aluno = self.sistema.adicionar_aluno("João", 20, "12345", "Computação")
        self.assertEqual(aluno.nome, "João")
        self.assertEqual(aluno.idade, 20)
        self.assertEqual(aluno.matricula, "12345")
        self.assertEqual(aluno.curso, "Computação")
        self.assertIn(aluno, self.sistema.alunos)

    def test_adicionar_aluno_lista(self):
        self.sistema.adicionar_aluno("Maria", 22, "67890", "Engenharia")
        self.assertEqual(len(self.sistema.alunos), 1)
        self.assertEqual(self.sistema.alunos[0].nome, "Maria")

if __name__ == '__main__':
    unittest.main()
```

#### 3. Testando com `pytest`

A biblioteca `pytest` oferece uma sintaxe mais simples e poderosa para escrever testes. Aqui está como podemos usar `pytest` para testar a mesma funcionalidade:

```python
# test_aluno_pytest.py
import pytest
from aluno import SistemaCadastro, Aluno

@pytest.fixture
def sistema():
    return SistemaCadastro()

def test_adicionar_aluno(sistema):
    aluno = sistema.adicionar_aluno("João", 20, "12345", "Computação")
    assert aluno.nome == "João"
    assert aluno.idade == 20
    assert aluno.matricula == "12345"
    assert aluno.curso == "Computação"
    assert aluno in sistema.alunos

def test_adicionar_aluno_lista(sistema):
    sistema.adicionar_aluno("Maria", 22, "67890", "Engenharia")
    assert len(sistema.alunos) == 1
    assert sistema.alunos[0].nome == "Maria"
```

#### 4. Executando os Testes

Para executar os testes utilizando `unittest`, você pode usar o seguinte comando no terminal:

```bash
python -m unittest test_aluno_unittest.py
```

Para executar os testes utilizando `pytest`, você pode usar o comando:

```bash
pytest test_aluno_pytest.py
```

### Conclusão

A prática de escrever testes automatizados para suas funcionalidades é crucial para garantir a qualidade e a confiabilidade do seu software. `unittest` e `pytest` são ferramentas poderosas que permitem escrever e executar testes de maneira eficiente. Com essas ferramentas, você pode assegurar que seu sistema de cadastro de alunos funcione conforme o esperado, mesmo após futuras alterações no código.
