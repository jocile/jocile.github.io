---
title: Introdução ao CSS
description: é um mecanismo utilizado para adicionar estilo a documentos web
tags:
- Webdesign/css
---

## Introdução ao CSS

### O que é CSS?

CSS é um acrônimo em inglês, significando **Cascading Style Sheets** (Folhas de Estilo em Cascata). Em português, traduzimos como uma folha de estilos com cascata. Basicamente, o CSS é um mecanismo utilizado para adicionar estilo a documentos web escritos em HTML.

### Para que ele serve?

Com o CSS, podemos determinar **como deve ser o layout das nossas páginas** e definir as propriedades de estilos nos elementos do HTML. Exemplos práticos incluem:

- Definir cores
- Estilizar fundos
- Controlar largura e altura
- Configurar tamanhos de espaçamento e fontes
- Posicionar elementos na tela

### Origem e desenvolvimento

O CSS foi proposto pela primeira vez em **1994** por um indivíduo chamado **Håkon Lie**, online. O desenvolvimento formal da linguagem ocorreu nos meados de **1995**, sendo padronizado pela W3C (World Wide Web Consortium) entre **1997 e 1999**.

### Benefícios do CSS

- Permite controlar o estilo de várias páginas HTML com um único documento CSS
- Facilita a criação de layouts simples e eficientes
- O mesmo conceito pode ser aplicado em aplicações web, sites móveis, entre outros projetos (usando bibliotecas/frameworks)

### Diferença para programação

É importante destacar que o CSS **não é considerado uma linguagem de programação**. Ele não possui as capacidades típicas de uma linguagem de programação como:

- Fazer cálculos
- Armazenar e alterar informações em memória
- Tomar decisões ou mudar fluxos de execução

### Linguagem de estilos, não marcação

O CSS é uma **linguagem de estilos**, não de marcação. Diferente do HTML (que é uma linguagem de marcação), o CSS apenas declara como os elementos devem ser apresentados na tela.

### Propriedades e Aplicação

Olá! Vamos aprender juntos como adicionar estilos à nossa página web utilizando o poderoso recurso chamado CSS (Cascading Style Sheets). Nesta aula, vamos explorar os conceitos fundamentais de propriedade no CSS e as três formas mais comuns de aplicar esses estilos: CSS inline, CSS interno e CSS externo.

---

#### O Conceito de Propriedade

Então, pra começar, o que é uma propriedade no CSS? Basicamente, uma **propriedade** é uma característica de um elemento HTML. Por exemplo:

- Cor do fundo (`background`)
- Altura
- Largura
- Espaçamento entre linhas (line-height)
- E muitas outras!

Cada propriedade recebe um **valor**, e juntos eles definem como o navegador deve exibir o estilo de um elemento. 

A declaração básica é:

```css
nome-da-propriedade: valor;
```

O ponto-e-vírgula (`;`) finaliza a declaração, indicando que aquela propriedade está sendo aplicada.

---

#### 1. CSS Inline (Inline)

Essa é uma forma direta de adicionar estilos em um elemento específico. Utilizamos o atributo HTML `style` dentro da tag para definir as propriedades diretamente.

##### Exemplo Prático

```html
<h1 style="background: red; color: white;">Trilha de CSS</h1>
```

Neste exemplo, a cor do fundo do título será vermelha e o texto ficará branco. 

**Vantagens:** 
- Ideal para estilos isolados ou específicos em um único elemento.

**Desvantagens:** 
- Dificulta a manutenção global dos estilos no site.
- Não é reutilizável, pois cada estilo está ligado a uma tag específica.

---

#### 2. CSS Interno (Interno)

Nessa abordagem, adicionamos o código CSS dentro da tag `<style>` do nosso documento HTML. É útil quando queremos aplicar estilos em múltiplos elementos sem precisar de um arquivo externo.

##### Exemplo Prático

```html
<style>
 h1 {
 background: red;
 color: white;
 }
 
 h2 {
 font-family: Arial, sans-serif;
 }
</style>
```

**Vantagens:** 
- Mais organizado que o inline.
- Permite reutilização de estilos dentro do mesmo arquivo HTML.

---

#### 3. CSS Externo (Externo)

Agora vamos para a forma mais utilizada em projetos profissionais: **CSS externo**. Nessa técnica, criamos um arquivo separado com extensão `.css` e referenciado na nossa página HTML via tag `<link>`.

##### Passo a passo

1. Crie uma pasta chamada `css` dentro da sua raiz de projeto.
2. Dentro dessa pasta, crie um arquivo `.css`, por exemplo: `estilo.css`.
3. No cabeçalho (`<head>`) do seu HTML, adicione o link para esse arquivo:

```html
<link rel="stylesheet" href="./css/estilo.css">
```

**Vantagens:** 
- Código mais organizado e reutilizável em múltiplas páginas.
- Melhora a manutenção global dos estilos.

---

### Conclusão

Agora você já conhece os três métodos de aplicação do CSS:

1. **Inline:** Útil para estilos isolados ou rápidos testes.
2. **Interno:** Bom quando queremos estilizar elementos específicos do mesmo arquivo HTML.
3. **Externo:** A forma mais organizada e recomendada para projetos maiores.

## Referências

- [[Web Designer Senac]]
- [Title Unavailable \| Site Unreachable](https://www.w3schools.com/css/default.asp)
- [CSS Flexbox Layout Guide \| CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- 
