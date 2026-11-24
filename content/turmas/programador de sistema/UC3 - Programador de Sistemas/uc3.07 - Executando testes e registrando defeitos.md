---
quartz-properties: true
title: uc3.07 - Executando testes e registrando defeitos
description: Execução do plano de teste e do sistema Gestão de Produtos, com tabulação dos resultados e registro de defeitos reprodutíveis
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-18
uc: 3
aula: 7
---

> [!abstract] Contexto
> A equipe de desenvolvimento da **Loja do Bairro** enviou a **versão 0.9** do sistema Gestão de Produtos. A loja pede um relatório que mostre **o que passou, o que falhou e quais problemas precisam ser corrigidos primeiro**. O relatório precisa ser claro o bastante para que **outra pessoa consiga reproduzir cada problema** usando só o texto.

> [!todo] 🖥️ Atividades
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

⬅️ Aula anterior: [[uc3.06 - Executando testes e registrando defeitos]] | ➡️ Próxima aula: [[uc3.08 - Executando testes e registrando defeitos]]
