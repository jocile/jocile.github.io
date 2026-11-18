---
title: Modelo de tabela de resultados de teste
description: Modelo e exemplo para registrar os resultados dos casos de teste manuais e automatizados de uma versão do sistema
date: 2026-11-16
draft: false
tags:
  - testes/modelo
  - documentacao
---

A tabela de resultados responde: **o que foi executado, em qual versão, e o que aconteceu**. Sem ela, ninguém consegue comparar duas versões do sistema.

⬆️ [[uc3.06 - Executando testes e registrando defeitos]]

## Modelo para `docs/resultados-de-teste.md`

```markdown
# Resultados de teste: Sistema Gestão de Produtos

- **Versão testada:** 0.9
- **Ambiente:** local (sistema operacional, navegador, Python)
- **Data:** (data da execução)
- **Responsáveis:** (nomes da dupla)

## 1. Casos manuais

| Caso | Título | Resultado esperado | Resultado obtido | Status | Evidência |
| --- | --- | --- | --- | --- | --- |
| CT01 | | | | | |

## 2. Testes automatizados

| Arquivo | Total | Passaram | Falharam |
| --- | --- | --- | --- |
| tests/test_validacao.py | | | |

### Testes que falharam

| Teste | Mensagem resumida do pytest | Evidência |
| --- | --- | --- |
| | | |
```

> [!note] Cada linha tem versão e data
> Quando a versão mudar (na Aula 6, depois das correções), você acrescentará **uma nova execução** abaixo da anterior. Por isso a versão e a data aparecem no cabeçalho de cada execução, e a execução antiga **não é apagada**.

## Exemplo preenchido (de outro caso)

> [!example] Lista de produtos
>
> | Caso | Título | Resultado esperado | Resultado obtido | Status | Evidência |
> | --- | --- | --- | --- | --- | --- |
> | CT00 | Lista exibe os produtos cadastrados | Tabela com ID, nome, categoria, preço e estoque de cada produto | Tabela exibiu os 5 produtos com todas as colunas | Aprovado | `evidencias/ct00.png` |
>
> **Teste automatizado que falhou:**
>
> | Teste | Mensagem resumida | Evidência |
> | --- | --- | --- |
> | `test_exemplo_total_da_lista` | `assert 4 == 5` (a lista devolveu 4 produtos em vez de 5) | `evidencias/pytest-exemplo.txt` |

## Como preencher bem

| Campo | Mau exemplo | Bom exemplo |
| --- | --- | --- |
| Resultado obtido | "Deu erro" | "Formulário reexibido com a mensagem X no topo; nenhuma mensagem junto do campo preço" |
| Mensagem do pytest | Colar 40 linhas | Uma linha com a comparação (`assert ... == ...`) e o nome do teste |
| Status | "Mais ou menos" | **Aprovado** ou **Reprovado** |
| Evidência | "Está na minha máquina" | Caminho de um arquivo dentro do repositório |

## Lista de verificação

- [ ] Versão, ambiente, data e responsáveis no cabeçalho
- [ ] Todos os casos manuais (CT01 a CT06) aparecem, aprovados ou não
- [ ] Cada arquivo de teste automatizado tem total, aprovados e falhas
- [ ] Cada teste que falhou aparece com a mensagem resumida
- [ ] O resultado obtido descreve **o que aconteceu**, não só "funcionou" ou "falhou"
- [ ] Toda linha Reprovada tem evidência

⬆️ Volte para [[uc3.06 - Executando testes e registrando defeitos]].
