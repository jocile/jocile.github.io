---
title: "Gestão de Produtos 5: autenticação com hash de senha e sessão"
date: 2026-10-27
draft: false
tags:
  - python/web
  - bottle
  - seguranca
  - autenticacao
description: "Proteja o relatório do Bottle com login: senhas armazenadas como hash PBKDF2 com salt, cookie de sessão assinado e segredo lido do ambiente."
---

O relatório de vendas é uma informação corporativa e não deve estar aberto a qualquer pessoa. Nesta atividade você adiciona **login e sessão** à aplicação da nota anterior, guardando as senhas da forma correta.

> [!info] Ficha da atividade
>
> - **Ambiente:** computador local (VS Code e terminal)
> - **Tempo estimado:** 60 minutos
> - **Pré-requisito:** [[produtos-04-api-bottle|Nota 4]] funcionando
> - **Resultado esperado:** `/relatorio/ranking` acessível somente após o login, com senhas armazenadas como hash no SQLite
> - **Fecha o ciclo:** dados, análise, gráfico, web e proteção

## Conceitos antes do código

### Hash, criptografia e assinatura não são a mesma coisa

Os termos costumam ser confundidos, e a diferença é central em segurança.

| Técnica | Dá para reverter? | Usa chave? | Onde aparece nesta atividade |
| --- | --- | --- | --- |
| **Hash com salt** (PBKDF2) | Não | Não | Armazenar a senha |
| **Criptografia** | Sim, com a chave | Sim | Não é usada |
| **Assinatura** (HMAC) | Não se aplica: detecta alteração | Sim, um segredo | Cookie de sessão |

> [!important] Senhas não são criptografadas
> Uma senha **nunca** deve poder ser recuperada, nem por quem administra o sistema. Por isso ela é transformada em *hash*, que só permite **conferir** se a senha digitada gera o mesmo resultado. Dizer "senha criptografada" está tecnicamente errado.

### Por que o salt?

O **salt** é um valor aleatório e único para cada usuário, misturado à senha antes do cálculo. Assim, duas pessoas com a mesma senha têm hashes diferentes, e tabelas pré-calculadas de hashes (*rainbow tables*) perdem a utilidade.

### Por que o PBKDF2 é lento de propósito?

O algoritmo repete o cálculo centenas de milhares de vezes. Para o usuário, o login leva uma fração de segundo. Para quem tenta adivinhar milhões de senhas, o custo se multiplica. Usamos **600.000 iterações** com SHA-256, valor alinhado às recomendações atuais da OWASP. O ideal é rever esse número de tempos em tempos.

### Cookie assinado não é cookie secreto

Com `secret=...`, o Bottle **assina** o valor do cookie. Isso impede que o usuário o altere sem ser detectado, mas **o conteúdo continua legível**. Nunca guarde dados sensíveis nele.

> [!warning] O segredo precisa ser protegido
> O Bottle serializa o valor do cookie assinado com `pickle`. Quem descobrir a chave secreta consegue forjar cookies e, em alguns cenários, executar código no servidor. Por isso o segredo **nunca** fica escrito no código nem vai para o repositório: ele vem de uma variável de ambiente.

## Passo 1: módulo de segurança (`seguranca.py`)

```python
import hashlib
import hmac
import os

ITERACOES = 600_000


def gerar_hash_senha(senha: str) -> tuple[str, str]:
    """Gera um salt aleatório e devolve (hash_hex, salt_hex)."""
    salt = os.urandom(16)
    hash_bytes = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, ITERACOES)
    return hash_bytes.hex(), salt.hex()


def verificar_senha(senha: str, hash_salvo: str, salt_salvo: str) -> bool:
    """Recalcula o hash com o salt salvo e compara com o hash armazenado."""
    hash_calculado = hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"), bytes.fromhex(salt_salvo), ITERACOES
    )
    # compare_digest compara em tempo constante e evita ataques de temporização
    return hmac.compare_digest(hash_calculado.hex(), hash_salvo)
```

> [!bug] Atenção ao módulo
> A função `compare_digest` pertence aos módulos `hmac` e `secrets`. O módulo `hashlib` **não** a possui, e usá-lo causa `AttributeError`.

## Passo 2: tabela de usuários e script de cadastro (`criar_usuario.py`)

Em vez de deixar um usuário `admin` com senha fixa no código, o cadastro é feito por um script que pede a senha no terminal sem exibi-la.

