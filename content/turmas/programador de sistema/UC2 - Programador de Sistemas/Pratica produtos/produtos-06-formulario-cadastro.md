---
title: "Gestão de Produtos 6: formulário de cadastro de produtos"
date: 2026-11-04
draft: false
tags:
  - python/web
  - bottle
  - sqlite
  - formulario
  - seguranca
  - atividade-pratica/produtos
description: "Crie um formulário web para cadastrar produtos no SQLite com Bottle: validação no servidor, token CSRF, escape de HTML e redirecionamento após o POST."
---

Até aqui a aplicação só **lê** dados. Nesta atividade você implementa o **C do CRUD pela web**: um formulário protegido por login que cadastra novos produtos no banco, com validação no servidor e proteção contra requisições forjadas.

⬅️ [[produtos-05-autenticacao]] ⬆️ [[produtos-00-roteiro]]

> [!info] Ficha da atividade
>
> - **Ambiente:** computador local (VS Code e terminal)
> - **Tempo estimado:** 60 minutos
> - **Pré-requisito:** [[produtos-05-autenticacao|Nota 5]] funcionando (login e rota protegida)
> - **Resultado esperado:** página `/produtos/novo` que grava um produto, redireciona para a lista em `/produtos` e recusa dados inválidos com mensagens claras
> - **Fecha o ciclo:** *Create* pela web (Update e Delete ficam como desafio)

## Conceitos antes do código

### O caminho de uma requisição

| Etapa | Rota | O que acontece |
| --- | --- | --- |
| 1 | `GET /produtos/novo` | O servidor exibe o formulário e emite um token CSRF |
| 2 | `POST /produtos` | O navegador envia os dados e o token |
| 3 | (servidor) | Confere o token, valida os campos e executa o `INSERT` |
| 4 | redirecionamento | Se deu certo, envia o navegador para `GET /produtos` |
| 5 | `GET /produtos` | Exibe a lista com o aviso de sucesso |

O passo 4 é o padrão **Post/Redirect/Get**. Sem ele, apertar F5 depois do cadastro reenviaria o formulário e criaria um produto duplicado.

### Validação: navegador ajuda, servidor decide

Atributos como `required` e `min="0"` melhoram a experiência, mas qualquer pessoa pode ignorá-los (pelas ferramentas do desenvolvedor ou com `curl`). Por isso **toda regra é verificada de novo no servidor**.

### CSRF em uma frase

Um ataque *Cross-Site Request Forgery* faz o navegador de uma pessoa logada enviar uma requisição que ela não pretendia fazer. A defesa usada aqui é o **token duplo**: um valor aleatório vai em um cookie assinado e também em um campo oculto do formulário. Um site malicioso não consegue ler o campo oculto, então só o formulário legítimo envia os dois valores iguais.

## Passo 1: regras de validação (`validacao.py`)

Mantenha a validação em uma função simples, sem depender do Bottle. Assim ela pode ser testada isoladamente.

```python
import math


def validar_produto(campos: dict, ids_categoria_validos: set[int]):
    """
    Valida os campos recebidos do formulário (todos como texto).
    Devolve (dados, erros): se houver erros, 'dados' é None.
    """
    erros = {}

    nome = campos["nome"].strip()
    if not nome:
        erros["nome"] = "Informe o nome do produto."
    elif len(nome) > 100:
        erros["nome"] = "O nome deve ter no máximo 100 caracteres."

    preco = None
    try:
        preco = float(campos["preco"].strip().replace(",", "."))
        if not math.isfinite(preco) or preco < 0:
            raise ValueError
    except ValueError:
        erros["preco"] = "Informe um preço válido, igual ou maior que zero (ex.: 49,90)."

    estoque = None
    try:
        estoque = int(campos["estoque"].strip())
        if estoque < 0:
            raise ValueError
    except ValueError:
        erros["estoque"] = "Informe o estoque como um número inteiro, igual ou maior que zero."

    id_categoria = None
    try:
        id_categoria = int(campos["id_categoria"])
        if id_categoria not in ids_categoria_validos:
            raise ValueError
    except ValueError:
        erros["id_categoria"] = "Selecione uma categoria da lista."

    if erros:
        return None, erros

    return {
        "nome": nome,
        "preco": round(preco, 2),
        "estoque": estoque,
        "id_categoria": id_categoria,
    }, {}
```

