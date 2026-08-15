---
title: Variáveis CSS
description: permitem armazenar valores específicos que podem ser reutilizados ao
  longo do seu código.
tags:
- Webdesign/css
- padrão
---

Olá! Hoje vamos explorar um recurso poderoso do CSS que ajuda a manter o código organizado e fácil de manter: as variáveis CSS.

## Deixando Seu Código Mais Dinâmico e Organizado

### O Que São Variáveis CSS?

As variáveis CSS, também conhecidas como propriedades customizadas, permitem armazenar valores específicos que podem ser reutilizados ao longo do seu código. Isso facilita a manutenção e garante consistência visual.

### Como Declarar Variáveis CSS

Para declarar uma variável CSS, utilizamos a seguinte notação:

```css
--nome-da-variavel: valor;
```

Exemplos:

```css
--bg-color: #f0f0f0;
--font-size: 16px;
```

### Como Referenciar Variáveis CSS

Para referenciar uma variável e aplicar seu valor a uma propriedade, usamos a função `var()`:

```css
propriedade: var(--nome-da-variavel);
```

Exemplo:

```css
body {
  background-color: var(--bg-color);
  font-size: var(--font-size);
}
```

### Utilizando a Pseudoclasse `:root`

Uma prática comum é declarar variáveis CSS dentro da pseudoclasse `:root`. Isso permite que as variáveis sejam aplicadas globalmente em todo o documento CSS:

```css
:root {
  --bg-color: #f0f0f0;
  --font-size: 16px;
}

body {
  background-color: var(--bg-color);
  font-size: var(--font-size);
}
```

### Exemplo Prático: Gradiente e Cores

Vamos supor que temos um site com um gradiente que se repete em vários elementos, como um cabeçalho e um botão. Em vez de repetir o código do gradiente, podemos armazená-lo em uma variável:

```css
:root {
  --bg-gradient: linear-gradient(to right, #00bcd4, #9c27b0);
  --bg-body: #343434;
}

body {
  background-color: var(--bg-body);
}

h1,
a {
  background-image: var(--bg-gradient);
  color: white;
}
```

Se precisarmos alterar o gradiente, basta modificar o valor da variável `--bg-gradient`, e a mudança será refletida em todos os elementos que a utilizam.

### Escopo de Variáveis CSS

As variáveis CSS também podem ter escopo limitado a classes específicas. Isso é útil para criar temas diferentes, como claro e escuro:

```css
.light-theme {
  --bg-color: #f0f0f0;
  --text-color: #333;
}

.dark-theme {
  --bg-color: #333;
  --text-color: #f0f0f0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
```

Para aplicar o tema, basta adicionar a classe `.light-theme` ou `.dark-theme` ao elemento `body`:

```html
<body class="light-theme">
  <!-- Conteúdo do site -->
</body>
```

### Valores de Fallback

Ao utilizar a função `var()`, podemos definir um valor de fallback que será usado caso a variável não esteja definida:

```css
p {
  color: var(--text-color, blue); /* Se --text-color não estiver definido, usa azul */
}
```

Neste exemplo, se a variável `--text-color` não estiver definida, o texto do parágrafo será azul.

### Vantagens das Variáveis CSS

*   **Organização:** Mantém o código limpo e estruturado.
*   **Manutenção:** Facilita a alteração de valores em vários lugares ao mesmo tempo.
*   **Tematização:** Permite criar temas diferentes com facilidade.
*   **Reutilização:** Evita a repetição de código.

### Conclusão

As variáveis CSS são uma ferramenta poderosa para criar código CSS mais dinâmico, organizado e fácil de manter. Ao utilizá-las, você pode simplificar a tematização do seu site, evitar a repetição de código e garantir consistência visual.

%% [Organizando O Css Aula 01 Definindo Variáveis - YouTube](https://www.youtube.com/watch?v=myXp-B3-UsQ) %%
