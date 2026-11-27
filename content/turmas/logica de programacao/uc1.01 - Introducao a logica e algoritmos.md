---
title: uc1.01 - Introdução à lógica e aos algoritmos
date: 2026-11-26
draft: false
tags:
  - logica/aulas/uc1
  - algoritmos
  - senac
description: "Primeira aula de Lógica de Programação: desafios no Code.org, variáveis, constantes e primeiros programas em Python."
uc: 1
aula: 1
---

> [!abstract] Resumo da aula
> Na primeira aula, a turma se apresentou, conheceu os cursos e as oportunidades de vagas do Senac e experimentou a lógica passo a passo no Code.org. Em seguida, aprendemos o que é um algoritmo, escrevemos um exemplo com pastas e arquivos e o transformamos em um programa: um script `.bat` com comandos do PowerShell.

%%

## Apresentação da turma

Cada aluno se apresentou e contou qual era sua experiência anterior com programação. A quase totalidade da turma não tinha nenhuma, e isso é o ponto de partida do curso: não é preciso saber programar para começar.

## Cursos e oportunidades no Senac

Foi apresentada a lista de cursos disponíveis no Senac e as oportunidades de vagas, para situar onde a lógica de programação se encaixa nas trilhas de formação e no mercado de trabalho.

%%

## Pensando em instruções: Code.org

Os alunos acessaram o site [Code.org](https://studio.code.org/br/courses/pre-express-2025/units/1?lang=pt-BR) e resolveram desafios de lógica, como programar o movimento de um personagem de um ponto a outro. A tarefa exige **planejar** a sequência de instruções antes de executar e **conferir** se o resultado foi o esperado, a mesma atitude de quem escreve um programa. Mais sugestões de plataformas em [[Aprendendo Lógica com blocos]].

## O que é um algoritmo

Um **algoritmo** é uma sequência finita e ordenada de passos que resolve um problema. Ele não depende de uma linguagem: pode ser escrito em português, desenhado ou programado. Mais em [[Introducao aos algoritmos]].

### Exemplo: organizar pastas e arquivos

Algoritmo construído em aula:

1. Criar uma pasta com o nome do aluno.
2. Dentro dela, criar 3 pastas.
3. Dentro dela, criar 3 arquivos de texto (`.txt`).
4. Copiar um dos arquivos para uma das pastas.
5. Mover outro arquivo para outra pasta.

> [!tip] Observação
> A **ordem** dos passos importa: não é possível copiar um arquivo para uma pasta que ainda não foi criada.

## Conceitos de apoio

> [!info] Pasta, arquivo e extensão
> - **Pasta** (ou diretório): local que organiza arquivos e outras pastas.
> - **Arquivo**: conjunto de dados guardado com um nome, como um texto, uma imagem ou um programa.
> - **Extensão**: parte do nome depois do ponto, que indica o tipo de arquivo. Por exemplo, `.txt` é texto simples e `.bat` é um script do Windows.
> - **Copiar** cria uma cópia e mantém o original no lugar. **Mover** tira o arquivo da origem e o coloca no destino.

## Do algoritmo ao programa: o script .bat

Para o computador executar o algoritmo, cada passo foi escrito como um comando em um script `.bat`, que roda os comandos do PowerShell em sequência. O algoritmo é o plano; o script é uma implementação dele.

Exemplo de script equivalente aos cinco passos:

```powershell
@echo off
chcp 65001 >nul

:: 1. Solicita e cria a pasta com o nome do aluno
set /p aluno="Digite o nome do aluno: "
mkdir "%aluno%"
cd "%aluno%"

:: 2. Cria as 3 pastas dentro da pasta do aluno
mkdir "Pasta 1" "Pasta 2" "Pasta 3"

:: 3. Cria os 3 arquivos de texto (.txt) dentro da pasta do aluno
echo Conteudo do arquivo 1 > "arquivo1.txt"
echo Conteudo do arquivo 2 > "arquivo2.txt"
echo Conteudo do arquivo 3 > "arquivo3.txt"

:: 4. Copia o arquivo1.txt para a Pasta 1
copy "arquivo1.txt" "Pasta 1\" >nul

:: 5. Move o arquivo2.txt para a Pasta 2
move "arquivo2.txt" "Pasta 2\" >nul

echo.
echo Estrutura criada com sucesso para o aluno "%aluno%"!
pause

```

### Salvar o código como `.bat`

1. Abra o **Bloco de Notas** e cole o script.
2. Clique em **Arquivo > Salvar como...** (ou pressione `Ctrl + Shift + S`).
3. Escolha onde quer salvar (por exemplo, na **Área de Trabalho**).
4. Em **Tipo**, mude de _Documentos de texto (_.txt)* para **Todos os arquivos (_._)**.
5. Em **Nome**, digite um nome terminando obrigatoriamente em `.bat` (ex: `criar_pastas.bat`).
6. No campo **Codificação** (ao lado do botão Salvar), deixe em **UTF-8** e clique em **Salvar**.

### Executar o script

1. Vá até o local onde salvou o arquivo (o ícone dele terá duas engrenagens).
2. Dê um **clique duplo** no arquivo.
3. Uma janela preta (Prompt de Comando) vai abrir pedindo: _"Digite o nome do aluno:"_.
4. Digite o nome desejado, aperte **Enter**, e as pastas e arquivos serão criados na mesma pasta onde o `.bat` está salvo.

## Para revisar

> [!question] Perguntas
> 1. O que é um algoritmo?
> 2. Qual a diferença entre copiar e mover um arquivo?
> 3. O que a extensão `.txt` indica? E `.bat`?
> 4. Por que a ordem dos passos importa no algoritmo das pastas?

## Próxima aula

A [[uc1.02 - Variaveis constantes e primeiros programas|Aula 2]] retoma o que ficou para depois: **variáveis e constantes** e os primeiros programas em **Python** no Google Colab (entrada, atribuição e saída), seguidos de **expressões aritméticas e lógicas**. Veja também [[Python com Colab]].
