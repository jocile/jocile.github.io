---
quartz-properties: true
title: uc3.03 - Testes de integração com fixtures
description: Testes automatizados de integração com banco temporário, rotas Flask e fixtures do pytest no sistema Gestão de Produtos, e Avaliação 1 da UC3
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-13
uc: 3
aula: 3
---

> [!note] Testes de integração com fixtures
>
> - Teste unitário, teste de integração e teste de aceitação
> - **Fixtures** do pytest e o arquivo `conftest.py`
> - Banco de dados temporário
> - Test client do Flask
> - Teste de transação (rollback) e de acesso restrito
> - Independência entre testes
> - [Documentação do Flask sobre testes](https://flask.palletsprojects.com/en/stable/testing/)

> [!abstract] Contexto
> A **Loja do Bairro** vai registrar vendas pelo sistema, e cada venda **baixa o estoque**. Se a venda for registrada sem a baixa (ou a baixa sem a venda), o estoque da loja fica errado. Antes de aceitar a entrega, a loja exige **provas automáticas** de que isso não acontece. Hoje vocês testam o sistema **funcionando em conjunto**: banco de dados, rotas e login.

> [!todo] 🖥️ Atividades
>
> **1. Testar a venda no banco real**
>
> - **Antes de começar, faça uma cópia do banco:** `cp gestao_produtos.db gestao_produtos.bak` (no Windows: `copy gestao_produtos.db gestao_produtos.bak`).
> - Crie o [[gabarito-integracao-uc3-aula03#`tests/test_rascunho_banco_real.py`|arquivo `tests/test_rascunho_banco_real.py`.]]
> - Escreva **um teste** que confirme: *uma venda de 100 unidades de um produto com 3 em estoque não altera o estoque nem registra a venda.*
> - Como o banco real não tem um produto com exatamente 3 em estoque, o próprio teste deve **cadastrar um produto de teste** com estoque 3 antes de tentar a venda.
> - Execute o teste **duas vezes** `pytest .\tests\test_rascunho_banco_real.py -v` e olhe o banco (`/produtos`) depois de cada execução.
>
>> [!question] Questões
>>
>> - Por que o teste mexeu nos dados do sistema?
>> - O que mudou na segunda execução?
>> - Como preparar um cenário que seja **sempre igual**, sem sujar o banco do sistema?
>
> **2. Conhecer as fixtures**
>
> - Abra o [[gabarito-integracao-uc3-aula03#1. `tests/conftest.py`]] arquivo `tests/conftest.py`, e leia os comentários.
> - Identifique: o que cada fixture prepara e o que acontece com o banco temporário **depois** de cada teste.
> - Apague o arquivo `tests/test_rascunho_banco_real.py` e restaure a cópia: `cp gestao_produtos.bak gestao_produtos.db`.
>
> **3. Decidir o tipo de teste de cada funcionalidade**
>
> - Em [[gabarito-plano-de-teste-uc3-aula01#Tabela de plano de testes|`docs/plano-de-teste.md`]], acrescente à tabela dos casos **CT01 a CT06** duas colunas: **tipo de teste mais adequado** (manual, unitário, integração ou aceitação) e **justificativa**.
>
> **4. Escrever os testes de integração**
>
> - Crie [[gabarito-integracao-uc3-aula03#2. `tests/test_integracao.py`|`tests/test_integracao.py`]] com os **4 testes obrigatórios** da tabela abaixo.
> - Execute **toda a suíte** (`pytest`) e confira que os testes das Aulas 2 e 3 passam.
> - No [[gabarito-integracao-uc3-aula03#3. Mapa das metodologias por funcionalidade|`docs/plano-de-teste.md`]], marque **quais casos foram automatizados** e em qual arquivo.
> - Faça o commit local.
>
> **5. Avaliação 1**
>
> - Prepare a apresentação da sua dupla (veja o quadro **Avaliação 1** abaixo).

> [!info] Três níveis de teste
>
> | Tipo | O que testa | Exemplo no nosso sistema |
> | --- | --- | --- |
> | **Unitário** | Uma função isolada | `validar_produto` recusa preço negativo |
> | **Integração** | Várias partes funcionando juntas | Rota + sessão + banco: login e acesso à lista |
> | **Aceitação** | O sistema do ponto de vista de quem o usa | "Consigo cadastrar um produto e vê-lo na lista?" |
>
> Nenhum substitui os outros. A pergunta é: **para esta funcionalidade, qual tipo encontra os problemas mais importantes com menos esforço?**

>[!question] O que é uma fixture
> Uma **fixture** é um **cenário preparado antes de cada teste e descartado depois**, como uma bancada de laboratório montada e limpa a cada experimento.
>
> No pytest, você **pede** a fixture escrevendo o nome dela como parâmetro do teste:
>
> ```python
> def test_login_exibe_o_formulario(cliente):
>     resposta = cliente.get("/login")
>
>     assert resposta.status_code == 200
> ```
>
> O pytest vê o parâmetro `cliente`, procura a fixture com esse nome no `conftest.py`, prepara o cenário e entrega o resultado ao teste.

> [!info] Fixtures entregues no [[gabarito-integracao-uc3-aula03#1. `tests/conftest.py`|`tests/conftest.py`]]
>
> | Fixture | O que entrega |
> | --- | --- |
> | `banco_temporario` | Um banco novo e **descartável**, com 3 categorias, 5 produtos e 1 usuário. O sistema passa a usar esse banco durante o teste |
> | `banco` | Uma conexão para você **consultar** o banco temporário e conferir o resultado |
> | `cliente` | O **test client** do Flask: um "navegador de mentira" que faz requisições sem abrir o servidor |
> | `cliente_logado` | O mesmo cliente, já com o login feito |
> | `obter_token_csrf` | Função que lê o token CSRF do formulário (usada nos desafios) |
>
> **Dados do banco temporário** (sempre os mesmos, a cada teste):
>
> | id | Produto | Estoque |
> | --- | --- | --- |
> | 1 | Smartphone | 10 |
> | 2 | Notebook | 5 |
> | 3 | Sofá | 3 |
> | 4 | Cadeira de Escritório | 12 |
> | 5 | Camisa Polo | 25 |
>
> **Usuário de teste:** `tester` com a senha `SenhaTeste123`.

> [!info] Como usar o test client e verificar erros esperados
>
> ```python
> resposta = cliente.get("/produtos")            # como digitar o endereço
> resposta = cliente.post("/login", data={...})  # como enviar um formulário
>
> resposta.status_code                 # 200, 302 (redirecionamento), 403...
> resposta.headers["Location"]         # para onde redirecionou
> resposta.get_data(as_text=True)      # o HTML devolvido
> ```
>
> Quando **o erro é o resultado esperado** (a venda sem estoque deve falhar), use `pytest.raises`: o teste passa se o erro acontecer e falha se não acontecer.
>
> ```python
> import pytest
>
> def test_divisao_por_zero_gera_erro():
>     with pytest.raises(ZeroDivisionError):
>         1 / 0
> ```

> [!info] Os 4 testes obrigatórios de `tests/test_integracao.py`
>
> A função de venda é `dados.registrar_venda(conn, id_produto, quantidade)`. Para abrir a conexão, use `dados.abrir_conexao()`.
>
> | # | Teste | O que verificar |
> | --- | --- | --- |
> | 1 | Venda com estoque suficiente | Vender 3 unidades do Smartphone: o estoque cai de 10 para 7 **e** a venda fica registrada |
> | 2 | Venda com estoque insuficiente | Vender 100 unidades do Sofá (estoque 3): ocorre `sqlite3.IntegrityError`, o estoque continua 3 **e** nenhuma venda é registrada |
> | 3 | Acesso restrito | Abrir `/produtos/novo` **sem login**: a resposta é um redirecionamento (302) para o login |
> | 4 | Login válido | Enviar o login correto: a resposta é um redirecionamento (302); depois, `/produtos` responde 200 e mostra "Smartphone" |
>
> **Desafios opcionais**
>
> | # | Teste | O que verificar |
> |---|---|---|
> | 5 | Envio sem token CSRF | Com login feito, enviar o formulário de produto **sem** o token: resposta 403 e nenhum produto gravado |
> | 6 | Dados inválidos | Com login e token corretos, enviar preço `-10`: resposta 400, mensagem de preço inválido e nenhum produto gravado |
>
> Lembre-se do padrão **Preparar, Executar e Verificar**, e de que cada teste precisa funcionar **sozinho**.

> [!tip] Comandos úteis
>
> ```bash
> pytest -v                              # lista cada teste
> pytest tests/test_integracao.py        # só os de integração
> pytest -k "venda"                      # só os testes com "venda" no nome
> pytest --durations=3                   # mostra os 3 testes mais lentos
> ```
>
> O login faz o hash da senha (lento de propósito), então os testes de login levam um pouco mais.

> [!warning] Regras de ouro
>
> - **Nenhum teste da pasta `tests/` pode mexer no banco real** (exceto o rascunho da atividade 1, que será apagado).
> - Os testes **não devem depender da ordem** em que rodam.
> - Se um teste falhar, leia a mensagem completa antes de mexer no código.

%%
> [!warning] Avaliação 1 (última hora da aula)
> Cada dupla apresenta em **cerca de 8 minutos**:
>
> 1. O **plano de teste** e os 6 casos (como foram escritos e executados).
> 2. A **escolha do tipo de teste** para cada funcionalidade, com a justificativa.
> 3. A **suíte automatizada** rodando (`pytest -v`) e uma explicação de **um teste de integração**.
> 4. Uma resposta curta: *se um teste passa, isso garante que não há defeitos? Por quê?*
>
> **O que será observado (Indicador 1):** se vocês **usam metodologias diferentes de teste** e **escolhem cada uma conforme a funcionalidade**: casos manuais bem escritos, adequação do tipo de teste a cada funcionalidade e testes unitários e de integração funcionando.

> [!abstract] O que você vai entregar
>
> - `tests/test_integracao.py` com os 4 testes obrigatórios
> - `docs/plano-de-teste.md` atualizado: tipo de teste e justificativa por caso, e os casos automatizados marcados
> - O resultado do `pytest` **sem falhas** (captura de tela ou saída copiada)
> - Um commit local com mensagem clara

%%

> [!question] Para refletir
>
> - Qual funcionalidade vale mais a pena testar à mão, e qual vale mais a pena automatizar? Por quê?
> - O que aconteceria com a suíte se cada teste usasse o banco real?

⬅️ Aula anterior: [[uc3.02 - testes automatizados com pytest]] | ➡️ Próxima aula: [[uc3.05 - Executando testes e registrando defeitos]]
