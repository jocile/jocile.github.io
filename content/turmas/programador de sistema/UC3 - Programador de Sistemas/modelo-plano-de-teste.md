---
title: Modelo de plano de teste e de caso de teste
description: Modelos e exemplos para elaborar um plano de teste de uma página e casos de teste formais, com glossário de defeito, falha e erro
date: 2026-11-11
draft: false
tags:
  - programador-sistemas/aulas/uc3
  - testes
  - documentacao
---

Um bom teste pode ser **repetido por qualquer pessoa** e **diz de antemão qual é o resultado correto**. O plano de teste organiza o que será testado, e os casos de teste descrevem cada verificação.

⬆️ [[uc3.01 - Plano de teste e testes manuais]]

## Conceitos

> [!note] Erro, defeito e falha
>
> | Termo | O que é | Exemplo |
> | --- | --- | --- |
> | **Erro** | Engano de uma pessoa (quem programou, quem especificou) | Esquecer de checar se o preço é negativo |
> | **Defeito** | Problema no código ou no projeto, resultado do erro | A função de validação não tem essa verificação |
> | **Falha** | Comportamento errado que aparece quando o sistema executa | O sistema grava um produto com preço `-10` |
>
> O teste **observa a falha**. A depuração descobre o **defeito**.

> [!note] Tipos de teste que você vai usar
>
> | Tipo | Como é |
> | --- | --- |
> | **Manual** | Uma pessoa executa os passos e confere o resultado |
> | **Exploratório** | Sem roteiro: você investiga o sistema tentando descobrir falhas |
> | **Roteirizado** | Segue casos de teste escritos antes da execução |
> | **Caixa-preta** | Testa pelo que o sistema faz, sem olhar o código |
> | **Caixa-branca** | Testa conhecendo o código, as condições e os caminhos internos |

> [!info] Exploratório × roteirizado
> O exploratório **descobre** problemas e ajuda a escolher o que testar. O roteirizado **repete** o que já se sabe que importa. Um bom trabalho de qualidade usa os dois.

## Modelo de plano de teste

Copie a estrutura abaixo para `docs/plano-de-teste.md` e preencha. O plano deve caber em **uma página**.

```markdown
# Plano de teste: Sistema Gestão de Produtos

## 1. Identificação
- **Sistema:** Gestão de Produtos
- **Versão testada:** (informe a versão)
- **Responsáveis:** (nomes da dupla)
- **Data:** (data da execução)

## 2. Objetivo
(Em uma ou duas frases: o que este plano pretende garantir.)

## 3. Escopo
**Será testado:**
- (funcionalidades incluídas)

**Não será testado:**
- (o que ficou de fora e por quê)

## 4. Ambiente de teste
- Sistema operacional:
- Navegador e versão:
- Python e Flask (versões):
- Endereço do sistema:

## 5. Tipos de teste
- (Quais tipos serão usados e em quais funcionalidades.)

## 6. Critério de aprovação
(Quando o sistema será considerado aprovado. Exemplo: todos os
casos aprovados, sem defeito grave aberto.)

## 7. Casos de teste
(Os 6 casos, no formato abaixo.)
```

> [!tip] Como preencher cada parte
>
> - **Objetivo:** responda "para que estamos testando?", não "o que é o sistema".
> - **Escopo:** declare também o que **não** será testado. Assim ninguém acha que foi coberto.
> - **Ambiente:** o mesmo teste pode dar resultados diferentes em ambientes diferentes, por isso registre versões.
> - **Critério de aprovação:** precisa ser verificável, nunca "o sistema funciona bem".

## Modelo de caso de teste

```markdown
### CT00: Título curto e específico

| Campo | Conteúdo |
| --- | --- |
| ID | CT00 |
| Título | |
| Tipo | Manual, caixa-preta |
| Pré-condição | O que precisa estar pronto antes (ex.: usuário autenticado) |
| Dados de entrada | Valores exatos usados no teste |
| Passos | 1. ... 2. ... 3. ... |
| Resultado esperado | O que **deve** acontecer, de forma verificável |
| Resultado obtido | (preencher na execução) |
| Status | Aprovado / Reprovado |
| Evidência | Captura de tela ou trecho da saída |
| Observações | |
```

## Exemplo preenchido

Este exemplo é de **outra funcionalidade** (a lista de produtos). Use-o como referência de nível de detalhe, e não como resposta dos seus casos.

> [!example] CT00: Lista de produtos exibe os produtos cadastrados
>
> | Campo | Conteúdo |
> | --- | --- |
> | ID | CT00 |
> | Título | Lista de produtos exibe os produtos cadastrados |
> | Tipo | Manual, caixa-preta |
> | Pré-condição | Usuário autenticado; ao menos 1 produto cadastrado |
> | Dados de entrada | Nenhum |
> | Passos | 1. Abrir o menu e clicar em **Produtos** 2. Observar a tabela exibida |
> | Resultado esperado | A tabela mostra ID, nome, categoria, preço e estoque de cada produto cadastrado |
> | Resultado obtido | A tabela mostrou os 5 produtos cadastrados com todas as colunas |
> | Status | Aprovado |
> | Evidência | `evidencias/ct00-lista.png` |

### Bom caso × mau caso

| Campo | Mau exemplo | Bom exemplo |
| --- | --- | --- |
| Título | "Testar cadastro" | "Cadastro com preço negativo" |
| Passos | "Tentar cadastrar um produto errado" | "1. Acessar a página de novo produto 2. Preencher preço `-10` 3. Enviar" |
| Resultado esperado | "Dar erro" | "Formulário reexibido, com mensagem no campo preço; nada gravado" |
| Resultado obtido | "Funcionou" | "Produto `Teste` apareceu na lista com preço -10,00" |

## Lista de verificação do caso de teste

Use esta lista para revisar seus casos e para avaliar os casos da outra dupla.

- [ ] O ID e o título identificam o caso sem ambiguidade
- [ ] A pré-condição diz o que precisa estar pronto
- [ ] Os dados de entrada são exatos, com os valores usados
- [ ] Os passos são numerados e **repetíveis** por outra pessoa
- [ ] O resultado esperado foi escrito **antes** da execução
- [ ] O resultado esperado é **verificável** (dá para dizer sim ou não)
- [ ] O resultado obtido descreve o que aconteceu de fato
- [ ] O status é coerente com o esperado × obtido
- [ ] Há evidência quando o status é Reprovado

> [!question] Para refletir
>
> - Se o resultado esperado for escrito **depois** de ver o que o sistema fez, o teste ainda tem valor? Por quê?
> - Um caso **Reprovado** significa que o teste deu errado? Explique.

⬆️ Volte para [[uc3.01 - Plano de teste e testes manuais]].