```python
import getpass
import sqlite3
from contextlib import closing
from pathlib import Path

from seguranca import gerar_hash_senha

DB_PATH = Path(__file__).with_name("gestao_produtos.db")


def main():
    login = input("Novo usuário: ").strip()
    senha = getpass.getpass("Senha (mínimo 8 caracteres): ")
    confirmacao = getpass.getpass("Repita a senha: ")

    if not login:
        raise SystemExit("O nome de usuário não pode ficar vazio.")
    if len(senha) < 8:
        raise SystemExit("A senha deve ter pelo menos 8 caracteres.")
    if senha != confirmacao:
        raise SystemExit("As senhas não conferem.")

    senha_hash, salt = gerar_hash_senha(senha)

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:  # commit automático; rollback em caso de erro
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL UNIQUE,
                    senha_hash TEXT NOT NULL,
                    salt TEXT NOT NULL
                );
            """)
            try:
                conn.execute(
                    "INSERT INTO Usuario (login, senha_hash, salt) VALUES (?, ?, ?);",
                    (login, senha_hash, salt),
                )
            except sqlite3.IntegrityError:
                raise SystemExit(f"O usuário '{login}' já existe.")

    print(f"Usuário '{login}' criado com sucesso.")


if __name__ == "__main__":
    main()
```

Execute e cadastre seu usuário:

```bash
python criar_usuario.py
```

Depois, confira o que ficou gravado:

```bash
sqlite3 gestao_produtos.db "SELECT login, senha_hash, salt FROM Usuario;"
```

> [!note] O que observar
> A coluna `senha_hash` é uma sequência hexadecimal sem relação visível com a senha. Se o arquivo do banco vazar, a senha original não está lá.

## Passo 3: buscar o usuário (`dados.py`)

Acrescente esta função ao final do arquivo `dados.py` criado na Nota 4:

```python
def buscar_usuario(login: str):
    """Devolve a linha do usuário (ou None se não existir)."""
    with closing(abrir_conexao()) as conn:
        return conn.execute(
            "SELECT login, senha_hash, salt FROM Usuario WHERE login = ?;",
            (login,),
        ).fetchone()
```

