---
quartz-properties: true
title: uc3.08 - Executando testes e registrando defeitos
description: Execução do plano de teste e tabulação dos resultados e registro de defeitos reprodutíveis
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-19
uc: 3
aula: 8
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

⬅️ Aula anterior: [[uc3.07 - Executando testes e registrando defeitos]] | ➡️ Próxima aula: [[uc4.01 - Projeto integrador]]
