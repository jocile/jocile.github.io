---
title: Unittest Validacao
description: Testar entradas de formulário é crucial para garantir que seu aplicativo
  aceite apenas dados válidos e forneça feedback adequado aos usuários. Aqui estão…
date: '2026-09-17'
draft: false
---

## Como Testar Entradas de Formulário com unittest

Testar entradas de formulário é crucial para garantir que seu aplicativo aceite apenas dados válidos e forneça feedback adequado aos usuários. Aqui estão algumas melhores práticas para testar entradas de formulário usando o framework `unittest` do Python:

### 1. Teste cada campo individualmente

Crie testes separados para cada campo do formulário, verificando se a validação está funcionando corretamente para diferentes tipos de entrada. Por exemplo, para um campo de nome:

```python
def test_name_field_accepts_valid_input(self):
    form = MyForm(data={'name': 'John Doe'})
    self.assertTrue(form.is_valid())

def test_name_field_rejects_empty_input(self):
    form = MyForm(data={'name': ''})
    self.assertFalse(form.is_valid())
    self.assertIn('name', form.errors)
```

### 2. Use dados de teste realistas

Ao testar entradas de formulário, use dados de teste realistas que representem o que os usuários realmente inseririam. Isso ajudará a identificar problemas que podem surgir com entradas reais.

```python
def test_email_field_accepts_valid_input(self):
    form = MyForm(data={'email': 'johndoe@example.com'})
    self.assertTrue(form.is_valid())
```

### 3. Teste casos de borda

Além de testar entradas válidas, também teste casos de borda, como valores muito longos, caracteres especiais, etc. Isso ajudará a garantir que seu aplicativo lide com entradas inesperadas de maneira apropriada.

```python
def test_password_field_rejects_short_input(self):
    form = MyForm(data={'password': 'weak'})
    self.assertFalse(form.is_valid())
    self.assertIn('password', form.errors)
```

### 4. Verifique mensagens de erro

Certifique-se de que seu aplicativo forneça mensagens de erro claras e úteis quando uma entrada for rejeitada. Teste se as mensagens de erro corretas são exibidas para cada tipo de entrada inválida.

```python
def test_form_displays_correct_error_message_for_invalid_email(self):
    form = MyForm(data={'email': 'invalid'})
    self.assertFalse(form.is_valid())
    self.assertIn('Enter a valid email address.', form.errors['email'])
```

### 5. Teste a lógica de negócios relacionada

Além de testar a validação de entrada, também teste a lógica de negócios relacionada ao formulário, como cálculos baseados em valores de entrada ou interações com outros modelos.

```python
def test_form_calculates_total_correctly(self):
    form = OrderForm(data={'quantity': 10, 'price': 5.99})
    self.assertTrue(form.is_valid())
    order = form.save()
    self.assertEqual(order.total, 59.90)
```

Seguindo essas melhores práticas, você pode escrever testes abrangentes para entradas de formulário usando o `unittest`, garantindo que seu aplicativo aceite apenas dados válidos e forneça uma ótima experiência do usuário.

## Validando campos de formulário

Exemplos de funções que podem ser testadas usando as melhores práticas mencionadas anteriormente.

Suponha que tenhamos um sistema de cadastro de usuários com as seguintes funções:

```python
def register_user(name, email, password):
    """
    Registra um novo usuário no sistema.
    
    Args:
        name (str): O nome do usuário.
        email (str): O email do usuário.
        password (str): A senha do usuário.
    
    Returns:
        bool: True se o usuário foi registrado com sucesso, False caso contrário.
    """
    if not validate_name(name):
        return False
    if not validate_email(email):
        return False
    if not validate_password(password):
        return False
    
    # Lógica para criar o usuário no banco de dados
    # ...
    
    return True

def validate_name(name):
    """
    Valida o nome do usuário.
    
    Args:
        name (str): O nome do usuário.
    
    Returns:
        bool: True se o nome for válido, False caso contrário.
    """
    if not isinstance(name, str) or len(name.strip()) < 3:
        return False
    return True

def validate_email(email):
    """
    Valida o email do usuário.
    
    Args:
        email (str): O email do usuário.
    
    Returns:
        bool: True se o email for válido, False caso contrário.
    """
    if not isinstance(email, str) or '@' not in email:
        return False
    return True

def validate_password(password):
    """
    Valida a senha do usuário.
    
    Args:
        password (str): A senha do usuário.
    
    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    if not isinstance(password, str) or len(password) < 8:
        return False
    return True
```

Agora, vamos escrever os testes unitários para essas funções usando o `unittest`:

```python
import unittest

class TestUserRegistration(unittest.TestCase):
    def test_register_user_with_valid_input(self):
        self.assertTrue(register_user('John Doe', 'johndoe@example.com', 'MyStrongPassword'))

    def test_register_user_with_invalid_name(self):
        self.assertFalse(register_user('', 'johndoe@example.com', 'MyStrongPassword'))
        self.assertFalse(register_user(123, 'johndoe@example.com', 'MyStrongPassword'))

    def test_register_user_with_invalid_email(self):
        self.assertFalse(register_user('John Doe', 'johndoeexample.com', 'MyStrongPassword'))
        self.assertFalse(register_user('John Doe', 123, 'MyStrongPassword'))

    def test_register_user_with_invalid_password(self):
        self.assertFalse(register_user('John Doe', 'johndoe@example.com', 'weak'))
        self.assertFalse(register_user('John Doe', 'johndoe@example.com', 123456))

    def test_validate_name(self):
        self.assertTrue(validate_name('John Doe'))
        self.assertFalse(validate_name(''))
        self.assertFalse(validate_name(123))

    def test_validate_email(self):
        self.assertTrue(validate_email('johndoe@example.com'))
        self.assertFalse(validate_email('johndoeexample.com'))
        self.assertFalse(validate_email(123))

    def test_validate_password(self):
        self.assertTrue(validate_password('MyStrongPassword'))
        self.assertFalse(validate_password('weak'))
        self.assertFalse(validate_password(123456))

if __name__ == '__main__':
    unittest.main()
```

Neste exemplo, criamos uma classe `TestUserRegistration` que herda de `unittest.TestCase`. Dentro desta classe, definimos vários métodos de teste para verificar o comportamento das funções `register_user()`, `validate_name()`, `validate_email()` e `validate_password()`.

Cada método de teste verifica um cenário específico, como registrar um usuário com entrada válida, registrar um usuário com entrada inválida (nome, email ou senha), e testar individualmente as funções de validação.

Ao executar esses testes, o `unittest` irá verificar se as funções estão se comportando conforme o esperado, ajudando a garantir a integridade do sistema de cadastro de usuários.

Lembre-se de que essas são apenas algumas das melhores práticas para testar entradas de formulário. Você pode adaptar e expandir esses testes de acordo com as necessidades específicas do seu aplicativo.

## Referências

[1] <https://www.trilhadequalidade.com.br/dominando-testes-unitarios-em-react-e-node-js/>\
[2] <https://learn.microsoft.com/pt-br/dotnet/core/testing/unit-testing-best-practices>\
[3] <https://academy.pega.com/pt-br/topic/unit-tests/v3>\
[4] <https://blog.formacao.dev/testes-unitarios-em-python-usando-unittest/>\
[5] <https://www.devmedia.com.br/teste-unitario-com-pyunit/41233>
