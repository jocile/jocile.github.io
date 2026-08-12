---
title: Proposta de site
description: como personalizar elementos da sua página web
date: '2026-08-12'
draft: false
tags:
- css
- Webdesign
---

Este guia detalha a prática de desenvolvimento de um website de página única (one-page), baseada no projeto prático "O que eu mais gosto em São Paulo..." apresentado no livro html5 e css3 domine a web do futuro.

## 1. Objetivos do Projeto

O objetivo principal é criar um site simples, elegante e funcional que compile uma lista de recomendações sobre uma cidade. A prática visa consolidar os fundamentos do desenvolvimento **front-end**, focando na estruturação de conteúdo com **HTML** e na apresentação visual com **CSS**.

## 2. Escopo Técnico

Para garantir a interoperabilidade e modernidade do projeto, o escopo inclui:

- **Estrutura Semântica:** Uso de tags do **HTML5** para melhor organização e SEO.
- **Estilização:** Aplicação de conceitos do **Box Model** (margens, bordas, preenchimentos) e controle de fluxo com `float`.
- **Consistência:** Utilização do `Normalize.css` para garantir que o site seja exibido de forma similar em diferentes navegadores.
- **Responsividade:** Embora o exemplo utilize uma largura fixa de **960px**, as fontes recomendam a transição para unidades fluídas e **Media Queries** para suporte a dispositivos móveis.

---

## 3. Fases de Desenvolvimento Passo a Passo

### Fase 1: Configuração Inicial e Estrutura Básica

Comece criando um arquivo HTML utilizando um template padrão que inclua o **doctype** do HTML5 e as referências ao `Normalize.css` e ao `prefixfree.min.js`.

- **Título Principal:** Utilize a tag `<h1>` para o nome do site, como "O que eu mais gosto em São Paulo...".
- **Container:** Envolva todo o conteúdo em uma `<div class='container'>` para limitar a largura e centralizar o site na tela.

---

A **Fase 1**, focada na **Configuração Inicial e Estrutura Básica**, é o ponto de partida para garantir que o site funcione corretamente em diferentes dispositivos e navegadores. Abaixo, detalho o passo a passo para estruturar essa base utilizando as práticas recomendadas nas fontes:

#### Passo a Passo Detalhado da Fase 1

1. **Declaração do Doctype e Tag Raiz:** Inicie o documento com `<!doctype html>`, que no HTML5 é uma instrução simplificada e fácil de lembrar para informar ao navegador como processar o código. Em seguida, abra a tag `<html lang='pt-BR'>` para definir o idioma do conteúdo.
2. **Configuração do Cabeçalho (`<head>`):** Dentro do cabeçalho, defina o mapeamento de caracteres com `<meta charset="UTF-8">` para evitar erros de acentuação. Adicione o título que aparecerá na janela do navegador utilizando a tag `<title>`, como "O que eu mais gosto em São Paulo...".
3. **Inclusão de Estilos de Base:** Referencie o arquivo `normalize.css` logo no início do `<head>`. O uso deste arquivo é uma prática essencial para alinhar o comportamento dos navegadores em um mesmo patamar de estilo, corrigindo inconsistências de bordas, fontes e campos de formulário.
4. **Simplificação de Tags no HTML5:** Ao referenciar arquivos CSS e JavaScript, você pode omitir o atributo `type="text/css"` ou `type="text/javascript"`, pois no HTML5 o navegador já assume esses tipos por padrão. Além disso, tags como `<link>`, `<meta>` e `<img>` não precisam mais ser fechadas com uma barra ao final (`/>`), apenas com o sinal de maior (`>`).
5. **Automação de Prefixos:** Ainda no `<head>`, inclua o script `prefixfree.min.js`. Essa ferramenta é fundamental para tratar automaticamente os prefixos proprietários (como `-webkit-` ou `-moz-`) de propriedades CSS3 que ainda não são padrão em todos os browsers, permitindo que você foque na escrita do código canônico.
6. **Estruturação do Corpo (`<body>`):** No início do corpo da página, insira o título principal visível utilizando a tag `<h1>`. Para garantir o controle visual, envolva todo o conteúdo em uma `<div class='container'>`, que servirá para fixar a largura e centralizar o site na tela através do CSS posteriormente.
7. **Preparação para Interatividade:** No final do `<body>`, antes da tag de fechamento, adicione a referência ao `jquery.min.js`. Esta biblioteca de JavaScript será útil para facilitar o trabalho com o DOM e finalizar exemplos práticos de interatividade.

Ao completar esses passos, você terá um **template rock-solid** (sólido como rocha), baseado em boas práticas de compatibilidade e performance, pronto para receber o conteúdo e a estilização específica do seu projeto.

---

#### Estrutura da fase 1

Continuando com a **Fase 1**, a implementação do código HTML inicial estabelece o "esqueleto" e as configurações técnicas necessárias para que o site seja moderno e compatível com diversos navegadores.

