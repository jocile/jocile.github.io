---
title: 03 Introdução aos algoritmos
draft: false
tags:
  - programador
  - lógica
  - algoritmos
---
Algoritmos são conjuntos de instruções precisas e ordenadas que definem como realizar uma tarefa ou resolver um problema. Eles são a base da programação e estão presentes em diversos aspectos da nossa vida, desde o funcionamento de computadores e smartphones até a forma como realizamos tarefas cotidianas.

## Características

- **Precisão:** As instruções do algoritmo devem ser claras e inequívocas, não permitindo interpretações dúbias.
- **Ordem:** As instruções devem ser executadas em uma sequência específica para garantir o resultado correto.
- **Generalidade:** O algoritmo deve ser aplicável a diferentes casos dentro do problema que se pretende resolver.
- **Finitudes:** O algoritmo deve ter um número finito de instruções e chegar a um resultado final em um tempo determinado.
- **Eficiência:** O algoritmo deve utilizar o mínimo de recursos computacionais para alcançar o resultado desejado.

## Tipos

- **Algoritmos sequenciais:** Executam as instruções uma após a outra, em uma ordem pré-definida.
- **Algoritmos de decisão:** Permitem tomar decisões com base em condições específicas.
- **Algoritmos recursivos:** Dividem o problema em subproblemas menores e resolvem cada um deles de forma recursiva.
- **Algoritmos de busca:** Localizam um elemento específico dentro de um conjunto de dados.
- **Algoritmos de ordenação:** Organizam um conjunto de dados em uma ordem específica.

## Exemplos de algoritmos na vida cotidiana

- **Receita culinária:** Uma sequência de instruções para preparar um prato específico.
- **Montagem de móveis:** Um conjunto de passos para montar um móvel a partir de peças e ferramentas.
- **Resolução de um problema matemático:** Uma série de operações matemáticas para chegar a um resultado.
- **Jogos de tabuleiro:** Regras e instruções para jogar um jogo específico.
- **Algoritmos de busca na internet:** Encontram páginas web relevantes para uma pesquisa específica.

## Importância dos algoritmos

- **Eficiência e produtividade:** Permitem automatizar tarefas e otimizar processos, tornando-os mais rápidos e eficientes.
- **Precisão e confiabilidade:** Garantem a execução correta de tarefas e a obtenção de resultados confiáveis.
- **Criatividade e inovação:** Permitem desenvolver soluções inovadoras para problemas complexos.
- **Aprendizado e desenvolvimento:** Auxiliam no desenvolvimento do raciocínio lógico, da resolução de problemas e da capacidade de pensar de forma organizada.

> [!Nota] 
> Os algoritmos são ferramentas essenciais para a resolução de problemas, a automação de tarefas e a criação de soluções inovadoras. Compreender seus princípios e aplicá-los de forma eficiente é fundamental para o sucesso em diversas áreas da vida, desde a programação de computadores até a resolução de problemas cotidianos.

## Conceitos de algoritmos

Usamos a lógica para guiar nossos pensamentos ou ações para chegarmos a uma solução. Devemos ter sempre em mente que a lógica está correta se ela atingir o objetivo para que ela foi proposta.

Para conseguirmos inserir lógica em nossas atividades, precisamos aprender a pensar de forma estruturada, ou seja, desenvolver e aperfeiçoar a técnica de pensamento e seguir uma sequência de raciocínio que crie passos objetivos e seguros até a solução.


> [!NOTE] IMPORTANTE
Segundo Manzano e Oliveira (2012), para usar o raciocínio lógico, é necessário ter domínio do pensar, bem como saber pensar, ou seja, possuir e usar a "arte de pensar".
Quando organizamos nossos pensamentos de forma lógica conseguimos associar as informações e transformá-las em base para nossas soluções.

## Exemplos de algoritmos lógicos

Analise a lógica a seguir:

	Se: todo mamífero é um animal
	E: todos os gatos são mamíferos
	Logo: todos os gatos são animais!
	Ou
	Se: todos os veículos são transportes
	E: todas as motos são veículos
	Logo: todas as motos são transportes!

