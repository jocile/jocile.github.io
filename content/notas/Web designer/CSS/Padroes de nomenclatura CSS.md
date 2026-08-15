---
title: Padrões de nomenclatura CSS
description: como nomear bloco, elemento e modificador no CSS
tags:
- Webdesign/css
- padrão
---

## Padrões de nomenclatura CSS

%% 
 [Organizando O Css Aula 02 Bem Css - YouTube](https://www.youtube.com/watch?v=goFyjX2sWiE) 
 
<think>
Ok, eu preciso ajudar o usuário a organizar um texto em um artigo de markdown com estrutura de tópicos. Primeiro, vou ler o conteúdo que ele forneceu para entender o assunto principal.

O texto fala sobre convenções de nomenclatura no CSS, específicamente o BEM (Bloco, Elemento, Modificador). Parece que o usuário quer uma explicação clara e passo a passo de como usar essas conceitos.

Vou começar identificando os principais pontos do texto. Primeiro, ele explica o que é o BEM CSS, desenvolvido pela Yandex. Depois, detalha cada componente: Bloco, Elemento e Modificador, com exemplos práticos.

Também percebo que o usuário quer que eu use a primeira pessoa e mantenha o português. Além disso, ele menciona a necessidade de estrutura em tópicos h2 e subtítulos h3.

Vou estruturar o artigo começando com um título principal, seguido por subtítulos que dividam cada seção importante: Introdução ao BEM CSS, Componentes do BEM, Exemplo Prático, etc. Em cada seção, vou incluir exemplo de código e explicações claras.

Preciso garantir que o conteúdo esteja organizado de forma que seja fácil de seguir. Talvez dividir em seções como "O que é o BEM CSS?", "Bloco", "Elemento" e "Modificador", cada uma com explicações e exemplos.

Também vou incluir um exemplo completo de um projeto, mostrando como aplicar os conceitos em prática. Isso ajudará o leitor a entender melhor como as classes são nomeadas e usadas no CSS.

Finalmente, vou concluir com uma seção de conclusão que resuma os benefícios do uso do BEM CSS e dê dicas para começar.

Vou ter que garantir que todo o conteúdo esteja em português, use a primeira pessoa e mantenha a fluidez necessária para um artigo informativo.
</think>
%%

## Convenções de Nomenclatura no CSS: Entendendo o BEM (Bloco, Elemento, Modificador)

Quem já parou para pensar em como nomear classes no CSS? Se você está começando ou quer aprimorar suas habilidades, é importante entender as convenções que podem ajudar a organizar seu código e torná-lo mais eficiente. Hoje, vamos explorar o **BEM (Bloco, Elemento, Modificador)**, uma metodologia amplamente utilizada na comunidade de tecnologia para padronizar a nomenclatura de classes no CSS.

### O que é o BEM CSS?

O BEM foi desenvolvido pela empresa russa Yandex e serve como um padrão para criar convenções de nomenclatura. A ideia é ajudar os desenvolvedores a entender melhor o relacionamento entre o HTML, o CSS e as estruturas do projeto. O nome "BEM" é uma abreviação de "Bloco", "Elemento" e "Modificador".

#### Bloco

O **Bloco** é a entidade mais alta no BEM. Ele serve como um componente independente que pode conter outros elementos. Um exemplo comum é um botão (`btn`). O bloco `btn` não tem uma função específica, mas serve como um container para os elementos filhos.

```html
<div class="btn">
  <span class="elemento">Botão</span>
</div>
```

#### Elemento

O **Elemento** é a segunda camada na hierarquia BEM. Ele representa uma parte específica de um bloco e não possui uma funcionalidade intrínseca. O nome do elemento geralmente está associado ao que ele representa, como `link` para um link ou `list-item` para um item de lista.

```html
<div class="menu">
  <ul class="menu__list">
    <li class="menu__item">Item 1</li>
    <li class="menu__item">Item 2</li>
  </ul>
</div>
```

#### Modificador

Os **Modificadores** são usados para modificar um bloco ou um elemento, alterando sua aparência ou estado. Eles podem representar variantes de cores, estilos específicos ou até mesmo estados como "ativo" ou "inativo". Um exemplo é `btn--primary` para um botão primário ou `menu__item--active` para um item ativo em uma navegação.

```html
<div class="menu">
  <ul class="menu__list">
    <li class="menu__item menu__item--active">Item Ativo</li>
    <li class="menu__item">Item Inativo</li>
  </ul>
</div>
```

### Prática: Como aplicar o BEM CSS em um Projeto

Vamos criar um exemplo prático para ilustrar como usar as classes no BEM CSS. Imagine que você está trabalhando em uma página web com uma barra de navegação:

#### Estrutura HTML e CSS

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BEM CSS - Exemplo</title>
  <style>
    .menu {
      background-color: rgb(30, 30, 30);
     }

    .menu__list {
      margin: 0px;
      padding: 24px 0 ;
    }

    .menu__item {
      display: inline-block;
      color: white;
      margin: 0 16px;
      border-radius: 4px;
      padding: 8px;
    }

   .menu__link {
     color: white;
     background: linear-gradiente(90deg, #FC4668 0%, #3FSEF8 100%);
     padding: 12px 14px;
     border-radius: 4px;
     text-decoration: none;
   }

  .menu__item--active {
    font-weight: bold;
    color: #00d9ff;
  }

  </style>
</head>
<body>
  <nav class="menu">
    <ul class="menu__list">
      <li class="menu__item menu__item--activie">Início</li>
      <li class="menu__item">Sobre Nós</li>
      <li class="menu__item">Contato</li>
        <a href="http://jocile.com" class=menu__link">Site</a>
    </ul>
  </nav>
</body>
</html>
```

### Conclusão

O BEM CSS é uma convenção poderosa para organizar as classes no CSS, tornando o código mais legível e manejável. Ao usar blocos, elementos e modificadores de forma consistente, você pode criar um sistema de nomes que sejam fáceis de entender e aplicar em diferentes projetos.

Se você está começando com o BEM CSS, lembre-se de:
- **Manter os nomes de classes menores:** Evite nomes muito longos para manter a hierarquia clara.
- **Ser consistente:** Use as mesmas convenções em todo o projeto para evitar confusão.
- **Testar e ajustar:** Sempre revise os resultados no navegador para garantir que suas classes estejam funcionando como você espera.

Para saber mais acesse: [Padrões CSS - Blog do André Felizardo](https://www.andrefelizardo.com.br/blog/padroes-css/)
