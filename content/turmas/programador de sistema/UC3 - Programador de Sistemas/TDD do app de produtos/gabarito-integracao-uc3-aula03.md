---
title: Gabarito - Testes de integração da Aula 3 da UC3
description: conftest.py, tests/test_integracao.py, demonstração do teste no banco real e rubrica da Avaliação 1 da uc3.03. Não publicar.
date: 2026-11-13
draft: false
tags:
  - programador-sistemas/gabarito
  - uc3
---

%%
> [!warning] Uso exclusivo do docente
> Não publicar no Quartz. O `conftest.py` abaixo é **material que você entrega aos alunos** no repositório-base (`tests/conftest.py`); o restante é só seu.

> [!bug] Suposições sobre o repositório-base em Flask
> O repositório em Flask não aparece nas notas; reconstruí o contrato a partir do código em Bottle (`produtos-04` a `produtos-06`). **Rode tudo uma vez antes da aula** e ajuste:
>
> - `app.py` expõe o objeto `app` (Flask) e **não** inicializa nem cria banco ao ser importado.
> - `dados.py` tem `DB_PATH` (variável do módulo) e `abrir_conexao()`, que lê `DB_PATH` a cada chamada. É isso que permite trocar o banco em teste.
> - `dados.py` tem `registrar_venda(conn, id_produto, quantidade)`. Na nota `produtos-02` ela existe só no Colab; se o repositório não a tiver, acrescente (código abaixo).
> - Rotas: `/login` (POST: `usuario`, `senha`), `/produtos`, `/produtos/novo`, `POST /produtos`, com as mesmas mensagens da nota `produtos-06`.
> - O segredo vem da variável `APP_SECRET`, lida **quando o app é importado**.
> - Tabelas `Categoria`, `Produto`, `Vendas` e `Usuario`, como nas notas da UC2.

%%

**Testar a venda no banco real**

- **Antes de começar, faça uma cópia do banco:** `cp gestao_produtos.db gestao_produtos.bak` (no Windows: `copy gestao_produtos.db gestao_produtos.bak`).
- Crie o arquivo `tests/test_rascunho_banco_real.py`.
- Escreva **um teste** que confirme: _uma venda de 100 unidades de um produto com 3 em estoque não altera o estoque nem registra a venda._
- Como o banco real não tem um produto com exatamente 3 em estoque, o próprio teste deve **cadastrar um produto de teste** com estoque 3 antes de tentar a venda.
- Execute o teste **duas vezes** `pytest .\tests\test_rascunho_banco_real.py -v` e olhe o banco (`/produtos`) depois de cada execução.

## `tests/test_rascunho_banco_real.py`

```python
import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

import dados


def test_venda_maior_que_estoque_nao_altera_nada():
    caminho_bd = str(Path(__file__).parent.parent / "gestao_produtos.db")
    with closing(dados.abrir_conexao(caminho_bd)) as conn:
        conn.execute(
            "INSERT INTO Produto (nome, preco, estoque, id_categoria) "
            "VALUES ('Produto de teste', 10.0, 3, 1);"
        )
        conn.commit()
        id_produto = conn.execute("SELECT MAX(id_produto) FROM Produto;").fetchone()[0]

    with pytest.raises(sqlite3.IntegrityError):
        dados.registrar_venda(caminho_bd, id_produto, 100)

```

Outra versão:

```python
# tests/test_rascunho_banco_real.py   (APAGAR depois da conversa)
from contextlib import closing

import pytest
import sqlite3

import dados


def test_venda_maior_que_estoque_nao_altera_nada():
    with closing(dados.abrir_conexao()) as conn:
        conn.execute(
            "INSERT INTO Produto (nome, preco, estoque, id_categoria) "
            "VALUES ('Produto de teste', 10.0, 3, 1);"
        )
        conn.commit()
        id_produto = conn.execute("SELECT MAX(id_produto) FROM Produto;").fetchone()[0]

        with pytest.raises(sqlite3.IntegrityError):
            dados.registrar_venda(conn, id_produto, 100)

        estoque = conn.execute(
            "SELECT estoque FROM Produto WHERE id_produto = ?;", (id_produto,)
        ).fetchone()[0]
        assert estoque == 3
```

