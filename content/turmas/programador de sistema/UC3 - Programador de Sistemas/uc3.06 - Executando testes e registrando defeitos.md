---
quartz-properties: true
title: uc3.06 - Executando testes e registrando defeitos
description: Execução do plano de teste e da suíte automatizada na versão 0.9 do sistema Gestão de Produtos, com tabulação dos resultados e registro de defeitos reprodutíveis
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-19
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
>
> **5. Trocar com outra dupla**
>
> - Entregue seu `docs/registro-de-defeitos.md` a outra dupla. Ela tenta **reproduzir cada defeito usando somente o texto escrito**.
> - Ajuste o que a outra dupla não conseguiu seguir.

> [!info] Falha, defeito e a regra "um registro por defeito"
> A tela de erro, a linha vermelha do pytest e o produto errado na lista são **falhas**: o que você observa. O **defeito** é a causa no código. Hoje vocês ainda não sabem onde ela está, mas podem perceber que **falhas diferentes descrevem o mesmo comportamento errado**. O número de linhas vermelhas **não** é o número de defeitos.

> [!info] Severidade × prioridade
>
> | | Pergunta | Quem decide | Exemplo |
> | --- | --- | --- | --- |
> | **Severidade** | Qual o **impacto** do problema no sistema e no negócio? | Quem testa | Crítica, alta, média, baixa |
> | **Prioridade** | Qual a **urgência** de corrigir? | Equipe e cliente | Alta, média, baixa |
>
> As duas podem divergir. Um erro de grafia no logotipo tem severidade baixa, mas pode ter prioridade alta antes de uma apresentação ao cliente.
>
> **Justifique** a severidade em uma frase: o que acontece de ruim se esse defeito chegar ao cliente?

> [!tip] Guardando evidências
>
> ```bash
> mkdir docs/evidencias
> pytest -v --tb=short > docs/evidencias/pytest-v0.9.txt
> ```
>
> Se o arquivo ficar ilegível no PowerShell, use uma captura de tela. Para as falhas manuais, capture a tela com o resultado visível e salve em `docs/evidencias/`.

> [!abstract] O que você vai entregar
>
> - `docs/resultados-de-teste.md`: um registro por caso executado
> - `docs/registro-de-defeitos.md`: um registro por defeito distinto, **reproduzível por outra dupla**
> - Evidências em `docs/evidencias/`
> - Um commit local com mensagem clara

> [!question] Para refletir
>
> - Se dois registros de defeito descrevem o mesmo problema, o que se perde na hora de corrigir?
> - Por que "o sistema deu erro" não serve como resultado obtido?

⬅️ Aula anterior: [[uc3.05 - Aplicando TDD fase 2]] | ➡️ Próxima aula: ✨ Em edição
