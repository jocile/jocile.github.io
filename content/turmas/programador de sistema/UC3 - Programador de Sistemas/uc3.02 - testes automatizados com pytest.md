---
quartz-properties: true
title: uc3.02 - Primeiros testes automatizados com pytest
description: Conversão de casos de teste manuais em testes automatizados com pytest, para a validação de produtos e a segurança de senhas do sistema Gestão de Produtos
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-12
uc: 3
aula: 2
---

> [!note] Primeiros testes automatizados com pytest
>
> - Teste unitário
> - pytest e `assert`
> - Funções `test_*`
> - Padrão **Preparar, Executar e Verificar**
> - Valores de fronteira (preço `0` e negativo, estoque decimal)
> - Teste caixa-branca
> - Leitura da saída verde e vermelha
> - [Guia inicial da documentação oficial do pytest](https://docs.pytest.org/en/stable/getting-started.html)

> [!abstract] Contexto
> Ontem a equipe de qualidade da **Loja do Bairro** executou casos de teste **à mão**. Funciona, mas cansa: a cada nova versão seria preciso repetir tudo. Hoje vocês vão ensinar o computador a **repetir as verificações sozinho**, começando pelas funções que validam o cadastro de produtos e protegem as senhas.

> [!todo] 🖥️ Atividades
>
> **1. Verificar sem pytest**
> - Crie um arquivo `testar_validacao.py` na raiz do projeto.
> - Escreva um script que chama a função `validar_produto` com **3 entradas**: uma válida, uma com preço negativo e uma com nome vazio.
> - Use `assert` para conferir o que a função devolve em cada caso.
> - Execute com `python testar_validacao.py`.
>
>> [!question] Questões
>> - Se o segundo `assert` falhar, o que acontece com os demais?
>> - Como saber qual verificação falhou e por quê?
>
> **2. Conhecer o pytest**
> - Execute `pytest --version` para confirmar a instalação.
> - Leia o guia inicial da documentação do pytest e descubra: **como o pytest encontra os testes?** (nome de arquivo, nome de função)
>
> **3. Converter o script em testes automatizados**
> - Crie o arquivo `tests/test_validacao.py` com **6 testes** para `validar_produto`: um caso válido, preço negativo, preço infinito, estoque decimal, categoria inexistente e nome vazio.
> - Crie o arquivo `tests/test_seguranca.py` com testes para as funções de senha: a mesma senha gera **hashes diferentes** (por causa do salt), a senha correta é **aceita** e a errada é **recusada**.
> - Execute `pytest` e registre o resultado.
> - Faça o commit local.

> [!info] Antes de escrever os testes
>
> **O que a função devolve.** `validar_produto(campos, ids_categoria_validos)` recebe os campos do formulário **como texto** e devolve um par `(dados, erros)`:
> - se tudo estiver certo: `dados` é um dicionário limpo e `erros` é `{}`
> - se algo estiver errado: `dados` é `None` e `erros` indica o campo problemático
>
> **Como o `assert` funciona.** `assert condição` não faz nada se a condição for verdadeira. Se for falsa, o Python interrompe com um erro. O pytest usa isso para decidir se o teste **passou** ou **falhou**.
>
> **Como o pytest encontra os testes.** Ele procura arquivos `test_*.py` e executa as funções cujo nome começa com `test_`.

> [!info]- Estrutura do teste: Preparar, Executar e Verificar
>
> ```python
> def test_nome_muito_longo_e_recusado():
>     # 1. PREPARAR: monte os dados de entrada
>     campos = {
>         "nome": "x" * 101,
>         "preco": "10,00",
>         "estoque": "1",
>         "id_categoria": "1",
>     }
>
>     # 2. EXECUTAR: chame a função que está sendo testada
>     dados, erros = validar_produto(campos, {1, 2, 3})
>
>     # 3. VERIFICAR: compare com o resultado esperado
>     assert dados is None
>     assert "nome" in erros
> ```
>
> Este exemplo é de **outra regra** (nome com mais de 100 caracteres). Use-o como modelo, não como resposta.

> [!tip] Como um bom teste se parece
> - O **nome diz o que está sendo testado** e qual é o resultado esperado: `test_preco_negativo_e_recusado`, e não `test1`.
> - Tem **um único motivo para falhar**: verifica uma regra por teste.
> - É **independente**: funciona sozinho, em qualquer ordem.
> - Os dados de entrada ficam **visíveis dentro do teste**.

> [!info] Valores de fronteira
> Os erros costumam morar **na beira** das regras. Para a regra "preço igual ou maior que zero", teste **os dois lados da fronteira**:
>
> | Entrada | Resultado esperado |
> |---|---|
> | `-0,01` (logo abaixo) | recusado |
> | `0` (exatamente na fronteira) | **aceito** |
> | `0,01` (logo acima) | aceito |
>
> Faça o mesmo raciocínio para o estoque e para o tamanho do nome.

> [!info] Casos obrigatórios do `tests/test_validacao.py`
>
> | Teste | O que verificar |
> |---|---|
> | Caso válido | `erros` vazio e `dados` com o produto limpo (nome sem espaços nas pontas, preço como número) |
> | Preço negativo | `dados` é `None` e há erro em `preco` |
> | Preço infinito (`inf`) | `dados` é `None` e há erro em `preco` |
> | Estoque decimal (`2.5`) | `dados` é `None` e há erro em `estoque` |
> | Categoria inexistente | `dados` é `None` e há erro em `id_categoria` |
> | Nome vazio | `dados` é `None` e há erro em `nome` |
>
> **Desafio opcional:** teste também o preço `0` (deve ser aceito) e o preço escrito com vírgula, como `49,90`.

> [!info] Casos obrigatórios do `tests/test_seguranca.py`
>
> As funções `gerar_hash_senha` e `verificar_senha` estão em `seguranca.py`.
>
> | Teste | O que verificar |
> |---|---|
> | Mesma senha, hashes diferentes | Gerar o hash da mesma senha **duas vezes**: os hashes e os salts devem ser **diferentes** |
> | Senha correta | `verificar_senha` devolve `True` |
> | Senha errada | `verificar_senha` devolve `False` |
>
> > [!note] Por que é mais lento?
> > Gerar um hash de senha é lento **de propósito**. O arquivo de segurança levará alguns segundos para rodar. Isso é normal.

> [!tip] Como executar o pytest
>
> ```bash
> pytest              # roda todos os testes
> pytest -v           # lista cada teste com o resultado
> pytest tests/test_validacao.py        # roda um arquivo
> pytest -k "preco"   # roda só os testes com "preco" no nome
> ```
>
> **Como ler a saída**
> - `.` ou `PASSED` (verde): o teste passou
> - `F` ou `FAILED` (vermelho): o teste falhou
> - Na falha, o pytest mostra **a linha do `assert`**, o valor esperado e o valor obtido
>
> Experimente **quebrar um teste de propósito** (troque `is None` por `is not None`), leia a mensagem de falha e desfaça a mudança.

> [!warning] Se aparecer `ModuleNotFoundError: No module named 'validacao'`
> O pytest precisa saber onde está o código do sistema. Na raiz do projeto, crie o arquivo `pytest.ini` com:
>
> ```ini
> [pytest]
> pythonpath = .
> testpaths = tests
> ```

> [!info] Programação em pares
> No item 3, trabalhem com **dois papéis** e **troquem a cada teste**:
> - **Piloto:** digita o código
> - **Navegador:** lê, confere o caso e sugere melhorias
>
> Vale uma regra: o piloto só digita o que o navegador consegue explicar.

> [!tip] Fazendo o commit local
>
> ```bash
> git status
> git add tests/ testar_validacao.py pytest.ini
> git commit -m "Adiciona testes automatizados de validação e segurança"
> ```
>
> Confira com `git log --oneline` e nunca inclua o banco `.db`, o ambiente `.venv` nem arquivos de segredo.

> [!abstract] O que você vai entregar
> - `tests/test_validacao.py` com 6 testes
> - `tests/test_seguranca.py` com 3 testes
> - O resultado do `pytest` **sem falhas** (captura de tela ou saída copiada)
> - Um commit local com mensagem clara

> [!question] Para refletir
> - O que um teste automatizado oferece que o caso de teste manual de ontem não oferecia?
> - Se um teste passar, isso prova que a função **não tem defeitos**? Por quê?

⬅️ Aula anterior: [[uc3.01 - Plano de teste e testes manuais]] | ➡️ Próxima aula: [[uc3.03 - Testes de integracao com fixtures]]
