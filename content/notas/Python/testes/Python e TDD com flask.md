---
title: "Python e TDD com Flask"
date: 2026-11-08
draft: false
tags: ["python", "tdd", "testing", "flask", "pytest"]
description: "Guia prático de Test-Driven Development em Flask com Pytest, focado em fixtures e aplicação Factory pattern."
---

Para configurar o **Pytest** em uma aplicação **Flask**, o segredo está em usar as `fixtures` do Pytest. Elas permitem criar uma instância limpa do seu aplicativo e um cliente de testes que simula requisições HTTP (como GET e POST) sem precisar levantar um servidor real.

Aqui está o passo a passo prático para estruturar, configurar e rodar seus testes.

## 📋 1. Instalação das Dependências

Instale o **pytest** e, opcionalmente, o **pytest-flask** (que ajuda com utilitários extras):

```bash
pip install pytest Flask
```

## 📁 2. Estrutura Recomendada de Pastas

Para manter o projeto organizado, separe o código da aplicação dos testes:

```text
meu_projeto/
│
├── app.py             # Código do seu aplicativo Flask
├── conftest.py        # Configurações globais e fixtures do Pytest
└── tests/
    ├── __init__.py
    └── test_api.py    # Seus arquivos de teste
```

## 🔧 3. Configurando o Arquivo Principal (`app.py`)

Certifique-se de que seu aplicativo Flask está encapsulado em uma função (padrão _Application Factory_). Isso é fundamental para o TDD, pois permite criar instâncias isoladas do app para cada teste.

```python
# app.py
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True  # Ativa o modo de teste (melhora logs de erro)

    @app.route('/api/saudacao', methods=['GET'])
    def saudacao():
        return jsonify({"mensagem": "Olá, Mundo!"})

    @app.route('/api/soma', methods=['POST'])
    def soma():
        dados = request.get_json()
        resultado = dados['a'] + dados['b']
        return jsonify({"resultado": resultado})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

## ⚙️ 4. Configurando as Fixtures (`conftest.py`)

O Pytest lê o arquivo `conftest.py` automaticamente. É aqui que definimos o `client` que será injetado nos testes.

```python
# conftest.py
import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    yield app
    # Código de limpeza pós-teste viria aqui (ex: limpar banco)

@pytest.fixture()
def client(app):
    """Um cliente de testes para simular requisições HTTP"""
    return app.test_client()
```

## 🧪 5. Escrevendo os Testes (`tests/test_api.py`)

Agora, no ciclo TDD, você pode criar seus testes usando a fixture `client` apenas passando-a como argumento da função. O Pytest faz a injeção de dependência automaticamente.

```python
# tests/test_api.py

def test_rota_saudacao_deve_retornar_sucesso_e_mensagem_correta(client):
    # Executa uma requisição GET simulada
    resposta = client.get('/api/saudacao')
    
    # Validações (Asserts puros do Pytest)
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Olá, Mundo!"}

def test_rota_soma_deve_calcular_valores_corretamente(client):
    # Executa uma requisição POST simulada enviando JSON
    payload = {"a": 5, "b": 10}
    resposta = client.post('/api/soma', json=payload)
    
    assert resposta.status_code == 200
    assert resposta.json == {"resultado": 15}
```

## ▶️ 6. Como Executar os Testes

Abra o terminal na pasta raiz do projeto (`meu_projeto/`) e digite simplesmente:

```bash
pytest
```

Se quiser ver um relatório detalhado de quais funções passaram, use o modo verboso:

```bash
pytest -v
```

### 💡 Dica de TDD para Flask: Testando Erros Primeiro

Se você estivesse aplicando TDD e quisesse criar uma validação para impedir que a rota `/api/soma` recebesse strings, você escreveria o teste de falha primeiro:

```python
def test_soma_com_dados_invalidos_deve_retornar_erro(client):
    payload = {"a": "texto", "b": 10}
    resposta = client.post('/api/soma', json=payload)
    
    # O teste vai falhar (Red) até você tratar o TypeError na sua rota do app.py
    assert resposta.status_code == 400 
```

---

## 🏦 Exemplo Prático: Sistema Bancário com TDD

Vamos construir um **exemplo prático completo** aplicando o ciclo do TDD no Flask com Pytest.

### Cenário: API de Débitos para Sistema Bancário

Precisamos criar uma rota `/api/deposito`. Se o valor for menor ou igual a zero, a API deve rejeitar.

#### Passo 1: Escrever o Teste Primeiro (RED 🔴)

```python
# test_app.py
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_deposito_com_sucesso_deve_atualizar_saldo(client):
    payload = {"valor": 150.00}
    resposta = client.post('/api/deposito', json=payload)
    
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Depósito realizado!", "novo_saldo": 150.00}

def test_deposito_com_valor_negativo_deve_retornar_erro(client):
    payload = {"valor": -50.00}
    resposta = client.post('/api/deposito', json=payload)
    
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "O valor do depósito deve ser maior que zero."}
```

#### Passo 2: Escrever o Código Mínimo (GREEN 🟢)

```python
# app.py
from flask import Flask, request, jsonify

SALDO_ATUAL = 0.0

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.route('/api/deposito', methods=['POST'])
    def deposito():
        global SALDO_ATUAL
        dados = request.get_json()
        valor = dados.get('valor', 0)

        if valor <= 0:
            return jsonify({"erro": "O valor do depósito deve ser maior que zero."}), 400

        SALDO_ATUAL += valor
        return jsonify({"mensagem": "Depósito realizado!", "novo_saldo": SALDO_ATUAL}), 200

    return app
```

#### Passo 3: Refatorar com Segurança (REFACTOR 🔵)

```python
# app.py - Versão Refatorada
from flask import Flask, request, jsonify

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor
        return self.saldo

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    
    conta = ContaBancaria()

    @app.route('/api/deposito', methods=['POST'])
    def deposito():
        dados = request.get_json()
        valor = dados.get('valor', 0)

        try:
            novo_saldo = conta.depositar(valor)
            return jsonify({"mensagem": "Depósito realizado!", "novo_saldo": novo_saldo}), 200
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    return app
```

---

## 🐛 Como Identificar e Corrigir Erros

Imagine que um usuário descobriu um erro: _"Se eu enviar um texto no campo valor em vez de número, a API quebra com erro 500!"_

### Adicione o Teste do Bug

```python
# test_app.py
def test_deposito_com_texto_deve_retornar_erro_de_validacao(client):
    payload = {"valor": "texto_invalido"}
    resposta = client.post('/api/deposito', json=payload)
    
    assert resposta.status_code == 400
    assert "erro" in resposta.json
```

### Correção na Classe `ContaBancaria`

```python
def depositar(self, valor):
    if not isinstance(valor, (int, float)):
        raise ValueError("O valor enviado deve ser um número válido.")
    if valor <= 0:
        raise ValueError("O valor do depósito deve ser maior que zero.")
    self.saldo += valor
    return self.saldo
```

---

## 🚀 Próximos Passos Sugeridos

- **Banco de Dados Real**: Adicionar SQLite usando SQLAlchemy para persistir o saldo?
- **Autenticação JWT**: Testar cenários que exigem validação de tokens em cabeçalhos HTTP?
