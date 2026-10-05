---
title: Teste De Cadastro De Usuario
description: 'Descreva como usar o unittest em python para testar um cadastro de usuário
  com: receber nome, cpf, numero, email e idade do usuário'
date: '2026-09-26'
draft: false
tags:
- Python/testes
---

Descreva como usar o unittest em python para testar um cadastro de usuário com: receber nome, cpf, numero, email e idade do usuário

Para utilizar o unittest em Python para testar um cadastro de usuário, você pode seguir os seguintes passos:

1. Importe o modulo unittest:

```python
import unittest
```

2. Crie uma classe que irá conter os seus testes:

```python
class UserRegistrationTest(unittest.TestCase):
    pass
```

3. Defina um método de setup para criar um objeto usuário que pode ser usado nos seus testes:

```python
def setUp(self):
    self.user = {
        'nome': '',
        'cpf': '',
        'numero': '',
        'email': '',
        'idade': 0
    }
```

4. Defina os métodos de teste para cada caso de teste:

```python
def test_receber_nome_correto(self):
    self.user['nome'] = 'João'
    # Chame o método de cadastro com os dados do usuário
    registration_method(self.user)
    # Verifique se o nome foi cadastrado corretamente
    self.assertEqual(self.user, {'nome': 'João', ...})

def test_receber_nome_vazio(self):
    self.user['nome'] = ''
    try:
        # Tente chamar o método de cadastro com os dados do usuário
        registration_method(self.user)
    except ValueError as e:
        self.assertEqual(str(e), 'Nome é obrigatório')
    else:
        self.fail('Deveria ter sido lançado um erro')

def test_receber_cpf_invalido(self):
    self.user['cpf'] = '123.456-78'
    try:
        # Tente chamar o método de cadastro com os dados do usuário
        registration_method(self.user)
    except ValueError as e:
        self.assertEqual(str(e), 'CPF inválido')
    else:
        self.fail('Deveria ter sido lançado um erro')

def test_receber_email_invalido(self):
    self.user['email'] = 'não é um email válido'
    try:
        # Tente chamar o método de cadastro com os dados do usuário
        registration_method(self.user)
    except ValueError as e:
        self.assertEqual(str(e), 'Email inválido')
    else:
        self.fail('Deveria ter sido lançado um erro')

def test_receber_idade_invalida(self):
    self.user['idade'] = -1
    try:
        # Tente chamar o método de cadastro com os dados do usuário
        registration_method(self.user)
    except ValueError as e:
        self.assertEqual(str(e), 'Idade inválida')
    else:
        self.fail('Deveria ter sido lançado um erro')

def test_receber_todos_campos_corretos(self):
    self.user['nome'] = 'João'
    self.user['cpf'] = '123.456-78'
    self.user['numero'] = ''
    self.user['email'] = 'joao@example.com'
    self.user['idade'] = 25
    # Chame o método de cadastro com os dados do usuário
    registration_method(self.user)
    # Verifique se o cadastro foi realizado com sucesso
    self.assertEqual(self.user, {'nome': 'João', ...})
```

5. Execute os testes:

```python
if __name__ == '__main__':
    unittest.main()
```
