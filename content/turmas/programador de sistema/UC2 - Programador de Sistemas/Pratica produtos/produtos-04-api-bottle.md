---
title: "Gestão de Produtos 4: API e relatório web com Bottle"
date: 2026-10-27
draft: false
tags:
  - python/web
  - bottle
  - sqlite
  - api-rest
description: "Publique o ranking de vendas em uma API JSON e em uma página HTML com o micro-framework Bottle, rodando localmente com VS Code e terminal."
---

Agora os dados saem do banco e chegam ao navegador. Você vai criar uma aplicação com o micro-framework **Bottle** que oferece duas formas de consultar o ranking de vendas: uma **API JSON** (para outros sistemas) e uma **página HTML** com tabela e gráfico (para pessoas).

> [!info] Ficha da atividade
>
> - **Ambiente:** computador local (VS Code e terminal). **Não funciona no Colab.**
> - **Tempo estimado:** 50 minutos
> - **Pré-requisitos:** [[produtos-03-visualizacao|Nota 3]] concluída; Python 3.10 ou superior instalado
> - **Resultado esperado:** `http://localhost:8080/api/ranking-vendas` devolvendo JSON e `http://localhost:8080/relatorio/ranking` exibindo a tabela e o gráfico
> - **Próxima nota:** [[produtos-05-autenticacao|Autenticação]]

## Preparar o projeto

### Estrutura de pastas

```text
projeto-bottle/
├── app.py                  # rotas da aplicação
├── dados.py                # acesso ao banco de dados
├── gestao_produtos.db      # baixado do Colab (Nota 3)
├── static/
│   └── ranking_vendas.png  # baixado do Colab (Nota 3)
└── views/
    └── ranking.tpl         # página HTML
```

Separar o acesso a dados (`dados.py`) das rotas (`app.py`) mantém cada arquivo com uma responsabilidade e facilita as próximas notas.

### Ambiente virtual e dependências

No terminal, dentro da pasta onde deseja criar o projeto:

```bash
mkdir projeto-bottle && cd projeto-bottle
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install "bottle>=0.13"
mkdir static views
```

Depois, copie `gestao_produtos.db` para a raiz do projeto e `ranking_vendas.png` para a pasta `static/`.

> [!note] E o Pandas?
> O Pandas foi essencial para a análise, mas esta camada web não precisa dele: o módulo `sqlite3` entrega as linhas prontas para virar JSON. Menos dependências significam instalação mais simples e aplicação mais leve.

## Passo 1: acesso aos dados (`dados.py`)

```python
import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "gestao_produtos.db"

QUERY_RANKING = """
SELECT
    p.nome AS produto,
    c.nome_categoria AS categoria,
    p.preco AS preco_unitario,
    COALESCE(SUM(v.quantidade), 0) AS total_vendido,
    COALESCE(SUM(v.quantidade * p.preco), 0.0) AS faturamento_total,
    p.estoque AS estoque_restante
FROM Produto p
LEFT JOIN Vendas v ON p.id_produto = v.id_produto
LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, p.preco, p.estoque, c.nome_categoria
ORDER BY total_vendido DESC;
"""


def abrir_conexao() -> sqlite3.Connection:
    """Abre o banco com chaves estrangeiras ativas e linhas acessíveis por nome."""
    if not DB_PATH.exists():
        # Sem esta checagem, o SQLite criaria um banco vazio em silêncio
        raise FileNotFoundError(f"Banco de dados não encontrado: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn


def consultar_ranking() -> list[dict]:
    """Devolve o ranking de vendas como lista de dicionários."""
    with closing(abrir_conexao()) as conn:
        return [dict(linha) for linha in conn.execute(QUERY_RANKING)]
```

> [!tip] Caminho baseado no arquivo
> `Path(__file__).resolve().parent` faz o banco ser localizado sempre ao lado do código, independentemente da pasta em que o terminal esteja aberto.

## Passo 2: rotas da aplicação (`app.py`)

```python
from pathlib import Path

from bottle import TEMPLATE_PATH, Bottle, run, static_file, template

from dados import consultar_ranking

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH.insert(0, str(BASE_DIR / "views"))

app = Bottle()


@app.get("/api/ranking-vendas")
def api_ranking_vendas():
    """Retorna o ranking em JSON. O Bottle converte dicionários em JSON sozinho."""
    return {"status": "sucesso", "dados": consultar_ranking()}


@app.get("/relatorio/ranking")
def pagina_ranking():
    """Renderiza a página HTML com a tabela e o gráfico."""
    return template("ranking", linhas=consultar_ranking())


@app.get("/static/<caminho:path>")
def arquivos_estaticos(caminho):
    """Entrega imagens e outros arquivos da pasta static/."""
    return static_file(caminho, root=str(BASE_DIR / "static"))


if __name__ == "__main__":
    print("Servidor rodando em http://localhost:8080")
    run(app, host="localhost", port=8080, debug=True, reloader=True)
```

> [!warning] Modo de desenvolvimento
> `debug=True` e `reloader=True` são práticos enquanto você programa (mensagens de erro detalhadas e reinício automático), mas **não devem ser usados em produção**.

## Passo 3: a página HTML (`views/ranking.tpl`)

