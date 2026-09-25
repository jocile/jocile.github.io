---
title: "Atividade Prática: Manipulação de Funções em Python"
date: 2026-09-24
tags: [atividade, python, funcoes]
---

# Atividade Prática: Manipulação de Funções em Python

## Objetivo
Aplicar os conceitos aprendidos na aula sobre [[Funcoes em Python]], exercitando a definição de funções, uso de diferentes tipos de parâmetros, escopo e documentação.

## Cenário
Você está desenvolvendo um pequeno sistema para gerenciar uma biblioteca. Sua tarefa é criar funções que ajudem a organizar o acervo e o atendimento aos usuários.

## Tarefas

### 1. Cadastro de Livro (Parâmetros Padrão)
Crie uma função chamada `cadastrar_livro` que receba `titulo`, `autor` e `disponivel` (com valor padrão `True`). A função deve retornar uma string formatada com os dados do livro.

### 2. Listagem de Livros (*args)
Crie uma função chamada `listar_livros` que receba um número variável de títulos de livros e imprima cada um deles em uma linha.

### 3. Atualização de Dados (**kwargs)
Crie uma função chamada `atualizar_detalhes` que receba o título de um livro e um número variável de argumentos nomeados (ex: `ano`, `editora`, `genero`) para atualizar as informações extras do livro. A função deve imprimir as novas informações.

### 4. Documentação (Docstrings)
Escolha uma das funções acima e adicione uma *docstring* seguindo o padrão de documentação Python, descrevendo o objetivo, os parâmetros e o que a função retorna.

### 5. Escopo de Variáveis
Crie uma função que tente modificar uma variável definida fora da função (escopo global) e observe o que acontece. Documente o resultado em um comentário no código.

## Entregáveis
- Um arquivo `.py` contendo todas as funções desenvolvidas.
- Comentários explicativos sobre cada tarefa.

---
> [!NOTE]
> Consulte o guia de estudos [[Funcoes em Python]] sempre que tiver dúvidas sobre a sintaxe ou sobre como utilizar os diferentes tipos de parâmetros.
