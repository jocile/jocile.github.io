---
title: Sistema Bancário Com Poo
description: plataforma gratuita baseada em nuvem que permite aos usuários escrever
  e executar código Python diretamente em um navegador da web
date: '2026-09-26'
draft: false
tags:
- Python/POO
- programador/desafios
---

Criar o sistema bancário com orientação a objetos

## Objetivos

- O objetivo geral é iniciar A modelagem no sistema bancário em programação orientada a objetos e adicionar classes para cliente e as operações bancárias depósito e saque.
- O que precisamos fazer é atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
- O código deve seguir o modelo UML de classes a seguir:

![Diagrama de classes - Sistema bancário](diagrama-sistema-bancario.png)

## Classe conta

A classe conta deve ter:

- saldo;
- número;
- agência;
- cliente;
- e histórico;
- todos como atributos da classe e eles são privados (sinal de menos)
- 4 métodos:
	- saldo - não recebe nenhum argumento ele retorna float;
	- nova conta - é um método que cria uma conta (método de fábrica) então ele vai receber um cliente e o número da conta que pode ser um temporário, e tem retornar o objeto contra;
	- a operação de sacar - recebe um valor que é float e retorna um boleano;
	- e o depositar recebe um valor que é float e retorna boleano, para que se a operação aconteceu com sucesso ou falha retorna True se deu certo sacar, e caso se não depositar retorna falso, se deu errado e não depositar, por falso se deu errado também.

## Exemplo de implementação de conta

```python
"""
Esta classe representa um banco, com funcionalidades básicas de depósito e saque.
O saldo da conta é mantido internamente e pode ser acessado através da propriedade 'saldo'.
Caso o valor do saque seja maior que o saldo disponível, um aviso de erro é mostrado.
"""
from datetime import datetime

class Banco:
 def __init__(self):
 self._saldo = 0
 self._extrato = []
 
 @property
 def saldo(self):
 return self._saldo
 
 @property
 def extrato(self):
 return f'Extrato: {self._extrato}\n Saldo: {self._saldo}'

 def depositar(self, valor):
 self._saldo += valor
 self._extrato.append(
 {
 "tipo":'deposito',
 "valor": valor,
 "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
 }
 )
 print(f'Deposito de R$ {valor} realizado com sucesso!')

 def sacar(self, valor):
 if valor > self._saldo:
 print('Saldo insuficiente') 
 else:
 self._saldo -= valor
 self._extrato.append(
 {
 "tipo":'-saque--',
 "valor": valor,
 "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
 }
 )
 print(f'Saque de R$ {valor} realizado com sucesso!')

 def __str__(self):
 return f'Saldo: {self._saldo}'
 
 def mostrar_extrato(self):
 for item in self._extrato:
 print(f'{item["data"]}\t{item["tipo"]}\tR$ {item["valor"]}')
 print('=' * 20)
 print(f'Saldo: {self._saldo}')

def menu():
 menu = """\n
 ================ MENU ================
 [d]\tDepositar
 [s]\tSacar
 [e]\tExtrato
 [q]\tSair
 => """
 return input(menu)

def main():
 cliente = Banco()
 while True:
 opcao = menu()
 if opcao == 'd':
 valor = int(input('Digite o valor: '))
 cliente.depositar(valor)
 elif opcao == 's':
 valor = int(input('Digite o valor: '))
 cliente.sacar(valor)
 elif opcao == 'e':
 cliente.mostrar_extrato()
 elif opcao == 'q':
 break

if __name__ == '__main__':
 print('Bem-vindo ao Banco App')
 print('=' * 20) 
 main()
```

### Conta corrente com herança

A Conta ela tem uma classe filha, então aqui a conta corrente estende a conta porque é uma classe do tipo conta, então ela tem tudo que a conta tem mais dois atributos que seriam: o limite e o limite de saques.

### Atributo Histórico

Ainda continuando na conta temos o histórico, ele é um tipo de classe e essa classe é histórica, então uma conta tem um histórico, que pertence a uma conta.

#### Interface Transação

- O histórico tem um método que é adicionar transação, ele também tem um argumento que são as transações, onde se depositando transações, que é do tipo transação, esta é uma interface, onde essa interface que seria a classe abstrata. 
- Aclasse abstrata Interface, é uma classe pai, então ela tem um método registrar que recebe uma conta, assim também temos duas classes que implementam essa interface.
- As classe que implementam a abstrata da transação são: uma de depósito e a outra é a de saque, ambas tem os atributos do valor e consequentemente a implementação do método registrar.

## Classe cliente

A classe cliente tem:

- endereço;
- e tem uma lista de contas - que é do tipo conta;
- 2 operações:
	- o primeiro é realizar transação - ele recebe dois atributos, que seria uma conta e a transação, onde a conta é do tipo conta e a transação é do tipo aqui da classe que estava na transação, então pode ser um saque, passar um depósito, mas a gente vai olhar ai para saber se temos um **polimorfismo**.
	- Adicionar conta - lembrando que o meu cliente pode ter várias contas, e com várias contas onde a conta é relacionada a um cliente e temos uma **generalização**. 

### Pessoa física

A classe pessoa física e é um tipo de cliente, ela tem:

- CPF;
- nome;
- data de nascimento.

## Fase seguir

> [!NOTE] Implementar a interface gráfica 

> [!NOTE] Salvar os dados em um arquivo txt.
