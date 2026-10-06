---
title: "Passo a Passo - Desafio Sistema Bancário em Python"
date: 2026-10-06
draft: false
description: "Atividade passo a passo para refatoração de um sistema bancário utilizando funções em Python."
aliases:
  - Passo a Passo Desafio Sistema Bancário
  - Exercício Sistema Bancário Funções
tags:
  - python
  - funcoes
  - exercicio
---

![[Desafio sistema bancario#Desafio]]

> [!info] Objetivo
> Refatorar e expandir um sistema bancário simples utilizando funções em Python, dividindo a lógica em pequenos blocos de responsabilidade, aplicando validações e uso correto de argumentos.

## Contexto

O desafio consiste em pegar um sistema bancário que antes rodava em um fluxo único e modularizar o código usando funções. Além disso, o sistema deve ser expandido para permitir a criação e associação de clientes (usuários) e suas respectivas contas bancárias (contas correntes).

- **Operações Básicas:** Depositar, sacar e exibir extrato.
- **Novas Entidades:** Cadastrar usuário (cliente) e cadastrar conta corrente vinculada a um usuário.

---

## Passo a Passo

### Passo 1: Separando as Operações Básicas em Funções

A primeira etapa consiste em organizar o fluxo principal, movendo as operações existentes de depósito, saque e extrato para dentro de funções específicas. O desafio impõe regras claras de como os argumentos devem ser recebidos em cada uma:

- `depositar`: Deve receber argumentos **apenas por posição** (`saldo`, `valor`, `extrato`) e retornar `saldo` e `extrato`.
- `sacar`: Deve receber argumentos **apenas por nome** (`saldo`, `valor`, `extrato`, `limite`, `numero_saques`, `limite_saques`) e retornar `saldo` e `extrato`.
- `exibir_extrato`: Recebe `saldo` por posição e `extrato` por nome.

```python
# Utilização de barras (/) e asteriscos (*) para definir tipos de argumentos
def depositar(saldo, valor, extrato, /):
    # Lógica de depósito com atualizações de saldo e extrato
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Lógica de saque e validações (saldo, limite, número de saques diários)
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    # Exibição do extrato e formatação
    pass
```

### Passo 2: Filtrando e Criando Usuários

Agora vamos criar a funcionalidade para cadastrar clientes. Cada cliente será um dicionário contendo nome, data de nascimento, CPF (apenas números) e endereço completo, e ficará armazenado em uma lista de usuários.

> [!warning] Validação de CPF
> Não podem existir dois clientes com o mesmo CPF! Antes de cadastrar um novo usuário, é vital checar se aquele CPF já existe na lista. Criar uma função dedicada de `filtrar_usuario` facilita não apenas essa etapa, mas também na hora de criar contas depois.

```python
def filtrar_usuario(cpf, usuarios):
    # Usando list comprehension para buscar o CPF na lista
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return # Interrompe o fluxo e volta ao menu
        
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    
    # Adicionando na lista de usuários recebida por parâmetro
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")
```

### Passo 3: Criando as Contas Correntes

Uma conta corrente deve sempre pertencer a um usuário. Portanto, a conta será um dicionário contendo a `agencia` (fixada em `"0001"`), o `numero_conta` (sequencial iniciando em 1) e o próprio `usuario`.

> [!tip] Número Sequencial Simples
> Como nesse desafio as contas não podem ser excluídas, o número da próxima conta pode ser descoberto calculando o tamanho da nossa lista atual de contas e somando 1: `len(contas) + 1`.

```python
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios) # Reaproveitamos a função!
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Retorna o dicionário da conta, que depois sofrerá um .append() na lista principal
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("\n@@@ Usuário não encontrado! Fluxo de criação de conta encerrado. @@@")
    return None
```

### Passo 4: Listando Contas e Loop Principal

Para finalizar e testar as novidades, precisamos de uma função para visualizar as contas cadastradas de forma estruturada. Todo esse sistema é executado através de uma função `main()`, que gerencia um loop infinito (o menu de opções) e armazena as listas mestres de usuários e de contas.

```python
def listar_contas(contas):
    for conta in contas:
        # Formatação de string em múltiplas linhas
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)

def main():
    # Inicialização das variáveis mestres (estado do sistema)
    usuarios = []
    contas = []
    # Loop de menu chamando as funções recém-criadas...
```
