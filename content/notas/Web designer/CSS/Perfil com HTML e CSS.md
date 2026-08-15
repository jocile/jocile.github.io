---
title: Desenvolvendo uma Página de Perfil com HTML e CSS
description: como personalizar elementos da sua página web
tags:
- Webdesign/css
---

Neste artigo, você vai aprender a usar HTML e CSS para criar elementos estilizados na sua página web. Vamos abordar desde os conceitos básicos até detalhes específicos que podem fazer diferença no resultado final.

---

## Configurando os Elementos Básicos 

### O que precisamos fazer 

Primeiro, vamos estruturar nossa página em blocos de conteúdo. Neste exemplo, temos três partes principais:

- **Cabeçalho**: com o título e informações gerais
- **Perfil**: sobre mim 
- **Detalhes**: links e imagens adicionais

Exemplo:

```html
<DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
 <title>Sobre mim</title>
</head>
<body>
<div class="header">
<hl>
Sou um Professor de Programação
</p>
<img class="avatar" src="avatar.jpg">
</div>
<!-- continua -->
</body>
</html>
```

---

Em seguida vamos organizar a página em blocos de conteúdo bem definidos. Isso cria uma hierarquia visual e facilita o processo de estilização. Um bom exemplo prático seria estruturar uma página de perfil profissional, que costuma conter três elementos essenciais: 

1. **Cabeçalho**: área para título principal e identificação do usuário
2. **Seção Principal**: espaço dedicado ao conteúdo textual sobre a pessoa
3. **Detalhes Complementares**: local para informações adicionais como links, redes sociais ou imagens

Aqui está um exemplo completo de estrutura HTML:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Perfil do Professor Carlos</title>
 <!-- Importação de fonte Google Fonts -->
 <link rel="preconnect" href="https://fonts.googleapis.com">
 <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap" rel="stylesheet">

 <!-- Os estilos CSS ficam aqui -->
 <style>
 body {
 font-family: 'Ubuntu', sans-serif;
 }
 </style>

</head>
<body>
 <!-- Área de cabeçalho com título e avatar -->
 <div class="header">
 <h1>Sou um Professor de Programação</h1>
 <img class="avatar" src="https://via.placeholder.com/150" alt="Meu Avatar">
 </div>

 <!-- Container principal para o conteúdo da página -->
 <main class="profile-container">
 <section class="about-section">
 <!-- Texto introdutório sobre a pessoa -->
 <p>Olá! Sou Carlos, um desenvolvedor web apaixonado por tecnologia e criatividade desde 2015.</p>
 <br>
 <p>Tenho experiência em criar interfaces responsivas usando HTML e CSS. Minha paixão é transformar ideias abstratas em experiências digitais tangíveis.</p>
 </section>

 <!-- Seção de detalhes adicionais -->
 <aside class="additional-details">
 <!-- Exemplo: links para redes sociais -->
 <a href="#" class="social-link">LinkedIn</a><br>
 <a href="#" class="social-link">GitHub</a>
 
 <!-- Espaço para uma imagem de capa estilo hover -->
 <img src="https://via.placeholder.com/400x200" alt="Imagem representativa">
 </aside>
 </main>

 <!-- Área de rodapé com informações contextuais -->
 <footer class="profile-footer">
 <p>© 2023 Perfil do Professor Carlos | Todos os direitos reservados</p>
 </footer>
</body>
</html>
```

---

### Definindo estilos 

#### Como fazer a página ficar bonita 

Agora, vamos definir os estilos. Neste caso, vou começar com uma fonte do Google — o Ubuntu.

```css
body {
 font-family: 'Ubuntu', sans-serif;
}
```

Eis! Com isso, nossa página já tem um visual mais moderno e amigável. 

---

#### Aplicação de Fontes Modernas 

Para modernizar a visualização, podemos integrar uma fonte Google Fonts. O Ubuntu é um ótimo exemplo para projetos web por ser legível e com aparência contemporânea:

```css
body {
 font-family: 'Ubuntu', sans-serif;
 font-size: 16px;
 line-height: 1.5;
 color: #333; /* Cor de fundo padrão do texto */
}

