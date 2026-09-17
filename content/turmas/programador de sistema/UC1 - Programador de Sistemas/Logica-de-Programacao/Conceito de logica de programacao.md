---
title: Conceito de Lógica de Programação
description: É o conjunto de métodos utilizados para organizar pensamentos, raciocínios e argumentos
date: 2026-09-14
draft: false
tags:
  - Lógica
---

## Introdução à Lógica de Programação

### O que é lógica?

Lógica é a arte de pensar corretamente. É o conjunto de métodos utilizados para organizar pensamentos, raciocínios e argumentos de forma clara e objetiva.

#### Por que estudar lógica?

Apreender os conceitos de lógica permite-nos:

- Evitar erros no raciocínio
- Comunicar ideias com mais precisão
- Construir soluções estruturadas para problemas complexos

### Principais conceitos

#### O que é um algoritmo?

Um algoritmo é uma sequência finita e bem definida de instruções que visam atingir um objetivo específico. Imagine ser o mestre de uma receita culinária: cada passo precisa estar especificamente definido para obter o resultado desejado.

#### O que é um padrão de comportamento?

Padrão de comportamento nada mais é do que um algoritmo aplicado repetidamente a diferentes situações. É como aprender um ritual mágico: seguindo os mesmos passos, você obtém resultados previsíveis em contextos similares.

#### Complexidade

A complexidade representa o número de possíveis variações que um problema pode ter. No desenvolvimento de software, nosso objetivo principal é minimizar essa complexidade:

- Decompondo problemas grandes em partes menores
- Identificando padrões repetitivos
- Criando soluções escaláveis e eficientes

#### Questionamento errôneo

Um erro comum que aumenta a complexidade é fazer perguntas inadequadas ao resolver um problema. Em vez de "Como implementar isso?", devemos nos concentrar em:

1. Definir claramente o objetivo
2. Identificar os dados necessários
3. Estabelecer as relações entre eles

### Construindo algoritmos

#### Método para construção de algoritmo

Para criar um bom algoritmo, siga estes passos:

1. Leia atentamente o problema (enunciado)
2. Identifique todas as entradas necessárias
3. Defina claramente quais são os resultados esperados
4. Determine como transformar as entradas nas saídas
5. Escreva o algoritmo passo a passo

#### Exemplo prático em JavaScript

Vamos criar um exemplo simples de função que utiliza lógica para resolver um problema:

```javascript
function calcularMedia(nota1, nota2, nota3) {
  // Calcula a média das três notas fornecidas pelo usuário
  const media = (nota1 + nota2 + nota3) / 3;
  
  // Verifica se o aluno foi aprovado ou reprovado com base na média
  if (media >= 7.0) {
    return "Aprovado";
  } else if (media >= 5.0 && media < 7.0) {
    return "Recuperação";
  } else {
    return "Reprovado";
  }
}

// Testando a função
console.log(calcularMedia(8, 9, 10)); // Saída: Aprovado
console.log(calcularMedia(5.5, 6.5, 7.5)); // Saída: Recuperação
```

### Tratamento de informações

#### O que são informações?

Informações são os dados que utilizamos para construir soluções computacionais. Elas podem ser:

- Numéricas (inteiros ou reais)
- Textuais (caracteres alfanuméricos)
- Lógicas (verdadeiro/falso)

#### Tipos primitivos de dados

JavaScript possui os seguintes tipos básicos de dados:

1. `number`: para números inteiros e reais
2. `string`: para textos e caracteres
3. `boolean`: para valores lógicos (true/false)
4. `null` e `undefined`: representando ausência de valor

#### Trabalhando com variáveis

```javascript
let nome = "Maria"; // Variável do tipo string
const idade = 25;    // Constante numérica
var notaFinal = null; // Variável que pode receber diferentes valores no futuro

// Verificando tipos de dados usando typeof
console.log(typeof nome);     // Saída: 'string'
console.log(typeof idade);    // Saída: 'number'
console.log(typeof notaFinal); // Saída: 'undefined' (até então)

// Convertendo tipos de dados
let populacao = "50.2";       // Inicialização como string
populacao = Number(populacao); // Conversão para número

console.log(populacao + 100); // Agora será uma operação numérica: 600.2
```

### Princípios fundamentais de programação lógica

#### Modularização

É importante quebrar problemas grandes em partes menores e mais gerenciáveis:

```javascript
function somar(a, b) {
  return a + b;
}

// Função principal que utiliza o módulo acima
function calcularTotal(precoProduto, quantidade) {
  const subtotal = somar(precoProduto * quantidade);
  
  // Outros cálculos ou validações poderiam ser adicionados aqui
  
  return `O total da compra é R$ ${subtotal}`;
}

console.log(calcularTotal(25.90, 3)); // Saída: O total da compra é R$ 77.7
```

#### Clareza e objetividade

No desenvolvimento de software, cada linha de código deve transmitir um único propósito:

```javascript
// Exemplo de código claro para validação de CPF
function validarCPF(cpf) {
  // Remove caracteres não numéricos do CPF informado pelo usuário
  const cpfLimpo = cpf.replace(/\D/g, '');
  
  // Verifica se o CPF possui 11 dígitos válidos
  if (cpfLimpo.length !== 11 || isNaN(Number(cpfLimpo))) {
    return false;
  }
  
  // Adicionaria aqui a lógica completa de validação
  
  return true; // Placeholder para demonstrar clareza no código
}

// Uso da função
console.log(validarCPF("123.456.789-09")); // Saída: true ou false dependendo do CPF válido/inválido
```

### Usando Formulários HTML

