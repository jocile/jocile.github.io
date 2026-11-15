---
title: Roteiro de instalação e execução do sistema Gestão de Produtos
description: Passo a passo para extrair o repositório-base, criar o ambiente virtual, instalar as dependências e executar o sistema Gestão de Produtos em Flask
date: 2026-11-11
draft: false
tags:
  - python/web
  - flask
  - testes/roteiro
---

Antes de testar um sistema, é preciso fazê-lo funcionar no seu computador. Este roteiro leva você do projeto base até o sistema aberto no navegador.

[GitHub - jocile/gestao-produtos-base: TDD repositório-base do sistema Gestão de Produtos para atividades de testes · GitHub](https://github.com/jocile/gestao-produtos-base)

⬆️ [[uc3.01 - Plano de teste e testes manuais]]

> [!info] Ficha do roteiro
>
> - **Ambiente:** computador local (VS Code e terminal)
> - **Tempo estimado:** 40 minutos
> - **Pré-requisitos:** Python 3.10 ou superior e VS Code instalados
> - **Resultado esperado:** o sistema Gestão de Produtos aberto no navegador, com login funcionando

## Passo 1: conferir o Python

Abra o terminal e execute:

```bash
python --version
```

O resultado deve ser **Python 3.10** ou superior. Se aparecer um erro ou uma versão antiga, tente `python3 --version` (Linux e macOS) ou `py --version` (Windows). Use o comando que funcionar nos próximos passos.

## Passo 2: extrair o repositório-base

1. [Baixe](https://github.com/jocile/gestao-produtos-base) e extraia em uma pasta de fácil acesso (por exemplo, `Documentos`).
2. Abra o VS Code, escolha **Arquivo > Abrir Pasta** e selecione a pasta extraída.
3. Abra o terminal integrado: **Terminal > Novo Terminal**.

> [!warning] Cuidado com a pasta dentro da pasta
> Ao extrair, às vezes o sistema cria `gestao-produtos/gestao-produtos/`. Abra no VS Code a pasta que contém diretamente o arquivo `app.py`.

Confira o conteúdo da pasta:

```bash
ls          # Linux e macOS
dir         # Windows
```

Você deve ver, entre outros, `app.py`, `requirements.txt`, as pastas `views` e `static`, e a pasta `tests`.

## Passo 3: criar o ambiente virtual

O ambiente virtual isola as bibliotecas deste projeto das demais instaladas no computador.

```bash
python -m venv .venv
```

Ative o ambiente:

| Sistema | Comando |
| --- | --- |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Prompt de Comando) | `.venv\Scripts\activate.bat` |
| Linux e macOS | `source .venv/bin/activate` |

Quando der certo, o terminal mostra `(.venv)` no início da linha.

> [!bug] Erro "a execução de scripts foi desabilitada" (Windows)
> No PowerShell, execute uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirme e ative o ambiente de novo. Se preferir, use o Prompt de Comando.

## Passo 4: instalar as dependências

Com o ambiente ativo:

```bash
pip install -r requirements.txt
```

Confira o que foi instalado:

```bash
pip list
```

Devem aparecer, no mínimo, `Flask` e `pytest`.

## Passo 5: definir o segredo da aplicação

O sistema assina o cookie de login com um **segredo** que **não fica escrito no código**: ele vem de uma variável de ambiente.

O segredo assina o cookie de sessão. Sem ele, o sistema usa um valor temporário e **você será deslogado toda vez que o servidor reiniciar**.

| Sistema | Comando |
| --- | --- |
| Windows (PowerShell) | `$env:APP_SECRET = "troque-por-um-texto-longo-e-aleatorio"` |
| Linux e macOS | `export APP_SECRET="troque-por-um-texto-longo-e-aleatorio"` |

>[!tip] O comando seguinte cria o segredo aleatório
>
> **Windows (PowerShell):**
>
> ```powershell
> $env:APP_SECRET = python -c "import secrets; print(secrets.token_hex(32))"
> ```
>
> **Linux e macOS:**
>
> ```bash
> export APP_SECRET=$(python -c "import secrets; print(secrets.token_hex(32))")
> ```

> [!note] A variável vale só para este terminal
> Se você fechar o terminal, repita este passo. Sem a variável, o sistema pode gerar um segredo temporário, e o login cai a cada reinício.

## Passo 6: criar o banco e o usuário de teste

Se o repositório-base já trouxer o arquivo `gestao_produtos.db`, pule para o passo 7. Caso contrário, siga  para criar o banco, e depois cadastre um usuário:

```bash
python criar_banco.py
python criar_usuario.py
```

O segundo comando pede o nome do usuário e a senha (mínimo de 8 caracteres). A senha não aparece enquanto você digita. **Anote os dois**: você vai usá-los nos testes.

## Passo 7: executar o sistema

```bash
flask --app app run --debug
```

O terminal mostrará o endereço do servidor (algo como `http://127.0.0.1:5000`). Copie esse endereço, abra no navegador e faça login com o usuário criado.

> [!example] Resultado esperado
>
> - A tela de login aparece.
> - Depois de entrar, é possível abrir a lista de produtos.
> - O terminal continua aberto, mostrando cada requisição que você faz. Para encerrar o servidor, use `Ctrl + C`.

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| `python` não é reconhecido | Python fora do PATH | Use `py` ou `python3`, ou reinstale marcando "Add Python to PATH" |
| `No module named 'flask'` | Ambiente virtual não ativado | Ative o `.venv` e rode o `pip install` de novo |
| `No such file: requirements.txt` | Terminal na pasta errada | Entre na pasta que contém o `app.py` |
| `Address already in use` | Outro programa usa a porta | Encerre o outro programa ou avise o docente |
| `no such table` | Banco ausente ou vazio | Confira o passo 6 |
| Login sempre recusado | Usuário não cadastrado ou senha diferente | Cadastre outro usuário com `criar_usuario.py` |
| A sessão cai a cada reinício | `APP_SECRET` não definido | Repita o passo 5 antes de executar |

> [!tip] Registre cada obstáculo
> Se algo deu errado e você resolveu, anote o que aconteceu e como corrigiu. Isso é um **registro de teste** da instalação e será útil mais adiante.

## Checklist de verificação

- [ ] `python --version` mostra 3.10 ou superior
- [ ] O terminal mostra `(.venv)` no início da linha
- [ ] `pip list` mostra Flask e pytest
- [ ] A variável `APP_SECRET` foi definida
- [ ] Existe pelo menos um usuário cadastrado
- [ ] O sistema abre no navegador e o login funciona

⬆️ Volte para [[uc3.01 - Plano de teste e testes manuais]] e siga para a exploração do sistema.
