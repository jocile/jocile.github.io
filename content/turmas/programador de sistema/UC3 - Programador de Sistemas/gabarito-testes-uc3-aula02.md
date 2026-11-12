---
title: Gabarito - Testes automatizados da Aula 2 da UC3 (uso do docente)
description: Gabarito de testar_validacao.py, tests/test_validacao.py e tests/test_seguranca.py da uc3.02, com versão parametrizada e notas de correção.
date: 2026-11-12
draft: false
tags:
  - programador-sistemas/gabarito
  - uc3
---

%%
> [!warning] Uso exclusivo do docente
> Não publicar no Quartz. Este gabarito supõe o repositório-base **sem defeitos** (a v0.9 só entra na Aula 4). Por isso todos os testes devem **passar**. Se algum falhar, ou o aluno escreveu o esperado errado, ou o repositório-base difere do que está nas notas `produtos-05` e `produtos-06`.

%%

> [!info] Contrato assumido
>
> - `validacao.py`: `validar_produto(campos, ids_categoria_validos)` recebe os campos **como texto** e devolve `(dados, erros)`. Em caso de erro, `dados` é `None` e `erros` é um dicionário com as chaves `nome`, `preco`, `estoque` ou `id_categoria`.
> - `seguranca.py`: `gerar_hash_senha(senha)` devolve `(hash_hex, salt_hex)` e `verificar_senha(senha, hash_salvo, salt_salvo)` devolve `True` ou `False`.
>
> Se o repositório do Flask mudar nomes, chaves ou ordem de argumentos, ajuste **tudo abaixo e a nota `uc3.02`**.

---

## 0. Arquivos de apoio

### `pytest.ini` (raiz do projeto)

```ini
[pytest]
pythonpath = .
testpaths = tests
```

Sem `pythonpath = .`, o pytest não enxerga `validacao.py` e `seguranca.py` e gera `ModuleNotFoundError`. O ideal é já entregar esse arquivo no repositório-base.

### Estrutura esperada ao final da aula

```text
projeto/
├── app.py
├── dados.py
├── validacao.py
├── seguranca.py
├── pytest.ini
├── testar_validacao.py      # script de partida (item 1)
├── docs/
│   └── plano-de-teste.md
└── tests/
    ├── test_validacao.py
    └── test_seguranca.py
```

---

## 1. Item 1: script sem pytest (`testar_validacao.py`)

```python
from validacao import validar_produto

CATEGORIAS = {1, 2, 3}

# Caso válido
dados, erros = validar_produto(
    {"nome": "Mouse sem fio", "preco": "89,90", "estoque": "20", "id_categoria": "1"},
    CATEGORIAS,
)
assert erros == {}
assert dados == {"nome": "Mouse sem fio", "preco": 89.9, "estoque": 20, "id_categoria": 1}

# Preço negativo
dados, erros = validar_produto(
    {"nome": "Mouse", "preco": "-5", "estoque": "2", "id_categoria": "1"},
    CATEGORIAS,
)
assert dados is None
assert "preco" in erros

# Nome vazio
dados, erros = validar_produto(
    {"nome": "", "preco": "10", "estoque": "2", "id_categoria": "1"},
    CATEGORIAS,
)
assert dados is None
assert "nome" in erros

print("Todas as verificações passaram.")
```

> [!tip] Resposta para a pergunta da aula
> **"Se o segundo `assert` falhar, o que acontece com os demais?"** O script é interrompido naquele ponto. Os `assert` seguintes **nem chegam a executar**, e a única informação é a linha do erro. O pytest resolve isso: cada função `test_*` roda de forma independente, e o relatório mostra todas as falhas de uma vez.
>
> **"Como saber qual verificação falhou e por quê?"** No script, só pela linha do `AssertionError`, sem mostrar os valores. No pytest, a saída mostra o valor esperado e o obtido.

---

## 2. Item 3: `tests/test_validacao.py` (versão simples, 6 testes obrigatórios)