Abaixo está o exemplo prático do HTML para esta fase, integrando o template básico com os elementos do site "O que eu mais gosto em São Paulo...".

```html
<!doctype html>
<html lang='pt-BR'>
<head>
 <!-- Define a codificação de caracteres para evitar erros em acentos -->
 <meta charset="UTF-8">

 <!-- Título que aparece na aba do navegador -->
 <title>O que eu mais gosto em São Paulo</title>

 <!-- O Normalize.css garante que o site seja exibido sem inconsistências entre diferentes browsers -->
 <link rel="stylesheet" href="normalize.css">

 <!-- O script prefixfree.min.js automatiza a escrita de prefixos de CSS3 -->
 <script src="prefixfree.min.js"></script>
</head>
<body>

 <!-- Título principal da página -->
 <h1>O que eu mais gosto em São Paulo</h1>

 <!-- A div 'container' é essencial para fixar a largura (ex: 960px) e centralizar o conteúdo futuramente via CSS -->
 <main>

 <!-- O conteúdo principal (Fase 2) será inserido aqui -->
 <!-- Exemplo: <h2>Passear na Avenida Paulista!</h2> -->

 </main>

 <!-- O jQuery é carregado ao final do corpo para não atrasar a renderização da página -->
 <script src="jquery.min.js"></script>
</body>
</html>
```

### Detalhes Importantes da Estrutura Acima:

- **Doctype Simplificado:** No HTML5, utiliza-se apenas `<!doctype html>`, o que informa ao navegador para processar o código seguindo os padrões atuais sem a necessidade de URLs complexas.
- **Omissão de Atributos Desnecessários:** Seguindo as práticas de "escrever menos e fazer mais", não é necessário informar o atributo `type="text/css"` em links de estilo ou `type="text/javascript"` em scripts, pois o HTML5 já assume esses valores por padrão.
- **Fechamento de Tags:** Tags como `<meta>` e `<link>` não precisam mais da barra de fechamento (`/>`) ao final, sendo aceito apenas o sinal de maior (`>`).
- **Uso do Container:** A criação da `<div class='container'>` logo no início da Fase 1 é estratégica para permitir que, na fase de estilização, possamos usar `margin: 0 auto;` para centralizar todo o site na tela do usuário.

---

### Fase 2: Organização do Conteúdo (HTML)

Estruture os locais recomendados utilizando elementos de agrupamento.

- **Conteúdo Principal:** Cada local deve ter um título secundário (`<h2>`), uma breve descrição em parágrafos (`<p>`) e links (`<a>`) para referências externas.
- **Imagens:** Adicione fotos de cada lugar usando a tag `<img>`, sempre preenchendo o atributo `alt` para acessibilidade.
- **Elementos Secundários:** Crie uma barra lateral com uma lista ordenada (`<ol>`) de atrações adicionais e um rodapé (`<footer>`) para informações de autoria.

### Fase 3: Estilização e Layout (CSS)

Inicie a formatação visual para dar identidade ao site.

- **Tipografia:** Defina uma lista de fontes no `body` (ex: Lucida Grande, Verdana) e ajuste o `line-height` para 1.6 para melhorar a leitura.
- **Cores e Fundo:** Aplique uma cor ou imagem de fundo com textura no `body`. Defina cores específicas para links e utilize o pseudo-seletor `:hover` para criar efeitos interativos quando o mouse passar sobre eles.
- **Espaçamento (Box Model):** Adicione `padding` interno e `margin-bottom` aos blocos de conteúdo para que não fiquem colados uns aos outros.

### Fase 4: Posicionamento Avançado

Ajuste a disposição dos elementos na página.

- **Alinhamento de Imagens:** Utilize `float: left` nas imagens para que o texto flua ao lado delas.
- **Colunas:** Posicione o conteúdo principal à esquerda (`float: left`) e a barra lateral à direita (`float: right`), garantindo que a soma de suas larguras não ultrapasse os 960px do container.
- **Limpeza de Fluxo (Clearfix):** Utilize a classe `.clear` ou a técnica de **clearfix** para evitar que elementos flutuantes "vazem" para fora de seus containers.

### Fase 5: Refatoração para HTML5

Para tornar o código mais semântico e modular, substitua as `divs` genéricas pelas novas tags do HTML5:

- Substitua os blocos de cada lugar por `<article>`.
- Substitua a barra lateral por `<aside>`.
- Utilize `<header>` para o título do site e `<footer>` para o rodapé final.

Ao final dessas fases, você terá um site de página única organizado, com uma separação clara entre estrutura e estilo, seguindo as melhores práticas do desenvolvimento web moderno.

## Referências

- [Estudos HTML5 e CSS3 - Mirror Fashion](https://kauanallyson.github.io/livro-html-css/)
- [Arquivos do livro html5-css3-lucas-mazza: Estudos práticos do livro "HTML5 e CSS3: Domine a web do futuro" de Lucas Mazza (Editora Casa do Código).](https://github.com/jocile/html5-css3-lucas-mazza)
