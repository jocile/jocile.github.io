---
title: Cadastro De Alunos Com Tdd
description: 'Desafio: Definir os requisitos iniciais e casos de uso para os sistemas
  de cadastro de alunos.'
date: '2026-09-26'
draft: false
---

**Desafio**: Definir os requisitos iniciais e casos de uso para os sistemas de cadastro de alunos.

**Objetivo**: Estruturar projetos de forma clara e compreensível, assegurando que todos os envolvidos entendam o escopo e os objetivos iniciais. 

---

**Atividade**:
1. **Definição de Requisitos**:
   - Identificar as funcionalidades essenciais do sistema de cadastro de alunos (ex.: adicionar, editar, remover alunos; visualizar lista de alunos).
   - Identificar as funcionalidades essenciais do sistema de movimentação bancária (ex.: depósitos, saques, transferências, consulta de saldo).
   - Documentar os requisitos funcionais e não funcionais para ambos os sistemas.

---

1. **Elaboração de Casos de Uso**:
   - Criar casos de uso detalhados para cada funcionalidade identificada.
   - Incluir cenários principais e alternativos, descrevendo claramente as interações entre o usuário e o sistema.

---

**Exemplo de Caso de Uso para Sistema de Cadastro de Alunos**:

- **Título**: Adicionar Novo Aluno
- **Descrição**: Permite ao usuário adicionar um novo aluno ao sistema.
- **Ator Principal**: Administrador do Sistema
- **Pré-condições**: O usuário deve estar autenticado no sistema.

---

- **Fluxo Principal**:
  1. O usuário seleciona a opção "Adicionar Novo Aluno".
  2. O sistema solicita as informações do aluno (nome, idade, matrícula, curso).
  3. O usuário insere as informações e confirma.
  4. O sistema valida as informações e adiciona o novo aluno no banco de dados.
  5. O sistema confirma a adição do aluno e exibe os detalhes inseridos.

---

- **Fluxos Alternativos**:
  - Caso as informações inseridas sejam inválidas, o sistema exibe uma mensagem de erro e solicita a correção dos dados.