>[!info] O que observar
>
> - O teste **passa**, mas deixa um "Produto de teste" no banco real a cada execução.
> - Na segunda execução existem **dois** produtos de teste, o `MAX(id_produto)` é outro e a lista do sistema foi poluída.
> - Se o teste falhasse no meio, ficaria pior: dados órfãos sem ninguém saber.
>
>>[!question] Respostas esperadas
>>
>> - **Por que o teste mexeu nos dados?** Porque preparou o cenário **no banco real**, e ninguém desfaz.
>> - **O que mudou na segunda execução?** Há mais um produto, o id mudou e o resultado passa a depender do estado anterior.
>> - **Como preparar um cenário sempre igual?** Um banco novo e descartável a cada teste: a **fixture**.

## 0. `registrar_venda` (acrescentar a `dados.py` se não existir)

```python
def registrar_venda(conn, id_produto, quantidade):
    """Baixa o estoque e registra a venda na mesma transação."""
    with conn:  # commit se der certo, rollback se der erro
        conn.execute(
            "UPDATE Produto SET estoque = estoque - ? WHERE id_produto = ?;",
            (quantidade, id_produto),
        )
        conn.execute(
            "INSERT INTO Vendas (id_produto, quantidade) VALUES (?, ?);",
            (id_produto, quantidade),
        )
```

Se o estoque ficaria negativo, o `CHECK(estoque >= 0)` levanta `sqlite3.IntegrityError` e o `with conn` desfaz tudo.

## 1. `tests/conftest.py`

```python
"""
Fixtures compartilhadas pelos testes.

O pytest carrega este arquivo sozinho. Qualquer teste pode "pedir" uma
fixture escrevendo o nome dela como parâmetro.
"""
import os
import re
import sqlite3

# O segredo precisa existir ANTES de importar o app
os.environ.setdefault("APP_SECRET", "segredo-somente-para-testes")

import pytest

import dados
from app import app as aplicacao
from seguranca import gerar_hash_senha

USUARIO_TESTE = "tester"
SENHA_TESTE = "SenhaTeste123"

ESQUEMA = """
CREATE TABLE Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);
CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL CHECK(estoque >= 0),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);
CREATE TABLE Vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    data_venda TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);
CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    salt TEXT NOT NULL
);
"""

CATEGORIAS = [("Eletrônicos",), ("Móveis",), ("Vestuário",)]

# (nome, preço, estoque, id_categoria)
PRODUTOS = [
    ("Smartphone", 1600.00, 10, 1),
    ("Notebook", 3500.00, 5, 1),
    ("Sofá", 800.00, 3, 2),
    ("Cadeira de Escritório", 350.00, 12, 2),
    ("Camisa Polo", 80.00, 25, 3),
]


@pytest.fixture(scope="session")
def credenciais_hash():
    """Gera o hash da senha UMA vez por execução (o hash é lento de propósito)."""
    return gerar_hash_senha(SENHA_TESTE)


@pytest.fixture
def banco_temporario(tmp_path, monkeypatch, credenciais_hash):
    """Cria um banco novo para cada teste e faz o sistema usá-lo.

    O arquivo fica numa pasta temporária que o pytest apaga depois,
    então o banco real do sistema nunca é tocado.
    """
    caminho = tmp_path / "banco_de_teste.db"

    conn = sqlite3.connect(caminho)
    conn.executescript(ESQUEMA)
    conn.executemany("INSERT INTO Categoria (nome_categoria) VALUES (?);", CATEGORIAS)
    conn.executemany(
        "INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);",
        PRODUTOS,
    )
    senha_hash, salt = credenciais_hash
    conn.execute(
        "INSERT INTO Usuario (login, senha_hash, salt) VALUES (?, ?, ?);",
        (USUARIO_TESTE, senha_hash, salt),
    )
    conn.commit()
    conn.close()

    # Aponta o sistema para o banco temporário (desfeito ao fim do teste)
    monkeypatch.setattr(dados, "DB_PATH", caminho)
    return caminho


@pytest.fixture
def banco(banco_temporario):
    """Conexão para o teste consultar o banco temporário."""
    conn = sqlite3.connect(banco_temporario)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


@pytest.fixture
def cliente(banco_temporario):
    """Test client do Flask: simula o navegador sem abrir o servidor."""
    aplicacao.config.update(TESTING=True)
    with aplicacao.test_client() as c:
        yield c


@pytest.fixture
def cliente_logado(cliente):
    """O mesmo cliente, já autenticado com o usuário de teste."""
    resposta = cliente.post(
        "/login", data={"usuario": USUARIO_TESTE, "senha": SENHA_TESTE}
    )
    assert resposta.status_code == 302, "O login de teste falhou"
    return cliente


@pytest.fixture
def obter_token_csrf(cliente_logado):
    """Devolve uma função que lê o token CSRF do formulário de novo produto."""

    def _obter():
        pagina = cliente_logado.get("/produtos/novo").get_data(as_text=True)
        achou = re.search(r'name="csrf_token" value="([^"]+)"', pagina)
        assert achou, "Token CSRF não encontrado no formulário"
        return achou.group(1)

    return _obter
```