> [!note] Por que `math.isfinite`?
> O Python aceita `float("nan")` e `float("inf")` como números válidos. Sem essa verificação, alguém poderia cadastrar um preço "infinito".

### Teste rápido, sem servidor

Crie um arquivo `testar_validacao.py` e execute com `python testar_validacao.py`:

```python
from validacao import validar_produto

CATEGORIAS = {1, 2, 3}

# Caso válido (vírgula decimal e espaços são aceitos)
dados, erros = validar_produto(
    {"nome": " Mouse sem fio ", "preco": "89,90", "estoque": "20", "id_categoria": "1"},
    CATEGORIAS,
)
assert erros == {}
assert dados == {"nome": "Mouse sem fio", "preco": 89.9, "estoque": 20, "id_categoria": 1}

# Preço negativo, estoque decimal e categoria inexistente
dados, erros = validar_produto(
    {"nome": "X", "preco": "-5", "estoque": "2.5", "id_categoria": "99"},
    CATEGORIAS,
)
assert dados is None
assert set(erros) == {"preco", "estoque", "id_categoria"}

# Preço infinito
_, erros = validar_produto(
    {"nome": "X", "preco": "inf", "estoque": "1", "id_categoria": "1"}, CATEGORIAS
)
assert "preco" in erros

print("Todos os testes passaram.")
```

## Passo 2: funções de banco (`dados.py`)

Acrescente ao final do arquivo `dados.py`:

```python
def listar_categorias() -> list[dict]:
    """Categorias em ordem alfabética, para preencher a lista do formulário."""
    with closing(abrir_conexao()) as conn:
        return [
            dict(linha)
            for linha in conn.execute(
                "SELECT id_categoria, nome_categoria FROM Categoria ORDER BY nome_categoria;"
            )
        ]


def listar_produtos() -> list[dict]:
    """Produtos com o nome da categoria, do mais recente para o mais antigo."""
    with closing(abrir_conexao()) as conn:
        return [
            dict(linha)
            for linha in conn.execute("""
                SELECT p.id_produto, p.nome, p.preco, p.estoque, c.nome_categoria
                FROM Produto p
                LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
                ORDER BY p.id_produto DESC;
            """)
        ]


def inserir_produto(nome: str, preco: float, estoque: int, id_categoria: int) -> int:
    """Insere um produto e devolve o id gerado."""
    with closing(abrir_conexao()) as conn:
        with conn:  # commit automático; rollback em caso de erro
            cursor = conn.execute(
                "INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);",
                (nome, preco, estoque, id_categoria),
            )
            return cursor.lastrowid
```

> [!tip] Parâmetros `?`, sempre
> Os valores digitados no formulário **nunca** são concatenados ao texto do SQL. Os marcadores `?` fazem o banco tratar tudo como dado, o que elimina o SQL Injection (visto na [[produtos-01-crud-analise|Nota 1]]).

## Passo 3: páginas HTML

### Estilo compartilhado (`static/estilo.css`)

```css
body { font-family: "Segoe UI", Arial, sans-serif; margin: 30px; background: #f8f9fa; }
h1 { color: #0d6efd; }
nav { margin-bottom: 20px; }
form { background: white; padding: 20px; border-radius: 8px; max-width: 420px;
       box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
label { display: block; margin-top: 12px; font-weight: bold; }
input, select { width: 100%; padding: 8px; margin-top: 4px; box-sizing: border-box; }
input[type="submit"], .botao { background: #0d6efd; color: white; border: none; font-weight: bold;
       cursor: pointer; border-radius: 4px; padding: 10px 16px; text-decoration: none;
       display: inline-block; width: auto; margin-top: 18px; }
.erro { color: #dc3545; font-size: 0.9em; margin: 4px 0 0; }
.ok { color: #146c43; background: #d1e7dd; padding: 10px; border-radius: 4px; }
table { width: 100%; border-collapse: collapse; background: white; margin-top: 15px; }
th, td { border: 1px solid #dee2e6; padding: 10px; text-align: left; }
th { background: #0d6efd; color: white; }
```

### Formulário (`views/produto_form.tpl`)

Os valores digitados voltam preenchidos quando há erro, e cada mensagem aparece junto do campo correspondente.

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Novo produto</title>
  <link rel="stylesheet" href="/static/estilo.css">
