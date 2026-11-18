---
quartz-properties: true
title: uc3.04 - Aplicando TDD
description: Desenvolvimento do Carrinho de Compras seguindo TDD com pytest e ciclo Red-Green-Refactor
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-17
uc: 3
aula: 4
---

> [!note] Exemplo prático de TDD com Carrinho de Compras
>
>>[!info] O TDD (Test-Driven Development) é uma abordagem de desenvolvimento de software onde escrevemos os testes automáticos *antes* do código de produção, seguindo o ciclo Red-Green-Refactor.
>> 🔴 **O ciclo Red-Green-Refactor:** Entender a teoria básica, a lógica por trás de escrever um teste que falha e como o código evolui a partir disso.
>> 🐍 **O ecossistema em Python:** Conhecer as ferramentas mais usadas, como o `pytest`, e ver como estruturar o ambiente de testes.
>> 🛠️ **Um exemplo prático do zero:** Construir um Carrinho de Compras passo a passo aplicando TDD imediatamente.
>
>> [!abstract] Contexto
>> Vamos construir um aplicativo **Carrinho de Compras** para praticar o TDD no dia a dia. Ao invés de apenas listar falhas, você vai interpretar os resultados, priorizar testes e descobrir quais funcionalidades precisam ser implementadas.

> [!todo] 🖥️ Atividades
> 
> Cronograma: [[1. Aplicando TDD com app carrinho de compras]]
>
> **1. Estruturar ambiente de testes**
> - Crie um ambiente virtual (`.venv`) no seu projeto usando `python -m venv .venv`.
> - Ative o ambiente virtual (`source venv/bin/activate` ou `venv\Scripts\activate.bat`).
> - Instale o framework de testes com `pip install pytest`.
> - Execute os testes com `pytest` para validar cada funcionalidade.
>
>> [!question] Verificação do ambiente
>> - O nome `(venv)` deve aparecer no terminal quando ativado.
> - Execute `pytest` e verifique se ele identifica arquivos `test_*.py` e funções que começam com `test_`.
>
> **2. Desenvolver o Carrinho de Compras**
>
> >> [!abstract] Objetivo geral
>> Criar a classe `CarrinhoDeCompras` com as funcionalidades: iniciar vazio, adicionar item, remover item, calcular total e atualizar preço. Cada funcionalidade será desenvolvida através do ciclo TDD.
>
> **Passo 2.1 - Carrinho inicia vazio**
> - Escreva o teste `test_carrinho_deve_iniciar_vazio()` que verifica se `len(carrinho.itens) == 0` após criar uma nova instância.
> - Implemente o construtor `__init__(self)` para inicializar a lista de itens vazia.
>
> **Passo 2.2 - Adicionar item ao carrinho**
> - Escreva o teste `test_deve_adicionar_item_ao_carrinho()` que adiciona um produto (ex: "Livro", 45.0) e verifica se a lista passa a conter esse elemento (`len(carrinho.itens) == 1`).
> - Implemente o método `adicionar_item(self, nome, preco)` que armazena o item no formato dicionário `{ "nome": nome, "preco": preco }`.
>
> **Passo 2.3 - Calcular preço total**
> - Escreva o teste `test_deve_calcular_preco_total_do_carrinho()` que adiciona itens e verifica se a soma está correta (ex: Livro 45.0 + Caneta 5.0 = 50.0).
> - Implemente o método `calcular_total(self)` percorrendo `self.itens` e somando os preços.
> - **Refatoração:** Melhore a implementação usando a função `sum()` e compreensão de lista: `return sum(item["preco"] for item in self.itens)`.
> - Escreva o teste `test_carrinho_vazio_deve_retornar_total_zero()` para garantir que carrinho vazio retorne 0.0.
>
>> [!question] Refatoração com sum()
>> Qual é a vantagem de usar `sum(item["preco"] for item in self.itens)` em comparação com um laço for tradicional?
>
> **Passo 2.4 - Remover itens do carrinho**
> - Escreva o teste `test_deve_remover_item_do_carrinho()` que adiciona um item e remove-o para verificar se a lista volta ao tamanho zero.
> - Implemente o método `remover_item(self, nome)` usando compreensão de lista: `self.itens = [item for item in self.itens if item["nome"] != nome]`.
> - **Prevenção de erros:** Escreva o teste `test_nao_deve_remover_item_inexistente()` usando `with pytest.raises(ValueError)`.
> - Implemente a validação no método `remover_item` usando `any()`: `if not any(item["nome"] == nome for item in self.itens): raise ValueError(...)`.
>
>> [!warning] Não use .remove() em laço for
>> Alterar o tamanho de uma lista enquanto o Python percorre ela faz com que alguns elementos sejam pulados. Evite `.remove()` dentro de laços for na mesma lista.
>
> **Passo 2.5 - Atualizar preço de item**
> - Escreva o teste `test_deve_atualizar_preco_do_item()` que altera o preço de um produto (ex: Livro 45.0 → 50.0) e verifica a atualização correta.
> - Implemente o método `atualizar_preco(self, nome, novo_preco)` com validação usando `any()`.
> - Escreva o teste `test_deve_retornar_mensagem_ao_atualizar_preco_inexistente()` usando `pytest.raises(ValueError) as exc_info` para validar a mensagem de erro.
>
>> [!info] Validação com pytest.raises
>> Para capturar e verificar a mensagem da exceção:
>> ```python
>> with pytest.raises(ValueError) as exc_info:
>>     carrinho.atualizar_preco("Item Inexistente", 50.0)
>> assert "não encontrado" in str(exc_info.value)
>> ```

>[!done] Resolução de testes automatizados com pytest
>
> - [GitHub - profjocile/TDD-carrinho-de-compras · GitHub](https://github.com/profjocile/TDD-carrinho-de-compras)

⬅️ Aula anterior: [[uc3.03 - Testes de integracao com fixtures]] | ➡️ Próxima aula: [[uc3.05 - Aplicando TDD fase 2]]