Correção `tests/conftest.py`

```python
"""
Fixtures compartilhadas pelos testes.

O pytest carrega este arquivo sozinho. Qualquer teste pode "pedir" uma
fixture escrevendo o nome dela como parâmetro.
"""

import re
from contextlib import closing

import pytest

import dados
from app import create_app
from seguranca import gerar_hash_senha

USUARIO_TESTE = "tester"
SENHA_TESTE = "SenhaTeste123"


@pytest.fixture(scope="session")
def credenciais_hash():
    """Gera o hash da senha UMA vez por execução (o hash é lento de propósito)."""
    return gerar_hash_senha(SENHA_TESTE)


@pytest.fixture
def banco_temporario(tmp_path, credenciais_hash):
    """Cria um banco novo para cada teste e devolve o CAMINHO dele.

    O arquivo fica numa pasta temporária que o pytest apaga depois,
    então o banco real do sistema nunca é tocado.
    """
    caminho = tmp_path / "banco_de_teste.db"

    dados.criar_estrutura(caminho)  # cria as tabelas
    dados.popular_exemplo(caminho)  # 3 categorias e 5 produtos, sempre os mesmos

    senha_hash, salt = credenciais_hash
    with closing(dados.abrir_conexao(caminho)) as conn:
        with conn:
            conn.execute(
                "INSERT INTO Usuario (login, senha_hash, salt) VALUES (?, ?, ?);",
                (USUARIO_TESTE, senha_hash, salt),
            )
    return caminho


@pytest.fixture
def banco(banco_temporario):
    """Conexão para o teste consultar o banco temporário."""
    conn = dados.abrir_conexao(banco_temporario)
    yield conn
    conn.close()


@pytest.fixture
def aplicacao(banco_temporario):
    """Uma aplicação Flask nova, configurada para usar o banco temporário."""
    return create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "segredo-somente-para-testes",
            "DB_PATH": banco_temporario,
        }
    )


@pytest.fixture
def cliente(aplicacao):
    """Test client do Flask: simula o navegador sem abrir o servidor."""
    with aplicacao.test_client() as c:
        yield c


@pytest.fixture
def cliente_logado(cliente):
    """O mesmo cliente, já autenticado com o usuário de teste."""
    resposta = cliente.post(
        "/login", data={"usuario": USUARIO_TESTE, "senha": SENHA_TESTE}
    )
    assert resposta.status_code == 302, "O login de teste falhou"
    return cliente


@pytest.fixture
def obter_token_csrf(cliente_logado):
    """Devolve uma função que lê o token CSRF do formulário de novo produto."""

    def _obter():
        pagina = cliente_logado.get("/produtos/novo").get_data(as_text=True)
        achou = re.search(r'name="csrf_token"\s+value="([^"]+)"', pagina)
        assert achou, "Token CSRF não encontrado no formulário"
        return achou.group(1)

    return _obter

```

> [!tip] Pontos para observar
>
> - `tmp_path` e `monkeypatch` são fixtures **do próprio pytest**.
> - `yield` separa "preparar" (antes) de "limpar" (depois).
> - `scope="session"` evita refazer o hash a cada teste. Sem isso, cada teste pagaria o custo do PBKDF2 duas vezes.
> - `monkeypatch.setattr` troca o `DB_PATH` **só durante o teste**.

## 2. `tests/test_integracao.py`

