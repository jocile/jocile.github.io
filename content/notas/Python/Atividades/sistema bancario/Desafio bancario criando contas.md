---
title: Criando contas bancárias
description: criação de contas bancárias utilizando funções e um menu interativo
date: '2026-09-26'
draft: false
tags:
- programador/desafios
---

Com base nos fundamentos de organização, **modularização** e controle de fluxo apresentados nas fontes, aqui está uma proposta de atividade prática voltada para a **criação de contas bancárias** utilizando **funções** e um **menu interativo**.

Esta atividade exercita a **decomposição de problemas** em sub-rotinas específicas e o gerenciamento de diferentes tipos de dados.

---

## Fase 1 Sistema de abertura de contas

### Atividade Prática: Sistema de Abertura de Contas Bancárias

**Objetivo:** Desenvolver um algoritmo que permita cadastrar três tipos de contas (Corrente, Poupança e Pessoa Jurídica) através de um menu, utilizando funções para isolar a lógica de criação de cada uma.

#### 1. Definição das Funções (Responsabilidades Isoladas)

Cada tipo de conta possui requisitos diferentes. O aluno deve criar funções específicas para capturar esses dados e retornar um resumo:

- **`criar_corrente(nome, saldo_inicial)`**: Recebe o nome e o valor de abertura, retornando uma confirmação.
- **`criar_poupanca(nome, saldo_inicial)`**: Além dos dados básicos, pode incluir a definição de uma data de aniversário da conta.
- **`criar_pj(nome_fantasia, cnpj, saldo_inicial)`**: Exige um parâmetro extra (**CNPJ**), demonstrando como funções podem lidar com diferentes quantidades de informações.


#### 2. Implementação do Menu e Controle de Fluxo

Para garantir que o programa seja interativo, deve-se utilizar uma estrutura de repetição **`while` (Enquanto)**, permitindo que o usuário realize várias operações sem que o sistema feche sozinho. Dentro do laço, uma estrutura **`if-elif-else`** direcionará a escolha do usuário para a função correta.

#### 3. Exemplo de Código Esperado (Python)

```python
# Funções para processar cada tipo de conta (Sub-rotinas)
def criar_corrente(titular, saldo):
 return f"Conta Corrente criada para {titular} com R$ {saldo:f}."

def criar_poupanca(titular, saldo):
 return f"Conta Poupança criada para {titular}. Saldo inicial: R$ {saldo:f}."

def criar_pj(empresa, cnpj, saldo):
 return f"Conta PJ criada: {empresa} (CNPJ: {cnpj}). Saldo inicial: R$ {saldo:f}."

# Programa Principal com Menu Interativo
opcao = -1
while opcao!= 0:
 print("\n--- BANCO DIGITAL - ABERTURA DE CONTA ---")
 print("1. Abrir Conta Corrente")
 print("2. Abrir Conta Poupança")
 print("3. Abrir Conta Pessoa Jurídica (PJ)")
 print("0. Sair")

 # Capturando a entrada do usuário e convertendo para inteiro
 opcao = int(input("Escolha o tipo de conta: "))

 if opcao == 1:
 nome = input("Digite o nome do titular: ")
 valor = float(input("Valor do primeiro depósito: "))
 print(criar_corrente(nome, valor)) # Chamada da função específica

 elif opcao == 2:
 nome = input("Digite o nome do titular: ")
 valor = float(input("Valor do primeiro depósito: "))
 print(criar_poupanca(nome, valor))

 elif opcao == 3:
 nome_empresa = input("Digite o Nome Fantasia: ")
 cnpj = input("Digite o CNPJ: ")
 valor = float(input("Valor do aporte inicial: "))
 print(criar_pj(nome_empresa, cnpj, valor))

 elif opcao == 0:
 print("Finalizando atendimento...")
 else:
 print("Opção inválida! Tente novamente.")
```

### Por que esta prática é importante?

1. **Tipagem de Dados:** O aluno pratica a conversão de entradas, transformando o texto do `input()` em `float` para realizar cálculos ou armazenar valores monetários corretamente.
2. **Organização por Paradigma Funcional:** Em vez de um código gigante e confuso, as funções permitem que a lógica de cada conta seja testada e mantida separadamente.
3. **Abstração:** Ao criar a conta PJ, o aluno percebe que pode adicionar campos novos (como o CNPJ) sem quebrar a lógica das outras funções.
4. **Uso de Variáveis e Atribuição:** A prática reforça o conceito de que variáveis são "caixas" que armazenam temporariamente os dados digitados pelo usuário até que sejam processados pelas funções.


