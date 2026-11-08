---
title: tests/test_cadastro_usuarios.py
description: Neste artigo, vamos aplicar a metodologia de Desenvolvimento Orientado
  a Testes (TDD) utilizando pytest. No TDD, escrevemos os testes primeiro e depois…
date: '2026-09-17'
draft: false
---

## Criando Testes com TDD e `pytest` em Python para um Sistema de Cadastro de Usuários de um Banco

### Introdução

Neste artigo, vamos aplicar a metodologia de Desenvolvimento Orientado a Testes (TDD) utilizando `pytest`. No TDD, escrevemos os testes primeiro e depois implementamos o código para passar nesses testes. Vamos criar um sistema de cadastro de usuários de um banco, incluindo validações de CPF e data de nascimento.

### 1. Introdução ao TDD

TDD é uma prática de desenvolvimento de software onde os testes são escritos antes do código funcional. Isso garante que cada parte do código é testada desde o início, aumentando a confiança e reduzindo bugs.

### 2. Estrutura do Projeto

Nosso projeto será estruturado da seguinte forma:

```
projeto_cadastro_banco/
│
├── banco/
│   ├── __init__.py
│   └── cadastro_usuarios.py
├── tests/
│   ├── __init__.py
│   └── test_cadastro_usuarios.py
└── README.md
```

### 3. Escrevendo os Testes com `pytest`

Primeiro, vamos escrever os testes para a nossa classe `Usuario` em `test_cadastro_usuarios.py`.

```python
import pytest
from banco.cadastro_usuarios import Usuario

def test_criacao_usuario():
    usuario = Usuario("Maria Souza", "123.456.789-00", "15/05/1985")
    assert usuario.nome == "Maria Souza"
    assert usuario.cpf == "123.456.789-00"
    assert usuario.data_nascimento == "15/05/1985"

def test_str_usuario():
    usuario = Usuario("Maria Souza", "123.456.789-00", "15/05/1985")
    assert str(usuario) == "Usuario(nome=Maria Souza, cpf=123.456.789-00, data_nascimento=15/05/1985)"

def test_validar_cpf():
    assert Usuario.validar_cpf("123.456.789-00")
    assert not Usuario.validar_cpf("123.456.789-0A")
    assert not Usuario.validar_cpf("12345678900")

def test_validar_data_nascimento():
    assert Usuario.validar_data_nascimento("15/05/1985")
    assert not Usuario.validar_data_nascimento("15-05-1985")
    assert not Usuario.validar_data_nascimento("31/02/2020")
    assert not Usuario.validar_data_nascimento("15/05/2050")
```

### 4. Implementando a Classe `Usuario`

Com os testes escritos, agora vamos implementar a classe `Usuario` em `cadastro_usuarios.py` para passar nesses testes.

```python
# banco/cadastro_usuarios.py

import re
from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Usuario(nome={self.nome}, cpf={self.cpf}, data_nascimento={self.data_nascimento})"

    @staticmethod
    def validar_cpf(cpf):
        # Simples validação de CPF (apenas formato)
        return re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf) is not None

    @staticmethod
    def validar_data_nascimento(data_nascimento):
        # Simples validação de data (formato e lógica básica)
        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data <= datetime.now()
        except ValueError:
            return False
```

### 5. Executando os Testes

Para executar os testes, basta rodar o comando `pytest` no terminal dentro do diretório do projeto:

```bash
pytest
```

### 6. Explicação dos Testes

- **test_criacao_usuario**: Verifica se o objeto `Usuario` é criado corretamente com todos os atributos fornecidos.
- **test_str_usuario**: Verifica se a representação em string do objeto `Usuario` está correta.
- **test_validar_cpf**: Testa a função `validar_cpf` para verificar se ela valida corretamente os CPFs.
- **test_validar_data_nascimento**: Testa a função `validar_data_nascimento` para verificar se ela valida corretamente as datas de nascimento.

### Conclusão

Neste artigo, aplicamos a metodologia TDD para criar um sistema de cadastro de usuários de um banco utilizando `pytest`. Escrevemos os testes primeiro e depois implementamos o código para passar nesses testes. O TDD nos ajuda a garantir que nosso código é confiável e bem testado desde o início.

### Exercício para os Alunos

Como exercício adicional, adicione novos métodos à classe `Usuario`, como a atualização dos dados do usuário, e crie testes para verificar se essas atualizações estão sendo realizadas corretamente.

```python
# Adicione este método à classe Usuario
def atualizar_cpf(self, novo_cpf):
    if self.validar_cpf(novo_cpf):
        self.cpf = novo_cpf
        return True
    return False

# E crie um teste para ele
def test_atualizar_cpf():
    usuario = Usuario("Maria Souza", "123.456.789-00", "15/05/1985")
    assert usuario.atualizar_cpf("987.654.321-00")
    assert usuario.cpf == "987.654.321-00"
    assert not usuario.atualizar_cpf("invalid_cpf")
```

Pratique e explore outras funcionalidades do `pytest` para garantir a qualidade do seu código. Se tiverem dúvidas, sintam-se à vontade para perguntar. Vamos praticar!
