---
title: Fluxogramas
draft: false
tags:
  - programador
  - algoritmos
  - diagramas
---

Fluxograma é uma maneira de representar um processo por meio de um desenho, ou seja, é uma forma simples e fácil de identificar o fluxo com que as atividades acontecem.

[03-introdução-aos-algoritmos ⬅️](03-introdução-aos-algoritmos.md) | [➡️ 05-editor-de-Diagramas-mermaid](05-editor-de-Diagramas-mermaid.md)

- Os fluxogramas são formados de caixas com formato variado que conectadas de forma ordenada e lógica informam as instruções a serem executadas. São muito populares por serem de fácil entendimento das ideias contidas no algoritmo.
- A representação do fluxograma é ótima para descrever algoritmos de pequeno e médio tamanho.
- **Visualização Clara:** Os fluxogramas transformam a lógica abstrata dos algoritmos em uma linguagem visual compreensível, facilitando o aprendizado e a análise de cada etapa do processo.
- **Comunicação Eficaz:** Funcionam como ferramenta de comunicação entre desenvolvedores, permitindo que diferentes pessoas compreendam a estrutura e o funcionamento do algoritmo de forma clara e objetiva.
- **Identificação de Falhas:** Ao visualizar o algoritmo passo a passo, fica mais fácil identificar erros de lógica, falhas de processamento ou inconsistências na sequência de instruções.
- **Documentação Detalhada:** Os fluxogramas servem como documentação detalhada do algoritmo, registrando todas as etapas e decisões envolvidas no processo.

## Tipos de fluxogramas

- Diagrama de Blocos
- Processo Simples
- Funcional
- Vertical

