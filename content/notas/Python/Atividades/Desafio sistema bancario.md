---
title: Desafio sistema bancário
date: 2026-09-25
draft: false
tags:
  - python
  - strings
  - exercicios
description: "Desafio de exercícios com Sistemas em Python."
---

Criar um sistema bancário com as operações:

- sacar, depositar e visualizar extrato;
- criar usuário e criar conta corrente.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.

Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Para segunda versão precisamos deixar o código modularizado com funções e introduzir novas funcionalidades: criar usuário do banco e criar conta corrente, que vincula com o usuário.

## Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45

## Fluxograma

![[Desafio-bancario-fluxograma.excalidraw]]

%%

## Exemplo de solução

```python
# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
menu = '''
Escolha:
  [d] depósitar
  [s] sacar
  [e] extrato
  [x] sair
'''
saldo = 0
limite_de_saque = 500
quantidade_de_saques = 3
while True:
    opcao = input(menu)
    if opcao == 'x': break
    # Depósito
    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: R$ '))
        if valor > 0 :
            saldo += valor  # equivale a saldo + valor
            print(f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
    # Saque
    if opcao == 's':
        valor = float(input('Digite o valor do saque: R$ '))
        if quantidade_de_saques > 0:
            if valor <= saldo:
                saldo -= valor
                print(f'Saque de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
            else:
                print(f'Infelizmente não será possível sacar o dinheiro por falta de saldo\nSaldo: R$ {saldo}')
        else:
            print(f'Infelizmente não será possível sacar o dinheiro por limite de saques')

# Extrato

```

%%
