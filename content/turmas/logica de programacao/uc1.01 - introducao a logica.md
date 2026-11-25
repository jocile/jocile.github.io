---
title: uc1.01 - introdução à lógica de programação
description: Algoritmos, variáveis, constantes, tipos primitivos e introdução a Python
tags:
  - logica/aulas/uc1
  - senac
date: 2026-11-26
uc: 1
aula: 1
---

## 🎯 Contexto: Caixa da Cantina

A cantina da escola está informatizando o caixa. Antes de programar, a equipe precisa descrever, passo a passo e sem ambiguidades, como o caixa calcula o total de um pedido, aplica desconto e devolve o troco. **Quem escreve as instruções sem pensar em todos os casos descobre o erro só quando o caixa já está em uso.**

Esta situação de aprendizagem inicia com uma abordagem ativa: os alunos simulam a escrita de instruções para um robô antes de conhecer Python, tornando explicitos seus erros e falhas.

## 📝 Descrição da Aula

### 1ª Ação (20 min) - O Robô do Caixa

Programar um **robô** e escrever as instruções para que o robô calcule o total de um pedido da cantina:

- Receber: nome do cliente, itens comprados, quantidades, preços
- Calcular: soma dos itens
- Aplicar desconto (10% se compra acima de R$ 50,00)
- Calcular troco (se pagamento > total)

O **robô executa exatamente o que está escrito, sem interpretar** — assim como um computador ou Python. Se a instrução for ambígua, incompleta ou estiver na ordem errada, o robô "falha".

### 2ª Reflexão

Perguntas-guia que ativam o raciocínio crítico:

- **Onde a instrução falhou?** Que erro o robô apresentou?
- **Que informação faltava para calcular corretamente?**
- **Em que ordem os passos precisam acontecer?**
- **Que dados o caixa precisa receber e o que deve devolver?**

A partir das respostas vamos sistematizar:

1. O que é um **algoritmo**
2. Conceitos de **variável** e **constante**
3. Tipos primitivos (inteiro, real)
4. Operadores aritméticos básicos (+, -, *, /)

### 3ª Ação - Blocos Lógicos no Code.org

Explorar desafios em blocos (Code.org, Blockly Games, Scratch), sempre **prevendo a saída antes de executar**:

- Simular entrada, atribuição e saída com blocos
- Identificar falhas nas instruções escritas anteriormente
- Comparar o que sabem de blocos com o conceito de algoritmo

### 4ª Ação - Meu Primeiro Programa em Python

Individualmente no **Google Colab**, vamos criar um programa que:

1. Receba **nome** e **idade** do cliente como entrada
2. Exiba uma frase de saída: `f"{nome} tem {idade} anos"`

### 5ª Reflexão  - Reescrevendo o Caixa em Pseudocódigo

As duplas reescrevem as instruções do caixa da cantina em **pseudocódigo** ou **fluxograma**, sistematizando os erros encontrados:

- Entrada de dados
- Cálculo com operadores
- Condição para desconto
- Saída de total e troco

> [!tip] Atenção à qualidade
> Cada instrução deve ser única, não ambígua e executável sem interpretação.

## 🛠️ Atividades Digitais

### ODA 1: Blocos Lógicos (Code.org)

**Objetivo**: Prever saída antes de executar

- Code.org: [[Aprendendo Lógica com blocos]]
- Blockly Games
- Scratch

> [!tip] Dica prática
> Use o modo "teste de mesa": escreva em papel como seria a sequência de instruções, execute e compare.

### ODA 2: Slides "Variáveis e Constantes"

**Objetivo**: Entender diferença entre variável e constante

- [Variáveis e constantes - Google Slides](https://docs.google.com/presentation/d/19obsTYpucf1e19y6CGrdZi4Ml6RfLVnRiSC7rXiFRpE/edit?usp=sharing)

### ODA 3: Python com Colab

**Objetivo**: Entrar no ambiente de programação Python

- [Python com Colab](https://colab.research.google.com/notebooks/supervised-learning-with-python.ipynb) (se existente)
- Notebook "Meu primeiro programa em Python"

## 📚 Objetivos de Aprendizagem (ODAs)

| ODA | Título | Link |
| ----- | -------- | ------ |
| 1 | Blocos Lógicos | Code.org, Blockly, Scratch |
| 2 | Variáveis e Constantes | Slides - Google |
| 3 | Python no Colab | Meu primeiro programa |

## 🔗 Navegação

### Anterior: Introdução ao curso

- [[turmas/logica de programacao/index|Conhecendo a Lógica de programação]]
- [[Formacao em Logica|Formação em Lógica]]
- [[Introducao aos algoritmos]]

### Próxima: Expressões aritméticas e lógicas

- [[uc1.02 - expressoes aritmeticas e logicas.md|Aula 2: Expressões aritméticas e lógicas]]

---

>[!note] Referências adicionais
>
> - **Desafios**: Code.org Blockly, Python Colab notebooks