Se você quer entender a **lógica de programação com JavaScript usando formulários HTML como entrada e exibindo a saída em campos do DOM**, aqui está um guia prático e direto com os principais conceitos, exemplos e dicas:

#### 1. Estrutura Básica do Formulário HTML

Um formulário HTML convencional inclui campos de entrada (como `<input>`, `<select>`, `<textarea>`) onde o usuário pode digitar ou escolher dados.

```html
<form id="formularioExemplo">
  <label for="num1">Número 1:</label>
  <input type="number" id="num1" name="num1">

  <label for="num2">Número 2:</label>
  <input type="number" id="num2" name="num2">

  <button type="submit">Somar</button>
</form>

<div id="resultado"></div>
```

#### 2. Ligando o JavaScript ao Formulário

O JavaScript permite capturar os valores digitados, processá-los e mostrar o resultado na própria página sem recarregar.

```javascript
<script>
document.getElementById('formularioExemplo').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita o recarregamento da página
  // Captura dos valores de entrada
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  // Lógica de programação (exemplo: soma)
  const soma = num1 + num2;
  // Exibindo a saída no campo DOM
  document.getElementById('resultado').textContent = `O resultado é: ${soma}`;
});
</script>
```

#### 3. Explicação dos conceitos usados

- **event.preventDefault()**: Impede que o formulário recarregue a página após o envio.
- **Captura de dados**: Usando `.value` dos campos de entrada para obter os dados inseridos pelo usuário.
- **Manipulação do DOM**: O resultado é exibido modificando o texto do elemento `<div id="resultado">`.
- **Lógica de programação**: O cálculo da soma neste caso, mas poderia ser qualquer outro tipo de processamento.

#### 4. Exemplos de entrada e saída em campos DOM

Você pode tanto mostrar resultados em uma `<div>`, quanto em outros `<input>` ou `<textarea>`:

```html
<input type="text" id="saida" readonly>
```

```javascript
document.getElementById('saida').value = soma;
```

#### 5. Dicas práticas para lógica de programação com formulários

- Valide os dados antes de processar (por exemplo, assegure que não estejam vazios e sejam números).
- Use funções para modularizar sua lógica.
- Interaja com o DOM sempre após garantir que ele está carregado (coloque seu `<script>` no final do `<body>` ou use `DOMContentLoaded`).

#### 6. Recursos para estudo

- **MDN Web Docs**: Explicações detalhadas sobre manipulação de formulários e DOM em JavaScript[^1][^2].
- **Tutoriais interativos**: Exemplos de formulários com processamento JavaScript customizado[^3][^4][^2].

Com esses conceitos, você pode fazer desde um simples somador até lógicas mais complexas (validações, exibir mensagens de erro, calcular médias, cadastrar dados etc.), sempre usando **formulários HTML para entrada de dados e manipulando o DOM para exibir a saída** – base fundamental da programação web interativa com JavaScript[^1][^3][^2].

### Conclusão

A lógica de programação é uma habilidade essencial para qualquer desenvolvedor. Ao dominá-la, você:

- Pensa de forma mais estruturada ao resolver problemas
- Cria soluções mais eficientes e menos propensas a erros
- Comunica ideias com clareza nas suas implementações

Lembre-se: cada vez que você se depara com um problema, pergunte primeiro:

1. Qual é o objetivo principal?
2. Quais são as entradas necessárias?
3. Como transformar essas entradas nos resultados desejados?

Essa mentalidade lógica ajudará você a construir soluções cada vez mais eficientes!

### Referências

- [[Formacao em Logica]]
- [JavaScript Introduction](https://www.w3schools.com/js/js_intro.asp)

[^1]: <https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity>

[^2]: <https://blog.openreplay.com/pt/manuseio-entrada-formulario-javascript-vanilla/>

[^3]: <https://pt.scribd.com/document/17582325/Formularios>

[^4]: <https://www.alura.com.br/artigos/eventos-do-dom>

[^5]: <https://www.youtube.com/watch?v=ECLctgz_1YI>

[^6]: <https://www.kufunda.net/publicdocs/Lógica de Programação e Algorítmos com JavaScript (Edécio Fernando Iepsen).pdf>

[^7]: <http://www.telecentros.sp.gov.br/saber/apostilas/antigas/html_logica.pdf>

[^8]: <https://techdocs.broadcom.com/br/pt_br/ca-enterprise-software/business-management/ca-service-management/17-3/using/service-catalog-management/manage-forms/perform-automated-tasks-in-form-fields/use-javascript-functions-in-fields.html>

[^9]: <https://www.homehost.com.br/blog/tutoriais/formulario-html/>

[^10]: <https://www.ffclrp.usp.br/divulgacao/informatica/Daniel/Topico I/Aula 5 - Formulários HTML e JavaScript.pdf>

[^11]: <https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Forms/Your_first_form>

[^12]: <https://www.freecodecamp.org/espanol/news/manejo-de-formularios-del-lado-del-cliente-con-javascript-explicado-con-codigo-de-ejemplo/>

[^13]: <https://www.devmedia.com.br/trabalhando-com-dom-em-javascript/29039>

[^14]: <https://www.youtube.com/watch?v=3Ec9zY1C2og>

[^15]: <https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Using_the_Document_Object_Model>

[^16]: <https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Forms/How_to_structure_a_web_form>

[^17]: <https://www.youtube.com/watch?v=k7iMlH5YyK8>

[^18]: <https://www.locaweb.com.br/blog/temas/codigo-aberto/dom-javascript/>

[^19]: <https://www.youtube.com/watch?v=TLkds5BJ-vA>

[^20]: <https://www.devmedia.com.br/criando-form-de-contato-com-html5-css3-e-javascript/29415>
