---
quartz-properties: true
title: uc2.14 - Análise de dados com transações
description: prática passo a passo de como agrupar informações
tags:
  - programador-sistemas/aulas/uc2
date: 2026-10-29
uc: 2
aula: 15
---

> [!note] Criando segurança de estruturas de dados com transações
>
> Uma **transação em banco de dados** ==é uma unidade de trabalho que agrupa várias operações SQL para que elas funcionem sob a regra do "tudo ou nada"==. No **SQLite**, as transações garantem que os dados permaneçam consistentes, seguros e que o banco de dados cumpra as propriedades **ACID** (Atomicidade, Consistência, Isolamento e Durabilidade), mesmo que ocorra uma queda de energia ou erro no código no meio do processo. [[1](https://coddy.tech/docs/pt/sqlite/transactions), [2](https://translate.google.com/translate?u=https://www.geeksforgeeks.org/sqlite/sqlite-transaction/&hl=pt&sl=en&tl=pt&client=sge), [3](https://www.usinadepesquisa.com/?p=7659)]

> [!todo] 🖥️ Atividades
>
>>[!done]  Descrição da atividade
>>
>> - Você vai trabalhar como *analista de dados de uma empresa* e executar todas as operações de escrita e manipulação de dados de forma segura e responde a perguntas de análise sobre o estoque.
>> - Esta sequência de atividades parte de um banco de dados vazio e termina em uma aplicação web protegida por login. Cada nota depende da anterior e entrega algo que será reaproveitado na próxima.
>> - Agora vamos registrar a venda e baixar o estoque, mas são duas operações que precisam acontecer **juntas**. Se apenas uma delas fosse gravada, o banco ficaria inconsistente: estoque reduzido sem venda registrada, ou venda registrada sem baixa.
>
>>[!question]  Questões
>>
>> | Estoque | Pergunta |
>> | --- | --- |
>> | 📒 **categorias** | - |
>> | 📗 **produtos** | O que deve acontecer se faltar estoque para uma venda? |
>> | 📗 **vendas** | Em qual ordem devem acontecer o registro da venda e a baixa do estoque? |
>
>> [!abstract] O que você vai construir
>> Um sistema de **Gestão de Produtos e Categorias** com banco SQLite, controle de estoque, análise de vendas, gráfico, API JSON, relatório em HTML e acesso restrito por usuário e senha.
>>
>> - [[produtos-00-roteiro|Gestão de Produtos: roteiro da atividade]]
>> - [[produtos-02-vendas-estoque]] - Nesta atividade você registra **vendas**, dá baixa no estoque de forma segura e descobre qual produto é o campeão de vendas.

⬅️ Aula anterior: [[uc2.14 - Analise de dados]] | ➡️ Próxima aula: ✨em edição!