Para saber mais acesse: [5 passos para criacao de um fluxograma](https://blog.zeev.it/5-passos-para-criacao-de-um-fluxograma/)

## Como fazer fluxogramas

Para criar diagramas de fluxo ou fluxogramas, primeiro é preciso um editor, como o Mermaid, em seguida seguir os seguintes passos:

Escolha uma plataforma de edição de texto ou código que suporte a sintaxe do Mermaid. Algumas opções populares incluem VS Code, Atom, Sublime Text, ou mesmo o [editor online do Mermaid](https://mermaid.live/).

Comece definindo o tipo de gráfico que você deseja criar, utilizando a sintaxe apropriada do Mermaid. Por exemplo, para criar um diagrama de fluxo, você pode começar com o seguinte código:

```plaintext
graph LR;
A-->B;
A-->C;
B-->D;
C-->D;
```

Resultado:

```mermaid

graph LR;

A-->B;

A-->C;

B-->D;

C-->D;

  

```

Este código cria um diagrama de fluxo básico com quatro nós (A, B, C e D) e quatro setas conectando-os.

Personalize seu gráfico adicionando nós adicionais, alterando as cores ou estilos, adicionando texto descritivo e ajustando o layout. Existem muitas opções de personalização disponíveis na sintaxe do Mermaid, e você pode encontrar uma lista completa de opções na documentação oficial.

## Formato

- **Caixas:** Cada caixa representa uma ação específica, como ler um dado, realizar um cálculo ou escrever um resultado. Elas podem ter diferentes formatos e cores para indicar funções distintas.
- **Símbolos:** Os símbolos são os sinais de trânsito do mundo dos fluxogramas. Eles guiam o fluxo da execução do algoritmo, indicando o início, o fim, decisões a serem tomadas e a direção que o processo deve seguir.
- **Linhas de Conexão:** As linhas de conexão são as estradas que ligam as caixas e os símbolos, definindo a ordem em que as instruções devem ser executadas. Elas podem ser contínuas ou segmentadas para indicar diferentes fluxos de execução.
- **Início:** Um símbolo especial marca o início da execução do algoritmo.
- **Comandos e Decisões:** Uma sequência de caixas representa as instruções que o algoritmo deve executar, incluindo cálculos, leituras e decisões a serem tomadas.
- **Bifurcações:** As decisões geram bifurcações no fluxo do algoritmo, direcionando a execução para diferentes caminhos de acordo com o resultado da decisão.
- **Processamento:** As informações são processadas e manipuladas ao longo das etapas do algoritmo.
- **Armazenamento:** Dados e resultados são armazenados em caixas específicas para serem utilizados posteriormente.
- **Fim:** Um símbolo especial marca a finalização da execução do algoritmo

Usando editor de diagramas [mermaid - fluxograma](https://mermaid.js.org/syntax/flowchart.html):

## Símbolos do fluxograma

Exemplo básico de um diagrama de fluxo com Mermaid que exiba todos os elementos comuns do fluxograma:

```plaintext

graph TD;

Inicio([Inicio]) --> Entrada[\Entrada de dados/];
Entrada --> Decisao{Tomar decisão?};
Decisao -- Sim --> Processo[Processo 1];
Processo -- Condição 1 --> Decisao2{Outra decisão?};
Decisao2 -- Sim --> Processo2[Processo 2];
Decisao2 -- Não --> Subprocesso[Subprocesso 1];
Subprocesso --> Processo3((Conector));
Processo2 --> Processo3;
Processo3 --> DecisaoFinal((Conector));
DecisaoFinal -- Resultado --> Exibir>Exibir resultado];
Exibir -- Fim --> Fim([Fim]);
Decisao -- Não --> Subprocesso2[Subprocesso 2];
Subprocesso2 --> DecisaoFinal;
```

Resultado:

```mermaid

graph TD;

Inicio([Inicio]) --> Entrada[\Entrada de dados/];

Entrada --> Decisao{Tomar decisão?};

Decisao -- Sim --> Processo[Processo 1];

Processo -- Condição 1 --> Decisao2{Outra decisão?};

Decisao2 -- Sim --> Processo2[Processo 2];

Decisao2 -- Não --> Subprocesso[Subprocesso 1];

Subprocesso --> Processo3((Conector));

Processo2 --> Processo3;

Processo3 --> DecisaoFinal((Conector));

DecisaoFinal -- Resultado --> Exibir>Exibir resultado];

Exibir -- Fim --> Fim([Fim]);

Decisao -- Não --> Subprocesso2[Subprocesso 2];

Subprocesso2 --> DecisaoFinal;

  

```

Nesse exemplo, temos os seguintes elementos do fluxograma:

- Início: Representado pelo nó Inicio.
- Entrada: Representa uma entrada de dados pelo usuário.
- Decisão: Representado pelo nó Decisao com uma seta saindo para Processo 1 quando a resposta é sim, e para Subprocesso 2 quando a resposta é não.
- Processo: Representado pelo nó Processo 1, Processo 2, Processo 3.
- Condição: Representada pela seta com texto Condição 1.
- Subprocesso: Representado pelo nó Subprocesso 1 e Subprocesso 2.
- Exibir resultado: mostra o resultado na saída padrão.
- Conclusão: Representado pelo nó DecisaoFinal com uma seta saindo para Fim quando a decisão é tomada.

> [!info]  
> Lembre-se de que a sintaxe do Mermaid pode ser personalizada para atender às suas necessidades específicas de fluxograma. Portanto, você pode alterar as cores, formas, tamanhos e estilos dos nós e das setas, bem como adicionar texto descritivo e ajustar o layout para tornar seu diagrama de fluxo mais claro e legível.

[Veja a lista completa de símbolos aqui!](https://blog.zeev.it/wp-content/uploads/2021/01/OD_SML_info.png)

## Exemplos

### Verificar se um Número é Par ou Ímpar

Verificar se um Número é Par ou Ímpar: Um fluxograma pode ser utilizado para determinar se um número é par ou ímpar, dividindo-o por dois e verificando o restante da divisão.

```mermaid
flowchart TD
A[Início] --> B{Ler número}
B --> C{Armazenar número em variável}
C --> D{Dividir número por 2}
D --> E{Armazenar resto da divisão em variável}
E --> F[Verificar resto da divisão]
    F --> G[Se resto for 0, então o número é par]
        G --> H[Mostrar mensagem O número é par]
        H --> I[Fim]
    F --> J[Se resto for diferente de 0, então o número é ímpar]
        J --> K[Mostrar mensagem O número é ímpar]
        K --> I[Fim]

```

**Explicação do Fluxograma:**

1. **Início:** O algoritmo começa com a leitura de um número.
2. **Ler número:** Um número é lido do usuário e armazenado em uma variável.
3. **Armazenar número:** O número lido é armazenado em uma variável chamada `numero`.
4. **Dividir número por 2:** O número armazenado na variável `numero` é dividido por 2 e o resultado é armazenado em uma variável chamada `resto`.
5. **Armazenar resto:** O valor da variável `resto` é armazenado em uma variável chamada `restoDivisao`.
6. **Verificar resto da divisão:** O valor da variável `restoDivisao` é verificado.
7. **Se resto for 0, então o número é par:** Se o valor da variável `restoDivisao` for 0, então o número é par e a mensagem "O número é par" é exibida na tela.
8. **Mostrar mensagem "O número é par":** A mensagem "O número é par" é exibida na tela do usuário.
9. **Fim:** O algoritmo termina.
10. **Se resto for diferente de 0, então o número é ímpar:** Se o valor da variável `restoDivisao` for diferente de 0, então o número é ímpar e a mensagem "O número é ímpar" é exibida na tela.
11. **Mostrar mensagem "O número é ímpar":** A mensagem "O número é ímpar" é exibida na tela do usuário.
12. **Fim:** O algoritmo termina.

### **Calcular a Média de Três Notas** 

Um fluxograma pode ser usado para representar o processo de calcular a média de três notas, mostrando os passos de somar as notas e dividir o resultado por três.

```mermaid
flowchart TD
A[Início] --> B{Ler nota 1}
B --> C{Armazenar nota 1 em variável}
C --> D{Ler nota 2}
D --> E{Armazenar nota 2 em variável}
E --> F{Ler nota 3}
F --> G{Armazenar nota 3 em variável}
G --> H{Somar notas 1, 2 e 3}
H --> I{Armazenar soma em variável total}
I --> J{Dividir total por 3}
J --> K{Armazenar média em variável média}
K --> L[Mostrar média na tela]
L --> M[Fim]
```

**Explicação do Fluxograma:**

1. **Início:** O algoritmo começa com a leitura da primeira nota.
2. **Ler nota 1:** A nota 1 é lida do usuário e armazenada em uma variável.
3. **Armazenar nota 1:** A nota 1 é armazenada em uma variável chamada `nota1`.
4. **Ler nota 2:** A nota 2 é lida do usuário e armazenada em uma variável.
5. **Armazenar nota 2:** A nota 2 é armazenada em uma variável chamada `nota2`.
6. **Ler nota 3:** A nota 3 é lida do usuário e armazenada em uma variável.
7. **Armazenar nota 3:** A nota 3 é armazenada em uma variável chamada `nota3`.
8. **Somar notas 1, 2 e 3:** As notas 1, 2 e 3 são somadas e o resultado é armazenado em uma variável chamada `total`.
9. **Armazenar soma:** O valor da variável `total` é armazenado em uma variável chamada `soma`.
10. **Dividir total por 3:** O valor da variável `soma` é dividido por 3 e o resultado é armazenado em uma variável chamada `media`.
11. **Armazenar média:** O valor da variável `media` é armazenado em uma variável chamada `média`.
12. **Mostrar média na tela:** A média é exibida na tela do usuário.
13. **Fim:** O algoritmo termina.
