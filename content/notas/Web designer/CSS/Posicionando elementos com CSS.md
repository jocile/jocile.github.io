---
title: Posicionando elementos
description: Existem cinco valores principais para a propriedade CSS `position`
tags:
- Webdesign/css
- editor
---

## Posicionando elementos na tela com CSS

<iframe src="https://jocile.github.io/webdesigner/formacao-css/2-Trabalhando-com-layouts-no-css/position.html" style="height: 800px; width: 90%;"></iframe>

## Descrição

Existem cinco valores principais para a propriedade CSS `position`. Aqui está uma lista e explicação de cada um:

1. `static`:    
    - É o valor padrão para todos os elementos.
    - O elemento segue o fluxo normal do documento.
    - As propriedades top, right, bottom e left não têm efeito.
2. `relative`:    
    - O elemento é posicionado de acordo com o fluxo normal do documento.
    - Pode ser deslocado em relação à sua posição normal usando top, right, bottom e left.
    - Não afeta a posição de outros elementos.
3. `absolute`:    
    - O elemento é removido do fluxo normal do documento.
    - É posicionado em relação ao ancestral posicionado mais próximo (não static).
    - Se não houver ancestral posicionado, usa o elemento como referência.
    - Pode ser posicionado usando top, right, bottom e left.
4. `fixed`:    
    - O elemento é removido do fluxo normal do documento.
    - É posicionado em relação à viewport do navegador.
    - Não se move quando a página é rolada.
    - Pode ser posicionado usando top, right, bottom e left.
5. `sticky`:    
    - É um híbrido entre relative e fixed.
    - O elemento é tratado como relative até atingir um limite especificado na viewport, então se torna fixed.
    - Útil para criar cabeçalhos que "grudam" no topo da página durante a rolagem.

>[!note] Cada um desses valores de `position` oferecem diferentes maneiras de controlar o layout e o posicionamento dos elementos em uma página web, permitindo designs flexíveis e responsivos.

## Referências

- [Editor - Posicionando os elementos na tela](https://jocile.github.io/webdesigner/formacao-css/2-Trabalhando-com-layouts-no-css/position.html)
- [Positioning - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning#introducing_positioning)
- [w3schools.com/css/css_positioning.asp](https://www.w3schools.com/css/css_positioning.asp)
