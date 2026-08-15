---
title: Unidades de medida do css
description: são fundamentais para definir tamanhos e espaçamentos em elementos
tags:
- Webdesign/css
---

# Unidades de medida usadas no CSS

No CSS, as unidades de medida são fundamentais para definir tamanhos e espaçamentos em elementos. Elas se dividem em duas categorias principais: **unidades absolutas** e **unidades relativas**.

## Unidades Absolutas

As unidades absolutas são fixas e não se ajustam ao tamanho da tela ou ao contexto em que estão sendo usadas. As mais comuns incluem:

- **Pixels (px)**: A unidade mais utilizada, onde 1px é igual a 1/96 de uma polegada. É ideal para definir tamanhos que não precisam ser flexíveis.
  
- **Centímetros (cm)** e **Milímetros (mm)**: Usadas raramente em telas, são mais comuns em impressão.

- **Polegadas (in)**: Também raramente utilizadas em design web, mas equivalem a 96px por polegada.

- **Pontos (pt)** e **Paicas (pc)**: Unidades herdadas da tipografia, onde 1pt é igual a 1/72 de uma polegada e 1pc é igual a 12pt ^[https://www.treinaweb.com.br/blog/unidades-de-medidas-no-css] ^[https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula]  ^[https://www.w3.org/Style/Examples/007/units.pt_BR.html].

## Unidades Relativas

As unidades relativas são mais flexíveis e se adaptam ao contexto do elemento ou à configuração do usuário. As principais incluem:

- **Em (em)**: Baseada no tamanho da fonte do elemento pai. Por exemplo, se o tamanho da fonte do elemento pai for 16px, 1em será igual a 16px. Isso permite que os elementos se ajustem proporcionalmente ao tamanho da fonte ^[https://pt.linkedin.com/pulse/unidades-de-medida-relativas-em-css-px-e-rem-daniel-moniz] ^[https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula] .

- **Rem (rem)**: Semelhante ao `em`, mas sempre baseado no tamanho da fonte do elemento raiz (`<html>`). Isso evita confusões que podem ocorrer com `em` quando aninhados ^[https://dev.to/lixeletto/entendendo-unidades-css-e-quando-utiliza-las-3ecc] ^[https://pt.linkedin.com/pulse/unidades-de-medida-relativas-em-css-px-e-rem-daniel-moniz].

- **Porcentagem (%)**: Usada para definir tamanhos relativos ao elemento pai. Por exemplo, `width: 50%` fará com que o elemento ocupe metade da largura do seu contêiner ^[https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula] ^[https://www.w3.org/Style/Examples/007/units.pt_BR.html].

- **Viewport Width (vw)** e **Viewport Height (vh)**: Representam uma porcentagem da largura ou altura da janela de visualização. Por exemplo, `100vw` é igual à largura total da janela ^[https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula].

- **Vmin e Vmax**: Representam a menor ou maior medida entre `vw` e `vh`, respectivamente. Isso é útil para garantir que os elementos se ajustem adequadamente em diferentes tamanhos de tela ^[https://dev.to/lixeletto/entendendo-unidades-css-e-quando-utiliza-las-3ecc] ^[https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula].

## Considerações Finais

A escolha entre unidades absolutas e relativas depende do design desejado e da responsividade necessária. As unidades relativas são geralmente preferidas em layouts responsivos, pois permitem que os elementos se ajustem melhor a diferentes dispositivos e configurações de usuário ^[https://www.treinaweb.com.br/blog/unidades-de-medidas-no-css] ^[https://pt.linkedin.com/pulse/unidades-de-medida-relativas-em-css-px-e-rem-daniel-moniz].

Para saber mais acesse:

- [css - É recomendado utilizar a unidade "em" ao invés de "px" para fontes? - Stack Overflow em Português](https://pt.stackoverflow.com/questions/14217/%C3%89-recomendado-utilizar-a-unidade-em-ao-inv%C3%A9s-de-px-para-fontes)
- [Guia de Unidades no CSS | Alura](https://www.alura.com.br/artigos/guia-de-unidades-no-css)
- [developer.mozilla - Values_and_units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)
- [Unidades de medida no CSS (px, em, rem, vw, vh, vmax, vmin e %) - Curso de HTML e CSS - Aula 26 - YouTube](https://www.youtube.com/watch?v=xCvXXIOQtwI)

[treinaweb]: https://www.treinaweb.com.br/blog/unidades-de-medidas-no-css
[dev.to]: https://dev.to/lixeletto/entendendo-unidades-css-e-quando-utiliza-las-3ecc
[youtube]: https://www.youtube.com/watch?v=xCvXXIOQtwI
[linkedin]: https://pt.linkedin.com/pulse/unidades-de-medida-relativas-em-css-px-e-rem-daniel-moniz
[vainaweb]: https://vainaweb.gitbook.io/construcao-de-paginas-web/capitulos/as-unidades-de-medidas-css/aula
[w3]: https://www.w3.org/Style/Examples/007/units.pt_BR.html