```python
from validacao import validar_produto

CATEGORIAS = {1, 2, 3}


def campos_validos(**alteracoes):
    """Devolve campos válidos, trocando só os que o teste quer alterar."""
    campos = {
        "nome": "Mouse sem fio",
        "preco": "89,90",
        "estoque": "20",
        "id_categoria": "1",
    }
    campos.update(alteracoes)
    return campos


def test_produto_valido_e_aceito():
    # Preparar
    campos = {
        "nome": " Mouse sem fio ",   # espaços nas pontas devem sumir
        "preco": "89,90",            # vírgula decimal deve ser aceita
        "estoque": "20",
        "id_categoria": "1",
    }

    # Executar
    dados, erros = validar_produto(campos, CATEGORIAS)

    # Verificar
    assert erros == {}
    assert dados == {
        "nome": "Mouse sem fio",
        "preco": 89.9,
        "estoque": 20,
        "id_categoria": 1,
    }


def test_preco_negativo_e_recusado():
    dados, erros = validar_produto(campos_validos(preco="-5"), CATEGORIAS)

    assert dados is None
    assert "preco" in erros


def test_preco_infinito_e_recusado():
    dados, erros = validar_produto(campos_validos(preco="inf"), CATEGORIAS)

    assert dados is None
    assert "preco" in erros


def test_estoque_decimal_e_recusado():
    dados, erros = validar_produto(campos_validos(estoque="2.5"), CATEGORIAS)

    assert dados is None
    assert "estoque" in erros


def test_categoria_inexistente_e_recusada():
    dados, erros = validar_produto(campos_validos(id_categoria="99"), CATEGORIAS)

    assert dados is None
    assert "id_categoria" in erros


def test_nome_vazio_e_recusado():
    dados, erros = validar_produto(campos_validos(nome=""), CATEGORIAS)

    assert dados is None
    assert "nome" in erros
```

> [!note] A função `campos_validos`
> Ela evita repetir os 4 campos em todo teste e deixa **visível o que cada teste altera**. Alunos iniciantes podem escrever o dicionário completo em cada teste: é mais repetitivo, mas correto. Aceite os dois e mostre o auxiliar como melhoria.

### Desafios opcionais (fronteiras)

```python
def test_preco_zero_e_aceito():
    dados, erros = validar_produto(campos_validos(preco="0"), CATEGORIAS)

    assert erros == {}
    assert dados["preco"] == 0.0


def test_preco_logo_abaixo_de_zero_e_recusado():
    dados, erros = validar_produto(campos_validos(preco="-0,01"), CATEGORIAS)

    assert dados is None
    assert "preco" in erros


def test_preco_com_virgula_vira_numero():
    dados, erros = validar_produto(campos_validos(preco="49,90"), CATEGORIAS)

    assert erros == {}
    assert dados["preco"] == 49.9


def test_nome_com_100_caracteres_e_aceito():
    dados, erros = validar_produto(campos_validos(nome="x" * 100), CATEGORIAS)

    assert erros == {}


def test_nome_com_101_caracteres_e_recusado():
    dados, erros = validar_produto(campos_validos(nome="x" * 101), CATEGORIAS)

    assert dados is None
    assert "nome" in erros


def test_varios_erros_sao_reportados_juntos():
    campos = campos_validos(preco="-5", estoque="2.5", id_categoria="99")

    dados, erros = validar_produto(campos, CATEGORIAS)

    assert dados is None
    assert set(erros) == {"preco", "estoque", "id_categoria"}
```

> [!bug] Armadilha do `-0`
> `validar_produto` aceita o preço `"-0"`, pois `-0.0 < 0` é falso em Python. O dado sai como `-0.0`, que é igual a `0.0`. Não é problema prático, mas é uma boa **pergunta para a turma**: "o que acontece com `-0`?". Não coloque como caso obrigatório.

---

## 3. Versão parametrizada (para quem terminar antes)

`@pytest.mark.parametrize` roda o **mesmo teste** com várias entradas, e cada uma aparece separada no relatório.

