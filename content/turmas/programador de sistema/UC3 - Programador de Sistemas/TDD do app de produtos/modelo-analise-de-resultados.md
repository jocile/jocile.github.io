---
title: Modelo de análise de resultados
description: Modelo e exemplo para interpretar os resultados de teste, priorizar defeitos e registrar a cobertura de código em cinco linhas de análise
date: 2026-11-17
draft: false
tags:
  - testes/modelo
  - documentacao
---

Os números do teste não falam sozinhos. A **análise** transforma "14 casos passaram e 5 falharam" em uma conclusão que a Loja do Bairro consegue usar: **o sistema pode ser entregue? Onde está o risco? O que fazer primeiro?**

⬆️ [[uc3.04 - Aplicando TDD]]

## Modelo para `docs/analise-de-resultados.md`

```markdown
# Análise de resultados: Sistema Gestão de Produtos v0.9

## 1. Taxa de aprovação

| Conjunto | Aprovados | Total | Taxa |
| --- | --- | --- | --- |
| Casos manuais | | | |
| Testes automatizados | | | |
| Todos | | | |

## 2. Padrões nos resultados
(Falhas parecidas? Várias falhas com a mesma causa? Alguma área com muitas falhas?)

## 3. Ordem de correção

| Ordem | Defeito | Severidade | Prioridade | Por que nesta posição |
| --- | --- | --- | --- | --- |
| 1 | | | | |

## 4. Cobertura de código

| Momento | Cobertura de linhas | Cobertura com ramos | Principais trechos não cobertos |
| --- | --- | --- | --- |
| Antes | | | |
| Depois | | | |

**Testes acrescentados:** (quais e o que verificam)
**O que ficou de fora e por quê:**

## 5. Conclusão (5 linhas)
1. O que o resultado indica sobre a qualidade do sistema.
2. Onde está o maior risco.
3. O que a cobertura mostrou que os casos manuais não mostravam.
4. O que **não** dá para afirmar só com esses testes.
5. Recomendação à Loja do Bairro.
```

## Exemplo da conclusão (de outro sistema)

> [!example] Conclusão em 5 linhas: sistema de agendamento de consultas
> 1. Dos 20 testes, 16 passaram (80%), mas as 4 falhas estão todas no cancelamento de consulta, o que indica um problema concentrado nessa funcionalidade.
> 2. O maior risco é o cancelamento não liberar o horário, o que gera horários perdidos e reclamação de pacientes.
> 3. A cobertura mostrou que a rota de reagendamento nunca foi executada por nenhum teste, e os casos manuais também não a cobriam.
> 4. Com estes testes não dá para afirmar que o sistema suporta muitos usuários ao mesmo tempo, pois ninguém testou carga.
> 5. Recomendamos corrigir o cancelamento e acrescentar testes de reagendamento antes da entrega.

## Como escrever uma boa análise

| Critério | Mau exemplo | Bom exemplo |
| --- | --- | --- |
| Interpreta o número | "76,9% passaram." | "76,9% passaram, mas as falhas estão em venda e acesso, que são as áreas de maior impacto." |
| Aponta o risco | "O sistema tem erros." | "Vendas aceitas sem baixa de estoque deixam o estoque e o faturamento inconsistentes." |
| Usa a cobertura | "A cobertura é 82%." | "A cobertura é 82%; as linhas fora são o relatório e o logout, de baixo impacto." |
| Reconhece limites | "Com 100% o sistema está perfeito." | "Cobertura alta não prova que os testes verificam tudo." |
| Recomenda | "Melhorar." | "Corrigir A e B antes da entrega e manter a suíte rodando a cada versão." |

## Lista de verificação

- [ ] A taxa de aprovação foi calculada para manuais, automatizados e total
- [ ] A ordem de correção tem **justificativa** por severidade **e** prioridade
- [ ] Os números de cobertura de **antes** e **depois** estão registrados
- [ ] Os testes novos **verificam** algo (têm `assert` sobre o resultado)
- [ ] O que ficou fora da cobertura está **justificado**
- [ ] A conclusão tem 5 linhas e fala de **risco**, não só de números
- [ ] A conclusão reconhece **o que os testes não provam**

⬆️ Volte para [[uc3.04 - Aplicando TDD]].