</head>
<body>
  <nav>
    <a href="/produtos">Produtos</a> ·
    <a href="/relatorio/ranking">Relatório</a> ·
    <a href="/logout">Sair</a>
  </nav>

  <h1>Novo produto</h1>

  <form action="/produtos" method="post">
    % if 'geral' in erros:
    <p class="erro">{{ erros['geral'] }}</p>
    % end

    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">

    <label for="nome">Nome</label>
    <input id="nome" type="text" name="nome" maxlength="100" required
           value="{{ valores.get('nome', '') }}">
    % if 'nome' in erros:
    <p class="erro">{{ erros['nome'] }}</p>
    % end

    <label for="preco">Preço (R$)</label>
    <input id="preco" type="text" name="preco" inputmode="decimal" required
           placeholder="49,90" value="{{ valores.get('preco', '') }}">
    % if 'preco' in erros:
    <p class="erro">{{ erros['preco'] }}</p>
    % end

    <label for="estoque">Estoque (unidades)</label>
    <input id="estoque" type="number" name="estoque" min="0" step="1" required
           value="{{ valores.get('estoque', '') }}">
    % if 'estoque' in erros:
    <p class="erro">{{ erros['estoque'] }}</p>
    % end

    <label for="id_categoria">Categoria</label>
    <select id="id_categoria" name="id_categoria" required>
      <option value="">Selecione...</option>
      % for c in categorias:
      %   marcada = ' selected' if str(c['id_categoria']) == valores.get('id_categoria', '') else ''
      <option value="{{ c['id_categoria'] }}"{{! marcada }}>{{ c['nome_categoria'] }}</option>
      % end
    </select>
    % if 'id_categoria' in erros:
    <p class="erro">{{ erros['id_categoria'] }}</p>
    % end

    <input type="submit" value="Cadastrar produto">
  </form>
</body>
</html>
```

> [!note] Escape automático
> Os trechos `{{ ... }}` escapam o HTML. Se alguém cadastrar um produto chamado `<script>alert(1)</script>`, o navegador exibirá o texto, sem executá-lo. A forma `{{! ... }}` desativa o escape e foi usada apenas para o texto fixo `selected`, definido por nós.

### Lista de produtos (`views/produtos.tpl`)

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Produtos</title>
  <link rel="stylesheet" href="/static/estilo.css">
</head>
<body>
  <nav>
    <a href="/produtos">Produtos</a> ·
    <a href="/relatorio/ranking">Relatório</a> ·
    <a href="/logout">Sair</a>
  </nav>

  <h1>Produtos cadastrados</h1>

  % if aviso:
  <p class="ok">{{ aviso }}</p>
  % end

  <a class="botao" href="/produtos/novo">Novo produto</a>

  <table>
    <tr>
      <th>ID</th>
      <th>Produto</th>
      <th>Categoria</th>
      <th>Preço</th>
      <th>Estoque</th>
    </tr>
    % for p in produtos:
    <tr>
      <td>{{ p['id_produto'] }}</td>
      <td>{{ p['nome'] }}</td>
      <td>{{ p['nome_categoria'] }}</td>
      <td>R$ {{ "%.2f" % p['preco'] }}</td>
      <td>{{ p['estoque'] }}</td>
    </tr>
    % end
  </table>
</body>
</html>
```

## Passo 4: rotas e token CSRF (`app.py`)

Atualize o bloco de importações do `app.py`:

```python
import functools
import hmac
import os
import secrets
import sqlite3
from pathlib import Path

from bottle import (
    TEMPLATE_PATH, Bottle, abort, redirect, request, response, run, static_file, template
)

from dados import (
    buscar_usuario, consultar_ranking, inserir_produto, listar_categorias, listar_produtos
)
from seguranca import verificar_senha
from validacao import validar_produto
```

Acrescente as funções e rotas abaixo **antes** do bloco `if __name__ == "__main__":`:

