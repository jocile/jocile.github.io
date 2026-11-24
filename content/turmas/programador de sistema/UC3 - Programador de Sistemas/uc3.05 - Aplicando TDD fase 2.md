---
quartz-properties: true
title: uc3.04 - Aplicando TDD fase 2
description: Desenvolvimento do Carrinho de Compras seguindo TDD com pytest e ciclo Red-Green-Refactor
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-16
uc: 3
aula: 5
---

> [!note] Exemplo prático de TDD com Carrinho de Compras
>
>>[!info] Quando precisamos testar a mesma funcionalidade com vários cenários diferentes (como diferentes listas de produtos no carrinho), escrever vários testes separados gera código duplicado. O `pytest` resolve isso com a ferramenta de **parametrização** (`@pytest.mark.parametrize`). 🧪
>> - Com ela, definimos uma lista de tuplas contendo os dados de entrada e o resultado esperado, e o `pytest` roda o teste para cada caso de forma isolada.
>
>> [!abstract] Contexto
>> Vamos construir um aplicativo **Carrinho de Compras** para praticar o TDD no dia a dia. Ao invés de apenas listar falhas, você vai interpretar os resultados, priorizar testes e descobrir quais funcionalidades precisam ser implementadas.

> [!todo] 🖥️ Atividades Testes parametrizados
> 
> Cronograma:  [[2. Testes parametrizados no app carrinho]]
>  
> - Aplique `@pytest.mark.parametrize` para testar múltiplos cenários de remoção (ex: remover Livro de um carrinho com dois itens → resultado 1 item).
> - Crie parâmetros no formato: `(itens_iniciais, item_remover, tamanho_esperado)`.
> - Execute o teste parametrizado para verificar se cada cenário resulta no comportamento esperado.
>
>> [!example]- Exemplo de teste parametrizado
>> ```python
>> @pytest.mark.parametrize(
>>     "itens_iniciais, item_remover, tamanho_esperado",
>>     [
>>         ([( "Livro", 45.0), ("Caneta", 5.0) ], "Livro", 1),
>>         ([( "Caderno", 15.0 )], "Caderno", 0),
>>     ]
>> )
>> def test_remover_varios_itens(itens_iniciais, item_remover, tamanho_esperado):
>>     carrinho = CarrinhoDeCompras()
>>     for nome, preco in itens_iniciais:
>>         carrinho.adicionar_item(nome, preco)
>>     carrinho.remover_item(item_remover)
>>     assert len(carrinho.itens) == tamanho_esperado
>> ```
>
> **Registrar e concluir**
> - Documente todos os testes desenvolvidos em uma pasta `tests/` com arquivo `test_carrinho.py`.
> - Crie documentação dos resultados em `docs/resultados-tdd.md` com: lista de funcionalidades implementadas, estrutura da classe `CarrinhoDeCompras`, e fluxo Red-Green-Refactor utilizado.
> - Faça o commit local do projeto com todas as alterações desenvolvidas.
>
>> [!question] Para refletir
>> - Qual foi o valor agregado de escrever testes *antes* do código em vez de depois?
>> - O ciclo Red-Green-Refactor preveniu problemas comuns durante a implementação?
>> - Por que testes parametrizados são mais eficientes que múltiplos testes separados?

⬅️ Aula anterior: [[uc3.04 - Aplicando TDD]] | ➡️ Próxima aula: [[uc3.06 - Executando testes e registrando defeitos]]

---
