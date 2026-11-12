---
title: Modelo de registro de defeitos
description: Modelo, níveis de severidade e prioridade e exemplo de registro de defeito reprodutível
date: 2026-11-16
draft: false
tags:
  - testes/modelo
  - documentacao
---

O registro de defeito é um **pedido de correção** que precisa ser entendido por quem não estava na sala. Se a pessoa que vai corrigir não conseguir reproduzir o problema, ele não será corrigido.

⬆️ [[uc3.04 - Executando testes e registrando defeitos]]

## Modelo para `docs/registro-de-defeitos.md`

```markdown
### DEF-01: Título curto que descreve o comportamento errado

| Campo | Conteúdo |
| --- | --- |
| ID | DEF-01 |
| Título | |
| Versão | 0.9 |
| Rota ou módulo | Tela, rota ou parte do sistema onde aparece |
| Casos relacionados | CT.. e/ou nomes de testes automatizados |
| Passos para reproduzir | 1. ... 2. ... 3. ... |
| Resultado esperado | |
| Resultado obtido | |
| Severidade | Crítica / Alta / Média / Baixa |
| Justificativa da severidade | O que acontece de ruim se chegar ao cliente |
| Prioridade | Alta / Média / Baixa |
| Status | Aberto |
| Evidência | |
```

## Severidade, prioridade e status

> [!info] Severidade (impacto)
>
> | Nível | Significa |
> | --- | --- |
> | **Crítica** | Perda ou corrupção de dados, ou falha de segurança grave |
> | **Alta** | Função importante errada, sem alternativa para o usuário |
> | **Média** | Função com problema, mas há proteção parcial ou alternativa |
> | **Baixa** | Problema leve: mensagem, aparência ou texto |

> [!info] Prioridade (urgência)
> **Alta**: corrigir antes de qualquer outra entrega. **Média**: corrigir na próxima versão. **Baixa**: corrigir quando houver tempo.

> [!info] Status
> **Aberto** → **Em correção** → **Corrigido** → **Verificado**. Hoje todos os defeitos ficam **Aberto**.

## Exemplo preenchido (de outro defeito)

> [!example] DEF-00: Lista de produtos mostra o estoque no lugar do preço
>
> | Campo | Conteúdo |
> | --- | --- |
> | ID | DEF-00 |
> | Título | Lista de produtos mostra o estoque na coluna Preço |
> | Versão | 0.9 |
> | Rota ou módulo | Página `/produtos` |
> | Casos relacionados | CT00; `test_exemplo_colunas_da_lista` |
> | Passos para reproduzir | 1. Fazer login 2. Abrir `/produtos` 3. Comparar a coluna Preço do Smartphone com o cadastro |
> | Resultado esperado | Smartphone com preço R$ 1600,00 |
> | Resultado obtido | Smartphone com valor 10 na coluna Preço (o valor do estoque) |
> | Severidade | Alta |
> | Justificativa da severidade | A loja mostraria preços errados a quem consulta a lista |
> | Prioridade | Alta |
> | Status | Aberto |
> | Evidência | `evidencias/def00-lista.png` |

## Um registro por defeito, não por falha

Quando duas falhas descrevem **o mesmo comportamento errado**, elas são **sintomas do mesmo defeito**: viram **um único registro**, com os dois casos listados em "Casos relacionados". Isso evita corrigir a mesma coisa duas vezes e mostra que você analisou os resultados, e não só os copiou.

## Bom registro × mau registro

| Campo | Mau exemplo | Bom exemplo |
| --- | --- | --- |
| Título | "Erro no cadastro" | "Cadastro de produto aceita preço negativo" |
| Passos | "Tentar cadastrar um produto errado" | "1. Fazer login 2. Abrir `/produtos/novo` 3. Preencher preço `-10` 4. Enviar" |
| Resultado obtido | "Não funcionou" | "Página recarregou com a mensagem X no topo, sem mensagem junto do campo preço" |
| Severidade | "Grave" | "Alta, porque a venda pode ser aceita sem controle de estoque" |

## Lista de verificação

- [ ] Existe **um registro por defeito distinto**
- [ ] O título descreve o comportamento errado
- [ ] Os passos são numerados e **outra dupla conseguiu repeti-los**
- [ ] Esperado e obtido são específicos e comparáveis
- [ ] A severidade tem **justificativa em uma frase**
- [ ] A prioridade foi pensada separada da severidade
- [ ] Os casos manuais e testes automatizados relacionados estão listados
- [ ] Há evidência anexada
- [ ] O status de todos é **Aberto**

⬆️ Volte para [[uc3.04 - Executando testes e registrando defeitos]].
