---
title: Cores com css
description: Exemplo de uso de cores com CSS
tags:
- cores
- Webdesign/css
- editor
---

# Estilizando cores com CSS

## Exemplo

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <title>Cores com CSS</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      body {
        background: azure;
      }
      li {
        background: aqua;
      }
      #pre-definidas {
        background: red;
      }
      #currente-color {
        background: transparent;
        color: orange;
        border: 2px solid currentColor;
      }
      #hex {
        color: #ff89ff;
      }
      #hex-transparencia {
        color: #0000ff80;
      }
      #rgb {
        color: rgb(255, 120, 100);
      }
      #rgba {
        color: rgba(255, 0, 0, 0.5);
      }
      #hsl {
        background: hsl(240, 100%, 50%);
      }
      #hsla {
        color: hsla(240, 100%, 50%, 0.5);
      }
    </style>
  </head>
  <body>
    <h1>Cores com CSS</h1>
    <p>Existem várias forma de definir cores utilizando CSS</p>
    <ul>
      <li id="pre-definidas">Cores pré-definidas</li>
      <li id="currente-color">Palavra-chave "currentcolor"</li>
      <li id="hex">Hexadecimal</li>
      <li id="hex-transparencia">Hexadecimal com transparência</li>
      <li id="rgb">RGB</li>
      <li id="rgba">RGBA</li>
      <li id="hsl">HSL - matriz, saturação e luminosidade</li>
      <li id="hsla">HSLA - com transparência</li>
    </ul>
    <h2>Referências</h2>
    <p><a href="https://www.w3schools.com/colors/colors_names.asp">W3schools color names</a><br>
    <a href="https://pt.dreamstime.com/ilustra%C3%A7%C3%A3o-stock-roda-de-cores-da-cor-nomeia-os-graus-rgb-image78027630">Roda de cores</a></p>
  </body>
</html>
```

## Visualização

<iframe src="https://jocile.github.io/webdesigner/formacao-css/1-Primeiros-passos-com-css/cores.html" style="height: 780px; width: 90%;"></iframe>

## Referências

- [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp)
- [A Roda De Cores Nomeia Os Graus Rgb Ilustração](https://pt.dreamstime.com/ilustra%C3%A7%C3%A3o-stock-roda-de-cores-da-cor-nomeia-os-graus-rgb-image78027630)
- [Cores no design](Cores%20no%20design.md)
- [CSS3 Patterns Gallery](https://projects.verou.me/css3patterns/)
- [webdesigner/formacao-css/1-Primeiros-passos-com-css/cores.html at main · jocile/webdesigner · GitHub](https://github.com/jocile/webdesigner/blob/main/formacao-css/1-Primeiros-passos-com-css/cores.html)
