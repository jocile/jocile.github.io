---
quartz-properties: true
title: uc2.17 - ### Consolidando o CRUD na Interface Web
description: prática passo a passo de como agrupar informações
tags:
  - programador-sistemas/aulas/uc2
date: 2026-11-04
uc: 2
aula: 17
---

> [!note] Criando Relatórios em gráficos
>
> Gráficos de barras horizontais são ideais para rankings: os nomes dos produtos ficam legíveis, sem rotação, e a comparação entre quantidades é imediata.
> [Matplotlib Tutorial](https://www.w3schools.com/python/matplotlib_intro.asp)

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
>> | 📗 **produtos** | Qual o ranking de vendas de produtos? |
>> | 📗 **vendas** | Quais os produtos mais vendidos? |
>
>> [!abstract] O que você vai construir
>> Um sistema de **Gestão de Produtos e Categorias** com banco SQLite, controle de estoque, análise de vendas, gráfico, API JSON, relatório em HTML e acesso restrito por usuário e senha.
>>
>> - [[produtos-00-roteiro|Gestão de Produtos: roteiro da atividade]]
>> - [[produtos-04-api-bottle]] - Você vai criar uma aplicação com o micro-framework **Bottle** que oferece duas formas de consultar o ranking de vendas: uma **API JSON** (para outros sistemas) e uma **página HTML** com tabela e gráfico (para pessoas).

![[solucao dos exercicios da uc2#Produtos 04]]

⬅️ Aula anterior: [[uc2.16 - Analise de dados com graficos]] | ➡️ Próxima aula: [[uc2.18 - Gestao de Dados Acessos e Permissoes]]