```python
import sqlite3
from contextlib import closing

import pytest

import dados
from conftest import SENHA_TESTE, USUARIO_TESTE


def test_venda_com_estoque_suficiente_baixa_estoque_e_registra_venda(banco):
    # Preparar: Smartphone (id 1) começa com 10 unidades (ver conftest)
    # Executar
    with closing(dados.abrir_conexao()) as conn:
        dados.registrar_venda(conn, 1, 3)

    # Verificar
    estoque = banco.execute(
        "SELECT estoque FROM Produto WHERE id_produto = 1;"
    ).fetchone()["estoque"]
    vendas = banco.execute(
        "SELECT COUNT(*) AS total, SUM(quantidade) AS unidades "
        "FROM Vendas WHERE id_produto = 1;"
    ).fetchone()

    assert estoque == 7
    assert vendas["total"] == 1
    assert vendas["unidades"] == 3


def test_venda_com_estoque_insuficiente_nao_altera_nada(banco):
    # Preparar: Sofá (id 3) tem 3 unidades
    # Executar e Verificar o erro esperado
    with closing(dados.abrir_conexao()) as conn:
        with pytest.raises(sqlite3.IntegrityError):
            dados.registrar_venda(conn, 3, 100)

    # Verificar que nada mudou
    estoque = banco.execute(
        "SELECT estoque FROM Produto WHERE id_produto = 3;"
    ).fetchone()["estoque"]
    total_vendas = banco.execute("SELECT COUNT(*) FROM Vendas;").fetchone()[0]

    assert estoque == 3
    assert total_vendas == 0


def test_pagina_de_novo_produto_sem_login_redireciona_para_o_login(cliente):
    resposta = cliente.get("/produtos/novo")

    assert resposta.status_code == 302
    assert "/login" in resposta.headers["Location"]


def test_login_valido_libera_a_lista_de_produtos(cliente):
    # Executar o login
    login = cliente.post(
        "/login", data={"usuario": USUARIO_TESTE, "senha": SENHA_TESTE}
    )
    assert login.status_code == 302

    # Verificar que a lista agora abre
    lista = cliente.get("/produtos")

    assert lista.status_code == 200
    assert "Smartphone" in lista.get_data(as_text=True)


# ---- Desafios opcionais ----

def test_envio_sem_token_csrf_retorna_403(cliente_logado, banco):
    resposta = cliente_logado.post(
        "/produtos",
        data={"nome": "Teste CSRF", "preco": "10,00", "estoque": "1", "id_categoria": "1"},
    )

    assert resposta.status_code == 403
    assert banco.execute("SELECT COUNT(*) FROM Produto;").fetchone()[0] == 5


def test_dados_invalidos_retornam_400(cliente_logado, obter_token_csrf, banco):
    resposta = cliente_logado.post(
        "/produtos",
        data={
            "csrf_token": obter_token_csrf(),
            "nome": "Teste",
            "preco": "-10",
            "estoque": "1",
            "id_categoria": "1",
        },
    )

    assert resposta.status_code == 400
    assert "Informe um preço válido" in resposta.get_data(as_text=True)
    assert banco.execute("SELECT COUNT(*) FROM Produto;").fetchone()[0] == 5
```

> [!note] Importar do `conftest`
> `from conftest import ...` funciona com o `pythonpath` e o `pytest.ini` da Aula 2. Se der erro, o aluno pode escrever a senha e o usuário direto no teste. Não é o foco.

### Resultado esperado

```text
tests/test_validacao.py ......
tests/test_seguranca.py ...
tests/test_integracao.py ....  (ou ......, com os opcionais)

======================== 13 passed in X.XXs ========================
```

> [!example] Prova de independência
> Rode `pytest` duas vezes seguidas, depois `pytest -p no:randomly tests/test_integracao.py`, e confira que o resultado é o mesmo. O banco temporário é recriado a cada teste.

## 3. Mapa das metodologias por funcionalidade

Há mais de uma resposta defensável. O que conta é a **justificativa**.

