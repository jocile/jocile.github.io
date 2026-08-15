---
title: Estruturando Seu Html
description: Como usar as tags div e span para organizar o conteúdo do site
tags:
- Webdesign/html
---

## Estrutura de uma Página HTML

### Introdução  

Então, vamos entender juntos como organizar uma página web usando HTML. O sucesso da sua página vai depender muito de uma estrutura bem criada do código. Isso porque o HTML é a base e depois dele vem o CSS para deixar tudo mais bonito.

---

### Tags Curinga - Div e Span  

Você já ouviu falar das tags curingas? São elas: `div` e `span`. Essas tags são essenciais para estruturar sua página porque não carregam um significado semântico específico. Elas servem basicamente para delimitar espaços em seu HTML.

#### Como Funcionam  

- **Div** (`<div>`): É uma tag que ocupa a horizontal inteira do espaço onde está inserida (display: block). Ideal para estruturar partes maiores da página.
- **Span** (`<span>`): Uma tag mais pequena, útil para formatar trechos de texto específicos sem afetar todo o conteúdo ao redor.

---

### Pensamento Estrutural  

O segredo é pensar na organização da sua página antes mesmo de começar a codificar. Você precisa estruturar do mais básico possível e depois ir detalhando.

#### O Processo Correto

1. Comece com as tags externas (como o cabeçalho `<header>`, rodapé `<footer>`).
2. Dentro delas, organize os elementos de forma lógica.
3. Use `div` para criar seções maiores e `span` para detalhes específicos.

---

### Exemplo Prático  

Imagine você criando um site simples com cabeçalho, menu lateral e rodapé:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Site Básico</title>
</head>
<body>
    <!-- Cabeçalho -->
    <header class="header">
        <img src="logo.png" alt="Logo do site">
    </header>

    <!-- Menu Lateral -->
    <nav class="menu-lateral">
        <ul>
            <li><a href="#">Início</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>

    <!-- Conteúdo Principal -->
    <main class="conteudo">
        <article class="artigo">
            <h1>Título do Artigo</h1>
            <p>Texto principal...</p>
        </article>
    </main>

    <!-- Rodapé -->
    <footer class="rodape">
        <p>&copy; 2024 Site Desenvolvido por [Nome]</p>
    </footer>
</body>
</html>
```

---

### Propriedade Display  

Essa propriedade é essencial para controlar como os elementos se apresentam na página:

- **display: block** (div): Ocupa a horizontal inteira.
- **display: inline-block**: Permite posicionamento flexível.

- [[Display com css|A propriedade CSS]] `display` é fundamental para controlar como um elemento se apresenta na página. Ela determina o tipo de caixa que o elemento forma e afeta seu comportamento em relação ao layout, como ele ocupa espaço e interage com outros elementos posicionados.

#### Valores Básicos

Quando um elemento é definido com `display: block`, ele se torna uma caixa de bloco. Isso significa que o elemento ocupa toda a largura disponível do seu contêiner, começando em uma nova linha para cada instância do elemento.

##### Exemplo Prático

Considere a seguinte estrutura HTML básica:

```html
<div class="container">
  <div class="block-element">Este é um elemento com display: block</div>
  <div class="block-element">Outro exemplo de elemento com display: block</div>
</div>
```

E o estilo aplicado:

```css
.container {
  border: 1px solid #ccc;
  padding: 10px;
}

.block-element {
  display: block;
}
```

Neste caso, cada `.block-element` começará em uma nova linha dentro do contêiner. O primeiro elemento (`div`) ocupará a largura inteira da área de conteúdo do contêiner até quebrar (por exemplo, ao fim da página ou quando outro bloco começar). Isso é útil para elementos como `div`, `p` (parágrafos), `h1-h6`, `ul`, e outros que precisam de controle mais amplo sobre a largura.

#### `display: inline-block`

O valor `inline-block` combina características de elementos de bloco com posicionamento em linha. Elementos com este display não forçam o início de uma nova linha, mantendo sua posição na sequência normal do texto ou outros elementos, mas podem ter suas dimensões explicitamente definidas.

##### Exemplo Prático

Vamos modificar o exemplo anterior:

```html
<div class="container">
  <span class="inline-block">Este é um elemento com display: inline-block</span>
  <p>Um parágrafo normal de texto.</p>
  <a href="#" class="inline-block">E este é outro elemento inline-block</a>
</div>
```

E o estilo:

```css
.container {
  border: 1px solid #ccc;
  padding: 10px;
}

.inline-block {
  display: inline-block;
}
```

Agora, os elementos `.inline-block` não forçarão a quebra de linha. Eles se comportarão como blocos (podendo ter largura e altura definidas), mas manterão seu posicionamento em linha com o restante do conteúdo.

>[!info] Entender a propriedade `display` é crucial para criar layouts responsivos e bem estruturados na web. Os valores básicos `block`, `inline-block`, e `inline` oferecem diferentes maneiras de controlar como os elementos se apresentam, influenciando diretamente o fluxo do documento e a organização visual dos conteúdos.

---

### Ferramentas Úteis  

Quer facilitar seu trabalho na internet? Existem várias ferramentas que podem ajudar:

- **Visual Studio Code** - [[IDE VScode]]: Editor de texto com recursos avançados.
- [**Brackets**](https://brackets.io/): IDE focada em web design e desenvolvimento.

### Conclusão  

Lembre-se: HTML é a base. Se você não estruturar corretamente, o CSS vai dificultar muito seu trabalho. Pratique e organize sua página antes de pensar em estilização!

Até a próxima pessoal!

### Referências

- [MDN Web Docs](https://developer.mozilla.org/pt-BR/)
- [HTML Block and Inline Elements](https://www.w3schools.com/html/html_blocks.asp)
- [[Estrutura HTML5]]
- [[Web Designer Senac]]
