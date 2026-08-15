---
title: Display com css
description: Organiza o layout e determina o comportamento visual de um elemento HTML
  em relação ao seu conteúdo
tags:
- Webdesign/css
- display
- editor
---

# Organizando o layout com a propriedade Display

<iframe src="https://jocile.github.io/webdesigner/formacao-css/2-Trabalhando-com-layouts-no-css/display.html" style="height: 840px; width: 90%;"></iframe>

A propriedade CSS `display` é uma das mais poderosas e versáteis no desenvolvimento web. Ela determina o comportamento visual de um elemento HTML em relação ao seu conteúdo.

## **Valores possíveis da propriedade `display`**

1. **none**: Esconde completamente o elemento.
2. **block**: O elemento ocupa todo o espaço disponível na linha e pode ter altura (por exemplo, `<p>`, `<div>`).
3. **inline**: O elemento é exibido ao lado dos outros elementos do mesmo nível sem quebrar a linha.
4. **flex** ou `flexbox`: Faz com que os filhos do elemento sejam dispostos em uma configuração flexível (Flexbox).
5. **grid**: Cria um grid para organizar seus filhos.
6. **table**: Transforma o elemento e seus filhos em uma tabela HTML.
7. **list-item**: O elemento é tratado como um item de lista.

## **Efeitos da propriedade `display` nos elementos**

- Ao usar `display: none`, você está escondendo completamente o elemento do fluxo principal, mas ele continua a existir no código-fonte.
- Com `display: block`, os filhos do elemento podem ser dispostos em várias linhas e ocupam todo o espaço disponível na linha. Isso significa que cada filho será exibido em uma nova linha.
- Ao usar `display: inline` ou `inline-block`, os elementos são colocados ao lado um do outro sem quebrar a linha, independentemente de sua largura total.

## Referências

- [Learn HTML Free – Basic HTML Codes for Beginners](https://www.websiteplanet.com/blog/html-guide-beginners/)
- [The box model - Aprendendo desenvolvimento web | MDN](https://developer.mozilla.org/pt-BR/docs/Learn/CSS/Building_blocks/The_box_model)
- [W3schools CSS Layout - The display Property](https://www.w3schools.com/css/css_display_visibility.asp)