```python
import pytest

from validacao import validar_produto

CATEGORIAS = {1, 2, 3}


def campos_validos(**alteracoes):
    campos = {
        "nome": "Mouse sem fio",
        "preco": "89,90",
        "estoque": "20",
        "id_categoria": "1",
    }
    campos.update(alteracoes)
    return campos


@pytest.mark.parametrize(
    "campo, valor",
    [
        ("preco", "-5"),
        ("preco", "-0,01"),
        ("preco", "inf"),
        ("preco", "nan"),
        ("preco", "abc"),
        ("preco", ""),
        ("estoque", "-1"),
        ("estoque", "2.5"),
        ("estoque", "abc"),
        ("estoque", ""),
        ("id_categoria", "99"),
        ("id_categoria", ""),
        ("nome", ""),
        ("nome", "   "),
        ("nome", "x" * 101),
    ],
)
def test_entradas_invalidas_sao_recusadas(campo, valor):
    dados, erros = validar_produto(campos_validos(**{campo: valor}), CATEGORIAS)

    assert dados is None
    assert campo in erros


@pytest.mark.parametrize(
    "preco, esperado",
    [
        ("0", 0.0),
        ("0,01", 0.01),
        ("49,90", 49.9),
        ("49.90", 49.9),
        ("1500", 1500.0),
    ],
)
def test_precos_validos_sao_convertidos(preco, esperado):
    dados, erros = validar_produto(campos_validos(preco=preco), CATEGORIAS)

    assert erros == {}
    assert dados["preco"] == esperado
```

> [!info] Procedimento
>
> - Rode `pytest -v`: os 15 casos inválidos aparecem separados, e se um falhar o relatório diz **qual combinação** (por exemplo, `preco-nan`).
> - Compare com escrever 15 funções iguais. Pergunte: **o que ganhamos? E o que perdemos em clareza?**
> - Não cobre a precisão de `float`: se algum aluno testar `"0,1"` somado a outro valor, vale falar de `pytest.approx`.

---

## 4. Item 3: `tests/test_seguranca.py` (3 testes obrigatórios)

```python
from seguranca import gerar_hash_senha, verificar_senha

SENHA = "SenhaForte123"


def test_mesma_senha_gera_hashes_diferentes():
    # Preparar e Executar
    hash_1, salt_1 = gerar_hash_senha(SENHA)
    hash_2, salt_2 = gerar_hash_senha(SENHA)

    # Verificar
    assert salt_1 != salt_2
    assert hash_1 != hash_2


def test_senha_correta_e_aceita():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)

    assert verificar_senha(SENHA, hash_salvo, salt_salvo) is True


def test_senha_errada_e_recusada():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)

    assert verificar_senha("OutraSenha456", hash_salvo, salt_salvo) is False
```

### Desafios opcionais

```python
def test_hash_nao_contem_a_senha():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)

    assert SENHA not in hash_salvo
    assert SENHA not in salt_salvo


def test_tamanho_do_hash_e_do_salt():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)

    assert len(hash_salvo) == 64   # SHA-256: 32 bytes em hexadecimal
    assert len(salt_salvo) == 32   # salt de 16 bytes em hexadecimal


def test_senha_com_letras_maiusculas_diferentes_e_recusada():
    hash_salvo, salt_salvo = gerar_hash_senha(SENHA)

    assert verificar_senha(SENHA.lower(), hash_salvo, salt_salvo) is False


def test_senha_com_acentos_funciona():
    hash_salvo, salt_salvo = gerar_hash_senha("açaí-é-bom")

    assert verificar_senha("açaí-é-bom", hash_salvo, salt_salvo) is True
```

> [!note] Por que esse arquivo é lento
> São **600.000 iterações por hash**. Cada chamada leva cerca de uma fração de segundo, e este arquivo faz em torno de 2 chamadas por teste. Com os 3 testes obrigatórios, conte com **poucos segundos**. Com os opcionais, mais alguns. Aproveite para perguntar: "por que o desenvolvedor quer que o hash seja lento, mas o testador gostaria que fosse rápido?"

> [!tip] Resposta esperada sobre "o teste prova que a senha é segura?"
> Não. Ele verifica **propriedades** (salt diferente, aceita e recusa corretamente). Não prova resistência a ataques. É um bom exemplo de que **teste passando não significa ausência de defeito**.

---

## 5. Resultado esperado do `pytest`