```python
CAMPOS_PRODUTO = ("nome", "preco", "estoque", "id_categoria")
AVISOS = {"cadastrado": "Produto cadastrado com sucesso."}


def emitir_token_csrf() -> str:
    """Gera um token aleatório, guarda em cookie assinado e devolve para o formulário."""
    token = secrets.token_hex(16)
    response.set_cookie(
        "csrf", token, secret=CHAVE_SECRETA,
        httponly=True, samesite="Lax", max_age=3600, path="/",
    )
    return token


def token_csrf_valido() -> bool:
    """Confere se o token do campo oculto é igual ao do cookie."""
    esperado = request.get_cookie("csrf", secret=CHAVE_SECRETA)
    recebido = request.forms.getunicode("csrf_token") or ""
    if not esperado:
        return False
    return hmac.compare_digest(esperado.encode("utf-8"), recebido.encode("utf-8"))


def pagina_formulario(valores: dict, erros: dict, categorias: list):
    return template(
        "produto_form",
        valores=valores,
        erros=erros,
        categorias=categorias,
        csrf_token=emitir_token_csrf(),
    )


@app.get("/produtos")
@requer_autenticacao
def listar():
    aviso = AVISOS.get(request.query.get("ok", ""), "")
    return template("produtos", produtos=listar_produtos(), aviso=aviso)


@app.get("/produtos/novo")
@requer_autenticacao
def exibir_formulario():
    return pagina_formulario({}, {}, listar_categorias())


@app.post("/produtos")
@requer_autenticacao
def cadastrar_produto():
    if not token_csrf_valido():
        abort(403, "Requisição inválida. Recarregue o formulário e tente novamente.")

    campos = {c: request.forms.getunicode(c) or "" for c in CAMPOS_PRODUTO}
    categorias = listar_categorias()
    ids_validos = {c["id_categoria"] for c in categorias}

    dados, erros = validar_produto(campos, ids_validos)

    if not erros:
        try:
            inserir_produto(**dados)
        except sqlite3.IntegrityError:
            erros["geral"] = "O banco de dados recusou os dados informados."

    if erros:
        response.status = 400
        return pagina_formulario(campos, erros, categorias)

    redirect("/produtos?ok=cadastrado")
```

> [!warning] Ordem dos decoradores
> Em cada rota, `@app.get(...)` ou `@app.post(...)` vem **primeiro** (acima) e `@requer_autenticacao` logo abaixo. Invertendo a ordem, a rota é registrada sem a proteção.

Inicie o servidor (com `APP_SECRET` definido, como na Nota 5) e acesse `http://localhost:8080/produtos/novo` depois de fazer login.

> [!example] Resultado esperado
> Cadastre `Mouse sem fio`, preço `89,90`, estoque `20`, categoria `Eletrônicos`. Você deve ser levado a `/produtos` com a mensagem de sucesso e o novo produto no topo da lista.
>
> O ID será **7** se você seguiu a Nota 1 sem usar o script de restauração da Nota 2: o `AUTOINCREMENT` nunca reaproveita o id 6 da Calça Jeans excluída.

## Passo 5: testar

> [!question] Teste 1: pressionar F5 após o cadastro
> Na página `/produtos` exibida depois do cadastro, aperte F5. Algum produto foi duplicado? Por quê?

> [!question] Teste 2: ignorar a validação do navegador
> Abra as ferramentas do desenvolvedor (F12), remova o atributo `required` dos campos e envie o formulário com o preço `-10` e o nome vazio. O que o servidor responde?

> [!question] Teste 3: remover o token CSRF
> Nas ferramentas do desenvolvedor, apague o campo oculto `csrf_token` (ou altere o valor dele) e envie o formulário. O que acontece?

> [!question] Teste 4: injeção de HTML
> Cadastre um produto chamado `<b>teste</b>`. Como ele aparece na lista?

> [!question] Teste 5: formulário sem login
> Em uma janela anônima, acesse `/produtos/novo`. Depois, tente enviar um `POST` direto com `curl`:
>
> ```bash
> curl -i -X POST http://localhost:8080/produtos -d "nome=X&preco=1&estoque=1&id_categoria=1"
> ```

> [!success]- Resultados esperados
>
> 1. Nenhum duplicado. Após o `POST`, o servidor redireciona, e o F5 repete apenas o `GET /produtos`, que só lê dados.
> 2. Resposta com status 400 e o formulário reexibido com as mensagens de erro e os valores preenchidos. A regra vale no servidor, não só no navegador.
> 3. Erro 403 ("Requisição inválida"). Sem o token que corresponde ao cookie, o servidor recusa o envio.
> 4. O texto `<b>teste</b>` aparece literalmente, sem negrito, porque o `{{ }}` escapa o HTML.
> 5. A janela anônima é redirecionada ao login. O `curl` também recebe um redirecionamento para `/login`, pois não há cookie de sessão.

