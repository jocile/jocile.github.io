---
title: 'Implementação da classe SistemaBancario:'
description: Implemente um sistema que gerencie várias contas bancárias. Cada conta
  será representada como uma instância da classe ContaBancaria criada no desafio…
date: '2026-09-26'
draft: false
tags:
- programador/desafios
---

## Descrição

Implemente um sistema que gerencie várias contas bancárias. Cada conta será representada como uma instância da classe `ContaBancaria` criada no desafio anterior. O sistema deve permitir que você crie contas para diferentes titulares e liste todas as contas cadastradas ao final da execução.

#### **Requisitos**

- O sistema deve permitir:
    - **Criar contas**:  Ao criar uma conta, forneça o nome do titular e o saldo inicial no formato `"Titular, SaldoInicial"`.
    - **Listar contas**:  Ao digitar o comando especial `"FIM"`, o sistema deverá listar todas as contas cadastradas no formato especificado.

## Entrada

O sistema deve permitir:

- Criação de contas no formato: `"Titular, SaldoInicial"`.
- Um comando especial `"FIM"` será usado para encerrar o processo de entrada e listar as contas.

## Saída

Liste todas as contas cadastradas no formato: `"Titular: X, Saldo: R$ Y"`

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                 | Saída                                           |
| ------------------------------------------------------- | ----------------------------------------------- |
| João, 500  <br>Maria, 1000  <br>FIM                     | João: R$ 500, Maria: R$ 1000                    |
| Ana, 150  <br>Bruno, 250  <br>FIM                       | Ana: R$ 150, Bruno: R$ 250                      |
| Fernando, 50  <br>Gustavo, 75  <br>Helena, 125  <br>FIM | Fernando: R$ 50, Gustavo: R$ 75, Helena: R$ 125 |


```python

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


class SistemaBancario:
    # Inicializa a lista de contas:
    def __init__(self):
        self.contas = []

    # Cria uma nova conta e adiciona à lista de contas:
    def criar_conta(self, titular, saldo):
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)

    # Lista todas as contas no formato "Titular: X, Saldo: R$ Y":
    def listar_contas(self):
        resultado = []
        for conta in self.contas:
            resultado.append(f"{conta.titular}: R$ {conta.saldo}")
        print(", ".join(resultado))


# Cria uma instância de SistemaBancario:
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()

```

## Explicação da implementação

1. **Classe SistemaBancario**:
    
    - `__init__()`: Inicializa uma lista vazia para armazenar as contas
    - `criar_conta()`: Cria uma nova instância de ContaBancaria e adiciona à lista
    - `listar_contas()`: Percorre todas as contas e imprime no formato solicitado
2. **Instância do sistema**: Criamos `sistema = SistemaBancario()` antes do loop    
3. **Loop principal**: Já estava implementado, lê as entradas até encontrar "FIM"    
4. **Formato de saída**: "Titular: Saldo, " conforme especificado    
5. **Método `listar_contas()`**:    
    - Cria uma lista com todas as contas formatadas
    - Usa `", ".join()` para juntar todas as contas em uma única linha separadas por vírgula e espaço
    - Formato de cada conta: "Titular: R$ Saldo"
6. **Saída**: Agora todas as contas são exibidas em uma única linha, conforme mostrado na tabela de exemplos.

O sistema agora pode criar múltiplas contas bancárias e listá-las todas ao final da execução quando o usuário digitar "FIM".