- No exemplo apresentado usamos a lógica para averiguar uma situação e chegar a uma conclusão, fazendo associações entre eles.
- A primeira parte analisa que se todos os seres mamíferos são animais e que se todos os gatos são mamíferos, então os gatos também fazem partes do grupo de animais.
- A segunda faz uma análise parecida, que se todos os veículos são chamados de transportes e se todas as motos são consideradas veículos, então as motos também fazem parte do grupo de transportes.

Utilizamos a lógica a todo o momento em nossas vidas, quando pensamos, falamos ou escrevemos, utilizamos a lógica para ordenar as palavras e dar sentido ao que estamos fazendo.\
Ao longo do dia, usamos o nosso raciocínio lógico para resolvermos questões, das mais simples as mais complexas.\
A lógica nos ensina a corrigirmos nosso pensamento, nos ensinando a usá-lo corretamente. Usando o raciocínio de forma ordenada dividindo a ação em vários passos até a solução do problema.

Analise a lógica a seguir:

	Se: A porta está fechada
	E: a mochila está dentro da casa
	Logo: Preciso primeiro abrir a porta, entrar em casa para depois pegar a mochila!
	Ou
	Se: Se Jussara é mais nova que José
	E: José é mais novo que Fábio
	Logo: Jussara é mais nova que Fábio!

Neste exemplo, somos apresentados com duas premissas e uma conclusão:

- **Premissa 1:** A porta está fechada.
- **Premissa 2:** A mochila está dentro de casa.
- **Conclusão:** Preciso primeiro abrir a porta, entrar em casa e depois pegar a mochila!

Para analisar este raciocínio lógico, podemos usar uma **tabela verdade**:

|Premissa 1|Premissa 2|Conclusão|
|---|---|---|
|Verdadeiro|Verdadeiro|Verdadeiro|
|Verdadeiro|Falso|Falso|
|Falso|Verdadeiro|Falso|
|Falso|Falso|Verdadeiro|

> [!Nota] 
Como podemos ver, a conclusão só é verdadeira quando ambas as premissas são verdadeiras. Isso significa que, para recuperar a mochila, primeiro devemos abrir a porta e entrar em casa. Se a porta estiver aberta ou se a mochila estiver fora de casa, a conclusão não necessariamente se segue.

**Exemplo: Comparando Idades**

Neste exemplo, somos apresentados com três declarações que comparam as idades de três pessoas:

- **Declaração 1:** Jussara é mais nova que José.
- **Declaração 2:** José é mais novo que Fábio.
- **Conclusão:** Jussara é mais nova que Fábio.

Para analisar este raciocínio lógico, podemos usar a propriedade transitiva da idade. A propriedade transitiva afirma que se A é mais novo que B, e B é mais novo que C, então A também deve ser mais novo que C.

Neste caso, temos:

- **Jussara é mais nova que José.**
- **José é mais novo que Fábio.**

Portanto, pela propriedade transitiva da idade, podemos concluir que **Jussara é mais nova que Fábio**.

**Conclusão**

Ambos os exemplos de raciocínio lógico são válidos. O primeiro exemplo usa uma tabela verdade para mostrar que a conclusão só é verdadeira quando ambas as premissas são verdadeiras. O segundo exemplo usa a propriedade transitiva da idade para mostrar que a conclusão segue das duas declarações.


> [!tip] 
Em geral, o raciocínio lógico é uma ferramenta poderosa que pode ser usada para resolver problemas e tomar decisões. Ao compreender os princípios da lógica, podemos melhorar nossas habilidades de pensamento crítico e nos tornar comunicadores mais eficazes.

Podemos representar os algoritmos de forma gráfica com [fluxogramas](04-fluxogramas.md).

## 📚 Livros de introdução a programação

- [Desenvolvimento de sistemas Allen Oberleitner](https://jocile.notion.site/Desenvolvimento-de-sistemas-Allen-Oberleitner-7f43c99c571d43ecafd026cda967461e)
- [Lógica de programação Gley Fabiano Cardoso Xavier](https://jocile.notion.site/L-gica-de-programa-o-Gley-Fabiano-Cardoso-Xavier-1dbcc1c64e45402d9f130d07fd2914dd)

[02-logica-com-blocos ⬅️](02-logica-com-blocos.md) | [➡️ 04-fluxogramas](04-fluxogramas.md)
