---
title: Atividade Pratica Módulos Padrão
tags: [python, atividade, biblioteca-padrao]
---

Aprenda a aplicar os conceitos de módulos da biblioteca padrão Python em um script prático.

## Visão Geral

Esta atividade é projetada para colocar em prática o uso dos módulos `math`, `datetime`, `random`, `os` e `time`. Você criará um script que interage com o sistema, realiza cálculos e lida com aleatoriedade.

## Antes de Começar

- Certifique-se de ter o Python instalado em seu computador.
- Tenha lido a nota [[Modulos-Padrao-em-Python]].

## Passos

### Passo 1: Preparação
Crie um novo arquivo Python chamado `atividade_modulos.py` em seu ambiente de desenvolvimento.

### Passo 2: O Sorteador (Módulo `random`)
No topo do arquivo, importe o módulo `random`.
Crie uma lista com o nome de 5 colegas da turma.
Utilize `random.choice()` para sortear um nome e imprima-o na tela.

### Passo 3: O Calculador (Módulo `math`)
Importe o módulo `math`.
Solicite ao usuário um raio (número).
Calcule a área de um círculo (π * raio²) e imprima o resultado com duas casas decimais.

### Passo 4: O Relógio e o Sistema (Módulos `datetime`, `time`, `os`)
Importe os módulos `datetime`, `time` e `os`.
1. Imprima o diretório atual de trabalho (`os.getcwd()`).
2. Imprima a data e hora atuais (`datetime.datetime.now()`).
3. Faça o programa pausar por 3 segundos (`time.sleep(3)`).
4. Imprima uma mensagem informando que o programa foi finalizado.

### Passo 5: Exploração Livre (Função `dir()`)
No final do seu script, utilize a função `dir()` para listar todos os recursos disponíveis dentro do módulo `math` e imprima o resultado. Analise a saída no terminal.

## Verifique se Funcionou

Você saberá que teve sucesso quando o script executar todos os passos sequencialmente sem erros, exibindo as saídas esperadas no console.

## Desafio
Pesquise na documentação oficial do Python sobre o módulo `math` e descubra como calcular a raiz quadrada de um número. Adicione essa funcionalidade ao seu script.

## Próximos Passos

- [[Modulos-Padrao-em-Python]]