## Passo 4: tela de login (`views/login.tpl`)

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <style>
    body { font-family: Arial, sans-serif; display: flex; justify-content: center;
           align-items: center; height: 100vh; margin: 0; background: #f8f9fa; }
    .card { background: white; padding: 30px; border-radius: 8px; width: 300px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    label { display: block; margin-top: 10px; }
    input { width: 100%; padding: 8px; margin-top: 4px; box-sizing: border-box; }
    input[type="submit"] { margin-top: 18px; background: #0d6efd; color: white;
                           border: none; font-weight: bold; cursor: pointer; }
    .erro { color: #dc3545; font-size: 0.9em; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Acesso restrito</h2>
    % if mensagem:
    <p class="erro">{{ mensagem }}</p>
    % end
    <form action="/login" method="post">
      <label for="usuario">Usuário</label>
      <input id="usuario" type="text" name="usuario" required autocomplete="username">

      <label for="senha">Senha</label>
      <input id="senha" type="password" name="senha" required autocomplete="current-password">

      <input type="submit" value="Entrar">
    </form>
  </div>
</body>
</html>
```

Em `views/ranking.tpl`, logo abaixo do `<h1>`, acrescente a identificação da sessão e o link de saída:

```html
  <p>Sessão ativa: <strong>{{ usuario }}</strong> · <a href="/logout">Sair</a></p>
```

## Passo 5: aplicação completa (`app.py`)

Esta versão **mantém o relatório da Nota 4** e acrescenta a proteção, em vez de substituí-lo por uma página genérica.

```python
import functools
import os
import secrets
from pathlib import Path

from bottle import (
    TEMPLATE_PATH, Bottle, redirect, request, response, run, static_file, template
)

from dados import buscar_usuario, consultar_ranking
from seguranca import verificar_senha

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH.insert(0, str(BASE_DIR / "views"))

# O segredo vem do ambiente. Sem ele, usa-se um valor aleatório temporário,
# e todas as sessões são invalidadas a cada reinício do servidor.
CHAVE_SECRETA = os.environ.get("APP_SECRET") or secrets.token_hex(32)
NOME_COOKIE = "sessao"

# A URL carrega apenas um código; a mensagem real fica no servidor
MENSAGENS = {
    "restrito": "Acesso restrito. Faça login para continuar.",
    "invalido": "Usuário ou senha incorretos.",
    "saiu": "Sessão encerrada.",
}

app = Bottle()


def ir_para_login(codigo: str):
    redirect(f"/login?erro={codigo}")


def requer_autenticacao(funcao_rota):
    """Bloqueia a rota se o cookie de sessão estiver ausente ou adulterado."""
    @functools.wraps(funcao_rota)
    def wrapper(*args, **kwargs):
        usuario = request.get_cookie(NOME_COOKIE, secret=CHAVE_SECRETA)
        if not usuario:
            ir_para_login("restrito")
        return funcao_rota(*args, **kwargs)
    return wrapper


@app.get("/login")
def exibir_login():
    codigo = request.query.get("erro", "")
    return template("login", mensagem=MENSAGENS.get(codigo, ""))


@app.post("/login")
def processar_login():
    login = (request.forms.getunicode("usuario") or "").strip()
    senha = request.forms.getunicode("senha") or ""  # senha nunca recebe strip()

    registro = buscar_usuario(login)
    if registro and verificar_senha(senha, registro["senha_hash"], registro["salt"]):
        response.set_cookie(
            NOME_COOKIE,
            registro["login"],
            secret=CHAVE_SECRETA,
            httponly=True,    # JavaScript não consegue ler o cookie
            samesite="Lax",   # reduz o envio do cookie em requisições de outros sites
            max_age=3600,     # sessão de 1 hora
            path="/",
            # secure=True,    # ative quando o site usar HTTPS
        )
        redirect("/relatorio/ranking")

    ir_para_login("invalido")


@app.get("/logout")
def logout():
    response.delete_cookie(NOME_COOKIE, path="/")
    ir_para_login("saiu")


@app.get("/relatorio/ranking")
@requer_autenticacao
def pagina_ranking():
    usuario = request.get_cookie(NOME_COOKIE, secret=CHAVE_SECRETA)
    return template("ranking", linhas=consultar_ranking(), usuario=usuario)


@app.get("/api/ranking-vendas")
def api_ranking_vendas():
    return {"status": "sucesso", "dados": consultar_ranking()}


@app.get("/static/<caminho:path>")
def arquivos_estaticos(caminho):
    return static_file(caminho, root=str(BASE_DIR / "static"))


if __name__ == "__main__":
    if "APP_SECRET" not in os.environ:
        print("Aviso: APP_SECRET não definido. Usando segredo temporário.")
    print("Servidor rodando em http://localhost:8080")
    run(app, host="localhost", port=8080, debug=True, reloader=True)
```

> [!note] Por que a URL leva um código e não a mensagem?
> Se a página de login exibisse qualquer texto recebido em `?erro=...`, alguém poderia montar um link com uma mensagem enganosa (por exemplo, pedindo dados pessoais) e enviá-lo a outras pessoas. Aceitando apenas códigos conhecidos, o servidor controla o que é exibido.

### Definir o segredo e executar

Gere um segredo e guarde-o em uma variável de ambiente **antes** de iniciar o servidor.

**Linux e macOS:**

```bash
export APP_SECRET=$(python -c "import secrets; print(secrets.token_hex(32))")
python app.py
```

**Windows (PowerShell):**

```powershell
$env:APP_SECRET = python -c "import secrets; print(secrets.token_hex(32))"
python app.py
```

## Passo 6: testar a segurança

Faça cada teste e registre o que observou.

> [!question] Teste 1: acesso sem login
> Abra `http://localhost:8080/relatorio/ranking` em uma janela anônima. Para onde você foi levado?

> [!question] Teste 2: senha errada
> Tente entrar com uma senha incorreta. A mensagem diz se o erro foi no usuário ou na senha? Por que isso é intencional?

> [!question] Teste 3: cookie protegido
> Após o login, abra as ferramentas do desenvolvedor (F12), vá em **Application** (ou **Storage**) e inspecione o cookie `sessao`. A opção `HttpOnly` está marcada? Digite `document.cookie` no console: o cookie aparece?

> [!question] Teste 4: cookie adulterado
> Altere manualmente o valor do cookie `sessao` e recarregue o relatório. O que acontece?

> [!question] Teste 5: o conteúdo do cookie é secreto?
> No valor do cookie, o trecho após o `?` é Base64. Decodifique-o (pode ser necessário decodificar a URL antes) e procure o nome do usuário.

> [!success]- Resultados esperados
>
> 1. Redirecionamento para `/login` com a mensagem de acesso restrito.
> 2. A mensagem é genérica ("Usuário ou senha incorretos"). Revelar qual dos dois está errado ajudaria um invasor a descobrir quais usuários existem.
> 3. `HttpOnly` marcado; o cookie **não** aparece em `document.cookie`, o que dificulta o roubo por scripts maliciosos (XSS).
> 4. A assinatura deixa de conferir, o servidor trata como sem sessão e redireciona ao login.
> 5. O nome do usuário aparece legível. A assinatura impede a **alteração**, mas não esconde o conteúdo. Por isso o cookie não deve guardar informações sensíveis.

## Desafios

> [!question] Desafio 1: proteger a API
> Faça `/api/ranking-vendas` exigir login. Como clientes de API não seguem telas de login, responda com **status 401** e uma mensagem em JSON, em vez de redirecionar.

> [!success]- Solução do desafio 1
>
> ```python
> def requer_autenticacao_api(funcao_rota):
>     @functools.wraps(funcao_rota)
>     def wrapper(*args, **kwargs):
>         if not request.get_cookie(NOME_COOKIE, secret=CHAVE_SECRETA):
>             response.status = 401
>             return {"status": "erro", "mensagem": "Autenticação necessária."}
>         return funcao_rota(*args, **kwargs)
>     return wrapper
>
>
> @app.get("/api/ranking-vendas")
> @requer_autenticacao_api
> def api_ranking_vendas():
>     return {"status": "sucesso", "dados": consultar_ranking()}
> ```

> [!question] Desafio 2: logout seguro
> Trocar o logout de `GET` para `POST`, usando um botão em formulário. Por que uma ação que altera o estado da sessão não deveria ser feita por um simples link?

> [!question] Desafio 3: limite de tentativas
> Bloqueie o login por 1 minuto após 5 tentativas erradas do mesmo usuário. Qual estrutura você usaria para guardar as tentativas?

> [!question] Desafio 4: tempo de resposta constante
> Hoje, um usuário inexistente recebe resposta mais rápida que um usuário válido com senha errada, pois o hash só é calculado no segundo caso. Como evitar essa diferença?

> [!tip]- Dica do desafio 4
> Quando o usuário não existir, calcule o hash de uma senha fictícia antes de responder, para que o tempo gasto seja parecido nos dois casos.

> [!question] Desafio 5: guardar o número de iterações
> Acrescente uma coluna `iteracoes` na tabela `Usuario`. Por que isso permite aumentar o custo do hash no futuro sem invalidar as senhas já cadastradas?

> [!tip]- Alternativa: bcrypt
> Se puder instalar bibliotecas (`pip install bcrypt`), o `bcrypt` gera e embute o salt no próprio hash:
>
> ```python
> import bcrypt
>
> def gerar_hash_bcrypt(senha: str) -> str:
>     return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
>
> def verificar_senha_bcrypt(senha: str, hash_salvo: str) -> bool:
>     return bcrypt.checkpw(senha.encode("utf-8"), hash_salvo.encode("utf-8"))
> ```
>
> Nesse caso, a coluna `salt` deixa de ser necessária.

## O que ainda falta para produção

Esta atividade cobre o essencial, mas um sistema real também precisaria de:

- **HTTPS**, com `secure=True` no cookie
- **Proteção contra CSRF** nos formulários
- **Limite de tentativas de login** e registro de acessos
- **Gerenciamento de sessões** no servidor, em vez de confiar apenas no cookie
- **Servidor de produção** (por exemplo, Gunicorn atrás de um proxy), sem `debug` nem `reloader`

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| `no such table: Usuario` | `criar_usuario.py` não foi executado | Execute o script e cadastre um usuário |
| Login sempre recusado | Senha digitada diferente da cadastrada, ou banco errado | Recadastre com outro login e confira o `DB_PATH` |
| A sessão cai a cada alteração no código | `APP_SECRET` não definido: o segredo muda a cada reinício | Defina a variável de ambiente antes de rodar |
| `TypeError` em `set_cookie` com `samesite` | Versão antiga do Bottle ou do Python | Atualize: `pip install -U "bottle>=0.13"` (Python 3.8+) |
| `NameError: usuario is not defined` na página | Rota não passa `usuario` ao template | Passe `usuario=usuario` em `template("ranking", ...)` |

## Checklist de verificação

- [ ] A tabela `Usuario` guarda `senha_hash` e `salt`, e nenhuma senha em texto puro
- [ ] Nenhum segredo ou senha está escrito no código
- [ ] `/relatorio/ranking` redireciona ao login quando não há sessão
- [ ] Após o login, a página mostra o gráfico, a tabela e o nome do usuário
- [ ] O cookie tem `HttpOnly` e `SameSite=Lax`
- [ ] Um cookie adulterado é recusado
- [ ] O logout encerra a sessão
- [ ] Os cinco testes de segurança foram registrados

## Fechamento

Você percorreu o ciclo completo de uma aplicação de dados: **modelagem**, **CRUD**, **transações**, **análise**, **visualização**, **API**, **página web** e **autenticação**. Volte ao [[produtos-00-roteiro|roteiro]] para revisar os critérios de avaliação.