| Caso | Funcionalidade | Tipo mais adequado | Justificativa possível |
| --- | --- | --- | --- |
| CT01 | Validação de preço negativo | **Unitário** (automatizado) + manual | A regra mora em uma função isolada: rápido, preciso e repetível |
| CT02 | Acesso sem login | **Integração** (test client) | Envolve rota, sessão e redirecionamento juntos |
| CT03 | Login com senha errada | **Integração** (+ unitário do hash) | Rota + banco + verificação da senha |
| CT04 | Proteção CSRF | **Integração** (opcional 5) + exploratório | Depende de cookie, formulário e rota; a descoberta de como burlar é manual |
| CT05 | HTML escapado | **Manual / aceitação** (ou integração checando `&lt;b&gt;`) | É sobre o que **o usuário vê**; automatizar o texto escapado também é válido |
| CT06 | Cadastro válido | **Aceitação** (manual) + integração | Fluxo completo: formulário, banco, redirecionamento, aviso e F5 sem duplicar |

> [!info] Coluna "automatizado em"
> Esperado ao final: CT01 → `tests/test_validacao.py`; CT02 e CT03 → `tests/test_integracao.py` (CT03 só no login válido; senha errada fica como desafio); CT04 e CT06 → desafios 5 e 6, se feitos. Aceite "não automatizado" quando justificado.

%%
## 5. Rubrica da Avaliação 1 (Indicador 1)

> [!info] Indicador 1
> *Utiliza diferentes metodologias de testes, de acordo com a funcionalidade do sistema.*
> A **ação** é usar diferentes metodologias; o **contexto** é escolher conforme a funcionalidade. O contexto decide entre A e PA.

| Critério | A (atendido) | PA (parcialmente) | NA (não atendido) |
| --- | --- | --- | --- |
| **Casos manuais** | 6 casos completos, passos repetíveis, esperado verificável e escrito antes | Casos completos, mas com passos vagos ou esperado genérico em alguns | Casos incompletos ou sem repetibilidade |
| **Plano de teste** | Objetivo, escopo, ambiente, tipos e critério claros, em uma página | Faltam elementos ou o escopo não declara o que ficou de fora | Plano ausente ou sem estrutura |
| **Adequação da metodologia** | Escolhe o tipo de teste por funcionalidade **e justifica** coerentemente | Usa tipos diferentes, mas a escolha não é justificada ou é só uma lista | Usa um único tipo para tudo |
| **Suíte automatizada** | Testes unitários **e** de integração passando, com fixtures, independentes entre si | Suíte roda, mas há dependência entre testes, ou só um dos tipos | Suíte não roda ou os testes não verificam nada |
| **Comunicação** | Explica um teste de integração e responde "passar garante ausência de defeitos?" com a ideia de que **não** | Explica com apoio do docente | Não consegue explicar o que a dupla fez |

**Menção do Indicador 1**

- **A:** todos os critérios em A, ou 4 em A e 1 em PA, **sem** NA e **com** a adequação da metodologia em A.
- **PA:** avanço visível, mas a adequação da metodologia está em PA, ou há NA em um critério secundário.
- **NA:** adequação em NA, ou suíte ausente.

> [!warning] Avaliação individual numa dupla
> Pergunte a **cada aluno** algo sobre o trabalho (por exemplo, "o que a fixture `banco_temporario` faz?"). A menção é individual.

### Cronograma sugerido da aula (240 min)

| Tempo | Atividade |
| --- | --- |
| 0 a 25 min | Teste no banco real (sem fixtures) |
| 25 a 65 min | Conversa, fixtures, test client, tipos de teste |
| 65 a 160 min | Tabela de metodologias + `test_integracao.py` + commit |
| 160 a 220 min | **Avaliação 1** (≈ 8 min por dupla; com ~11 alunos, cerca de 6 duplas) |
| 220 a 240 min | Feedback e fechamento (10 min de revisão do mercado) |

> [!tip] Se faltar tempo
> Corte os desafios 5 e 6 e, se necessário, peça que a tabela de metodologias seja preenchida **durante a apresentação**. Não corte a justificativa: ela é o centro do indicador.

### Ficha de registro (por aluno)

| Aluno | Dupla | Casos manuais | Plano | Metodologia | Suíte | Comunicação | **Menção** | Observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

> [!info] Recuperação imediata
> Quem receber PA ou NA recebe feedback ao final da apresentação e, na Aula 4, reescreve o ponto frágil (por exemplo, a justificativa das metodologias) enquanto os colegas fazem a tabulação. A nota diz "recuperação imediata" no PTD: registre a data e o que foi refeito.

%%
