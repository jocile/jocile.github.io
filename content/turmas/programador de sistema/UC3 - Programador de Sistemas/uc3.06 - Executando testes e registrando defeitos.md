---
quartz-properties: true
title: uc3.06 - Executando testes e registrando defeitos
description: Execução do plano de teste e da suíte automatizada do sistema Gestão de Produtos, com tabulação dos resultados e registro de defeitos reprodutíveis
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-17
uc: 3
aula: 6
---

> [!note] Executando testes e registrando defeitos
>
> - Registros de teste e tabela de resultados
> - Registro de defeito (título, passos para reproduzir, esperado × obtido, severidade, prioridade, status, evidência)
> - Severidade × prioridade
> - Reprodutibilidade
> - [[modelo-resultados-de-teste|Modelo de tabela de resultados de teste]]
> - [[modelo-registro-de-defeitos|Modelo de registro de defeitos]]

> [!abstract] Contexto
> A equipe de desenvolvimento da **Loja do Bairro** enviou a **versão 0.9** do sistema Gestão de Produtos. A loja pede um relatório que mostre **o que passou, o que falhou e quais problemas precisam ser corrigidos primeiro**. O relatório precisa ser claro o bastante para que **outra pessoa consiga reproduzir cada problema** usando só o texto.

> [!todo] 🖥️ Atividades
>
> Trabalhem em **duplas**.
>
> **1. Receber a versão 0.9**
>
> - Antes de começar, execute `pytest` e confirme que está **tudo verde**. Confira também com `git status` que não há alterações pendentes.
> - Copie os 3 arquivos da pasta `versao-0.9/` (`app.py`, `dados.py` e `validacao.py`) para dentro do projeto, **substituindo os existentes**. Não mexa em `tests/` nem em `docs/`.
> - Faça o commit: `git commit -am "Atualiza para a versão 0.9"`.
>
> **2. Executar os testes**
>
> - Execute a suíte: `pytest -v --tb=short`.
> - Reinicie o sistema e execute de novo os **casos manuais CT01 a CT06** do seu plano de teste.
> - Anote **do seu jeito** o que falhou e o que você observou.
>
> > [!warning] Ainda não é hora de corrigir
> > Não abra os arquivos novos à procura do problema e **não use `git diff`** para ver o que mudou. Hoje o trabalho é **observar e registrar**. A busca pela causa é assunto da Aula 6.
>
>> [!question] Questões
>>
>> - Outra pessoa consegue repetir o que você anotou?
>> - Duas falhas podem ter o mesmo defeito como causa?
>> - Qual falha deve ser corrigida primeiro e por quê?
>
> **3. Tabular os resultados**
>
> - Em `docs/resultados-de-teste.md`, crie **um registro por caso executado** (manuais e automatizados), seguindo o [[modelo-resultados-de-teste]].
>
> **4. Registrar os defeitos**
>
> - Em `docs/registro-de-defeitos.md`, crie **um registro por defeito distinto**, seguindo o [[modelo-registro-de-defeitos]]. **Falhas que descrevem o mesmo comportamento errado entram no mesmo registro.**
> - Anexe evidências (saída do pytest, captura de tela).


⬅️ Aula anterior: [[uc3.05 - Aplicando TDD fase 2]] | ➡️ Próxima aula: [[uc3.07 - Executando testes e registrando defeitos]]