Com os 6 + 3 testes obrigatórios:

```text
tests/test_validacao.py ......                                [ 66%]
tests/test_seguranca.py ...                                   [100%]

========================= 9 passed in X.XXs =========================
```

O tempo varia com a máquina (em geral alguns segundos, por causa do hash). Com `pytest -v`, cada teste aparece com `PASSED`.

---

## 6. Demonstração: o teste pega um defeito de verdade

Esta demonstração prepara a SA2 (Aulas 4 a 6). Faça **no seu computador**, não nos dos alunos.

1. Em `validacao.py`, deixe o preço aceitar valores negativos, mudando `preco < 0` para `False` (ou comentando a condição).
2. Rode `pytest`.
3. Mostre a saída: `test_preco_negativo_e_recusado` falha, com `assert dados is None` indicando que `dados` não era `None`.
4. Desfaça a alteração e rode de novo: tudo volta a passar.

> [!question] Perguntas para a turma
>
> - O **defeito** está onde? (a linha alterada em `validacao.py`)
> - Qual é a **falha** observada? (um produto com preço negativo sendo aceito)
> - O **erro** foi de quem? (quem programou ou alterou a condição)
>
> Fecha o vocabulário da Aula 1 e antecipa a Aula 4.

---

## 7. Erros frequentes

| Erro | Como aparece | Como orientar |
| --- | --- | --- |
| Arquivo sem o prefixo `test_` | `no tests ran` | O pytest só procura `test_*.py` |
| Função sem o prefixo `test_` | Teste não é executado, e ninguém percebe | Use `pytest -v` para listar o que rodou |
| `ModuleNotFoundError` | O teste não acha `validacao` | Falta o `pytest.ini` com `pythonpath = .` |
| `assert dados == None` | Funciona, mas é fora do padrão | Mostre `is None` |
| `assert erros` esperando vazio | Teste passa quando **há** erro | `assert erros == {}` ou `assert not erros` |
| Vários motivos num teste | Teste longo que quebra por razões diferentes | Um comportamento por teste |
| Nome genérico (`test1`, `teste_a`) | Relatório não diz o que quebrou | Nome que descreve o comportamento esperado |
| `assert (cond, "msg")` com parênteses | O teste **sempre passa** (tupla é verdadeira) e o Python avisa | Mostre `assert cond, "mensagem"` |
| Valor de entrada como número | `"preco": 89.9` e a função faz `.strip()` | Os campos do formulário são **texto** |
| Testar duas coisas com o mesmo `assert` | `assert "preco" in erros or "estoque" in erros` | Separe |
| Teste que sempre passa | `assert True` ou verificação trivial | Faça o aluno **quebrar** a função e ver se o teste falha |

%%
> [!tip] Um bom teste para ensinar
> Peça que cada dupla **sabote a função de propósito** (como na seção 6) e confira se seus testes detectam. Se nada falhar, o teste não protege nada.

%%

---

## 8. Lista de verificação para correção

| Critério | Observação |
| --- | --- |
| Os 6 testes de validação existem e passam | Mínimo da aula |
| Os 3 testes de segurança existem e passam | Mínimo da aula |
| Nomes descrevem o comportamento esperado | Evita `test1` |
| Padrão Preparar, Executar e Verificar visível | Mesmo sem os comentários |
| Pelo menos um valor de fronteira testado | Preço `0` ou `-0,01` |
| Um comportamento por teste | Sem vários motivos de falha |
| Commit com mensagem clara | `git log --oneline` |
| Banco, `.venv` e segredo fora do commit | Prepara a Aula 7 |

%%

> [!info] Pontos de observação para o feedback
>
> - A dupla alternou piloto e navegador de fato?
> - O navegador explicou ou só ditou?
> - Algum aluno consegue **explicar a saída vermelha** sem ajuda?
> - Alguém experimentou quebrar um teste de propósito?

> [!tip] Sugestão de feedback
> "Seus nomes de teste dizem o que está sendo verificado, e isso ajuda quem lê o relatório. Para o próximo passo, experimentem o valor `0` no preço: é o ponto exato em que a regra muda."

%%
