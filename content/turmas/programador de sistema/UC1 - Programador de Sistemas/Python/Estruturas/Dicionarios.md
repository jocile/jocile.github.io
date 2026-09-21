---
title: Coleções em Python
description: Descrições das principais coleções de dicionários em Python
tags:
  - diagrama
  - programador/Python/estruturas
aliases:
  - Dicionários
---

Em Python, as coleções de dados (frequentemente chamadas genericamente de "listas" por iniciantes) são estruturas fundamentais para organizar informações de forma eficiente na memória do computador. Para estudantes de lógica, é importante diferenciar os quatro tipos principais baseados em suas propriedades de ordenação, mutabilidade e unicidade:

- **Listas (`list`):** São coleções **ordenadas e mutáveis**, representadas por colchetes `[]`. Elas permitem armazenar diferentes tipos de dados simultaneamente (como números, textos e até outras listas) e possibilitam a adição, remoção ou modificação de seus elementos a qualquer momento. O acesso aos itens é feito através de um **índice numérico**, que em Python sempre inicia no **zero**.
- **Tuplas (`tuple`):** Funcionam de forma semelhante às listas, sendo ordenadas e acessadas por índices, mas com a diferença crucial de serem **imutáveis**. Uma vez criada (usando parênteses `()`), uma tupla não pode ter seus valores alterados, sendo ideal para dados que devem permanecer constantes, como coordenadas geográficas.
- **Conjuntos (`set`):** São coleções de **elementos únicos e desordenados**, definidos por chaves `{}`. Eles são extremamente úteis para **eliminar duplicatas** automaticamente e realizar operações matemáticas de união ou intersecção, pois o Python remove entradas repetidas e não garante uma ordem fixa para os itens.
- **Dicionários (`dict`):** Diferente das outras estruturas que usam índices numéricos, os dicionários organizam os dados em pares de **chave e valor** dentro de chaves `{}`. Para acessar uma informação, você utiliza uma "chave" descritiva (como um rótulo em uma gaveta), o que torna a estrutura muito eficiente para representar objetos do mundo real, como o cadastro de um cliente.

Além dessas, na lógica de programação costuma-se utilizar os termos **Vetor** (para arrays unidimensionais) e **Matriz** (quando uma lista contém outras listas, formando uma estrutura multidimensional), conceitos essenciais para manipular tabelas e dados complexos.

## Usando Dicionários

Para criar um registro prático integrando essas ferramentas, você deve utilizar uma **função** (definida pela palavra-chave **`def`**) para capturar os dados e um **dicionário** (definido por **chaves `{}`**) para organizá-los em pares de **chave e valor**.

Abaixo, apresento um exemplo passo a passo de uma função de registro de clientes, integrando-a a uma lista para armazenamento permanente, conforme sugerido em nossa conversa anterior:

### Exemplo Prático: Função de Registro de Clientes

Neste cenário, a função recebe as informações como **parâmetros**, monta o dicionário e o devolve para ser guardado em uma **lista composta**.

```python
# 1. Lista para armazenar todos os registros (banco de dados)
banco_clientes = []

# 2. Função que cria o registro usando um dicionário
def registrar_cliente(nome, idade, profissao):
    # Retorna um dicionário estruturado com as informações recebidas
    return {
        "nome": nome,
        "idade": idade,
        "profissao": profissao
    }

# 3. Execução do registro e armazenamento na lista
novo_registro = registrar_cliente("Ana Silva", 30, "Engenheira")
banco_clientes.append(novo_registro) # Adiciona o dicionário à lista

# Exibindo o resultado
print(f"Cliente cadastrado: {banco_clientes}")
```

### Explicação dos Conceitos Utilizados:

- **Estrutura de Chave e Valor:** O dicionário permite que você acesse a informação de forma descritiva. Em vez de apenas salvar "Ana Silva", você salva que a **chave** "nome" tem o **valor** "Ana Silva".
- **Retorno de Valor (`return`):** A função não apenas executa o código, mas "devolve" o dicionário pronto para o programa principal, permitindo que ele seja manipulado ou salvo em outras estruturas.
- **Adição Dinâmica:** Como visto nas fontes, se você precisar adicionar uma nova informação a um dicionário já existente (como um "ID" ou "Status"), basta informar a nova chave entre colchetes e atribuir o valor; se a chave não existir, o Python a criará automaticamente.
- **Escalabilidade:** Ao utilizar o método **`.append()`**, você pode repetir a chamada da função diversas vezes dentro de um laço de repetição (**`for`** ou **`while`**), criando um banco de dados com milhares de registros organizados.

## [[Referencias de Logica de Programacao]]

- [[Exemplos de listas em python]]
- [[Aulas de Logica]]
- [[Formacao Python]]
