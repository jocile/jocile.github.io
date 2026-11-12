---
quartz-properties: true
title: uc3.05 - Analisando resultados e medindo cobertura
description: Análise dos resultados de teste da versão 0.9, priorização de defeitos e medição da cobertura de código com pytest-cov no sistema Gestão de Produtos
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-17
uc: 3
aula: 5
---

> [!note] Analisando resultados e medindo cobertura
>
> - Análise de resultados: taxa de aprovação, padrões, risco e priorização
> - Cobertura de linhas e de ramos
> - **pytest-cov** e relatório em HTML
> - Cobertura não garante qualidade
> - Cálculo de percentual
> - [Documentação do pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
> - [[modelo-analise-de-resultados|Modelo de análise de resultados]]

> [!abstract] Contexto
> A **Loja do Bairro** recebeu o seu relatório da versão 0.9 e fez duas perguntas: **"o sistema está bom o bastante?"** e **"o que vocês ainda não testaram?"**. Para responder, não basta listar o que falhou: é preciso **interpretar os números**, decidir **por onde começar a corrigir** e descobrir **quais partes do sistema nenhum teste executa**.

> [!todo] 🖥️ Atividades
>
> Trabalhem em **duplas**.
>
> **1. Interpretar os resultados**
> - A partir de `docs/resultados-de-teste.md`, calcule a **taxa de aprovação**: casos aprovados ÷ total de casos × 100. Faça três cálculos: casos manuais, testes automatizados e o total.
> - Proponha a **ordem de correção** dos defeitos de `docs/registro-de-defeitos.md`, **justificando** com severidade e prioridade.
> - Escreva uma **hipótese**: quais partes do sistema você acha que **nenhum teste executa**? (rotas, funções, caminhos de erro)
>
>> [!question] Questões
>> - Como confirmar a sua hipótese sobre o que não foi testado?
>> - Uma cobertura de 100% garante um sistema sem defeitos?
>
> **2. Medir a cobertura**
> - Instale o pytest-cov, se ainda não estiver instalado, e crie o arquivo `.coveragerc` (veja abaixo).
> - Gere o relatório no terminal e em HTML.
> - Abra `htmlcov/index.html` no navegador e navegue até as **linhas em vermelho**.
> - **Compare** o relatório com a sua hipótese: o que você previu e acertou? O que não previu?
>
> **3. Testar o que ficou de fora**
> - Escreva **pelo menos 2 novos testes**, com **verificação real**, para trechos relevantes que o relatório mostrou como não executados. Coloque-os em `tests/test_cobertura.py`.
> - Execute o relatório de novo e **compare a cobertura antes e depois**.
> - **Meta de referência:** cobertura de linhas **acima de 80%**. Se algum trecho ficar de fora, **justifique por escrito** por quê.
>
> **4. Registrar e concluir**
> - Em `docs/resultados-de-teste.md`, acrescente a **cobertura antes e depois**.
> - Redija em `docs/analise-de-resultados.md` a **análise em 5 linhas**: o que o resultado indica sobre a qualidade do sistema e onde está o maior risco. Use o [[modelo-analise-de-resultados]].
> - Faça o commit local.
>
> > [!warning] Ainda não corrija os defeitos
> > Os defeitos da v0.9 continuam abertos. Os testes novos devem cobrir partes **sem relação** com eles. Corrigir é assunto da Aula 6.

> [!info] Taxa de aprovação
>
> $$\text{taxa de aprova\c{c}\~{a}o} = \frac{\text{casos aprovados}}{\text{total de casos executados}} \times 100$$
>
> **Exemplo (outro sistema):** 17 casos aprovados em 20 executados → 17 ÷ 20 = 0,85 → **85%**.
>
> A taxa diz **quanto passou**, mas não diz **o que importa**. Um sistema com 90% de aprovação pode ter justamente a falha de segurança entre os 10% que falharam. Por isso a análise precisa olhar **quais** casos falharam e **que risco** representam.

> [!info] O que é cobertura de código
> **Cobertura** é a porcentagem do código que foi **executado** durante os testes.
>
> | Tipo | O que mede |
> |---|---|
> | **Cobertura de linhas** | Quantas linhas do código rodaram pelo menos uma vez |
> | **Cobertura de ramos** | Quantos **caminhos** de cada decisão (`if`/`else`) foram percorridos, tanto o verdadeiro quanto o falso |
>
> Um `if` pode ter a linha executada e **só um dos caminhos** testado. A cobertura de ramos mostra isso.

> [!warning] Limite importante
> Cobertura mede o que **rodou**, não o que foi **verificado**. Uma linha pode ser executada por um teste que **não confere nada**. Cobertura alta com testes fracos é uma falsa segurança. Nunca escreva um teste só para subir o número.

> [!info] Preparando e medindo
>
> **Instalar** (confira antes com `pip list`):
>
> ```bash
> pip install pytest-cov
> ```
>
> **Criar o `.coveragerc`** na raiz do projeto, para medir só o código do sistema:
>
> ```ini
> [run]
> branch = True
> source = .
> omit =
>     tests/*
>     .venv/*
>
> [report]
> show_missing = True
> ```
>
> **Gerar o relatório:**
>
> ```bash
> pytest --cov --cov-report=term-missing --cov-report=html
> ```
>
> - `term-missing` mostra, no terminal, **os números das linhas** não executadas (coluna `Missing`).
> - `html` cria a pasta `htmlcov/`. Abra `htmlcov/index.html`: linhas **vermelhas** não rodaram, linhas **amarelas** tiveram só um dos caminhos testado.
>
> Para ver só a cobertura de **linhas**, sem os ramos, use `pytest --cov --cov-branch` desligado no `.coveragerc` (`branch = False`) e compare.

> [!tip] Como ler o resultado do terminal
>
> ```text
> Name            Stmts   Miss Branch BrPart  Cover   Missing
> -----------------------------------------------------------
> exemplo.py         20      4      6      1    76%   14-17
> ```
>
> - `Stmts`: linhas executáveis; `Miss`: linhas não executadas
> - `Branch` e `BrPart`: ramos e ramos parcialmente testados
> - `Cover`: a porcentagem
> - `Missing`: **onde olhar**: as linhas do arquivo que nenhum teste executou

> [!info] Como decidir o que testar a seguir
> Nem toda linha vermelha merece um teste. Use três perguntas:
> 1. **Se esta parte falhasse, qual seria o impacto?** (dados, dinheiro, segurança)
> 2. **Ela é fácil de alcançar por um teste?**
> 3. **Um teste aqui verificaria alguma coisa de verdade?**
>
> Comece pelas linhas de **maior impacto**.

> [!tip] Um bom teste novo
> Siga o padrão **Preparar, Executar e Verificar**, use as fixtures do `conftest.py` e **sempre confira o resultado**: o status da resposta, o conteúdo devolvido ou o que ficou no banco. Um teste que só chama o código e não confere nada **sobe a cobertura, mas não protege nada**.

> [!info] Fazendo o commit sem os arquivos de cobertura
> A pasta `htmlcov/` e o arquivo `.coverage` são gerados pelo relatório e **não devem** ser versionados:
>
> ```bash
> git add tests/ docs/ .coveragerc
> git commit -m "Adiciona análise de resultados e testes de cobertura"
> ```
>
> Evite `git add .` hoje.

> [!abstract] O que você vai entregar
> - Taxa de aprovação (manuais, automatizados e total) e a ordem de correção justificada
> - O relatório de cobertura **antes** e **depois** em `docs/resultados-de-teste.md`
> - `tests/test_cobertura.py` com pelo menos 2 testes que verificam algo de verdade
> - A justificativa do que ficou de fora, se a cobertura de linhas não passar de 80%
> - `docs/analise-de-resultados.md` com a análise em 5 linhas
> - Um commit local com mensagem clara

> [!question] Para refletir
> - Um teste que executa uma linha **sem verificar nada** melhora a qualidade do sistema? Por quê?
> - A linha do defeito mais grave estava vermelha ou verde no relatório? O que isso significa?

⬅️ Aula anterior: [[uc3.04 - Executando testes e registrando defeitos]] | ➡️ Próxima aula: ✨em edição!