## Fase 2 Criando registros em dicionários

Para integrar **funções** com **dicionários** na organização de dados bancários, você deve utilizar o dicionário como a unidade de armazenamento de informações e as funções como os motores de processamento e criação desses dados. Abaixo, apresento o passo a passo para essa integração:

1. **Estruture a conta como um Dicionário:** Utilize a estrutura de **chave e valor** para representar cada conta bancária individual. Chaves descritivas como "titular", "tipo_conta" e "saldo" devem ser usadas para rotular os dados, facilitando a identificação do que cada valor representa.
2. **Crie uma Função de Cadastro:** Utilize a palavra reservada **`def`** para criar uma função que receba os dados do cliente como **parâmetros**. Dentro desta função, a lógica deve construir um dicionário e utilizá-lo como o valor de **`return`** para devolver a conta estruturada ao programa principal.
3. **Gerencie uma Lista de Contas (Estrutura Composta):** Para organizar múltiplos clientes, armazene cada dicionário de conta dentro de uma **lista**. Você pode usar a função **`append`** para inserir novos dicionários de contas nessa lista conforme elas forem criadas.
4. **Desenvolva Funções de Processamento:** Crie funções que recebam a lista de contas ou um dicionário específico como argumento para realizar operações financeiras. Por exemplo, uma função pode percorrer a lista usando um laço **`for`**, acessar a chave "saldo" de cada dicionário e calcular o montante total sob gestão do banco.
5. **Isole as Responsabilidades:** Seguindo o **paradigma funcional**, cada tarefa (abrir conta, depositar, calcular juros) deve ser uma função isolada. Isso garante que, se uma regra bancária mudar, você precise alterar o código apenas dentro da função correspondente, facilitando a **manutenção** e o **reuso** do software.

### Exemplo de Aplicação Prática

Abaixo, um exemplo de como essa lógica seria implementada em Python para gerenciar os dados:

```python
# Função para criar o dicionário da conta
def abrir_conta(titular, tipo, saldo_inicial):
 return {"titular": titular, "tipo": tipo, "saldo": saldo_inicial} #

# Lista para armazenar todas as contas (Estrutura Composta)
banco_dados_contas = [] #

# Integrando a criação com a lista
nova_conta = abrir_conta("Marcos", "Corrente", 500.0) #
banco_dados_contas.append(nova_conta) #

# Função para processar os dados dos dicionários na lista
def calcular_patrimonio_total(contas):
 total = 0
 for conta in contas: #
 total += conta["saldo"] # Acessando valor pela chave
 return total
```

Essa abordagem transforma dados desestruturados em um sistema organizado, permitindo que você manipule milhares de registros bancários com poucas linhas de código e alta produtividade.

## Fase 3 Listando os registros

Para listar e visualizar as contas cadastradas de forma organizada, a melhor prática é utilizar uma **estrutura de repetição (laço `for`)** para percorrer os dados e a função **`print()`** para exibir os valores de cada campo.

Considerando que você está utilizando uma **estrutura de dados composta** (uma lista que armazena vários dicionários de contas), o procedimento técnico é o seguinte:

1. **Utilize um laço `for`:** Ele permite que o programa passe por cada "caixa" (dicionário) dentro da sua lista de contas, uma por uma.
2. **Acesse os valores pelas chaves:** Dentro do laço, você deve referenciar as **chaves** específicas do dicionário (como `"titular"`, `"saldo"` ou `"tipo_conta"`) entre colchetes para capturar apenas a informação desejada.
3. **Formate a visualização com `f-strings`:** Para que a lista não seja apenas um amontoado de dados brutos, utilize a formatação `f"Texto {variável}"`. Isso permite intercalar descrições com os dados das contas, tornando a leitura intuitiva para o usuário.

**Exemplo de implementação para visualizar as contas:**

```python
# 'contas' é a sua lista de dicionários
print("--- LISTAGEM DE CONTAS CADASTRADAS ---")

for conta in banco_dados_contas: # Percorre cada conta na lista
 # Exibe os dados formatados acessando as chaves do dicionário
 print(f"Titular: {conta['titular']} | Tipo: {conta['tipo']} | Saldo: R$ {conta['saldo']:f}")
```

Essa abordagem é preferível a simplesmente imprimir o dicionário inteiro (`print(dicionario)`), pois o Python, ao imprimir a estrutura bruta, inclui chaves, aspas e colchetes que dificultam a leitura humana. Ao iterar e formatar, você isola o **valor** da **chave**, gerando um relatório limpo e profissional.

