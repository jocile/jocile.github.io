---
title: Solicita e armazena o nome do titular da conta bancária digitado pelo usuário
description: 'Para ler e escrever dados em Python, utilizamos as seguintes funções:'
date: '2026-10-05'
draft: false
tags:
- programador/desafios
---

Para ler e escrever dados em Python, utilizamos as seguintes funções:
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.

## Descrição

Implemente uma classe chamada ContaBancaria para representar uma conta bancária simples. Essa classe deve permitir que você realize as operações básicas de uma conta: depósito, saque e consulta de saldo. O saldo negativo.

## Requisitos

A classe ContaBancaria deve ter:

Atributos:
- titular (nome do dono da conta).
- saldo (saldo inicial, que começa com 0 por padrão).

Métodos:
- depositar(valor): adiciona o valor informado ao saldo.
- sacar(valor): subtrai o valor informado do saldo, se houver saldo suficiente. Caso contrário, exiba a mensagem "Saque não permitido".
- saldo_atual(): retorna o saldo atual da conta.

## Entrada

1. Nome do titular (string).
2. Sequência de valores representando operações de depósito e saque:

- Valores positivos representam depósitos.
- Valores negativos representam saques.

## Saída

Exiba as operações realizadas e o saldo final no formato:  "Operações: +500, -200; Saldo: 300"

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada|Saída|
|---|---|
|Maria  <br>100, -50, 200, -300|Operações: +100, -50, +200, Saque não permitido; Saldo: 250|
|Carlos  <br>1000, -500, -600|Operações: +1000, -500, Saque não permitido; Saldo: 500|
|Ana  <br>0, 100|Operações: 0, +100; Saldo: 100|

%%
```python
class ContaBancaria:
    """
    Inicializa uma nova conta bancária com o nome do titular.
    Configura o saldo inicial como zero e prepara uma lista para registrar as operações.
    Args:
        titular (str): Nome do titular da conta bancária.
    """

    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def depositar(self, valor):
        # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
        self.saldo += valor
        if valor == 0:
            self.operacoes.append("0")
        else:
            self.operacoes.append(f"+{valor}")

    # TODO: Implemente o método para realizar um saque:
    def sacar(self, valor):
        # TODO: Verifique se há saldo suficiente para o saque
        # valor já é negativo, então usamos abs() para comparar
        if self.saldo >= abs(valor):
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            self.saldo += valor  # valor já é negativo, então somamos
            self.operacoes.append(str(valor))
        else:
            # TODO: Registre a operação e retorne a mensagem de saque negado
            self.operacoes.append("Saque não permitido")

    def saldo_atual(self):
        return self.saldo

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    def extrato(self):
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")


nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()
```

## Explicação da implementação

1. **`__init__`**: Inicializa a conta com o titular, saldo zero e uma lista vazia para armazenar as operações.    
2. **`depositar`**: Adiciona o valor ao saldo e registra a operação. Para valores positivos, adiciona o sinal "+", e para zero, registra apenas "0".    
3. **`sacar`**: Verifica se há saldo suficiente antes de realizar o saque. Se houver, subtrai o valor (que já vem negativo) e registra a operação. Caso contrário, registra "Saque não permitido".    
4. **`saldo_atual`**: Retorna o saldo atual da conta.    
5. **`extrato`**: Formata e exibe todas as operações realizadas junto com o saldo final.

Esta implementação atende a todos os requisitos do desafio e produzirá as saídas esperadas para os exemplos fornecidos.
%%