## Desafios

> [!question] Desafio 1: nome duplicado
> Impeça o cadastro de dois produtos com o mesmo nome, ignorando diferença entre maiúsculas e minúsculas. Onde a regra deve ficar: na validação, no banco ou nos dois?

> [!tip]- Dica do desafio 1
> No banco, uma restrição `UNIQUE` em coluna com `COLLATE NOCASE` garante a regra mesmo que o código falhe. Na validação, uma consulta prévia permite mostrar uma mensagem amigável. Usar as duas camadas é o mais robusto. Lembre-se de tratar a corrida entre duas requisições simultâneas capturando o `IntegrityError`.

> [!question] Desafio 2: editar produto (Update)
> Crie `GET /produtos/<id:int>/editar` e `POST /produtos/<id:int>`, reaproveitando `validar_produto` e o mesmo template do formulário. Como o template deve saber se está criando ou editando?

> [!question] Desafio 3: excluir produto (Delete)
> Acrescente um botão de exclusão em cada linha da lista, usando **POST** (nunca um link `GET`) e token CSRF. Trate o caso de um produto que já tem vendas, lembrando do experimento da [[produtos-02-vendas-estoque|Nota 2]]. Que mensagem o usuário deve receber?

> [!tip]- Dica do desafio 3
> O `DELETE` de um produto com vendas gera `sqlite3.IntegrityError: FOREIGN KEY constraint failed`. Capture o erro e explique: "Este produto tem vendas registradas e não pode ser excluído". Uma alternativa de projeto é uma coluna `ativo` para desativar o produto sem apagar o histórico.

> [!question] Desafio 4: reaproveitar o layout
> Os arquivos `login.tpl` e `ranking.tpl` ainda repetem o `<head>` e o CSS. Crie `views/base.tpl` e use `% rebase('base', titulo='...')` para eliminar a repetição.

> [!question] Desafio 5: busca e filtro
> Na lista, acrescente um campo de busca por nome e um filtro por categoria, usando `GET` com parâmetros `?` na consulta.

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| Sempre aparece o erro 403 ao enviar | Cookie `csrf` ausente ou outro `APP_SECRET` | Recarregue a página do formulário e confira o `APP_SECRET` |
| O envio falha só na primeira aba aberta | Duas abas do formulário: a segunda substituiu o cookie | Use uma aba por vez ou recarregue a primeira |
| `NameError: CHAVE_SECRETA is not defined` | Funções novas colocadas antes das constantes do `app.py` | Posicione-as depois das constantes e do `app = Bottle()` |
| `Template 'produto_form' not found` | Nome ou pasta do arquivo incorretos | Confirme `views/produto_form.tpl` |
| A página fica sem estilo | `estilo.css` fora de `static/` | Coloque o arquivo em `static/estilo.css` |
| O select não mantém a categoria após um erro | Comparação entre número e texto | Compare com `str(c['id_categoria'])`, como no template |
| `/produtos/novo` abre sem pedir login | Decoradores na ordem errada | Deixe `@app.get(...)` acima de `@requer_autenticacao` |

## Checklist de verificação

- [ ] `/produtos/novo` exige login
- [ ] Um cadastro válido grava o produto e redireciona para `/produtos` com o aviso de sucesso
- [ ] F5 após o cadastro não duplica o produto
- [ ] Dados inválidos retornam status 400, com mensagens por campo e valores preservados
- [ ] Envio sem token CSRF válido é recusado com 403
- [ ] Nomes com HTML aparecem como texto puro na lista
- [ ] O script `testar_validacao.py` passa sem erros
- [ ] Pelo menos um dos desafios foi resolvido

## Fechamento

Com este formulário, a aplicação passou a **escrever** dados pela web de forma segura: validação no servidor, token CSRF, consultas parametrizadas e escape de HTML. O próximo passo natural é completar o CRUD com edição e exclusão (desafios 2 e 3). Volte ao [[produtos-00-roteiro|roteiro]] para revisar os critérios de avaliação.