Os trechos `{{ ... }}` inserem valores e **escapam o HTML automaticamente**, o que protege contra injeção de código. Linhas iniciadas por `%` são código Python.

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Ranking de vendas</title>
  <style>
    body { font-family: "Segoe UI", Arial, sans-serif; margin: 30px; background: #f8f9fa; }
    h1 { color: #0d6efd; }
    .card-grafico { text-align: center; margin-bottom: 25px; background: white;
                    padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    .card-grafico img { max-width: 100%; border-radius: 4px; }
    table { width: 100%; border-collapse: collapse; background: white; }
    th, td { border: 1px solid #dee2e6; padding: 12px; text-align: left; }
    th { background: #0d6efd; color: white; }
    tr:nth-child(even) { background: #f1f3f5; }
  </style>
</head>
<body>
  <h1>Painel e ranking de vendas</h1>

  <div class="card-grafico">
    <img src="/static/ranking_vendas.png" alt="Gráfico de barras com a quantidade vendida por produto">
  </div>

  <h2>Desempenho por produto</h2>
  <table>
    <tr>
      <th>Produto</th>
      <th>Categoria</th>
      <th>Qtd. vendida</th>
      <th>Faturamento</th>
      <th>Estoque</th>
    </tr>
    % for linha in linhas:
    <tr>
      <td><strong>{{ linha['produto'] }}</strong></td>
      <td>{{ linha['categoria'] }}</td>
      <td>{{ linha['total_vendido'] }} unid.</td>
      <td>R$ {{ "%.2f" % linha['faturamento_total'] }}</td>
      <td>{{ linha['estoque_restante'] }}</td>
    </tr>
    % end
  </table>
</body>
</html>
```

## Passo 4: executar e testar

```bash
python app.py
```

Teste as duas rotas:

- Página: `http://localhost:8080/relatorio/ranking`
- API: `http://localhost:8080/api/ranking-vendas`

Também é possível testar a API pelo terminal:

```bash
curl http://localhost:8080/api/ranking-vendas
```

> [!example] Resultado esperado da API
> O primeiro item da lista `dados` deve ser a Camisa Polo:
>
> ```json
> {
>   "status": "sucesso",
>   "dados": [
>     {
>       "produto": "Camisa Polo",
>       "categoria": "Vestuário",
>       "preco_unitario": 80.0,
>       "total_vendido": 10,
>       "faturamento_total": 800.0,
>       "estoque_restante": 15
>     }
>   ]
> }
> ```
>
> No `curl`, os acentos podem aparecer como `\u00e1`. O JSON está correto, e o navegador os exibe normalmente.

## Como as peças se encaixam

| Peça | Função |
| --- | --- |
| `@app.get("/api/...")` | Associa uma URL e o método `GET` a uma função |
| Retornar um `dict` | O Bottle serializa em JSON e define `Content-Type: application/json` |
| `template("ranking", linhas=...)` | Renderiza `views/ranking.tpl` com os dados informados |
| `static_file(...)` | Entrega arquivos da pasta `static/` ao navegador, como o PNG |

## Desafios

> [!question] Desafio 1: consultar um produto
> Crie a rota `GET /api/produtos/<id_produto>` que devolve os dados de um único produto. Se o `id` não existir, responda com **status 404** e uma mensagem em JSON.

> [!success]- Solução do desafio 1
> Acrescente em `app.py` (importando `closing`, `sqlite3`, `response` e `abrir_conexao`):
>
> ```python
> from contextlib import closing
>
> from bottle import response
>
> from dados import abrir_conexao, consultar_ranking
>
>
> @app.get("/api/produtos/<id_produto:int>")
> def api_produto(id_produto):
>     with closing(abrir_conexao()) as conn:
>         linha = conn.execute(
>             "SELECT id_produto, nome, preco, estoque FROM Produto WHERE id_produto = ?;",
>             (id_produto,),
>         ).fetchone()
>
>     if linha is None:
>         response.status = 404
>         return {"status": "erro", "mensagem": "Produto não encontrado."}
>     return {"status": "sucesso", "dados": dict(linha)}
> ```
>
> O filtro `:int` na rota já recusa valores que não sejam números.

> [!question] Desafio 2: filtrar por categoria
> Faça `/api/ranking-vendas?categoria=Móveis` devolver apenas os produtos dessa categoria. Use `request.query.getunicode("categoria")` e **parâmetros `?`**, nunca concatenação de texto na consulta.

> [!question] Desafio 3: registrar vendas pela web
> Crie uma rota `POST /api/vendas` que receba `id_produto` e `quantidade` e reaproveite a função `registrar_venda` da [[produtos-02-vendas-estoque|Nota 2]]. Devolva status 400 quando a venda for recusada pelo banco.

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'bottle'` | Ambiente virtual não ativado | Ative o `.venv` e rode `pip install "bottle>=0.13"` |
| `FileNotFoundError: Banco de dados não encontrado` | `.db` fora da pasta do projeto | Copie `gestao_produtos.db` para a raiz do projeto |
| Imagem quebrada na página | PNG ausente ou fora de `static/` | Coloque `ranking_vendas.png` em `static/` |
| `OSError: Address already in use` | Outro programa usa a porta 8080 | Encerre o outro programa ou troque a porta em `run(...)` |
| `Template 'ranking' not found` | Arquivo fora de `views/` ou com outro nome | Confirme `views/ranking.tpl` |
| Acentos estranhos na página | Falta `<meta charset="UTF-8">` | Mantenha a linha no `<head>` |

## Checklist de verificação

- [ ] O servidor inicia sem erros e imprime o endereço
- [ ] `/api/ranking-vendas` devolve JSON com 5 produtos, começando pela Camisa Polo
- [ ] `/relatorio/ranking` mostra o gráfico e a tabela com acentos corretos
- [ ] O banco é localizado mesmo quando o terminal está em outra pasta
- [ ] Pelo menos um dos desafios foi resolvido

## Próximo passo

A página de relatório está aberta a qualquer pessoa. Em [[produtos-05-autenticacao|Autenticação]], você vai restringir o acesso por usuário e senha.