## Fase 4 Removendo o registro

Sim, **é possível criar uma função que remova contas de um dicionário**. O processo de manipulação de dados é fundamentado no uso de **funções** (declaradas com a palavra-chave `def`) para isolar responsabilidades e automatizar tarefas.

Embora os exemplos detalhados de remoção nas fontes (como os métodos `remove` e `pop`) sejam demonstrados especificamente para **listas**, a lógica de programação apresentada permite a criação de funções customizadas para gerenciar qualquer estrutura de dados.

Para integrar essa funcionalidade ao sistema de dados bancários discutido anteriormente, você deve seguir estes princípios:

- **Paradigma Funcional:** Você pode definir uma função específica, por exemplo `remover_conta`, que receba o dicionário (ou a lista de dicionários) e o identificador da conta (como o nome do titular) como **parâmetros**.
- **Modularização:** Ao isolar a exclusão em uma função, você facilita a **manutenção do código** e evita erros semânticos no fluxo principal do programa.
- **Uso de Estruturas de Controle:** Dentro da função, você pode usar uma **estrutura de decisão** (`if`) para verificar se a conta existe antes de tentar removê-la, evitando que o programa gere erros de execução.
- **Estruturas Compostas:** Como vimos que dados bancários podem ser organizados em uma **lista de dicionários**, a função de remoção percorreria essa lista (usando um laço `for`), identificaria o dicionário correspondente e utilizaria comandos de remoção para excluí-lo da coleção.

Essa prática segue a recomendação das fontes de **decompor problemas complexos** em partes menores e reutilizáveis, garantindo que o software seja robusto e fácil de evoluir.

Para remover uma conta de uma base de dados (seja uma lista de dicionários ou um dicionário simples), você deve criar uma **função** que isole essa responsabilidade.

Abaixo, apresento um exemplo técnico que utiliza uma **estrutura de repetição** para localizar a conta e uma **estrutura de decisão** para validar a exclusão, seguindo o padrão de "limpeza de código" discutido nas fontes.

### Exemplo: Função para Remover Conta Bancária

Considerando que as contas estão organizadas em uma **lista de dicionários** (onde cada dicionário é uma conta), a lógica consiste em filtrar a lista original para excluir o titular desejado.

```python
# Definindo a função com parâmetros de entrada (lista e identificador)
def remover_conta(banco_dados, titular_para_remover):
 # Utilizamos compreensão de listas para criar uma nova lista
 # que contém apenas as contas que NÃO possuem o nome digitado
 nova_lista = [conta for conta in banco_dados if conta['titular']!= titular_para_remover]

 # Verificamos se houve mudança no tamanho da lista para confirmar a remoção
 if len(nova_lista) < len(banco_dados):
 print(f"Conta de {titular_para_remover} removida com sucesso!")
 return nova_lista
 else:
 print("Erro: Titular não encontrado na base de dados.")
 return banco_dados

# --- PROGRAMA PRINCIPAL ---
# Base de dados inicial (Lista de Dicionários)
meu_banco = [
 {"titular": "Marcos", "tipo": "Corrente", "saldo": 500.0},
 {"titular": "Julia", "tipo": "Poupança", "saldo": 1200.0}
]

# Chamada da função e atualização da variável global
nome = input("Digite o nome do titular que deseja remover: ")
meu_banco = remover_conta(meu_banco, nome) #
```

### Explicação do Processo Lógico

1. **Declaração da Função:** A função é definida com `def`, recebendo a coleção de dados e o nome do titular como **parâmetros**.
2. **Uso de Condicionais:** O programa utiliza o operador relacional de **diferente (`!=`)** para identificar quais contas devem permanecer, ignorando aquela que o usuário deseja apagar.
3. **Compreensão de Listas:** Seguindo a técnica de processamento em uma única linha vista nas fontes, a lógica percorre a lista e reconstrói o banco de dados filtrado, o que evita **erros semânticos** comuns em exclusões manuais dentro de laços.
4. **Retorno de Valor:** A função utiliza o comando **`return`** para devolver a nova lista atualizada ao fluxo principal, garantindo que a memória do computador reflita a exclusão.

Essa abordagem modular facilita a **manutenção do software**, pois permite que a regra de exclusão seja alterada em um único lugar sem afetar o restante do sistema bancário.

## Referências

- [Desafio Sistema Bancário - Google Colab](https://colab.research.google.com/drive/1DFPg5VakbWUVJ1RYquyTBBKTE9MKWSJX?usp=sharing)
- [[Aulas de Logica]]