/* Estilo para o cabeçalho principal */
.header h1 {
 margin-top: 20px;
 margin-bottom: 40px;
 font-size: 2rem;
 text-align: center;
}

/* Estilo para o avatar da pessoa */
.avatar {
 width: 150px; /* Largura fixa em pixels */
 height: auto; /* Altura automática mantém a proporção */
 border-radius: 50%; /* Transforma a imagem em formato circular */
 box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Adiciona sombra suave ao redor da imagem */
}
```

---

### Cores 

#### Deixando tudo colorido 

Quer deixar seu cabeçalho em vermelho? É só seguir o exemplo:

```css
h1 {
 background-color: red;
}
```

E para as imagens, posso definir um tamanho e borda arredondada. Vamos lá!

---

#### Personalizando com Paletas Vibrantes 

Agora vamos adicionar identidade visual à página usando cores estratégicas. Um exemplo prático seria destacar o cabeçalho:

```css
/* Cabeçalho em fundo vermelho */
.header {
 background-color: #e53935; /* Vermelho escuro */
}

.profile-container a.social-link:hover {
 color: #f44336; /* Altera para vermelho quando o mouse passa por cima */
}
```

---

### Efeitos nas Imagens 

#### Brincando com animações 

Quer uma imagem colorida ao passar o mouse? Segue a magia:

```css
img:hover {
 border: 5px solid yellow;
}
```

Legal né? Agora, vamos dar um acabamento especial nessa transição!

#### Criando Interatividade Visual 

Para tornar os elementos mais dinâmicos, podemos adicionar efeitos de hover. No exemplo da imagem de avatar:

```css
/* Efeito especial ao passar o cursor sobre a imagem */
.avatar:hover {
 transform: scale(1.05); /* Aumenta 5% do tamanho original */
 transition: all 0.3s ease; /* Transição suave entre mudanças */
}

/* Efeito para a imagem de capa estilo hover */
.additional-details img {
 border-radius: 8px;
 margin-top: 10px;
}

.profile-container.additional-details:hover img {
 filter: brightness(90%);
}
```

---

### Finalização dos Detalhes 

#### Refinando o Layout Responsivo 

Para garantir que a página funcione bem em diferentes dispositivos, incluímos um layout flexível:

```css
/* Container principal responsivo */
.profile-container {
 display: flex;
 justify-content: space-between; /* Espalha os itens do container horizontalmente */
 max-width: 800px; /* Largura máxima para desktops grandes */
}

/* Ajustes para visualização em dispositivos móveis */
@media screen and (max-width: 600px) {
.profile-container {
 flex-direction: column;
 }
 
.header h1 {
 font-size: 1.5rem; /* Tamanho de texto menor para mobile */
 }
}
```

---

## Conclusão 

Com estes elementos combinados, você pode criar uma página de perfil completa e profissional. O importante é entender que cada propriedade CSS serve a um propósito específico:

- `font-family`: Define qual fonte será usada
- `color`: Controla as cores do texto
- `background-color`: Altera o fundo visual dos elementos
- `border-radius`: Cria bordas arredondadas para imagem e botões
- `transition`: Garante mudanças suaves nos estilos durante animações

Lembre-se: mesmo sem conhecimento técnico profundo, ao aplicar esses princípios de forma consistente, você já pode criar interfaces web visualmente atraentes. A chave está em entender que cada linha de código CSS contribui para melhorar a experiência do usuário.

### O que aprendemos hoje 

Hoje você viu como:

- Estruturar elementos HTML em blocos claros
- Personalizar estilos com CSS usando fontes e cores
- Adicionar animações interativas para seus componentes

Para saber mais acesse: [Usando CSS - Criando uma página PERFIL com apenas HTML e CSS. Seletores e Efeitos no CSS - YouTube](https://www.youtube.com/watch?v=Hk-BwDupvT8)
